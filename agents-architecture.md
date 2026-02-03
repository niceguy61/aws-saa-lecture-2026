# DevOps 교육 과정 Multi-Agent 시스템 아키텍처

## 🤖 Agent 목록 및 역할

### 1. Orchestrator Agent (오케스트레이터)
**역할**: 사용자 요청을 분석하고 적절한 전문 Agent에게 라우팅
**책임**:
- 사용자 질문 의도 파악
- 적절한 전문 Agent 선택
- 응답 통합 및 최종 답변 생성
- 대화 흐름 관리

### 2. Curriculum Agent (커리큘럼 관리자)
**역할**: 교육 과정 전체 커리큘럼 관리
**책임**:
- 주차별/일별 커리큘럼 제공
- 학습 순서 및 선수 학습 안내
- 학습 진도 추적
- 프로젝트 요구사항 제공
**RAG Database**: curriculum_db

### 3. Docker Agent (Docker 전문가)
**역할**: Docker 관련 모든 질문 처리
**책임**:
- Docker 기본/심화 개념 설명
- Dockerfile 작성 가이드
- Docker Compose 구성
- Docker Swarm 설명
- 컨테이너 트러블슈팅
**RAG Database**: docker_db
**참조 문서**: Docker 공식 문서, Day 1-20 커리큘럼

### 4. Kubernetes Agent (Kubernetes 전문가)
**역할**: Kubernetes 관련 모든 질문 처리
**책임**:
- K8s 아키텍처 및 개념 설명
- 리소스 (Pods, Services, Deployments 등) 가이드
- Helm, Operators 설명
- K8s 트러블슈팅
- EKS, GKE, AKS 비교
**RAG Database**: kubernetes_db
**참조 문서**: Kubernetes 공식 문서, Day 41-80 커리큘럼

### 5. AWS Agent (AWS 클라우드 전문가)
**역할**: AWS 서비스 관련 질문 처리
**책임**:
- AWS 핵심 서비스 설명 (EC2, S3, RDS, VPC 등)
- AWS 네트워킹 및 보안
- AWS 컨테이너 서비스 (ECS, EKS, Fargate)
- AWS 비용 최적화
**RAG Database**: aws_db
**참조 문서**: AWS 공식 문서, Day 21-40 커리큘럼

### 6. Istio Agent (Service Mesh 전문가)
**역할**: Istio 및 Service Mesh 관련 질문 처리
**책임**:
- Service Mesh 개념 설명
- Istio 아키텍처 및 구성
- 트래픽 관리, 보안, 관찰성
- Istio 트러블슈팅
**RAG Database**: istio_db
**참조 문서**: Istio 공식 문서, Day 71-75 커리큘럼

### 7. CICD Agent (CI/CD 전문가)
**역할**: CI/CD 파이프라인 관련 질문 처리
**책임**:
- CI/CD 개념 및 모범 사례
- GitHub Actions, Jenkins, CircleCI 가이드
- 파이프라인 최적화
- 보안 및 품질 게이트
**RAG Database**: cicd_db
**참조 문서**: Day 81-95 커리큘럼

### 8. GitOps Agent (GitOps 전문가)
**역할**: GitOps 및 ArgoCD 관련 질문 처리
**책임**:
- GitOps 개념 및 원칙
- ArgoCD 설치 및 구성
- ApplicationSet, App of Apps
- Progressive Delivery
**RAG Database**: gitops_db
**참조 문서**: ArgoCD 공식 문서, Day 96-100 커리큘럼

### 9. Terraform Agent (IaC 전문가)
**역할**: Terraform 및 IaC 관련 질문 처리
**책임**:
- Terraform 기본 문법 및 개념
- State 관리, 모듈 개발
- AWS 리소스 배포
- Terraform Import
**RAG Database**: terraform_db
**참조 문서**: Terraform 공식 문서, Day 101-120 커리큘럼

### 10. FinOps Agent (비용 최적화 전문가)
**역할**: 클라우드 비용 관리 및 최적화
**책임**:
- FinOps 개념 및 프레임워크
- AWS 비용 분석
- 비용 최적화 전략
- 리소스 라이트사이징
**RAG Database**: finops_db
**참조 문서**: Day 118-120 커리큘럼

### 11. MSA Agent (마이크로서비스 전문가)
**역할**: 마이크로서비스 아키텍처 관련 질문 처리
**책임**:
- MSA 설계 원칙
- 서비스 분해 전략
- MSA 디자인 패턴
- 서비스 간 통신
**RAG Database**: msa_db
**참조 문서**: Day 12-14 커리큘럼

### 12. Lab Agent (실습 가이드)
**역할**: 실습 및 핸즈온 가이드 제공
**책임**:
- 단계별 실습 가이드
- 코드 예제 제공
- 트러블슈팅 시나리오
- 프로젝트 구현 가이드
**RAG Database**: lab_db

### 13. Interview Agent (면접 준비)
**역할**: 기술 면접 준비 지원
**책임**:
- 기술 면접 질문 및 답변
- 모의 면접 시나리오
- 이력서 및 포트폴리오 가이드
- 면접 팁
**RAG Database**: interview_db
**참조 문서**: Day 126-129 커리큘럼

---

## 🔄 Agent 워크플로우 (LangGraph)

```
User Query
    ↓
Orchestrator Agent
    ↓
[Intent Classification]
    ↓
┌─────────────────────────────────────────────────┐
│  Specialized Agents (병렬 실행 가능)              │
├─────────────────────────────────────────────────┤
│ Docker | K8s | AWS | Istio | CI/CD | GitOps    │
│ Terraform | FinOps | MSA | Lab | Interview     │
└─────────────────────────────────────────────────┘
    ↓
[RAG Retrieval from ChromaDB]
    ↓
[Response Generation]
    ↓
Orchestrator Agent (통합)
    ↓
Final Response to User
```

---

## 📊 ChromaDB Collections

각 Agent는 독립적인 ChromaDB Collection을 사용:

1. `curriculum_collection` - 전체 커리큘럼
2. `docker_collection` - Docker 관련 문서
3. `kubernetes_collection` - Kubernetes 관련 문서
4. `aws_collection` - AWS 관련 문서
5. `istio_collection` - Istio 관련 문서
6. `cicd_collection` - CI/CD 관련 문서
7. `gitops_collection` - GitOps 관련 문서
8. `terraform_collection` - Terraform 관련 문서
9. `finops_collection` - FinOps 관련 문서
10. `msa_collection` - MSA 관련 문서
11. `lab_collection` - 실습 가이드
12. `interview_collection` - 면접 준비 자료

---

## 🎯 Agent 선택 로직

**Orchestrator Agent의 라우팅 규칙**:

```python
if "docker" in query or "container" in query:
    → Docker Agent
elif "kubernetes" or "k8s" or "pod" or "deployment" in query:
    → Kubernetes Agent
elif "aws" or "ec2" or "s3" or "rds" in query:
    → AWS Agent
elif "istio" or "service mesh" in query:
    → Istio Agent
elif "ci/cd" or "pipeline" or "jenkins" or "github actions" in query:
    → CICD Agent
elif "argocd" or "gitops" in query:
    → GitOps Agent
elif "terraform" or "iac" in query:
    → Terraform Agent
elif "finops" or "cost" or "비용" in query:
    → FinOps Agent
elif "msa" or "microservice" in query:
    → MSA Agent
elif "실습" or "hands-on" or "lab" in query:
    → Lab Agent
elif "면접" or "interview" in query:
    → Interview Agent
elif "커리큘럼" or "주차" or "일차" in query:
    → Curriculum Agent
else:
    → Orchestrator (직접 처리 또는 복합 Agent 호출)
```

---

## 🔧 기술 스택

- **LangGraph**: Agent 워크플로우 오케스트레이션
- **LangChain**: LLM 체인 및 RAG 구현
- **ChromaDB**: 벡터 데이터베이스
- **OpenAI/Claude**: LLM 모델
- **Docker Compose**: ChromaDB 컨테이너 관리
- **Python**: Agent 구현 언어

