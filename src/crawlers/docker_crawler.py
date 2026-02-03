"""Docker documentation crawler"""
from src.crawlers.base_crawler import BaseCrawler, Document
from bs4 import BeautifulSoup
from typing import Optional


class DockerCrawler(BaseCrawler):
    """Crawler for Docker documentation"""
    
    def __init__(self):
        super().__init__(
            base_url="https://docs.docker.com",
            max_depth=2,
            delay=1.0
        )
    
    def is_valid_url(self, url: str) -> bool:
        """Docker-specific URL validation"""
        if not super().is_valid_url(url):
            return False
        
        # Focus on core documentation
        include_patterns = [
            '/get-started/',
            '/guides/',
            '/reference/',
            '/engine/',
            '/compose/',
            '/build/',
            '/storage/',
            '/network/',
            '/security/'
        ]
        
        return any(pattern in url for pattern in include_patterns)
    
    def extract_content(self, html: str, url: str) -> Optional[Document]:
        """Extract Docker documentation content"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove navigation and other non-content elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            element.decompose()
        
        # Get title
        title = soup.find('h1')
        title_text = title.get_text().strip() if title else url.split('/')[-1]
        
        # Get main content
        main = soup.find('main') or soup.find('article') or soup.find(class_='content')
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
        if '/compose/' in url:
            section = 'compose'
        elif '/engine/' in url:
            section = 'engine'
        elif '/build/' in url:
            section = 'build'
        elif '/network/' in url:
            section = 'network'
        elif '/storage/' in url:
            section = 'storage'
        
        return Document(
            url=url,
            title=title_text,
            content=content,
            metadata={
                'source': 'docker_docs',
                'section': section,
                'base_url': self.base_url
            },
            doc_id=self.generate_doc_id(url)
        )
    
    def get_start_urls(self) -> list[str]:
        """Get Docker documentation URLs to crawl
        
        Returns all documentation URLs by discovering subpages from main sections
        """
        # Main section URLs
        section_urls = [
            "https://docs.docker.com/get-started/",
            "https://docs.docker.com/guides/",
            "https://docs.docker.com/engine/",
            "https://docs.docker.com/compose/",
            "https://docs.docker.com/build/",
            "https://docs.docker.com/storage/",
            "https://docs.docker.com/network/",
            "https://docs.docker.com/security/",
        ]
        
        # Discover all subpages (max 30 per section to avoid too many URLs)
        print("\nDiscovering Docker documentation URLs...")
        all_urls = self.get_all_documentation_urls(section_urls, max_per_section=30)
        print(f"✓ Found {len(all_urls)} total documentation URLs")
        
        return all_urls
