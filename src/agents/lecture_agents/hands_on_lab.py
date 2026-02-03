"""Hands-on Lab 생성 에이전트"""
import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from src.vectorstore import VectorStoreManager
from .models import HandsOnLab, HandsOnStep
from .infographic import InfographicAgent


class HandsOnLabAgent:
    """Hands-on Lab 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
        self.infographic_agent = InfographicAgent(model_name)
    
    def generate(self, service_name: str, rag_context: str) -> HandsOnLab:
        """실습 섹션 생성 with retry logic"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 5년 차 DevOps 엔지니어이자 실습 교육 전문가입니다.
실제 프로덕션 환경에서 검증된 명령어와 워크플로우를 기반으로 실습을 설계합니다.

## 🎯 핵심 원칙: 신뢰성과 재현성

### ✅ 반드시 지켜야 할 것:

1. **실제 실행 가능한 명령어만 사용**
   - 모든 명령어는 복사-붙여넣기로 즉시 실행 가능해야 함
   - 플레이스홀더 사용 시 명확한 설명과 예시 제공
   - 명령어 실행 순서가 논리적이고 의존성이 명확해야 함

2. **명령어 실행 결과 기반 작성**
   - expected_output은 실제 명령어 실행 시 나오는 출력을 정확히 반영
   - 에러 메시지, 성공 메시지, 상태 코드 등을 구체적으로 명시
   - 출력 형식(JSON, 테이블, 로그 등)을 정확히 표현

3. **검증 가능성 (Verifiable)**
   - 각 스텝마다 성공 여부를 확인할 수 있는 verification 명령어 필수
   - verification 명령어도 실제 실행 가능하고 출력이 명확해야 함
   - 실패 시나리오와 해결 방법을 troubleshooting에 구체적으로 제시

4. **기술별 특화 패턴 적용**
   - Docker: 이미지 빌드 → 컨테이너 실행 → 로그 확인 → 정리
   - Kubernetes: YAML 작성 → apply → get/describe → logs → delete
   - Terraform: init → plan → apply → show → destroy
   - AWS CLI: configure → create → describe → test → delete
   - 각 기술의 베스트 프랙티스와 일반적인 워크플로우 준수

5. **주석의 품질**
   - 명령어 위에 한글 주석으로 "무엇을", "왜" 하는지 설명
   - 옵션/플래그의 의미를 주석으로 설명
   - 주의사항이나 팁을 주석으로 추가

### ❌ 절대 금지:

1. **추상적이거나 불완전한 명령어**
   - "적절한 값으로 변경", "필요에 따라 수정" 같은 모호한 표현 금지
   - 구체적인 예시 값을 제공하고, 변경이 필요한 부분만 명시

2. **검증 불가능한 스텝**
   - verification이 없거나 형식적인 스텝 금지
   - "정상 동작 확인" 같은 추상적 검증 금지
   - 구체적인 명령어와 예상 출력 필수

3. **기술 특성 무시**
   - Docker 실습에서 Kubernetes 명령어 사용 금지
   - 각 기술의 표준 워크플로우를 무시한 순서 금지
   - 비현실적이거나 안티패턴인 명령어 사용 금지

4. **불필요한 복잡성**
   - 학습 목표와 무관한 고급 기능 추가 금지
   - 한 스텝에 너무 많은 작업 포함 금지
   - 초보자가 이해하기 어려운 복잡한 스크립트 금지

## 📋 기술별 표준 워크플로우 패턴

### Docker 실습 패턴 (8-12 스텝)
```
1. 프로젝트 디렉토리 생성 (mkdir, cd)
2. 애플리케이션 파일 작성 (cat > app.js 또는 echo)
3. 의존성 파일 작성 (cat > package.json)
4. Dockerfile 작성 (cat > Dockerfile, 각 instruction 설명)
5. .dockerignore 작성 (선택, 최적화 시)
6. 이미지 빌드 (docker build -t name:tag .)
7. 이미지 확인 (docker images | grep name)
8. 컨테이너 실행 (docker run -d -p 8080:8080 --name container-name)
9. 컨테이너 상태 확인 (docker ps)
10. 애플리케이션 테스트 (curl http://localhost:8080)
11. 로그 확인 (docker logs container-name)
12. 정리 (docker stop, docker rm, docker rmi)
```

### Kubernetes 실습 패턴 (10-15 스텝)
```
1. 네임스페이스 생성 (kubectl create namespace)
2. Deployment YAML 작성 (cat > deployment.yaml)
3. Deployment 배포 (kubectl apply -f deployment.yaml)
4. Deployment 상태 확인 (kubectl get deployments -n namespace)
5. Pod 상태 확인 (kubectl get pods -n namespace)
6. Pod 상세 정보 (kubectl describe pod -n namespace)
7. Service YAML 작성 (cat > service.yaml)
8. Service 배포 (kubectl apply -f service.yaml)
9. Service 확인 (kubectl get svc -n namespace)
10. 애플리케이션 테스트 (kubectl port-forward 또는 curl)
11. 로그 확인 (kubectl logs -n namespace)
12. 스케일링 테스트 (kubectl scale deployment)
13. 롤링 업데이트 (kubectl set image)
14. 정리 (kubectl delete -f ., kubectl delete namespace)
```

### Terraform 실습 패턴 (8-12 스텝)
```
1. 프로젝트 디렉토리 생성
2. provider.tf 작성 (AWS provider 설정)
3. variables.tf 작성 (변수 정의)
4. main.tf 작성 (리소스 정의)
5. terraform.tfvars 작성 (변수 값)
6. Terraform 초기화 (terraform init)
7. 실행 계획 확인 (terraform plan)
8. 리소스 생성 (terraform apply)
9. 상태 확인 (terraform show)
10. 리소스 테스트 (AWS CLI 또는 curl)
11. 변경 사항 적용 (수정 후 terraform apply)
12. 정리 (terraform destroy)
```

### AWS CLI 실습 패턴 (8-12 스텝)
```
1. AWS CLI 설정 확인 (aws configure list)
2. 리소스 생성 (aws service create-resource)
3. 생성 확인 (aws service describe-resource)
4. 태그 추가 (aws service tag-resource)
5. 설정 변경 (aws service modify-resource)
6. 상태 확인 (aws service describe-resource)
7. 리소스 테스트 (실제 사용)
8. 로그/메트릭 확인 (CloudWatch)
9. 정리 (aws service delete-resource)
10. 삭제 확인 (aws service describe-resource - 에러 확인)
```

## 🔧 명령어 작성 가이드

### 좋은 명령어 예시:

```bash
# Node.js 애플리케이션 파일 생성
# Express 서버를 3000번 포트에서 실행
cat > app.js << 'EOF'
const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {{
  res.json({{ message: 'Hello from Docker!' }});
}});

app.listen(PORT, () => {{
  console.log(`Server running on port ${{PORT}}`);
}});
EOF

# 파일 생성 확인
cat app.js
```

### 나쁜 명령어 예시:
```bash
# 애플리케이션 파일 생성 (구체적이지 않음)
vi app.js  # ❌ 내용이 없음

# 적절한 값으로 설정 (모호함)
docker run -p PORT:PORT image  # ❌ PORT가 무엇인지 불명확
```

## 📊 expected_output 작성 가이드

### 좋은 예시:
```
REPOSITORY          TAG       IMAGE ID       CREATED         SIZE
nodejs-app          v1        abc123def456   5 seconds ago   180MB
```

### 나쁜 예시:
```
이미지가 생성되었습니다  # ❌ 너무 추상적
```

## 🔍 verification 작성 가이드

### 좋은 예시:
```bash
# 컨테이너가 실행 중인지 확인
docker ps --filter "name=nodejs-container" --format "table {{{{.Names}}}}\\t{{{{.Status}}}}"

# 예상 출력:
# NAMES               STATUS
# nodejs-container    Up 10 seconds
```

### 나쁜 예시:
```bash
# 확인
docker ps  # ❌ 필터링 없이 모든 컨테이너 출력
```

## 🚨 troubleshooting 작성 가이드

### 좋은 예시:
```
- 포트 충돌 (Error: bind: address already in use): 
  다른 프로세스가 3000번 포트 사용 중. 
  해결: lsof -i :3000 으로 프로세스 확인 후 kill 또는 다른 포트 사용
  
- 이미지 빌드 실패 (npm install 에러):
  네트워크 문제 또는 package.json 오류.
  해결: docker build --no-cache 로 재시도, package.json 문법 확인
```

### 나쁜 예시:
```
- 에러 발생 시 재시도  # ❌ 어떤 에러인지, 어떻게 재시도하는지 불명확
```

## 📝 스텝 구조 상세 가이드

### step_number (정수)
- 1부터 시작하는 순차 번호
- 스텝 순서는 논리적 의존성을 따름

### title (문자열, 30-50자)
- 형식: "동사 + 목적어 (도구/명령어)"
- 예: "프로젝트 디렉토리 생성 (mkdir)", "Dockerfile 작성 (cat)", "이미지 빌드 (docker build)"
- 명확하고 구체적으로

### objective (문자열, 50-100자)
- 이 스텝을 수행하는 이유와 목표
- "~을 위해 ~을 수행합니다" 형식
- 예: "Docker 이미지를 빌드하기 위한 Dockerfile을 작성합니다. 멀티 스테이지 빌드를 사용하여 이미지 크기를 최적화합니다."

### commands (문자열, 멀티라인)
- 실제 실행 가능한 bash 명령어
- 주석 포함 (# 한글 설명)
- 한 스텝에 1-3개 명령어 (관련된 것만)
- heredoc 사용 시 EOF 구분자 명확히
- 변수 사용 시 예시 값 제공

### expected_output (문자열, 멀티라인)
- 명령어 실행 시 실제 출력되는 내용
- 테이블, JSON, 로그 형식 그대로 표현
- 중요한 부분만 발췌 (너무 길면 "..." 사용)
- 성공 메시지, 상태 코드, ID 등 포함

### verification (문자열, 멀티라인)
- 스텝 성공 여부를 확인하는 명령어
- 출력 필터링 (grep, awk, jq 등 활용)
- 예상 출력도 주석으로 포함
- 실패 시 명확한 에러 메시지

### troubleshooting (배열)
- 각 항목: "문제 상황: 원인. 해결: 구체적 방법"
- 최소 2개, 최대 4개
- 실제 발생 가능한 문제만
- 해결 방법은 명령어 또는 구체적 액션

## 🎯 스텝 개수 가이드

- **간단한 실습** (기본 개념, 단일 리소스): 5-7 스텝
- **표준 실습** (일반적인 워크플로우): 8-12 스텝
- **복잡한 실습** (멀티 컴포넌트, 통합): 13-15 스텝

스텝 개수는 실습 복잡도에 맞춰 자연스럽게 결정하세요.

## 📚 Prerequisites & Setup 가이드

### Prerequisites (사전 요구사항)
각 항목 형식:
```
소프트웨어명 버전+ 설명
  - 설치 가이드: [공식 문서 URL]
  - 설정 가이드: [공식 문서 URL] (필요 시)
  - 확인 방법: 명령어 (예: docker --version)
```

예시:
```
Docker Desktop 24.0+ 설치
  - 설치 가이드: https://docs.docker.com/desktop/install/
  - 확인: docker --version
  
AWS CLI 2.0+ 설치 및 설정
  - 설치: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  - 설정: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
  - 확인: aws --version && aws sts get-caller-identity
```

### Setup Instructions (환경 설정)
각 항목은 구체적인 설정 단계:
```
1. 설정 항목 (예: AWS 자격 증명 설정)
   - 명령어: aws configure
   - 입력 값: Access Key, Secret Key, Region, Output format
   - 공식 문서: [URL]
   - 확인: aws sts get-caller-identity
```

## ✅ 최종 체크리스트

생성 전 반드시 확인:
- [ ] 모든 명령어가 복사-붙여넣기로 실행 가능
- [ ] expected_output이 실제 출력과 일치
- [ ] 모든 스텝에 verification 명령어 포함
- [ ] troubleshooting이 구체적이고 실용적
- [ ] 기술별 표준 워크플로우 패턴 준수
- [ ] Prerequisites에 공식 문서 링크 포함
- [ ] Setup Instructions에 공식 문서 링크 포함
- [ ] 주석이 명확하고 도움이 됨
- [ ] 스텝 순서가 논리적이고 의존성이 명확
- [ ] completion_summary와 next_steps 포함

JSON 형식으로 응답하세요."""),
            ("user", """서비스: {service_name}

RAG 컨텍스트:
{rag_context}

## 🎯 실습 생성 지침

### 1단계: 기술 식별
서비스명과 RAG 컨텍스트를 분석하여 주요 기술을 식별하세요:
- Docker 관련: 컨테이너, 이미지, Dockerfile, Docker Compose
- Kubernetes 관련: Pod, Deployment, Service, Ingress, Helm
- Terraform 관련: HCL, Provider, Resource, Module, State
- AWS CLI 관련: EC2, S3, RDS, VPC, IAM 등 AWS 서비스

### 2단계: 워크플로우 선택
식별된 기술에 맞는 표준 워크플로우 패턴을 선택하세요:
- Docker: 8-12 스텝 (디렉토리 생성 → 파일 작성 → Dockerfile → 빌드 → 실행 → 테스트 → 정리)
- Kubernetes: 10-15 스텝 (네임스페이스 → YAML 작성 → apply → 상태 확인 → 테스트 → 정리)
- Terraform: 8-12 스텝 (디렉토리 → tf 파일 작성 → init → plan → apply → 확인 → destroy)
- AWS CLI: 8-12 스텝 (configure → create → describe → test → delete)

### 3단계: 명령어 검증
각 스텝의 명령어가 다음 기준을 만족하는지 확인:
- ✅ 복사-붙여넣기로 즉시 실행 가능
- ✅ 주석으로 "무엇을", "왜" 하는지 설명
- ✅ 플레이스홀더 사용 시 구체적 예시 제공
- ✅ heredoc (cat > file << 'EOF') 사용 시 EOF 구분자 명확
- ✅ 명령어 실행 순서가 논리적이고 의존성 명확

### 4단계: 출력 및 검증 작성
- expected_output: 실제 명령어 실행 시 나오는 출력 그대로
- verification: 성공 여부를 확인하는 구체적 명령어
- troubleshooting: 실제 발생 가능한 문제와 해결 방법

## 📋 JSON 응답 형식

다음 JSON 스키마로 정확히 응답하세요:

{{
  "title": "실습 제목 (예: Docker 컨테이너 기초 실습)",
  "purpose": "실습 목적 (50-100자)",
  "learning_objectives": [
    "학습 목표 1 (구체적으로)",
    "학습 목표 2 (측정 가능하게)",
    "학습 목표 3 (실무 적용 가능하게)"
  ],
  "estimated_time": "45분",
  "difficulty": "Beginner",
  "prerequisites": [
    "Docker Desktop 24.0+ 설치\\n  - 설치 가이드: https://docs.docker.com/desktop/install/\\n  - 확인: docker --version",
    "Node.js 18+ 설치 (로컬 테스트용)\\n  - 설치 가이드: https://nodejs.org/en/download/\\n  - 확인: node --version",
    "텍스트 에디터 (VS Code 권장)\\n  - 다운로드: https://code.visualstudio.com/download"
  ],
  "setup_instructions": [
    "Docker Desktop 실행 확인\\n  - 명령어: docker info\\n  - 공식 문서: https://docs.docker.com/desktop/",
    "작업 디렉토리 준비\\n  - 명령어: mkdir -p ~/docker-labs && cd ~/docker-labs\\n  - 권한 확인: ls -la"
  ],
  "steps": [
    {{
      "step_number": 1,
      "title": "프로젝트 디렉토리 생성 (mkdir)",
      "objective": "Docker 실습을 위한 작업 공간을 준비합니다.",
      "commands": "# 프로젝트 디렉토리 생성\\nmkdir docker-nodejs-app\\ncd docker-nodejs-app\\n\\n# 디렉토리 확인\\npwd",
      "expected_output": "/Users/username/docker-nodejs-app",
      "verification": "# 현재 디렉토리 확인\\nls -la\\n\\n# 예상: 빈 디렉토리 (. 와 .. 만 존재)",
      "troubleshooting": [
        "권한 오류 (Permission denied): sudo를 사용하거나 홈 디렉토리에서 실행하세요",
        "디렉토리 이미 존재: cd docker-nodejs-app 으로 이동하거나 다른 이름 사용"
      ]
    }},
    {{
      "step_number": 2,
      "title": "package.json 파일 생성 (cat)",
      "objective": "Node.js 애플리케이션의 의존성을 정의합니다.",
      "commands": "# package.json 생성\\n# Express 웹 프레임워크를 의존성으로 추가\\ncat > package.json << 'EOF'\\n{{\\n  \\"name\\": \\"docker-nodejs-app\\",\\n  \\"version\\": \\"1.0.0\\",\\n  \\"main\\": \\"server.js\\",\\n  \\"dependencies\\": {{\\n    \\"express\\": \\"^4.18.0\\"\\n  }}\\n}}\\nEOF\\n\\n# 파일 생성 확인\\ncat package.json",
      "expected_output": "{{\\n  \\"name\\": \\"docker-nodejs-app\\",\\n  \\"version\\": \\"1.0.0\\",\\n  \\"main\\": \\"server.js\\",\\n  \\"dependencies\\": {{\\n    \\"express\\": \\"^4.18.0\\"\\n  }}\\n}}",
      "verification": "# JSON 문법 검증 (jq 설치 시)\\njq . package.json\\n\\n# 또는 파일 존재 확인\\nls -l package.json",
      "troubleshooting": [
        "EOF 에러: heredoc 구문 확인, 'EOF'는 따옴표로 감싸야 함",
        "JSON 문법 오류: 중괄호, 쉼표, 따옴표 확인"
      ]
    }},
    {{
      "step_number": 3,
      "title": "server.js 파일 생성 (cat)",
      "objective": "Express 웹 서버 코드를 작성합니다.",
      "commands": "# server.js 생성\\n# 3000번 포트에서 실행되는 간단한 웹 서버\\ncat > server.js << 'EOF'\\nconst express = require('express');\\nconst app = express();\\nconst PORT = 3000;\\n\\napp.get('/', (req, res) => {{\\n  res.json({{ message: 'Hello from Docker!' }});\\n}});\\n\\napp.listen(PORT, () => {{\\n  console.log(`Server running on port ${{PORT}}`);\\n}});\\nEOF\\n\\n# 파일 확인\\ncat server.js",
      "expected_output": "const express = require('express');\\nconst app = express();\\nconst PORT = 3000;\\n\\napp.get('/', (req, res) => {{\\n  res.json({{ message: 'Hello from Docker!' }});\\n}});\\n\\napp.listen(PORT, () => {{\\n  console.log(`Server running on port ${{PORT}}`);\\n}});",
      "verification": "# 파일 존재 및 크기 확인\\nls -lh server.js\\n\\n# 문법 확인 (Node.js 설치 시)\\nnode --check server.js",
      "troubleshooting": [
        "문법 오류: 중괄호, 괄호, 세미콜론 확인",
        "포트 충돌 예상: 나중에 3000번 포트 사용 중이면 다른 포트로 변경"
      ]
    }},
    {{
      "step_number": 4,
      "title": "Dockerfile 작성 (cat)",
      "objective": "Docker 이미지를 빌드하기 위한 Dockerfile을 작성합니다.",
      "commands": "# Dockerfile 생성\\n# Node.js 18 베이스 이미지 사용\\ncat > Dockerfile << 'EOF'\\n# Node.js 18 공식 이미지\\nFROM node:18\\n\\n# 작업 디렉토리 설정\\nWORKDIR /app\\n\\n# package.json 복사 및 의존성 설치\\nCOPY package.json .\\nRUN npm install\\n\\n# 애플리케이션 코드 복사\\nCOPY server.js .\\n\\n# 포트 노출\\nEXPOSE 3000\\n\\n# 애플리케이션 실행\\nCMD [\\"node\\", \\"server.js\\"]\\nEOF\\n\\n# Dockerfile 확인\\ncat Dockerfile",
      "expected_output": "# Node.js 18 공식 이미지\\nFROM node:18\\n\\n# 작업 디렉토리 설정\\nWORKDIR /app\\n\\n# package.json 복사 및 의존성 설치\\nCOPY package.json .\\nRUN npm install\\n\\n# 애플리케이션 코드 복사\\nCOPY server.js .\\n\\n# 포트 노출\\nEXPOSE 3000\\n\\n# 애플리케이션 실행\\nCMD [\\"node\\", \\"server.js\\"]",
      "verification": "# Dockerfile 문법 검증\\ndocker build --check .\\n\\n# 또는 파일 확인\\nls -l Dockerfile",
      "troubleshooting": [
        "Dockerfile 문법 오류: instruction 대소문자 확인 (FROM, RUN, COPY 등)",
        "COPY 경로 오류: 현재 디렉토리에 파일이 있는지 확인"
      ]
    }},
    {{
      "step_number": 5,
      "title": "Docker 이미지 빌드 (docker build)",
      "objective": "Dockerfile로부터 Docker 이미지를 생성합니다.",
      "commands": "# Docker 이미지 빌드\\n# -t: 이미지 이름과 태그 지정\\n# .: 현재 디렉토리를 빌드 컨텍스트로 사용\\ndocker build -t nodejs-app:v1 .",
      "expected_output": "[+] Building 45.2s (10/10) FINISHED\\n => [1/5] FROM docker.io/library/node:18\\n => [2/5] WORKDIR /app\\n => [3/5] COPY package.json .\\n => [4/5] RUN npm install\\n => [5/5] COPY server.js .\\n => exporting to image\\nSuccessfully tagged nodejs-app:v1",
      "verification": "# 이미지 생성 확인\\ndocker images nodejs-app\\n\\n# 예상 출력:\\n# REPOSITORY    TAG    IMAGE ID       CREATED         SIZE\\n# nodejs-app    v1     abc123def456   5 seconds ago   180MB",
      "troubleshooting": [
        "빌드 실패 (npm install 에러): 네트워크 확인, package.json 문법 확인",
        "디스크 공간 부족: docker system prune 으로 불필요한 이미지 정리",
        "베이스 이미지 다운로드 실패: 인터넷 연결 확인, Docker Hub 접근 가능 여부 확인"
      ]
    }},
    {{
      "step_number": 6,
      "title": "이미지 상세 정보 확인 (docker images)",
      "objective": "빌드된 이미지의 크기와 정보를 확인합니다.",
      "commands": "# 이미지 목록 확인 (크기 포함)\\ndocker images nodejs-app --format \\"table {{{{.Repository}}}}\\\\t{{{{.Tag}}}}\\\\t{{{{.Size}}}}\\"",
      "expected_output": "REPOSITORY    TAG    SIZE\\nnodejs-app    v1     180MB",
      "verification": "# 이미지 히스토리 확인 (레이어 정보)\\ndocker history nodejs-app:v1\\n\\n# 각 레이어의 크기와 생성 명령어 확인 가능",
      "troubleshooting": [
        "이미지가 보이지 않음: docker images 로 전체 목록 확인",
        "이미지 크기가 너무 큼: 멀티 스테이지 빌드 또는 alpine 베이스 이미지 고려"
      ]
    }},
    {{
      "step_number": 7,
      "title": "컨테이너 실행 (docker run)",
      "objective": "빌드한 이미지로 컨테이너를 실행합니다.",
      "commands": "# 컨테이너 실행\\n# -d: 백그라운드 실행\\n# -p: 포트 매핑 (호스트:컨테이너)\\n# --name: 컨테이너 이름 지정\\ndocker run -d -p 3000:3000 --name nodejs-container nodejs-app:v1",
      "expected_output": "abc123def456789...\\n(컨테이너 ID 출력)",
      "verification": "# 컨테이너 상태 확인\\ndocker ps --filter \\"name=nodejs-container\\" --format \\"table {{{{.Names}}}}\\\\t{{{{.Status}}}}\\\\t{{{{.Ports}}\\\\"\\n\\n# 예상 출력:\\n# NAMES               STATUS              PORTS\\n# nodejs-container    Up 10 seconds       0.0.0.0:3000->3000/tcp",
      "troubleshooting": [
        "포트 충돌 (address already in use): lsof -i :3000 으로 프로세스 확인 후 종료 또는 다른 포트 사용",
        "컨테이너 즉시 종료: docker logs nodejs-container 로 에러 확인",
        "이미지를 찾을 수 없음: docker images 로 이미지 존재 확인"
      ]
    }},
    {{
      "step_number": 8,
      "title": "컨테이너 상태 확인 (docker ps)",
      "objective": "실행 중인 컨테이너의 상태를 확인합니다.",
      "commands": "# 실행 중인 컨테이너 목록\\ndocker ps\\n\\n# 또는 특정 컨테이너만\\ndocker ps -f name=nodejs-container",
      "expected_output": "CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                    NAMES\\nabc123def456   nodejs-app:v1   \\"node server.js\\"        30 seconds ago  Up 28 seconds  0.0.0.0:3000->3000/tcp   nodejs-container",
      "verification": "# 컨테이너 상세 정보\\ndocker inspect nodejs-container | grep -A 5 \\"State\\"\\n\\n# 실행 중이면 \\"Running\\": true 확인",
      "troubleshooting": [
        "컨테이너가 보이지 않음: docker ps -a 로 중지된 컨테이너 포함 확인",
        "STATUS가 Restarting: docker logs 로 에러 확인, 애플리케이션 코드 문제 가능성"
      ]
    }},
    {{
      "step_number": 9,
      "title": "애플리케이션 테스트 (curl)",
      "objective": "컨테이너에서 실행 중인 애플리케이션이 정상 동작하는지 확인합니다.",
      "commands": "# HTTP 요청 전송\\ncurl http://localhost:3000\\n\\n# 또는 JSON 포맷팅 (jq 설치 시)\\ncurl -s http://localhost:3000 | jq .",
      "expected_output": "{{\\"message\\":\\"Hello from Docker!\\"}}",
      "verification": "# 여러 번 요청하여 안정성 확인\\nfor i in {{1..5}}; do curl -s http://localhost:3000; echo; done\\n\\n# 모두 동일한 응답이 나와야 함",
      "troubleshooting": [
        "Connection refused: 컨테이너가 실행 중인지 확인 (docker ps)",
        "Empty reply: 애플리케이션이 시작되는 중일 수 있음, 5초 대기 후 재시도",
        "404 Not Found: 경로 확인, server.js의 라우트 설정 확인"
      ]
    }},
    {{
      "step_number": 10,
      "title": "로그 확인 (docker logs)",
      "objective": "컨테이너의 로그를 확인하여 애플리케이션 동작을 모니터링합니다.",
      "commands": "# 컨테이너 로그 확인\\ndocker logs nodejs-container\\n\\n# 실시간 로그 확인 (Ctrl+C로 종료)\\n# docker logs -f nodejs-container",
      "expected_output": "Server running on port 3000",
      "verification": "# 최근 10줄만 확인\\ndocker logs --tail 10 nodejs-container\\n\\n# 타임스탬프 포함\\ndocker logs -t nodejs-container",
      "troubleshooting": [
        "로그가 없음: 애플리케이션이 로그를 출력하지 않거나 즉시 종료됨",
        "에러 메시지 확인: npm 관련 에러는 package.json 확인, 코드 에러는 server.js 확인"
      ]
    }},
    {{
      "step_number": 11,
      "title": "컨테이너 정지 (docker stop)",
      "objective": "실행 중인 컨테이너를 안전하게 정지합니다.",
      "commands": "# 컨테이너 정지 (SIGTERM 전송, 10초 대기 후 SIGKILL)\\ndocker stop nodejs-container",
      "expected_output": "nodejs-container",
      "verification": "# 컨테이너 상태 확인\\ndocker ps -a -f name=nodejs-container --format \\"table {{{{.Names}}}}\\\\t{{{{.Status}}\\\\"\\n\\n# 예상: STATUS가 Exited (0) 또는 Exited (137)",
      "troubleshooting": [
        "정지 실패: docker kill nodejs-container 로 강제 종료",
        "이미 정지됨: docker ps -a 로 상태 확인"
      ]
    }},
    {{
      "step_number": 12,
      "title": "정리 (docker rm, docker rmi)",
      "objective": "실습에 사용한 컨테이너와 이미지를 삭제합니다.",
      "commands": "# 컨테이너 삭제\\ndocker rm nodejs-container\\n\\n# 이미지 삭제\\ndocker rmi nodejs-app:v1\\n\\n# 작업 디렉토리 삭제 (선택사항)\\ncd ..\\nrm -rf docker-nodejs-app",
      "expected_output": "nodejs-container\\nnodejs-app:v1",
      "verification": "# 컨테이너 삭제 확인\\ndocker ps -a | grep nodejs-container\\n# 출력 없음\\n\\n# 이미지 삭제 확인\\ndocker images | grep nodejs-app\\n# 출력 없음",
      "troubleshooting": [
        "컨테이너 삭제 실패 (still running): docker stop 먼저 실행",
        "이미지 삭제 실패 (in use): 해당 이미지를 사용하는 컨테이너 먼저 삭제",
        "디렉토리 삭제 실패: 권한 확인, sudo 사용 또는 수동 삭제"
      ]
    }}
  ],
  "completion_summary": "이 실습을 통해 Docker의 기본 워크플로우(이미지 빌드 → 컨테이너 실행 → 테스트 → 정리)를 경험했습니다. Dockerfile 작성, 이미지 빌드, 컨테이너 실행 및 관리의 전체 과정을 실습하며 Docker의 핵심 개념을 이해했습니다. 이제 간단한 애플리케이션을 Docker로 컨테이너화하고 실행할 수 있습니다.",
  "next_steps": [
    ".dockerignore 파일을 활용하여 이미지 크기 최적화하기",
    "멀티 스테이지 빌드로 프로덕션 이미지 만들기",
    "Docker Compose로 멀티 컨테이너 애플리케이션 구성하기",
    "Docker Hub에 이미지 푸시하고 공유하기",
    "환경 변수와 볼륨을 활용한 설정 관리 실습하기"
  ]
}}

## ⚠️ CRITICAL 요구사항

1. **기술별 패턴 준수**: 서비스명에서 기술을 식별하고 해당 기술의 표준 워크플로우 패턴을 따르세요
2. **명령어 실행 가능성**: 모든 명령어는 복사-붙여넣기로 즉시 실행 가능해야 합니다
3. **공식 문서 링크**: prerequisites와 setup_instructions에 반드시 공식 문서 링크를 포함하세요
4. **검증 가능성**: 모든 스텝에 구체적인 verification 명령어를 포함하세요
5. **실제 출력**: expected_output은 실제 명령어 실행 결과를 정확히 반영하세요
6. **스텝 개수 유연성**: 5-15 스텝 범위에서 실습 복잡도에 맞게 조정하세요
7. **필수 필드**: completion_summary와 next_steps는 반드시 포함하세요

위 예시는 Docker 실습입니다. 서비스가 Kubernetes, Terraform, AWS CLI 등이면 해당 기술의 패턴을 따르세요.""")
        ])
        
        chain = prompt | self.llm
        
        # Use retry logic from BaseAgent
        from src.agents.base_agent import BaseAgent
        base_agent = BaseAgent(
            name="HandsOnLabAgent",
            collection_name="",
            system_prompt=""
        )
        
        # First attempt to generate
        try:
            lab = base_agent.generate_with_retry(
                chain=chain,
                input_dict={
                    "service_name": service_name,
                    "rag_context": rag_context[:8000]
                },
                validator_func=self._validate_handson_steps,
                error_context=f"Hands-on Lab for {service_name}"
            )
            return lab
            
        except ValueError as e:
            # If completion_summary or next_steps are missing, generate them with RAG
            if "completion_summary" in str(e) or "next_steps" in str(e):
                print(f"  ⚠️ Missing required fields, attempting to generate with RAG...")
                
                # Try one more time with the chain
                response = chain.invoke({
                    "service_name": service_name,
                    "rag_context": rag_context[:8000]
                })
                
                try:
                    data = json.loads(response.content)
                    
                    # Generate missing fields with RAG
                    if "completion_summary" not in data or not data["completion_summary"]:
                        data["completion_summary"] = self._generate_completion_summary(
                            service_name, data, rag_context
                        )
                    
                    if "next_steps" not in data or not data["next_steps"]:
                        data["next_steps"] = self._generate_next_steps(
                            service_name, data, rag_context
                        )
                    
                    # Validate again
                    return self._validate_handson_steps(data)
                    
                except Exception as inner_e:
                    print(f"  ❌ Failed to generate missing fields: {inner_e}")
                    raise
            else:
                raise
    
    def _validate_handson_steps(self, data: dict) -> HandsOnLab:
        """Validate and fix hands-on lab data structure with step padding"""
        
        # Validate required fields
        required_fields = ["title", "purpose", "learning_objectives", "estimated_time", 
                          "difficulty", "prerequisites", "setup_instructions", "steps"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate and fix steps structure
        if isinstance(data["steps"], dict):
            steps_list = []
            for key, value in sorted(data["steps"].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0):
                if isinstance(value, dict):
                    if "step_number" not in value:
                        value["step_number"] = int(key) if key.isdigit() else len(steps_list) + 1
                    steps_list.append(value)
            data["steps"] = steps_list
        
        # Validate and fix each step
        valid_steps = []
        required_step_fields = ["step_number", "title", "objective"]
        
        for i, s in enumerate(data["steps"], 1):
            if isinstance(s, dict):
                # Fix step number
                if "step_number" not in s or s["step_number"] != i:
                    s["step_number"] = i
                
                # Fix commands field if it's a list
                if "commands" in s and isinstance(s["commands"], list):
                    s["commands"] = "\n".join(s["commands"])
                
                # Fix expected_output field if it's a list
                if "expected_output" in s and isinstance(s["expected_output"], list):
                    s["expected_output"] = "\n".join(s["expected_output"])
                
                # Fix verification field if it's a list
                if "verification" in s and isinstance(s["verification"], list):
                    s["verification"] = "\n".join(s["verification"])
                
                # Validate required fields
                if all(k in s for k in required_step_fields):
                    valid_steps.append(s)
        
        data["steps"] = valid_steps
        
        # Validate minimum step count (flexible: 5-15)
        if len(data["steps"]) < 5:
            raise ValueError(f"Only {len(data['steps'])} steps generated, need at least 5")
        
        # Pad steps if needed (only if less than 7 but at least 5)
        # This ensures we have a reasonable number of steps without forcing exactly 7
        if 5 <= len(data["steps"]) < 7:
            print(f"  ⚠️ Only {len(data['steps'])} steps, padding to 7...")
            data["steps"] = self._pad_steps(data["steps"], target_count=7)
        
        # Validate completion_summary and next_steps
        if "completion_summary" not in data or not data["completion_summary"]:
            raise ValueError("Missing required field: completion_summary")
        
        if "next_steps" not in data or not data["next_steps"]:
            raise ValueError("Missing required field: next_steps")
        
        return HandsOnLab(**data)
    
    def _pad_steps(self, steps: list, target_count: int = 7) -> list:
        """Pad steps to reach target count by splitting complex steps"""
        
        if len(steps) >= target_count:
            return steps
        
        padded_steps = []
        steps_needed = target_count - len(steps)
        
        # Find steps that can be split (steps with multiple commands or long verification)
        splittable_indices = []
        for i, step in enumerate(steps):
            commands = step.get("commands", "")
            verification = step.get("verification", "")
            
            # Check if step has multiple commands or complex verification
            if commands.count('\n') > 2 or verification.count('\n') > 1:
                splittable_indices.append(i)
        
        # If we have enough splittable steps, split them
        if len(splittable_indices) >= steps_needed:
            split_indices = set(splittable_indices[:steps_needed])
            
            for i, step in enumerate(steps):
                if i in split_indices:
                    # Split this step into two
                    commands = step.get("commands", "").split('\n')
                    mid = len(commands) // 2
                    
                    # First half
                    step1 = step.copy()
                    step1["commands"] = '\n'.join(commands[:mid])
                    step1["title"] = f"{step['title']} (Part 1)"
                    padded_steps.append(step1)
                    
                    # Second half
                    step2 = step.copy()
                    step2["commands"] = '\n'.join(commands[mid:])
                    step2["title"] = f"{step['title']} (Part 2)"
                    padded_steps.append(step2)
                else:
                    padded_steps.append(step)
        else:
            # Not enough splittable steps, add verification steps
            for i, step in enumerate(steps):
                padded_steps.append(step)
                
                # Add verification step after certain steps
                if i < steps_needed and step.get("verification"):
                    verify_step = {
                        "step_number": len(padded_steps) + 1,
                        "title": f"{step['title']} 확인",
                        "objective": f"{step['title']} 단계가 정상적으로 완료되었는지 확인합니다.",
                        "commands": step.get("verification", ""),
                        "expected_output": "정상 동작 확인",
                        "verification": "",
                        "troubleshooting": []
                    }
                    padded_steps.append(verify_step)
        
        # Renumber steps
        for i, step in enumerate(padded_steps, 1):
            step["step_number"] = i
        
        return padded_steps[:target_count]
    
    def _generate_completion_summary(
        self, 
        service_name: str, 
        lab_data: dict, 
        rag_context: str
    ) -> str:
        """RAG 기반으로 completion_summary 생성"""
        
        # Extract key information from lab data
        title = lab_data.get("title", "")
        purpose = lab_data.get("purpose", "")
        objectives = lab_data.get("learning_objectives", [])
        steps_summary = "\n".join([
            f"- {step.get('title', '')}" 
            for step in lab_data.get("steps", [])[:5]  # First 5 steps
        ])
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 DevOps 교육 전문가입니다.
실습 완료 요약(completion_summary)을 작성하세요.

요약에는 다음을 포함해야 합니다:
1. 실습을 통해 달성한 구체적인 내용
2. 습득한 핵심 기술과 개념
3. 실무에서 활용할 수 있는 포인트

2-3문장으로 간결하게 작성하세요. 한글로 작성하세요."""),
            ("user", """서비스: {service_name}

실습 제목: {title}
실습 목적: {purpose}

학습 목표:
{objectives}

주요 실습 단계:
{steps_summary}

RAG 컨텍스트:
{rag_context}

위 정보를 바탕으로 실습 완료 요약을 작성하세요. JSON 없이 텍스트만 반환하세요.""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "service_name": service_name,
            "title": title,
            "purpose": purpose,
            "objectives": "\n".join([f"- {obj}" for obj in objectives]),
            "steps_summary": steps_summary,
            "rag_context": rag_context[:2000]
        })
        
        summary = response.content.strip()
        # Remove JSON formatting if present
        summary = summary.replace('"', '').replace('{', '').replace('}', '')
        
        return summary
    
    def _generate_next_steps(
        self, 
        service_name: str, 
        lab_data: dict, 
        rag_context: str
    ) -> list:
        """RAG 기반으로 next_steps 생성"""
        
        title = lab_data.get("title", "")
        purpose = lab_data.get("purpose", "")
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 DevOps 교육 전문가입니다.
실습 후 다음 학습 단계(next_steps)를 제안하세요.

다음 단계는:
1. 실습 내용을 심화하는 추가 학습
2. 관련 기술이나 서비스와의 통합
3. 실무 적용을 위한 고급 주제

3-5개 항목을 제안하세요. 한글로 작성하세요.

JSON 배열 형식으로 응답하세요: ["항목1", "항목2", "항목3"]"""),
            ("user", """서비스: {service_name}

실습 제목: {title}
실습 목적: {purpose}

RAG 컨텍스트:
{rag_context}

위 정보를 바탕으로 다음 학습 단계를 제안하세요.""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "service_name": service_name,
            "title": title,
            "purpose": purpose,
            "rag_context": rag_context[:2000]
        })
        
        try:
            # Try to parse as JSON array
            next_steps = json.loads(response.content)
            if isinstance(next_steps, list):
                return next_steps[:5]  # Max 5 items
        except:
            pass
        
        # Fallback: parse as text lines
        lines = response.content.strip().split('\n')
        next_steps = []
        for line in lines:
            line = line.strip()
            # Remove list markers
            line = line.lstrip('- ').lstrip('* ').lstrip('• ')
            line = line.lstrip('1234567890. ')
            if line and len(line) > 10:
                next_steps.append(line)
        
        # Ensure we have at least 3 items
        if len(next_steps) < 3:
            next_steps.extend([
                f"{service_name} 공식 문서를 참고하여 추가 기능 학습",
                "실습 내용을 바탕으로 개인 프로젝트 구성",
                "관련 서비스와의 통합 실습"
            ])
        
        return next_steps[:5]  # Max 5 items
    
    def format_step_markdown(
        self, 
        step: HandsOnStep, 
        step_num: int, 
        lab: HandsOnLab,
        service_name: str,
        rag_context: str
    ) -> str:
        """Format a single step as markdown with <details> tags and infographics"""
        md = f"# Hands-on Lab - Step {step_num}\n\n"
        
        # Add lab context on first step
        if step_num == 1:
            md += "## 실습 개요\n\n"
            md += f"**제목**: {lab.title}\n\n"
            md += f"**목적**: {lab.purpose}\n\n"
            md += "**학습 목표**:\n"
            for obj in lab.learning_objectives:
                md += f"- {obj}\n"
            md += f"\n**예상 소요 시간**: {lab.estimated_time}\n\n"
            md += f"**난이도**: {lab.difficulty}\n\n"
            
            # Generate infographic for hands-on flow
            print("  📊 Generating infographic for hands-on lab flow...")
            lab_context = f"{lab.title}\n{lab.purpose}\n" + "\n".join([f"Step {i}: {s.title}" for i, s in enumerate(lab.steps, 1)])
            lab_infographic = self.infographic_agent.generate(
                service_name=service_name,
                context=lab_context,
                section_type="hands_on",
                rag_context=rag_context
            )
            md += "### 실습 흐름도\n\n"
            md += self.infographic_agent.format_markdown(lab_infographic)
            md += "\n"
            
            md += "## 사전 요구사항\n\n"
            md += "<details>\n"
            md += "<summary>사전 요구사항 보기</summary>\n\n"
            for req in lab.prerequisites:
                md += f"- {req}\n"
            md += "\n</details>\n\n"
            
            md += "## 환경 설정\n\n"
            md += "<details>\n"
            md += "<summary>환경 설정 보기</summary>\n\n"
            for setup in lab.setup_instructions:
                md += f"{setup}\n\n"
            md += "</details>\n\n"
            
            md += "---\n\n"
        
        md += f"## Step {step_num}: {step.title}\n\n"
        
        md += f"**목표**: {step.objective}\n\n"
        
        if step.commands:
            md += "**명령어**:\n"
            md += "<details>\n"
            md += "<summary>명령어 보기</summary>\n\n"
            md += "```bash\n"
            md += f"{step.commands}\n"
            md += "```\n\n"
            md += "</details>\n\n"
        
        if step.expected_output:
            md += "**예상 출력**:\n"
            md += "<details>\n"
            md += "<summary>예상 출력 보기</summary>\n\n"
            md += "```\n"
            md += f"{step.expected_output}\n"
            md += "```\n\n"
            md += "</details>\n\n"
        
        if step.verification:
            md += "**확인 방법**:\n"
            md += "<details>\n"
            md += "<summary>확인 방법 보기</summary>\n\n"
            md += "```bash\n"
            md += f"{step.verification}\n"
            md += "```\n\n"
            md += "</details>\n\n"
        
        if step.troubleshooting:
            md += "**문제 해결**:\n"
            md += "<details>\n"
            md += "<summary>문제 해결 보기</summary>\n\n"
            for ts in step.troubleshooting:
                md += f"- {ts}\n"
            md += "\n</details>\n\n"
        
        # Add completion info on last step
        if step_num == len(lab.steps):
            md += "---\n\n"
            md += "## 실습 완료\n\n"
            md += f"{lab.completion_summary}\n\n"
            
            if lab.next_steps:
                md += "**다음 단계**:\n"
                for ns in lab.next_steps:
                    md += f"- {ns}\n"
                md += "\n"
        
        return md
