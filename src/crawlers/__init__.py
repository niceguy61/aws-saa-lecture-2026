"""Documentation crawlers"""
from src.crawlers.docker_crawler import DockerCrawler
from src.crawlers.kubernetes_crawler import KubernetesCrawler
from src.crawlers.terraform_crawler import TerraformCrawler
from src.crawlers.istio_crawler import IstioCrawler
from src.crawlers.argocd_crawler import ArgoCDCrawler
from src.crawlers.aws_crawler import AWSCrawler

__all__ = [
    'DockerCrawler',
    'KubernetesCrawler',
    'TerraformCrawler',
    'IstioCrawler',
    'ArgoCDCrawler',
    'AWSCrawler',
]
