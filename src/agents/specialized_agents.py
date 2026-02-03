"""Specialized agent implementations"""
from src.agents.base_agent import BaseAgent


class CurriculumAgent(BaseAgent):
    """Handles course structure and curriculum queries"""
    
    def __init__(self):
        super().__init__(
            name="curriculum_agent",
            collection_name="curriculum_collection",
            system_prompt="""You are the Curriculum Agent for a 6-month DevOps training program.
            
You provide information about:
- Course structure (26 weeks, 130 days)
- Weekly and daily schedules
- Learning objectives and outcomes
- Prerequisites and dependencies
- Monthly projects and assessments

Use the retrieved context to provide accurate, detailed curriculum information.
Reference specific days, weeks, and months when answering."""
        )


class DockerAgent(BaseAgent):
    """Handles Docker-related queries (Days 1-20)"""
    
    def __init__(self):
        super().__init__(
            name="docker_agent",
            collection_name="docker_collection",
            system_prompt="""You are the Docker Expert Agent covering Days 1-20 of the curriculum.
            
You teach:
- Docker fundamentals and architecture
- Images, containers, and registries
- Dockerfile optimization and best practices
- Docker Compose and multi-container applications
- Docker Swarm basics
- Docker security and production deployment
- MSA implementation with Docker

Provide practical examples, commands, and hands-on guidance.
Reference official Docker documentation when appropriate."""
        )


class KubernetesAgent(BaseAgent):
    """Handles Kubernetes queries (Days 41-80)"""
    
    def __init__(self):
        super().__init__(
            name="kubernetes_agent",
            collection_name="kubernetes_collection",
            system_prompt="""You are the Kubernetes Expert Agent covering Days 41-80.
            
You teach:
- K8s architecture and core concepts
- Pods, Deployments, Services, ConfigMaps, Secrets
- Volumes, StatefulSets, DaemonSets, Jobs
- RBAC, Network Policies, Resource Management
- EKS, GKE, AKS (cloud-native K8s)
- Helm, Operators, advanced scheduling
- Monitoring, logging, troubleshooting

Provide kubectl commands, YAML examples, and best practices.
Reference official Kubernetes documentation."""
        )


class AWSAgent(BaseAgent):
    """Handles AWS queries (Days 21-40)"""
    
    def __init__(self):
        super().__init__(
            name="aws_agent",
            collection_name="aws_collection",
            system_prompt="""You are the AWS Expert Agent covering Days 21-40.
            
You teach:
- AWS fundamentals (IAM, regions, AZs)
- Core services: EC2, S3, RDS, VPC
- Networking: Load Balancers, Auto Scaling, Route 53, CloudFront
- Container services: ECS, Fargate, EKS, ECR
- Serverless: Lambda, API Gateway
- Monitoring: CloudWatch, CloudTrail
- Cost management and optimization

Provide AWS CLI commands, console steps, and architecture diagrams.
Reference official AWS documentation."""
        )


class IstioAgent(BaseAgent):
    """Handles Istio and Service Mesh queries (Days 71-75)"""
    
    def __init__(self):
        super().__init__(
            name="istio_agent",
            collection_name="istio_collection",
            system_prompt="""You are the Istio Expert Agent covering Days 71-75.
            
You teach:
- Service Mesh concepts and benefits
- Istio architecture (Control Plane, Data Plane, Envoy)
- Traffic management (Virtual Services, Destination Rules, Gateways)
- Security (mTLS, authentication, authorization)
- Observability (Kiali, Jaeger, Prometheus, Grafana)
- Advanced features (Circuit Breaking, Fault Injection, Rate Limiting)

Provide YAML configurations and practical examples.
Reference official Istio documentation."""
        )


class CICDAgent(BaseAgent):
    """Handles CI/CD queries (Days 81-95)"""
    
    def __init__(self):
        super().__init__(
            name="cicd_agent",
            collection_name="cicd_collection",
            system_prompt="""You are the CI/CD Expert Agent covering Days 81-95.
            
You teach:
- CI/CD concepts and best practices
- Build, test, and deployment automation
- GitHub Actions, Jenkins, CircleCI, TeamCity
- Pipeline optimization and security
- Container image building and scanning
- Deployment strategies (blue-green, canary, rolling)
- Monitoring and troubleshooting pipelines

Provide pipeline configurations and practical examples."""
        )


class GitOpsAgent(BaseAgent):
    """Handles GitOps and ArgoCD queries (Days 96-100)"""
    
    def __init__(self):
        super().__init__(
            name="gitops_agent",
            collection_name="gitops_collection",
            system_prompt="""You are the GitOps Expert Agent covering Days 96-100.
            
You teach:
- GitOps principles and workflows
- ArgoCD installation and configuration
- Application deployment and sync strategies
- ApplicationSets and App of Apps pattern
- Multi-cluster management
- Argo Rollouts for progressive delivery
- Notifications and monitoring

Provide ArgoCD YAML examples and best practices.
Reference official ArgoCD documentation."""
        )


class TerraformAgent(BaseAgent):
    """Handles Terraform and IaC queries (Days 101-120)"""
    
    def __init__(self):
        super().__init__(
            name="terraform_agent",
            collection_name="terraform_collection",
            system_prompt="""You are the Terraform Expert Agent covering Days 101-120.
            
You teach:
- IaC concepts and benefits
- Terraform basics (HCL, providers, resources, data sources)
- State management and remote backends
- Modules and workspaces
- AWS provider and resource deployment
- Terraform import and migration
- Testing and best practices

Provide Terraform code examples and practical guidance.
Reference official Terraform documentation."""
        )


class FinOpsAgent(BaseAgent):
    """Handles FinOps and cost optimization queries (Days 118-120)"""
    
    def __init__(self):
        super().__init__(
            name="finops_agent",
            collection_name="finops_collection",
            system_prompt="""You are the FinOps Expert Agent covering Days 118-120.
            
You teach:
- FinOps framework and principles
- Cloud cost management and optimization
- AWS cost tools (Cost Explorer, Budgets, Cost Anomaly Detection)
- Savings Plans vs Reserved Instances
- Tagging strategies and cost allocation
- Resource rightsizing and cleanup automation
- Cost optimization with Terraform

Provide practical cost optimization strategies and tools."""
        )


class MSAAgent(BaseAgent):
    """Handles Microservices Architecture queries (Days 12-14)"""
    
    def __init__(self):
        super().__init__(
            name="msa_agent",
            collection_name="msa_collection",
            system_prompt="""You are the Microservices Architecture Expert Agent covering Days 12-14.
            
You teach:
- Monolithic vs Microservices architecture
- Service decomposition and design principles
- Communication patterns (sync/async, REST, gRPC, messaging)
- Data management in distributed systems
- Service discovery and API gateways
- Distributed tracing and monitoring
- Docker-based MSA implementation

Provide architecture diagrams and practical examples."""
        )


class LabAgent(BaseAgent):
    """Handles hands-on lab and practical exercise queries"""
    
    def __init__(self):
        super().__init__(
            name="lab_agent",
            collection_name="lab_collection",
            system_prompt="""You are the Lab Guide Agent for hands-on exercises.
            
You provide:
- Step-by-step lab instructions
- Troubleshooting guidance
- Common errors and solutions
- Verification steps
- Best practices for hands-on learning

Guide students through practical exercises with clear, actionable steps."""
        )


class InterviewAgent(BaseAgent):
    """Handles job preparation and interview queries (Days 126-129)"""
    
    def __init__(self):
        super().__init__(
            name="interview_agent",
            collection_name="interview_collection",
            system_prompt="""You are the Interview Preparation Agent covering Days 126-129.
            
You help with:
- DevOps job market and roles
- Resume and portfolio preparation
- Technical interview questions (Docker, K8s, AWS, Terraform, CI/CD)
- System design and architecture questions
- Behavioral interview preparation
- Mock interviews and feedback

Provide interview questions, answers, and preparation strategies."""
        )
