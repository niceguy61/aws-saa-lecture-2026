"""Main entry point for the DevOps Training Multi-Agent System"""
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from langchain_core.messages import HumanMessage
from src.graph import create_workflow
from src.state import AgentState


def run_query(query: str):
    """Run a query through the multi-agent system"""
    # Create workflow
    workflow = create_workflow()
    
    # Initialize state
    initial_state: AgentState = {
        "messages": [HumanMessage(content=query)],
        "current_day": 0,
        "current_week": 0,
        "current_month": 0,
        "topic": "",
        "agent_name": "",
        "context": "",
        "retrieved_docs": [],
        "next_action": ""
    }
    
    # Run workflow
    result = workflow.invoke(initial_state)
    
    # Extract response
    if result["messages"]:
        response = result["messages"][-1].content
        agent_name = result.get("agent_name", "unknown")
        
        print(f"\n{'='*60}")
        print(f"Agent: {agent_name}")
        print(f"{'='*60}")
        print(f"\n{response}\n")
        
        # Show retrieved context (optional)
        if result.get("retrieved_docs"):
            print(f"\n{'='*60}")
            print(f"Retrieved {len(result['retrieved_docs'])} relevant documents")
            print(f"{'='*60}\n")
    
    return result


def interactive_mode():
    """Run in interactive mode"""
    print("\n" + "="*60)
    print("DevOps Training Multi-Agent System")
    print("="*60)
    print("\nType your questions or 'quit' to exit.\n")
    
    while True:
        query = input("You: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break
        
        if not query:
            continue
        
        try:
            run_query(query)
        except Exception as e:
            print(f"\nError: {e}\n")


def main():
    """Main function"""
    import sys
    
    if len(sys.argv) > 1:
        # Run single query from command line
        query = " ".join(sys.argv[1:])
        run_query(query)
    else:
        # Run in interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
