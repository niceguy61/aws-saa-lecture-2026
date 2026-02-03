"""Verify ChromaDB data persistence"""
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import chromadb
from src.config import CHROMA_HOST, CHROMA_PORT


def verify_persistence():
    """Check if ChromaDB collections persist"""
    try:
        client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
        
        print("Checking ChromaDB persistence...")
        print("=" * 60)
        
        # List all collections
        collections = client.list_collections()
        
        if not collections:
            print("⚠️  No collections found!")
            print("\nRun data ingestion first:")
            print("  python src/data_ingestion.py")
            return False
        
        print(f"✓ Found {len(collections)} collections:\n")
        
        for col in collections:
            count = col.count()
            print(f"  - {col.name}: {count} documents")
        
        print("\n" + "=" * 60)
        print("✓ Data persistence verified!")
        print("\nTo test persistence:")
        print("  1. docker-compose down")
        print("  2. docker-compose up -d")
        print("  3. python scripts/verify_persistence.py")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        print("\nMake sure ChromaDB is running:")
        print("  docker-compose up -d")
        return False


if __name__ == "__main__":
    verify_persistence()
