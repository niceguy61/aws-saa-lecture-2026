# 🚀 DevOps 교육 과정 AI 강의 생성 시스템

6개월 DevOps 교육 과정을 위한 Multi-Agent RAG 기반 강의 자료 자동 생성 시스템

## 📋 개요

이 프로젝트는 Docker, Kubernetes, AWS, Terraform, CI/CD 등 DevOps 전 영역을 다루는 6개월(26주, 130일) 교육 과정의 강의 자료를 자동으로 생성하는 AI 시스템입니다.

**핵심 기능**:
- 📚 **일별 강의 자료 자동 생성**: 서비스 이해, Deep Dive, 실습, 퀴즈 포함
- 🤖 **Multi-Agent 시스템**: 13개 전문 Agent가 각 기술 영역 담당
- 🔍 **RAG 기반 검색**: ChromaDB를 활용한 공식 문서 기반 답변
- 🎯 **커리큘럼 기반**: 체계적인 6개월 학습 로드맵 제공

## 🏗️ 시스템 아키텍처

```
사용자 질의
    ↓
Orchestrator Agent (라우팅)
    ↓
┌─────────────────────────────────────────────────┐
│  전문 Agents (병렬 실행)                          │
├─────────────────────────────────────────────────┤
│ Docker | K8s | AWS | Istio | CI/CD | GitOps    │
│ Terraform | FinOps | MSA | Lab | Interview     │
└─────────────────────────────────────────────────┘
    ↓
ChromaDB RAG 검색 (12개 Collection)
    ↓
강의 자료 생성 (한글)
```

## 🎓 교육 과정 구조

### 6개월 커리큘럼 (26주, 130일)

| 기간 | 주제 | 주요 내용 |
|------|------|-----------|
| **1개월차** (1-4주) | Docker & MSA | 컨테이너 기초, Dockerfile, Compose, Swarm, MSA 설계 |
| **2개월차** (5-8주) | AWS 클라우드 | EC2, S3, RDS, VPC, ECS, EKS, Lambda, CloudFormation |
| **3개월차** (9-12주) | Kubernetes 기초 | Pods, Services, Volumes, RBAC, 공식 문서 Deep Dive |
| **4개월차** (13-16주) | K8s 심화 & Istio | EKS, Helm, Operators, Service Mesh, 트래픽 관리 |
| **5개월차** (17-20주) | CI/CD & GitOps | GitHub Actions, Jenkins, ArgoCD, Progressive Delivery |
| **6개월차** (21-26주) | Terraform & FinOps | IaC, State 관리, AWS 배포, 비용 최적화, 최종 프로젝트 |

## 🤖 Multi-Agent 시스템

### 13개 전문 Agent

1. **Orchestrator Agent** - 요청 라우팅 및 응답 통합
2. **Curriculum Agent** - 커리큘럼 관리 및 학습 순서 안내
3. **Docker Agent** - Docker 전문가
4. **Kubernetes Agent** - K8s 전문가
5. **AWS Agent** - AWS 클라우드 전문가
6. **Istio Agent** - Service Mesh 전문가
7. **CICD Agent** - CI/CD 파이프라인 전문가
8. **GitOps Agent** - GitOps & ArgoCD 전문가
9. **Terraform Agent** - IaC 전문가
10. **FinOps Agent** - 비용 최적화 전문가
11. **MSA Agent** - 마이크로서비스 아키텍처 전문가
12. **Lab Agent** - 실습 가이드 제공
13. **Interview Agent** - 기술 면접 준비 지원

각 Agent는 독립적인 ChromaDB Collection을 사용하여 전문 영역의 공식 문서를 검색합니다.

## 📚 강의 자료 구성 (EARS 패턴)

매일 생성되는 강의 자료는 4가지 필수 컴포넌트로 구성됩니다:

### 1. 서비스 이해 (오전)
- 배경 정보 및 역사
- 핵심 개념 및 아키텍처
- 장단점 분석
- 실제 사용 사례
- 연관 서비스
- 공식 문서 링크
- 인포그래픽 (Mermaid 다이어그램)

### 2. Deep Dive (오후)
- 공식 문서 기반 트러블슈팅 시나리오 (최소 2개)
- 시나리오 설명 → 원인 분석 → 진단 방법 → 해결 방법 → 검증

### 3. Hands-on Lab (실습)
- 실습 개요 및 학습 목표
- 사전 요구사항
- **최소 7단계** 상세 실습 (각 단계당 3-4개 액션)
- 단계별 검증 및 트러블슈팅
- 정리 및 추가 자료

### 4. Quiz (퀴즈)
- **최소 5문제** (멀티 서비스 시 10문제)
- 4가지 질문 유형: 지식 확인, 시나리오 대응, 명령어/설정, 비교/분석
- 모든 문제에 상세 설명 포함

## 🚀 빠른 시작

### 1. 사전 요구사항

```bash
# Python 3.9+
python --version

# Docker Desktop
docker --version
```

### 2. 설치

```bash
# 저장소 클론
git clone <repository-url>
cd kdt_devops_lecture_2026

# 가상환경 생성 및 활성화
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# 의존성 설치
pip install -r requirements.txt
```

### 3. ChromaDB 실행

```bash
# Docker Compose로 ChromaDB 시작
docker-compose up -d

# 연결 확인
docker ps | findstr chromadb
```

### 4. 환경 변수 설정

```bash
# .env 파일 생성
copy .env.example .env

# .env 파일 편집하여 API 키 입력
notepad .env
```

`.env` 파일 예시:
```env
# LLM Provider: "openai" or "ollama"
LLM_PROVIDER=openai

# OpenAI 설정 (LLM_PROVIDER=openai인 경우)
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-4o

# Ollama 설정 (LLM_PROVIDER=ollama인 경우)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen2.5:7b

# ChromaDB 설정
CHROMA_HOST=localhost
CHROMA_PORT=8000
```

### 5. 데이터 수집

```bash
# 커리큘럼 데이터 수집
python src/data_ingestion.py

# 공식 문서 크롤링 (선택사항, 10-20분 소요)
python src/ingest_official_docs.py --service all

# 또는 개별 서비스만
python src/ingest_official_docs.py --service docker
python src/ingest_official_docs.py --service kubernetes
```

### 6. 강의 자료 생성

```bash
# 특정 일차 강의 생성
python generate_lecture.py --week 1 --day 1

# 전체 주차 생성
python generate_lecture.py --week 1

# 대화형 모드
python main.py
```

## 📁 프로젝트 구조

```
kdt_devops_lecture_2026/
├── src/
│   ├── agents/              # Multi-Agent 시스템
│   │   ├── orchestrator.py  # 오케스트레이터
│   │   ├── lecture_agents.py # 강의 생성 Agent
│   │   └── specialized_agents.py # 전문 Agents
│   ├── crawlers/            # 공식 문서 크롤러
│   │   ├── docker_crawler.py
│   │   ├── kubernetes_crawler.py
│   │   ├── aws_crawler.py
│   │   ├── terraform_crawler.py
│   │   ├── istio_crawler.py
│   │   └── argocd_crawler.py
│   ├── config.py            # 설정
│   ├── vectorstore.py       # ChromaDB 관리
│   ├── graph.py             # LangGraph 워크플로우
│   └── lecture_generator.py # 강의 생성 로직
├── lectures/                # 생성된 강의 자료
│   └── week1/
│       ├── day1/
│       │   ├── service_understanding.md
│       │   ├── deep_dive.md
│       │   ├── handson_step1.md
│       │   └── quiz.md
│       └── day2/
├── scripts/                 # 유틸리티 스크립트
│   ├── backup_chromadb.sh
│   ├── reset_chromadb.sh
│   └── verify_persistence.py
├── .kiro/steering/          # Steering 문서
│   ├── lecture-content-generation-rules.md
│   └── devops-curriculum-guide.md
├── docker-compose.yml       # ChromaDB 컨테이너
├── requirements.txt
├── main.py                  # 메인 실행 파일
└── generate_lecture.py      # 강의 생성 스크립트
```

## 💡 사용 예시

### 강의 자료 생성

```bash
# Week 1, Day 1 강의 생성
python generate_lecture.py --week 1 --day 1

# 생성된 파일 확인
ls lectures/week1/day1/
# service_understanding.md
# deep_dive.md
# handson_step1.md ~ handson_step7.md
# quiz.md
```

### 대화형 질의응답

```bash
python main.py

> Docker와 가상 머신의 차이점은?
> Kubernetes에서 Pod가 재시작되는 이유는?
> AWS EKS 클러스터 생성 방법은?
> Terraform State 파일 관리 방법은?
```

### 특정 Agent 직접 호출

```python
from src.agents.specialized_agents import DockerAgent

agent = DockerAgent()
response = agent.answer("Dockerfile 멀티 스테이지 빌드 예제")
print(response)
```

## 🔧 고급 설정

### Ollama 사용 (로컬 LLM)

```bash
# Ollama 설치 및 모델 다운로드
ollama pull qwen2.5:7b
ollama pull nomic-embed-text

# .env 설정
LLM_PROVIDER=ollama
OLLAMA_MODEL=qwen2.5:7b
EMBEDDING_PROVIDER=ollama
```

### ChromaDB 백업 및 복구

```bash
# 백업
bash scripts/backup_chromadb.sh

# 복구
bash scripts/restore_chromadb.sh

# 초기화
bash scripts/reset_chromadb.sh
```

### 크롤링 진행 상황 확인

```bash
# 크롤링 인덱스 확인
python scripts/manage_crawl_index.py --list

# 특정 서비스 재크롤링
python scripts/manage_crawl_index.py --reset docker
python src/ingest_official_docs.py --service docker
```

## 📊 데이터 검증

```bash
# ChromaDB 데이터 확인
python scripts/verify_persistence.py

# 출력 예시:
# ✓ curriculum_collection: 130 documents
# ✓ docker_collection: 245 documents
# ✓ kubernetes_collection: 512 documents
# ✓ aws_collection: 389 documents
```

## 🎯 주요 기능

### 1. 자동 강의 생성
- 커리큘럼 기반 일별 강의 자료 자동 생성
- 한글로 작성된 전문적인 교육 자료
- 공식 문서 기반 정확한 정보

### 2. Multi-Agent RAG
- 13개 전문 Agent가 각 영역 담당
- ChromaDB 벡터 검색으로 관련 문서 자동 검색
- LangGraph 기반 워크플로우 오케스트레이션

### 3. 실습 중심 학습
- 최소 7단계 상세 실습 가이드
- 단계별 검증 및 트러블슈팅
- 실제 프로덕션 환경 시나리오

### 4. 공식 문서 크롤링
- Docker, Kubernetes, AWS, Terraform, Istio, ArgoCD 공식 문서
- 자동 업데이트 및 버전 관리
- 증분 크롤링 지원

## 🛠️ 기술 스택

- **LangGraph**: Agent 워크플로우 오케스트레이션
- **LangChain**: LLM 체인 및 RAG 구현
- **ChromaDB**: 벡터 데이터베이스
- **OpenAI GPT-4o / Ollama**: LLM 모델
- **Docker Compose**: ChromaDB 컨테이너 관리
- **Python 3.9+**: 구현 언어
- **BeautifulSoup4**: 웹 크롤링

## 📖 문서

- [전체 커리큘럼](DevOps_6개월_교육과정_커리큘럼.md) - 130일 상세 커리큘럼
- [Agent 아키텍처](agents-architecture.md) - Multi-Agent 시스템 설계
- [설치 가이드](SETUP_GUIDE.md) - 상세 설치 및 설정
- [Ollama 설정](OLLAMA_SETUP.md) - 로컬 LLM 사용 가이드
- [강의 생성 규칙](.kiro/steering/lecture-content-generation-rules.md) - EARS 패턴 상세

## 🤝 기여

이슈 및 PR은 언제나 환영합니다!

## 📝 라이선스

MIT License

## 👥 개발자

DevOps 교육 과정 개발팀

---

**🎓 6개월 만에 DevOps 전문가로 성장하세요!**
