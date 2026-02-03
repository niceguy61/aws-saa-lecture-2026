"""Terraform documentation crawler"""
from src.crawlers.base_crawler import BaseCrawler, Document
from bs4 import BeautifulSoup
from typing import Optional


class TerraformCrawler(BaseCrawler):
    """Crawler for Terraform documentation"""
    
    def __init__(self):
        super().__init__(
            base_url="https://developer.hashicorp.com/terraform",
            max_depth=2,
            delay=1.0
        )
    
    def is_valid_url(self, url: str) -> bool:
        """Terraform-specific URL validation"""
        if not super().is_valid_url(url):
            return False
        
        # Focus on core documentation
        include_patterns = [
            '/terraform/docs/',
            '/terraform/language/',
            '/terraform/cli/',
            '/terraform/tutorials/'
        ]
        
        return any(pattern in url for pattern in include_patterns)
    
    def extract_content(self, html: str, url: str) -> Optional[Document]:
        """Extract Terraform documentation content"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove non-content elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            element.decompose()
        
        # Get title
        title = soup.find('h1')
        title_text = title.get_text().strip() if title else url.split('/')[-1]
        
        # Get main content
        main = soup.find('main') or soup.find(class_='content') or soup.find(id='docs-content')
        if not main:
            return None
        
        content = main.get_text(separator='\n', strip=True)
        
        # Clean up
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        content = '\n'.join(lines)
        
        if len(content) < 100:
            return None
        
        # Extract section from URL
        section = 'general'
        if '/language/' in url:
            section = 'language'
        elif '/cli/' in url:
            section = 'cli'
        elif '/tutorials/' in url:
            section = 'tutorials'
        
        return Document(
            url=url,
            title=title_text,
            content=content,
            metadata={
                'source': 'terraform_docs',
                'section': section,
                'base_url': self.base_url
            },
            doc_id=self.generate_doc_id(url)
        )
    
    def get_start_urls(self) -> list[str]:
        """Get Terraform documentation URLs to crawl
        
        Returns all documentation URLs by discovering subpages from main sections
        """
        # Main section URLs
        section_urls = [
            "https://developer.hashicorp.com/terraform/docs",
            "https://developer.hashicorp.com/terraform/language",
            "https://developer.hashicorp.com/terraform/cli",
            "https://developer.hashicorp.com/terraform/tutorials",
        ]
        
        # Discover all subpages (max 40 per section)
        print("\nDiscovering Terraform documentation URLs...")
        all_urls = self.get_all_documentation_urls(section_urls, max_per_section=40)
        print(f"✓ Found {len(all_urls)} total documentation URLs")
        
        return all_urls
