"""AWS documentation crawler"""
from src.crawlers.base_crawler import BaseCrawler, Document
from bs4 import BeautifulSoup
from typing import Optional


class AWSCrawler(BaseCrawler):
    """Crawler for AWS documentation - focused on DevOps curriculum services"""
    
    def __init__(self):
        super().__init__(
            base_url="https://docs.aws.amazon.com",
            max_depth=2,
            delay=1.0
        )
    
    def is_valid_url(self, url: str) -> bool:
        """AWS-specific URL validation"""
        if not super().is_valid_url(url):
            return False
        
        # Focus on English docs
        if not url.startswith('https://docs.aws.amazon.com/'):
            return False
        
        # Skip non-English versions
        if any(lang in url for lang in ['/ko_kr/', '/ja_jp/', '/zh_cn/', '/zh_tw/', '/fr_fr/', '/de_de/', '/es_es/', '/pt_br/']):
            return False
        
        # Skip API references (too detailed)
        if '/api/' in url or '/APIReference/' in url:
            return False
        
        # Skip SDK docs
        if '/sdk-for-' in url:
            return False
        
        return True
    
    def extract_content(self, html: str, url: str) -> Optional[Document]:
        """Extract AWS documentation content"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove non-content elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'iframe']):
            element.decompose()
        
        # Remove AWS navigation elements
        for class_name in ['awsui-app-layout', 'awsui-util-container', 'awsdocs-filter-selector']:
            for element in soup.find_all(class_=class_name):
                element.decompose()
        
        # Get title
        title = soup.find('h1') or soup.find('title')
        title_text = title.get_text().strip() if title else url.split('/')[-1]
        
        # Get main content - AWS uses various structures
        main = (
            soup.find('main') or 
            soup.find(id='main-content') or 
            soup.find(class_='main-content') or
            soup.find('article') or
            soup.find(role='main')
        )
        
        if not main:
            # Fallback to body
            main = soup.find('body')
        
        if not main:
            return None
        
        content = main.get_text(separator='\n', strip=True)
        
        # Clean up
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        content = '\n'.join(lines)
        
        if len(content) < 100:
            return None
        
        # Extract service from URL
        service = 'general'
        url_parts = url.replace('https://docs.aws.amazon.com/', '').split('/')
        if len(url_parts) > 0:
            service = url_parts[0]
        
        return Document(
            url=url,
            title=title_text,
            content=content,
            metadata={
                'source': 'aws_docs',
                'service': service,
                'base_url': self.base_url
            },
            doc_id=self.generate_doc_id(url)
        )
    
    def get_start_urls(self) -> list[str]:
        """Get AWS documentation URLs to crawl
        
        Focus on services covered in the DevOps curriculum (weeks 5-8)
        """
        # Core services from curriculum
        service_urls = [
            # Week 5: AWS 기본
            "https://docs.aws.amazon.com/ec2/",
            "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html",
            "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html",
            "https://docs.aws.amazon.com/s3/",
            "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html",
            "https://docs.aws.amazon.com/rds/",
            "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html",
            "https://docs.aws.amazon.com/vpc/",
            "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html",
            
            # Week 6: Load Balancing, Auto Scaling
            "https://docs.aws.amazon.com/elasticloadbalancing/",
            "https://docs.aws.amazon.com/autoscaling/",
            "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html",
            "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html",
            
            # Week 7: Container Services
            "https://docs.aws.amazon.com/ecs/",
            "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html",
            "https://docs.aws.amazon.com/eks/",
            "https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html",
            "https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html",
            
            # Week 8: Serverless & IaC
            "https://docs.aws.amazon.com/lambda/",
            "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html",
            "https://docs.aws.amazon.com/sqs/",
            "https://docs.aws.amazon.com/sns/",
            "https://docs.aws.amazon.com/eventbridge/",
            "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html",
            
            # IAM (필수)
            "https://docs.aws.amazon.com/iam/",
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html",
        ]
        
        print("\nDiscovering AWS documentation URLs...")
        print(f"⚠️  AWS has extensive documentation - limiting to curriculum-relevant services")
        print(f"   Starting with {len(service_urls)} core service URLs")
        
        # For AWS, we'll use a smaller max_per_section to avoid overwhelming the system
        all_urls = self.get_all_documentation_urls(service_urls, max_per_section=20)
        print(f"✓ Found {len(all_urls)} total documentation URLs")
        
        return all_urls
