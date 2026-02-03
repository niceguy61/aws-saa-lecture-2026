"""State management for the multi-agent system"""
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """State shared across all agents"""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    current_day: int
    current_week: int
    current_month: int
    topic: str
    agent_name: str
    context: str
    retrieved_docs: list[str]
    next_action: str
