"""Base agent class with RAG capabilities"""
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from src.config import (
    OLLAMA_BASE_URL, OLLAMA_MODEL, AGENT_TEMPERATURE
)
from src.vectorstore import VectorStoreManager
from src.state import AgentState


class BaseAgent:
    """Base class for all specialized agents"""
    
    def __init__(self, name: str, collection_name: str, system_prompt: str):
        self.name = name
        self.collection_name = collection_name
        self.system_prompt = system_prompt
        
        # Initialize Ollama LLM
        self.llm = ChatOllama(
            base_url=OLLAMA_BASE_URL,
            model=OLLAMA_MODEL,
            temperature=AGENT_TEMPERATURE
        )
        
        self.vectorstore = VectorStoreManager()
    
    def retrieve_context(self, query: str, k: int = 5) -> list[str]:
        """Retrieve relevant context from vector store"""
        return self.vectorstore.search(self.collection_name, query, k=k)
    
    def generate_response(self, state: AgentState) -> dict:
        """Generate response using RAG"""
        # Get user query from messages
        user_query = state["messages"][-1].content if state["messages"] else ""
        
        # Retrieve relevant context
        retrieved_docs = self.retrieve_context(user_query)
        context = "\n\n".join(retrieved_docs)
        
        # Build messages with context
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"Context:\n{context}\n\nQuery: {user_query}")
        ]
        
        # Generate response using Ollama
        response = self.llm.invoke(messages)
        
        return {
            "messages": [response],
            "agent_name": self.name,
            "retrieved_docs": retrieved_docs,
            "context": context
        }
