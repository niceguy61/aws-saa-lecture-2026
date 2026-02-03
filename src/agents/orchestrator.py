"""Orchestrator agent for routing queries to specialized agents"""
from langchain_core.messages import SystemMessage, HumanMessage
from src.agents.base_agent import BaseAgent
from src.state import AgentState


ORCHESTRATOR_PROMPT = """You are the Orchestrator Agent for a DevOps training system.

Your role is to analyze user queries and route them to the appropriate specialized agent:

1. **curriculum_agent** - Course structure, weekly/daily schedules, learning paths (Days 1-130)
2. **docker_agent** - Docker, containers, images, Dockerfile, Compose, Swarm (Days 1-20)
3. **kubernetes_agent** - K8s basics, Pods, Services, Deployments, RBAC (Days 41-80)
4. **aws_agent** - AWS services, EC2, S3, RDS, VPC, ECS, EKS (Days 21-40)
5. **istio_agent** - Service Mesh, Istio, traffic management, security (Days 71-75)
6. **cicd_agent** - CI/CD concepts, GitHub Actions, Jenkins, pipelines (Days 81-95)
7. **gitops_agent** - GitOps, ArgoCD, Argo Rollouts (Days 96-100)
8. **terraform_agent** - IaC, Terraform, modules, state management (Days 101-120)
9. **finops_agent** - Cloud cost optimization, FinOps practices (Days 118-120)
10. **msa_agent** - Microservices architecture, design patterns (Days 12-14)
11. **lab_agent** - Hands-on labs, practical exercises, troubleshooting
12. **interview_agent** - Job preparation, interview questions (Days 126-129)

Analyze the query and respond with ONLY the agent name (e.g., "docker_agent").
If multiple agents are relevant, choose the most specific one.
"""


class OrchestratorAgent(BaseAgent):
    """Routes queries to appropriate specialized agents"""
    
    def __init__(self):
        super().__init__(
            name="orchestrator",
            collection_name="curriculum_collection",
            system_prompt=ORCHESTRATOR_PROMPT
        )
    
    def route(self, state: AgentState) -> str:
        """Determine which agent should handle the query"""
        user_query = state["messages"][-1].content if state["messages"] else ""
        
        # Use LLM to determine routing
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"Route this query: {user_query}")
        ]
        
        response = self.llm.invoke(messages)
        agent_name = response.content.strip().lower()
        
        # Validate agent name
        valid_agents = [
            "curriculum_agent", "docker_agent", "kubernetes_agent", "aws_agent",
            "istio_agent", "cicd_agent", "gitops_agent", "terraform_agent",
            "finops_agent", "msa_agent", "lab_agent", "interview_agent"
        ]
        
        if agent_name not in valid_agents:
            agent_name = "curriculum_agent"  # Default fallback
        
        return agent_name
