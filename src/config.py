"""Configuration settings for the multi-agent system"""
import os
from dotenv import load_dotenv

load_dotenv()

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")
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

# Persona Configuration
# Get DEFAULT_PERSONA from environment variable
# Empty string or None means no persona evaluation
_persona_env = os.getenv("DEFAULT_PERSONA", "").strip()
DEFAULT_PERSONA = _persona_env if _persona_env else None

AVAILABLE_PERSONAS = [
    "초등학생",
    "중학생", 
    "고등학생",
    "대학생",
    "주니어_DevOps_1년차",
    "주니어_DevOps_2년차",
    "시니어_DevOps",
    "IT_비전공자"
]

# Validate DEFAULT_PERSONA if set
if DEFAULT_PERSONA and DEFAULT_PERSONA not in AVAILABLE_PERSONAS:
    print(f"⚠️ Warning: Invalid DEFAULT_PERSONA '{DEFAULT_PERSONA}' in .env file")
    print(f"   Valid options: {', '.join(AVAILABLE_PERSONAS)}")
    print(f"   Disabling persona evaluation.")
    DEFAULT_PERSONA = None

# Content Generation Configuration
# Minimum requirements for lecture content
MIN_QUIZ_QUESTIONS = int(os.getenv("MIN_QUIZ_QUESTIONS", "5"))
MIN_QUIZ_QUESTIONS_MULTI_SERVICE = int(os.getenv("MIN_QUIZ_QUESTIONS_MULTI_SERVICE", "10"))
MIN_LAB_STEPS = int(os.getenv("MIN_LAB_STEPS", "7"))
MIN_ADVANTAGES = int(os.getenv("MIN_ADVANTAGES", "3"))
MIN_DISADVANTAGES = int(os.getenv("MIN_DISADVANTAGES", "2"))
MIN_USE_CASES = int(os.getenv("MIN_USE_CASES", "3"))
MIN_TROUBLESHOOTING_SCENARIOS = int(os.getenv("MIN_TROUBLESHOOTING_SCENARIOS", "2"))

# Validate minimum values
if MIN_QUIZ_QUESTIONS < 1:
    print(f"⚠️ Warning: MIN_QUIZ_QUESTIONS must be at least 1, using default: 5")
    MIN_QUIZ_QUESTIONS = 5

if MIN_QUIZ_QUESTIONS_MULTI_SERVICE < MIN_QUIZ_QUESTIONS:
    print(f"⚠️ Warning: MIN_QUIZ_QUESTIONS_MULTI_SERVICE should be >= MIN_QUIZ_QUESTIONS")
    MIN_QUIZ_QUESTIONS_MULTI_SERVICE = MIN_QUIZ_QUESTIONS * 2

if MIN_LAB_STEPS < 1:
    print(f"⚠️ Warning: MIN_LAB_STEPS must be at least 1, using default: 7")
    MIN_LAB_STEPS = 7
