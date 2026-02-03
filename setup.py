"""Setup script for DevOps Training Multi-Agent System"""
from setuptools import setup, find_packages

setup(
    name="devops-training-agents",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langgraph>=0.2.0",
        "langchain>=0.3.0",
        "langchain-openai>=0.2.0",
        "langchain-community>=0.3.0",
        "chromadb>=0.5.0",
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "tiktoken>=0.7.0",
        "beautifulsoup4>=4.12.0",
        "requests>=2.31.0",
        "lxml>=5.0.0",
    ],
    python_requires=">=3.10",
)
