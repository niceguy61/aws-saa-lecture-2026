"""LangGraph workflow definition"""
from langgraph.graph import StateGraph, END
from src.state import AgentState
from src.agents.orchestrator import OrchestratorAgent
from src.agents.specialized_agents import (
    CurriculumAgent, DockerAgent, KubernetesAgent, AWSAgent,
    IstioAgent, CICDAgent, GitOpsAgent, TerraformAgent,
    FinOpsAgent, MSAAgent, LabAgent, InterviewAgent
)


def create_workflow() -> StateGraph:
    """Create the multi-agent workflow graph"""
    
    # Initialize agents
    orchestrator = OrchestratorAgent()
    agents = {
        "curriculum_agent": CurriculumAgent(),
        "docker_agent": DockerAgent(),
        "kubernetes_agent": KubernetesAgent(),
        "aws_agent": AWSAgent(),
        "istio_agent": IstioAgent(),
        "cicd_agent": CICDAgent(),
        "gitops_agent": GitOpsAgent(),
        "terraform_agent": TerraformAgent(),
        "finops_agent": FinOpsAgent(),
        "msa_agent": MSAAgent(),
        "lab_agent": LabAgent(),
        "interview_agent": InterviewAgent(),
    }
    
    # Create workflow graph
    workflow = StateGraph(AgentState)
    
    # Add orchestrator node
    def orchestrator_node(state: AgentState) -> AgentState:
        """Route to appropriate agent"""
        agent_name = orchestrator.route(state)
        state["next_action"] = agent_name
        return state
    
    workflow.add_node("orchestrator", orchestrator_node)
    
    # Add specialized agent nodes
    for agent_name, agent in agents.items():
        def create_agent_node(agent_instance):
            def agent_node(state: AgentState) -> AgentState:
                result = agent_instance.generate_response(state)
                state.update(result)
                state["next_action"] = "end"
                return state
            return agent_node
        
        workflow.add_node(agent_name, create_agent_node(agent))
    
    # Define routing logic
    def route_to_agent(state: AgentState) -> str:
        """Route based on orchestrator decision"""
        next_action = state.get("next_action", "end")
        if next_action == "end":
            return END
        return next_action
    
    # Set entry point
    workflow.set_entry_point("orchestrator")
    
    # Add conditional edges from orchestrator to agents
    workflow.add_conditional_edges(
        "orchestrator",
        route_to_agent,
        {
            "curriculum_agent": "curriculum_agent",
            "docker_agent": "docker_agent",
            "kubernetes_agent": "kubernetes_agent",
            "aws_agent": "aws_agent",
            "istio_agent": "istio_agent",
            "cicd_agent": "cicd_agent",
            "gitops_agent": "gitops_agent",
            "terraform_agent": "terraform_agent",
            "finops_agent": "finops_agent",
            "msa_agent": "msa_agent",
            "lab_agent": "lab_agent",
            "interview_agent": "interview_agent",
            END: END,
        }
    )
    
    # Add edges from agents to END
    for agent_name in agents.keys():
        workflow.add_edge(agent_name, END)
    
    return workflow.compile()
