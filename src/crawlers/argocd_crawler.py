"""ArgoCD documentation crawler"""
from src.crawlers.base_crawler import BaseCrawler, Document
from bs4 import BeautifulSoup
from typing import Optional


class ArgoCDCrawler(BaseCrawler):
    """Crawler for ArgoCD documentation"""
    
    def __init__(self):
        super().__init__(
            base_url="https://argo-cd.readthedocs.io",
            max_depth=2,
            delay=1.0
        )
    
    def is_valid_url(self, url: str) -> bool:
        """ArgoCD-specific URL validation"""
        if not super().is_valid_url(url):
            return False
        
        # Focus on stable/latest docs
        include_patterns = [
            '/en/stable/',
            '/en/latest/'
        ]
        
        # Skip version-specific old docs
        if '/en/release-' in url:
            return False
        
        return any(pattern in url for pattern in include_patterns)
    
    def extract_content(self, html: str, url: str) -> Optional[Document]:
        """Extract ArgoCD documentation content"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove non-content elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            element.decompose()
        
        # Get title
        title = soup.find('h1')
        title_text = title.get_text().strip() if title else url.split('/')[-2]
        
        # Get main content - ArgoCD uses <article> tag
        main = soup.find('article') or soup.find(class_='md-content') or soup.find(role='main')
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
        if '/user-guide/' in url:
            section = 'user-guide'
        elif '/operator-manual/' in url:
            section = 'operator-manual'
        elif '/developer-guide/' in url:
            section = 'developer-guide'
        
        return Document(
            url=url,
            title=title_text,
            content=content,
            metadata={
                'source': 'argocd_docs',
                'section': section,
                'base_url': self.base_url
            },
            doc_id=self.generate_doc_id(url)
        )
    
    def get_start_urls(self) -> list[str]:
        """Get ArgoCD documentation URLs to crawl
        
        Returns all documentation URLs by discovering subpages from main sections
        """
        # Main section URLs
        section_urls = [
            "https://argo-cd.readthedocs.io/en/stable/",
            "https://argo-cd.readthedocs.io/en/stable/user-guide/",
            "https://argo-cd.readthedocs.io/en/stable/operator-manual/",
        ]
        
        # Discover all subpages (max 40 per section)
        print("\nDiscovering ArgoCD documentation URLs...")
        all_urls = self.get_all_documentation_urls(section_urls, max_per_section=40)
        print(f"✓ Found {len(all_urls)} total documentation URLs")
        
        return all_urls
