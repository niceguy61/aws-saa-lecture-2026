"""Base agent class with RAG capabilities"""
import json
import logging
from typing import Callable, Dict, Any, Optional
from datetime import datetime
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from src.config import (
    OLLAMA_BASE_URL, OLLAMA_MODEL, AGENT_TEMPERATURE
)
from src.vectorstore import VectorStoreManager
from src.state import AgentState


class AgentLogger:
    """구조화된 Agent 로깅"""
    
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.start_time = None
        
        # Setup logger
        self.logger = logging.getLogger(agent_name)
        self.logger.setLevel(logging.INFO)
        
        # Console handler
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%H:%M:%S'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def start(self, task: str):
        """Start task"""
        self.start_time = datetime.now()
        self.logger.info(f"🚀 Started: {task}")
    
    def progress(self, message: str):
        """Log progress"""
        self.logger.info(f"  ⏳ {message}")
    
    def complete(self, task: str):
        """Complete task"""
        if self.start_time:
            elapsed = (datetime.now() - self.start_time).total_seconds()
            self.logger.info(f"✅ Completed: {task} ({elapsed:.1f}s)")
        else:
            self.logger.info(f"✅ Completed: {task}")
    
    def error(self, task: str, error: Exception):
        """Log error"""
        self.logger.error(f"❌ Failed: {task} - {error}")
    
    def warning(self, message: str):
        """Log warning"""
        self.logger.warning(f"⚠️  {message}")


class BaseAgent:
    """Base class for all specialized agents with retry logic"""
    
    def __init__(self, name: str, collection_name: str, system_prompt: str, max_retries: int = 3):
        self.name = name
        self.collection_name = collection_name
        self.system_prompt = system_prompt
        self.max_retries = max_retries
        
        # Initialize Ollama LLM
        self.llm = ChatOllama(
            base_url=OLLAMA_BASE_URL,
            model=OLLAMA_MODEL,
            temperature=AGENT_TEMPERATURE,
            format="json"  # JSON 출력 강제
        )
        
        self.vectorstore = VectorStoreManager()
        self.logger = AgentLogger(name)
    
    def retrieve_context(self, query: str, k: int = 5) -> list[str]:
        """Retrieve relevant context from vector store"""
        return self.vectorstore.search(self.collection_name, query, k=k)
    
    def generate_with_retry(
        self,
        chain,
        input_dict: Dict[str, Any],
        validator_func: Callable[[Dict], Any],
        error_context: str = ""
    ) -> Any:
        """
        Retry logic with validation
        
        Args:
            chain: LangChain chain to invoke
            input_dict: Input dictionary for the chain
            validator_func: Function to validate and transform the response
            error_context: Context string for error messages
            
        Returns:
            Validated data from validator_func
        """
        original_temp = self.llm.temperature
        
        for attempt in range(self.max_retries):
            try:
                self.logger.progress(f"Attempt {attempt + 1}/{self.max_retries}")
                
                # Invoke chain
                response = chain.invoke(input_dict)
                
                # Parse JSON
                try:
                    if hasattr(response, 'content'):
                        raw_content = response.content
                        data = json.loads(raw_content)
                    else:
                        raw_content = str(response)
                        data = json.loads(raw_content)
                    
                    # DEBUG: Log parsed data structure for QuizAgent
                    if "QuizAgent" in self.name:
                        self.logger.info(f"🔍 DEBUG: Raw response length: {len(raw_content)}")
                        self.logger.info(f"🔍 DEBUG: Parsed data keys: {list(data.keys())}")
                        if "questions" in data:
                            self.logger.info(f"🔍 DEBUG: Questions type in parsed data: {type(data['questions'])}")
                            
                except json.JSONDecodeError as e:
                    self.logger.warning(f"JSON parse error: {e}")
                    if attempt < self.max_retries - 1:
                        # Increase temperature slightly for retry
                        self.llm.temperature = min(0.9, self.llm.temperature + 0.1)
                        continue
                    else:
                        raise ValueError(f"Failed to parse JSON after {self.max_retries} attempts")
                
                # Validate
                validated_data = validator_func(data)
                
                # Reset temperature
                self.llm.temperature = original_temp
                
                self.logger.progress("Generation successful")
                return validated_data
                
            except Exception as e:
                self.logger.warning(f"Attempt {attempt + 1} failed: {str(e)[:100]}")
                
                if attempt == self.max_retries - 1:
                    self.logger.error(f"All retries exhausted for {error_context}", e)
                    raise
                
                # Adjust temperature for retry
                self.llm.temperature = min(0.9, self.llm.temperature + 0.1)
        
        # Reset temperature
        self.llm.temperature = original_temp
        raise Exception(f"Failed after {self.max_retries} attempts: {error_context}")
    
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
