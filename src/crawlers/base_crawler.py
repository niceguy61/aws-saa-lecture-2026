"""Base crawler for documentation sites"""
import time
import hashlib
from typing import List, Dict, Optional
from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse


@dataclass
class Document:
    """Crawled document"""
    url: str
    title: str
    content: str
    metadata: Dict
    doc_id: str


class BaseCrawler:
    """Base class for documentation crawlers"""
    
    def __init__(self, base_url: str, max_depth: int = 3, delay: float = 1.0):
        self.base_url = base_url
        self.max_depth = max_depth
        self.delay = delay
        self.visited_urls = set()
        self.documents = []
        
    def is_valid_url(self, url: str) -> bool:
        """Check if URL should be crawled"""
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        
        # Same domain
        if parsed.netloc != base_parsed.netloc:
            return False
        
        # Skip non-documentation URLs
        skip_patterns = [
            '/blog/', '/news/', '/events/', '/community/',
            '.pdf', '.zip', '.tar.gz', '/download/',
            '/search', '/login', '/signup'
        ]
        
        for pattern in skip_patterns:
            if pattern in url.lower():
                return False
        
        return True
    
    def generate_doc_id(self, url: str) -> str:
        """Generate unique document ID"""
        return hashlib.md5(url.encode()).hexdigest()
    
    def extract_content(self, html: str, url: str) -> Optional[Document]:
        """Extract content from HTML - override in subclasses"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        # Get title
        title = soup.find('title')
        title_text = title.get_text().strip() if title else url
        
        # Get main content
        main_content = soup.find('main') or soup.find('article') or soup.find('body')
        if not main_content:
            return None
        
        content = main_content.get_text(separator='\n', strip=True)
        
        # Clean up content
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        content = '\n'.join(lines)
        
        if len(content) < 100:  # Skip very short pages
            return None
        
        return Document(
            url=url,
            title=title_text,
            content=content,
            metadata={'source': 'crawler', 'base_url': self.base_url},
            doc_id=self.generate_doc_id(url)
        )
    
    def fetch_page(self, url: str) -> Optional[str]:
        """Fetch page HTML"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"✗ Failed to fetch {url}: {e}")
            return None
    
    def discover_subpages(self, parent_url: str, max_pages: int = 50) -> List[str]:
        """Discover subpages from a parent URL
        
        Args:
            parent_url: Parent page URL to discover subpages from
            max_pages: Maximum number of subpages to discover
            
        Returns:
            List of discovered subpage URLs
        """
        print(f"  Discovering subpages from: {parent_url}")
        
        html = self.fetch_page(parent_url)
        if not html:
            return [parent_url]  # Return at least the parent
        
        soup = BeautifulSoup(html, 'html.parser')
        discovered_urls = [parent_url]  # Include parent
        
        # Find all links
        for link in soup.find_all('a', href=True):
            if len(discovered_urls) >= max_pages:
                break
                
            href = link['href']
            full_url = urljoin(parent_url, href)
            
            # Check if valid and not already discovered
            if self.is_valid_url(full_url) and full_url not in discovered_urls:
                # Check if it's a subpage (same path prefix)
                if full_url.startswith(parent_url.rstrip('/')):
                    discovered_urls.append(full_url)
        
        print(f"  ✓ Discovered {len(discovered_urls)} URLs")
        time.sleep(self.delay)
        
        return discovered_urls
    
    def crawl_url(self, url: str, depth: int = 0) -> List[str]:
        """Crawl a single URL and return found links"""
        if depth > self.max_depth or url in self.visited_urls:
            return []
        
        if not self.is_valid_url(url):
            return []
        
        self.visited_urls.add(url)
        print(f"{'  ' * depth}Crawling: {url}")
        
        # Fetch page
        html = self.fetch_page(url)
        if not html:
            return []
        
        # Extract content
        doc = self.extract_content(html, url)
        if doc:
            self.documents.append(doc)
        
        # Extract links
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            
            if self.is_valid_url(full_url) and full_url not in self.visited_urls:
                links.append(full_url)
        
        # Rate limiting
        time.sleep(self.delay)
        
        return links
    
    def crawl(self, start_urls: List[str], follow_links: bool = False) -> List[Document]:
        """Crawl documentation starting from given URLs
        
        Args:
            start_urls: List of URLs to crawl
            follow_links: If True, follow links recursively up to max_depth
                         If False, only crawl the provided URLs (batch mode)
        """
        print(f"\nCrawling {len(start_urls)} URLs from {self.base_url}")
        
        # Reset documents for this batch
        self.documents = []
        
        if follow_links:
            # Original recursive behavior
            urls_to_crawl = list(start_urls)
            depth = 0
            
            while urls_to_crawl and depth <= self.max_depth:
                next_urls = []
                
                for url in urls_to_crawl:
                    found_links = self.crawl_url(url, depth)
                    next_urls.extend(found_links)
                
                urls_to_crawl = list(set(next_urls))
                depth += 1
        else:
            # Batch mode: only crawl provided URLs, don't follow links
            for url in start_urls:
                if url in self.visited_urls:
                    continue
                
                if not self.is_valid_url(url):
                    continue
                
                self.visited_urls.add(url)
                print(f"  Crawling: {url}")
                
                # Fetch page
                html = self.fetch_page(url)
                if not html:
                    continue
                
                # Extract content
                doc = self.extract_content(html, url)
                if doc:
                    self.documents.append(doc)
                
                # Rate limiting
                time.sleep(self.delay)
        
        print(f"✓ Crawled {len(self.documents)} documents")
        return self.documents
    
    def get_all_documentation_urls(self, section_urls: List[str], max_per_section: int = 50) -> List[str]:
        """Get all documentation URLs by discovering subpages from section URLs
        
        Args:
            section_urls: List of section/category URLs
            max_per_section: Maximum subpages to discover per section
            
        Returns:
            Complete list of documentation URLs
        """
        all_urls = []
        
        for section_url in section_urls:
            subpages = self.discover_subpages(section_url, max_per_section)
            all_urls.extend(subpages)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_urls = []
        for url in all_urls:
            if url not in seen:
                seen.add(url)
                unique_urls.append(url)
        
        return unique_urls
