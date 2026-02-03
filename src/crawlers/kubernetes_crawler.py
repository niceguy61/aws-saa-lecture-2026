"""Kubernetes documentation crawler"""
from src.crawlers.base_crawler import BaseCrawler, Document
from bs4 import BeautifulSoup
from typing import Optional


class KubernetesCrawler(BaseCrawler):
    """Crawler for Kubernetes documentation"""
    
    def __init__(self):
        super().__init__(
            base_url="https://kubernetes.io",
            max_depth=2,
            delay=1.0
        )
    
    def is_valid_url(self, url: str) -> bool:
        """Kubernetes-specific URL validation"""
        if not super().is_valid_url(url):
            return False
        
        # Focus on core documentation
        include_patterns = [
            '/docs/concepts/',
            '/docs/tasks/',
            '/docs/tutorials/',
            '/docs/reference/',
            '/docs/setup/'
        ]
        
        return any(pattern in url for pattern in include_patterns)
    
    def extract_content(self, html: str, url: str) -> Optional[Document]:
        """Extract Kubernetes documentation content"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove non-content elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            element.decompose()
        
        # Get title
        title = soup.find('h1')
        title_text = title.get_text().strip() if title else url.split('/')[-2]
        
        # Get main content
        main = soup.find('main') or soup.find(id='main-content') or soup.find(class_='td-content')
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
        if '/concepts/' in url:
            section = 'concepts'
        elif '/tasks/' in url:
            section = 'tasks'
        elif '/tutorials/' in url:
            section = 'tutorials'
        elif '/reference/' in url:
            section = 'reference'
        
        return Document(
            url=url,
            title=title_text,
            content=content,
            metadata={
                'source': 'kubernetes_docs',
                'section': section,
                'base_url': self.base_url
            },
            doc_id=self.generate_doc_id(url)
        )
    
    def get_start_urls(self) -> list[str]:
        """Get Kubernetes documentation URLs to crawl
        
        Returns all documentation URLs by discovering subpages from main sections
        """
        # Main section URLs
        section_urls = [
            "https://kubernetes.io/docs/concepts/",
            "https://kubernetes.io/docs/tasks/",
            "https://kubernetes.io/docs/tutorials/",
            "https://kubernetes.io/docs/reference/",
        ]
        
        # Discover all subpages (max 50 per section for K8s - it has many docs)
        print("\nDiscovering Kubernetes documentation URLs...")
        all_urls = self.get_all_documentation_urls(section_urls, max_per_section=50)
        print(f"✓ Found {len(all_urls)} total documentation URLs")
        
        return all_urls
