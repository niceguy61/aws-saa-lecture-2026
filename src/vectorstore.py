"""ChromaDB vector store management"""
import chromadb
from chromadb.config import Settings
from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from src.config import (
    CHROMA_URL, COLLECTIONS, 
    EMBEDDING_PROVIDER, OPENAI_API_KEY,
    OLLAMA_BASE_URL, OLLAMA_EMBEDDING_MODEL
)


class VectorStoreManager:
    """Manages ChromaDB collections for different agents"""
    
    def __init__(self):
        self.client = chromadb.HttpClient(
            host=CHROMA_URL.split("://")[1].split(":")[0],
            port=int(CHROMA_URL.split(":")[-1])
        )
        
        # Initialize embeddings based on provider
        if EMBEDDING_PROVIDER == "openai":
            self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        else:  # ollama
            self.embeddings = OllamaEmbeddings(
                base_url=OLLAMA_BASE_URL,
                model=OLLAMA_EMBEDDING_MODEL
            )
        
        self.collections = {}
        
    def get_or_create_collection(self, collection_name: str) -> Chroma:
        """Get or create a ChromaDB collection"""
        if collection_name not in self.collections:
            self.collections[collection_name] = Chroma(
                client=self.client,
                collection_name=collection_name,
                embedding_function=self.embeddings
            )
        return self.collections[collection_name]
    
    def add_documents(self, collection_name: str, documents: list, metadatas: list = None):
        """Add documents to a collection"""
        collection = self.get_or_create_collection(collection_name)
        collection.add_texts(texts=documents, metadatas=metadatas)
    
    def search(self, collection_name: str, query: str, k: int = 5) -> list:
        """Search for relevant documents in a collection"""
        collection = self.get_or_create_collection(collection_name)
        results = collection.similarity_search(query, k=k)
        return [doc.page_content for doc in results]
    
    def list_collections(self) -> list[str]:
        """List all available collections"""
        return [col.name for col in self.client.list_collections()]
