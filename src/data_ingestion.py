"""Data ingestion script to populate ChromaDB collections"""
import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.vectorstore import VectorStoreManager
from src.config import COLLECTIONS


def load_markdown_file(filepath: str) -> list[dict]:
    """Load and chunk markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by major sections (## headers)
    sections = []
    current_section = []
    current_title = ""
    
    for line in content.split('\n'):
        if line.startswith('## '):
            if current_section:
                sections.append({
                    'content': '\n'.join(current_section),
                    'title': current_title,
                    'source': filepath
                })
            current_title = line.replace('## ', '').strip()
            current_section = [line]
        else:
            current_section.append(line)
    
    # Add last section
    if current_section:
        sections.append({
            'content': '\n'.join(current_section),
            'title': current_title,
            'source': filepath
        })
    
    return sections


def ingest_curriculum_data(vectorstore: VectorStoreManager):
    """Ingest curriculum data into ChromaDB"""
    print("Ingesting curriculum data...")
    
    # Load main curriculum file
    curriculum_file = "DevOps_6개월_교육과정_커리큘럼.md"
    if os.path.exists(curriculum_file):
        sections = load_markdown_file(curriculum_file)
        documents = [s['content'] for s in sections]
        metadatas = [{'title': s['title'], 'source': s['source']} for s in sections]
        
        vectorstore.add_documents(
            COLLECTIONS['curriculum'],
            documents,
            metadatas
        )
        print(f"✓ Ingested {len(documents)} sections from curriculum")
    
    # Load steering guide
    steering_file = ".kiro/steering/devops-curriculum-guide.md"
    if os.path.exists(steering_file):
        sections = load_markdown_file(steering_file)
        documents = [s['content'] for s in sections]
        metadatas = [{'title': s['title'], 'source': s['source']} for s in sections]
        
        vectorstore.add_documents(
            COLLECTIONS['curriculum'],
            documents,
            metadatas
        )
        print(f"✓ Ingested {len(documents)} sections from steering guide")


def extract_topic_sections(content: str, start_day: int, end_day: int) -> list[dict]:
    """Extract sections for specific day range"""
    sections = []
    current_section = []
    current_day = None
    
    for line in content.split('\n'):
        # Detect day markers
        if line.startswith('**Day '):
            day_num = int(line.split('Day ')[1].split(':')[0])
            
            if current_section and current_day and start_day <= current_day <= end_day:
                sections.append({
                    'content': '\n'.join(current_section),
                    'day': current_day
                })
            
            current_day = day_num
            current_section = [line]
        else:
            current_section.append(line)
    
    # Add last section
    if current_section and current_day and start_day <= current_day <= end_day:
        sections.append({
            'content': '\n'.join(current_section),
            'day': current_day
        })
    
    return sections


def ingest_specialized_data(vectorstore: VectorStoreManager):
    """Ingest data for specialized agents"""
    print("\nIngesting specialized agent data...")
    
    curriculum_file = "DevOps_6개월_교육과정_커리큘럼.md"
    if not os.path.exists(curriculum_file):
        print("✗ Curriculum file not found")
        return
    
    with open(curriculum_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Docker (Days 1-20)
    docker_sections = extract_topic_sections(content, 1, 20)
    if docker_sections:
        documents = [s['content'] for s in docker_sections]
        metadatas = [{'day': s['day'], 'topic': 'docker'} for s in docker_sections]
        vectorstore.add_documents(COLLECTIONS['docker'], documents, metadatas)
        print(f"✓ Docker: {len(documents)} sections (Days 1-20)")
    
    # AWS (Days 21-40)
    aws_sections = extract_topic_sections(content, 21, 40)
    if aws_sections:
        documents = [s['content'] for s in aws_sections]
        metadatas = [{'day': s['day'], 'topic': 'aws'} for s in aws_sections]
        vectorstore.add_documents(COLLECTIONS['aws'], documents, metadatas)
        print(f"✓ AWS: {len(documents)} sections (Days 21-40)")
    
    # Kubernetes (Days 41-80)
    k8s_sections = extract_topic_sections(content, 41, 80)
    if k8s_sections:
        documents = [s['content'] for s in k8s_sections]
        metadatas = [{'day': s['day'], 'topic': 'kubernetes'} for s in k8s_sections]
        vectorstore.add_documents(COLLECTIONS['kubernetes'], documents, metadatas)
        print(f"✓ Kubernetes: {len(documents)} sections (Days 41-80)")
    
    # Istio (Days 71-75)
    istio_sections = extract_topic_sections(content, 71, 75)
    if istio_sections:
        documents = [s['content'] for s in istio_sections]
        metadatas = [{'day': s['day'], 'topic': 'istio'} for s in istio_sections]
        vectorstore.add_documents(COLLECTIONS['istio'], documents, metadatas)
        print(f"✓ Istio: {len(documents)} sections (Days 71-75)")
    
    # CI/CD (Days 81-95)
    cicd_sections = extract_topic_sections(content, 81, 95)
    if cicd_sections:
        documents = [s['content'] for s in cicd_sections]
        metadatas = [{'day': s['day'], 'topic': 'cicd'} for s in cicd_sections]
        vectorstore.add_documents(COLLECTIONS['cicd'], documents, metadatas)
        print(f"✓ CI/CD: {len(documents)} sections (Days 81-95)")
    
    # GitOps (Days 96-100)
    gitops_sections = extract_topic_sections(content, 96, 100)
    if gitops_sections:
        documents = [s['content'] for s in gitops_sections]
        metadatas = [{'day': s['day'], 'topic': 'gitops'} for s in gitops_sections]
        vectorstore.add_documents(COLLECTIONS['gitops'], documents, metadatas)
        print(f"✓ GitOps: {len(documents)} sections (Days 96-100)")
    
    # Terraform (Days 101-120)
    terraform_sections = extract_topic_sections(content, 101, 120)
    if terraform_sections:
        documents = [s['content'] for s in terraform_sections]
        metadatas = [{'day': s['day'], 'topic': 'terraform'} for s in terraform_sections]
        vectorstore.add_documents(COLLECTIONS['terraform'], documents, metadatas)
        print(f"✓ Terraform: {len(documents)} sections (Days 101-120)")
    
    # FinOps (Days 118-120)
    finops_sections = extract_topic_sections(content, 118, 120)
    if finops_sections:
        documents = [s['content'] for s in finops_sections]
        metadatas = [{'day': s['day'], 'topic': 'finops'} for s in finops_sections]
        vectorstore.add_documents(COLLECTIONS['finops'], documents, metadatas)
        print(f"✓ FinOps: {len(documents)} sections (Days 118-120)")
    
    # MSA (Days 12-14)
    msa_sections = extract_topic_sections(content, 12, 14)
    if msa_sections:
        documents = [s['content'] for s in msa_sections]
        metadatas = [{'day': s['day'], 'topic': 'msa'} for s in msa_sections]
        vectorstore.add_documents(COLLECTIONS['msa'], documents, metadatas)
        print(f"✓ MSA: {len(documents)} sections (Days 12-14)")
    
    # Interview (Days 126-129)
    interview_sections = extract_topic_sections(content, 126, 129)
    if interview_sections:
        documents = [s['content'] for s in interview_sections]
        metadatas = [{'day': s['day'], 'topic': 'interview'} for s in interview_sections]
        vectorstore.add_documents(COLLECTIONS['interview'], documents, metadatas)
        print(f"✓ Interview: {len(documents)} sections (Days 126-129)")


def main():
    """Main ingestion function"""
    print("Starting data ingestion into ChromaDB...")
    print("=" * 60)
    
    vectorstore = VectorStoreManager()
    
    # Ingest curriculum data
    ingest_curriculum_data(vectorstore)
    
    # Ingest specialized agent data
    ingest_specialized_data(vectorstore)
    
    print("\n" + "=" * 60)
    print("Data ingestion complete!")
    print("\nAvailable collections:")
    for collection in vectorstore.list_collections():
        print(f"  - {collection}")


if __name__ == "__main__":
    main()
