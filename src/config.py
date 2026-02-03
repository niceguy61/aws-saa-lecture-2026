"""Configuration settings for the multi-agent system"""
import os
from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")  # "openai" or "ollama"

# OpenAI Configuration (optional)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")

# Embedding Configuration
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "ollama")  # "openai" or "ollama"
OLLAMA_EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")

# ChromaDB Configuration
CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))
CHROMA_URL = f"http://{CHROMA_HOST}:{CHROMA_PORT}"

# Collection Names
COLLECTIONS = {
    "curriculum": "curriculum_collection",
    "docker": "docker_collection",
    "kubernetes": "kubernetes_collection",
    "aws": "aws_collection",
    "istio": "istio_collection",
    "cicd": "cicd_collection",
    "gitops": "gitops_collection",
    "terraform": "terraform_collection",
    "finops": "finops_collection",
    "msa": "msa_collection",
    "lab": "lab_collection",
    "interview": "interview_collection",
}

# Agent Configuration
AGENT_TEMPERATURE = 0.7
MAX_ITERATIONS = 10
