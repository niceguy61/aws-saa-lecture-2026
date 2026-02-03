# DevOps 엔지니어 양성 과정 (6개월)
## Docker, Kubernetes, AWS, MSA, CI/CD, FinOps, Terraform

---

## 📋 과정 개요

**교육 대상**: 비전공자, 대학 막학기 학생  
**교육 기간**: 6개월 (주 5일, 일 8시간)  
**총 교육 시간**: 약 960시간  
**교육 목표**: 실무 중심의 DevOps 엔지니어 양성

---

## 📚 월별 커리큘럼 개요

### 1개월차: DevOps & Docker 기초
- DevOps 개념 및 문화 이해
- Docker 기본 및 심화 (Compose, Swarm)
- 컨테이너 기반 애플리케이션 개발

### 2개월차: AWS 클라우드 기초
- AWS 핵심 서비스 학습
- AWS 네트워킹 및 보안
- AWS 컨테이너 서비스

### 3개월차: Kubernetes 기초 및 실습
- Kubernetes 아키텍처 및 개념
- Kubernetes 핵심 리소스 실습
- 클라우드 네이티브 Kubernetes (EKS, GKE, AKS)

### 4개월차: Kubernetes 심화 및 Service Mesh
- Kubernetes 고급 기능
- Istio Service Mesh
- Kubernetes 운영 및 모니터링

### 5개월차: CI/CD 및 GitOps
- CI/CD 파이프라인 구축
- 다양한 CI/CD 도구 실습
- ArgoCD를 통한 GitOps 구현

### 6개월차: Terraform 및 FinOps
- Infrastructure as Code (Terraform)
- AWS 리소스 자동화
- FinOps 및 비용 최적화

---


## 📅 1개월차: DevOps & Docker 기초

### 1주차: DevOps 기본 이론 및 환경 구성

#### Day 1: DevOps 개요 및 문화
- **오전 (4시간)**
  - DevOps란 무엇인가?
  - DevOps의 역사와 필요성
  - DevOps 문화와 철학 (CALMS 모델)
  - 전통적 개발 방식 vs DevOps
- **오후 (4시간)**
  - DevOps 생명주기 (Plan → Code → Build → Test → Release → Deploy → Operate → Monitor)
  - DevOps 도구 생태계 개요
  - 실습 환경 구성 (Linux, Git, IDE)
  - Git 기본 명령어 실습

#### Day 2: 컨테이너 기술 개요 및 Docker 소개
- **오전 (4시간)**
  - 가상화 vs 컨테이너화
  - 컨테이너 기술의 역사
  - Docker 아키텍처 (Docker Engine, Docker Daemon, Docker CLI)
  - Docker 설치 (Windows, macOS, Linux)
- **오후 (4시간)**
  - Docker Hub 소개
  - 첫 번째 컨테이너 실행 (hello-world, nginx)
  - Docker 기본 명령어 (run, ps, stop, rm, images)
  - 실습: 간단한 웹 서버 컨테이너 실행

#### Day 3: Docker 이미지 기초
- **오전 (4시간)**
  - Docker 이미지란?
  - 이미지 레이어 구조
  - Docker Hub에서 이미지 검색 및 다운로드
  - 이미지 태그 관리
- **오후 (4시간)**
  - Dockerfile 기본 문법
  - FROM, RUN, COPY, ADD, CMD, ENTRYPOINT
  - 첫 번째 Dockerfile 작성
  - 실습: Node.js 애플리케이션 이미지 빌드

#### Day 4: Docker 컨테이너 관리
- **오전 (4시간)**
  - 컨테이너 생명주기 관리
  - 포트 매핑 (-p 옵션)
  - 볼륨 마운트 (-v 옵션)
  - 환경 변수 설정 (-e 옵션)
- **오후 (4시간)**
  - 컨테이너 로그 확인
  - 컨테이너 내부 접속 (exec)
  - 컨테이너 리소스 제한
  - 실습: 데이터베이스 컨테이너 실행 및 데이터 영속성

#### Day 5: Docker 네트워킹 기초
- **오전 (4시간)**
  - Docker 네트워크 종류 (bridge, host, none)
  - 사용자 정의 네트워크 생성
  - 컨테이너 간 통신
  - 네트워크 검사 및 디버깅
- **오후 (4시간)**
  - 실습: 멀티 컨테이너 애플리케이션 (웹 + DB)
  - 컨테이너 링크
  - 주간 복습 및 Q&A
  - 미니 프로젝트: 간단한 3-tier 애플리케이션 컨테이너화

---

### 2주차: Docker 심화 - Dockerfile 최적화 및 이미지 관리

#### Day 6: Dockerfile 최적화
- **오전 (4시간)**
  - 멀티 스테이지 빌드
  - 이미지 크기 최적화 기법
  - 레이어 캐싱 활용
  - .dockerignore 파일 활용
- **오후 (4시간)**
  - 베이스 이미지 선택 전략 (alpine, slim)
  - 보안 모범 사례
  - 실습: 프로덕션 레벨 Dockerfile 작성
  - 이미지 스캔 및 취약점 검사

#### Day 7: Docker Registry 및 이미지 배포
- **오전 (4시간)**
  - Docker Hub 심화
  - 프라이빗 레지스트리 구축
  - 이미지 태깅 전략
  - 이미지 푸시/풀
- **오후 (4시간)**
  - GitHub Container Registry (GHCR)
  - AWS ECR 소개
  - 실습: 프라이빗 레지스트리에 이미지 배포
  - 이미지 버전 관리 전략

#### Day 8: Docker Compose 기초
- **오전 (4시간)**
  - Docker Compose란?
  - docker-compose.yml 파일 구조
  - 서비스, 네트워크, 볼륨 정의
  - Compose 기본 명령어 (up, down, ps, logs)
- **오후 (4시간)**
  - 환경 변수 및 .env 파일
  - 의존성 관리 (depends_on)
  - 실습: 웹 애플리케이션 + 데이터베이스 + Redis 구성
  - 헬스체크 설정

#### Day 9: Docker Compose 심화
- **오전 (4시간)**
  - 멀티 컨테이너 애플리케이션 오케스트레이션
  - 볼륨 및 네트워크 고급 설정
  - 스케일링 (scale)
  - 오버라이드 파일 활용
- **오후 (4시간)**
  - 개발/프로덕션 환경 분리
  - 실습: 마이크로서비스 아키텍처 구성
  - 로깅 및 모니터링 설정
  - Compose 프로젝트 관리

#### Day 10: Docker Swarm 소개
- **오전 (4시간)**
  - Docker Swarm이란?
  - Swarm vs Kubernetes 비교
  - Swarm 클러스터 구성 (Manager, Worker 노드)
  - Swarm 초기화 및 노드 추가
- **오후 (4시간)**
  - 서비스 배포 및 관리
  - 스택 배포 (docker stack deploy)
  - 롤링 업데이트
  - 실습: Swarm 클러스터에 애플리케이션 배포

---

### 3주차: Docker 실전 프로젝트 및 MSA 기초

#### Day 11: Docker 보안
- **오전 (4시간)**
  - 컨테이너 보안 모범 사례
  - 루트리스 컨테이너
  - 시크릿 관리
  - 네트워크 보안
- **오후 (4시간)**
  - 이미지 서명 및 검증
  - 보안 스캔 도구 (Trivy, Clair)
  - 실습: 보안 강화된 컨테이너 구성
  - 컴플라이언스 체크

#### Day 12: 마이크로서비스 아키텍처 (MSA) 개요
- **오전 (4시간)**
  - 모놀리식 vs 마이크로서비스
  - MSA의 장단점
  - MSA 설계 원칙
  - 서비스 분해 전략
- **오후 (4시간)**
  - MSA 디자인 패턴 (API Gateway, Service Discovery, Circuit Breaker)
  - 데이터 관리 전략
  - 이벤트 기반 아키텍처
  - 실습: 간단한 MSA 설계

#### Day 13: MSA 통신 패턴
- **오전 (4시간)**
  - 동기 통신 (REST, gRPC)
  - 비동기 통신 (메시지 큐)
  - 서비스 간 인증/인가
  - API 버저닝
- **오후 (4시간)**
  - 실습: REST API 기반 마이크로서비스 구현
  - 서비스 메시 개념 소개
  - 분산 트랜잭션 패턴 (Saga, 2PC)
  - 에러 핸들링 및 재시도 전략

#### Day 14: Docker 기반 MSA 구현
- **오전 (4시간)**
  - 마이크로서비스 컨테이너화
  - API Gateway 구성 (Nginx, Traefik)
  - 서비스 디스커버리
  - 로드 밸런싱
- **오후 (4시간)**
  - 실습: 3개 이상의 마이크로서비스 구성
  - 서비스 간 통신 구현
  - 중앙 집중식 로깅
  - 분산 추적 기초

#### Day 15: 1개월차 종합 프로젝트
- **오전 (4시간)**
  - 프로젝트 요구사항 분석
  - 아키텍처 설계
  - 서비스 분해 및 역할 정의
  - Docker Compose 파일 작성
- **오후 (4시간)**
  - 프로젝트 구현 및 테스트
  - 문제 해결 및 디버깅
  - 프로젝트 발표 및 코드 리뷰
  - 1개월차 복습 및 Q&A

---

### 4주차: Docker 고급 주제 및 실전 운영

#### Day 16: Docker 모니터링 및 로깅
- **오전 (4시간)**
  - 컨테이너 메트릭 수집
  - Docker stats 및 모니터링 도구
  - 로깅 드라이버
  - 중앙 집중식 로깅 (ELK Stack 소개)
- **오후 (4시간)**
  - 실습: Prometheus + Grafana로 컨테이너 모니터링
  - 알림 설정
  - 로그 분석
  - 성능 튜닝

#### Day 17: Docker 성능 최적화
- **오전 (4시간)**
  - 컨테이너 리소스 제한 및 할당
  - CPU, 메모리 최적화
  - 스토리지 드라이버 선택
  - 네트워크 성능 최적화
- **오후 (4시간)**
  - 빌드 캐시 최적화
  - 이미지 레이어 최적화
  - 실습: 성능 벤치마킹
  - 병목 현상 분석 및 해결

#### Day 18: Docker 트러블슈팅
- **오전 (4시간)**
  - 일반적인 Docker 문제 및 해결
  - 컨테이너 디버깅 기법
  - 네트워크 문제 해결
  - 스토리지 문제 해결
- **오후 (4시간)**
  - 로그 분석을 통한 문제 진단
  - 실습: 다양한 시나리오 트러블슈팅
  - 성능 문제 진단
  - 복구 전략

#### Day 19: Docker 실전 운영 사례
- **오전 (4시간)**
  - 프로덕션 환경 Docker 운영
  - CI/CD 파이프라인에서의 Docker
  - 블루-그린 배포
  - 카나리 배포
- **오후 (4시간)**
  - 백업 및 복구 전략
  - 재해 복구 계획
  - 실습: 무중단 배포 시나리오
  - 운영 자동화

#### Day 20: 1개월차 최종 평가 및 복습
- **오전 (4시간)**
  - 1개월차 전체 내용 복습
  - 핵심 개념 정리
  - 실전 문제 풀이
  - 모의 면접 (Docker 관련)
- **오후 (4시간)**
  - 최종 프로젝트 발표
  - 피드백 및 개선 사항 논의
  - 2개월차 과정 소개
  - 학습 로드맵 점검

---


## 📅 2개월차: AWS 클라우드 기초

### 5주차: AWS 기본 이해 및 핵심 서비스

#### Day 21: AWS 클라우드 개요
- **오전 (4시간)**
  - 클라우드 컴퓨팅이란?
  - AWS 소개 및 글로벌 인프라
  - AWS 리전, 가용 영역, 엣지 로케이션
  - AWS 계정 생성 및 초기 설정
- **오후 (4시간)**
  - AWS Management Console 탐색
  - AWS CLI 설치 및 설정
  - IAM 기초 (사용자, 그룹, 역할, 정책)
  - 실습: IAM 사용자 생성 및 권한 설정

#### Day 22: AWS 컴퓨팅 서비스 - EC2
- **오전 (4시간)**
  - Amazon EC2 개요
  - 인스턴스 타입 및 선택 기준
  - AMI (Amazon Machine Image)
  - EC2 인스턴스 생성 및 연결
- **오후 (4시간)**
  - 보안 그룹 설정
  - 키 페어 관리
  - 실습: 웹 서버 EC2 인스턴스 구성
  - EC2 인스턴스 모니터링 및 관리

#### Day 23: AWS 스토리지 서비스
- **오전 (4시간)**
  - Amazon S3 개요 및 버킷 생성
  - S3 스토리지 클래스
  - S3 버전 관리 및 수명 주기 정책
  - S3 보안 및 액세스 제어
- **오후 (4시간)**
  - EBS (Elastic Block Store) 볼륨
  - EBS 스냅샷 및 백업
  - 실습: S3 정적 웹사이트 호스팅
  - 실습: EC2에 EBS 볼륨 연결

#### Day 24: AWS 데이터베이스 서비스
- **오전 (4시간)**
  - Amazon RDS 개요
  - RDS 데이터베이스 엔진 (MySQL, PostgreSQL, etc.)
  - RDS 인스턴스 생성 및 구성
  - 다중 AZ 배포
- **오후 (4시간)**
  - RDS 백업 및 복원
  - 읽기 전용 복제본
  - 실습: RDS MySQL 데이터베이스 생성 및 연결
  - Amazon DynamoDB 소개

#### Day 25: AWS 네트워킹 기초 - VPC
- **오전 (4시간)**
  - Amazon VPC 개요
  - 서브넷 (Public, Private)
  - 라우팅 테이블
  - 인터넷 게이트웨이
- **오후 (4시간)**
  - NAT 게이트웨이
  - 보안 그룹 vs NACL
  - 실습: 사용자 정의 VPC 생성
  - 실습: 3-tier 아키텍처 네트워크 구성

---

### 6주차: AWS 네트워킹 및 로드 밸런싱

#### Day 26: AWS 로드 밸런싱
- **오전 (4시간)**
  - Elastic Load Balancer (ELB) 개요
  - ALB (Application Load Balancer)
  - NLB (Network Load Balancer)
  - CLB (Classic Load Balancer)
- **오후 (4시간)**
  - 타겟 그룹 및 헬스 체크
  - 실습: ALB를 통한 웹 애플리케이션 로드 밸런싱
  - SSL/TLS 인증서 설정
  - 고급 라우팅 규칙

#### Day 27: AWS Auto Scaling
- **오전 (4시간)**
  - Auto Scaling 개요
  - Launch Template vs Launch Configuration
  - Auto Scaling 그룹 생성
  - 스케일링 정책 (동적, 예약, 예측)
- **오후 (4시간)**
  - 실습: Auto Scaling 그룹 구성
  - ALB와 Auto Scaling 통합
  - 스케일링 시나리오 테스트
  - 비용 최적화 전략

#### Day 28: AWS Route 53 및 CloudFront
- **오전 (4시간)**
  - Amazon Route 53 개요
  - DNS 기초
  - 호스팅 영역 및 레코드 세트
  - 라우팅 정책 (Simple, Weighted, Latency, Failover)
- **오후 (4시간)**
  - Amazon CloudFront 개요
  - CDN 개념 및 이점
  - CloudFront 배포 생성
  - 실습: S3 + CloudFront로 글로벌 콘텐츠 배포

#### Day 29: AWS 보안 서비스
- **오전 (4시간)**
  - AWS 공동 책임 모델
  - IAM 심화 (정책 작성, 역할 위임)
  - AWS KMS (Key Management Service)
  - AWS Secrets Manager
- **오후 (4시간)**
  - AWS WAF (Web Application Firewall)
  - AWS Shield (DDoS 방어)
  - 실습: 보안 강화된 웹 애플리케이션 구성
  - 보안 모범 사례

#### Day 30: AWS 모니터링 및 로깅
- **오전 (4시간)**
  - Amazon CloudWatch 개요
  - 메트릭 및 알람
  - CloudWatch Logs
  - CloudWatch Dashboards
- **오후 (4시간)**
  - AWS CloudTrail
  - AWS Config
  - 실습: 종합 모니터링 대시보드 구성
  - 로그 분석 및 알림 설정

---

### 7주차: AWS 컨테이너 서비스

#### Day 31: AWS 컨테이너 서비스 개요
- **오전 (4시간)**
  - AWS 컨테이너 서비스 비교 (ECS, EKS, Fargate)
  - 각 서비스의 장단점 및 사용 사례
  - 컨테이너 오케스트레이션 필요성
  - AWS 컨테이너 로드맵
- **오후 (4시간)**
  - Amazon ECR (Elastic Container Registry)
  - ECR 리포지토리 생성
  - 이미지 푸시/풀
  - 실습: Docker 이미지를 ECR에 배포

#### Day 32: Amazon ECS 기초
- **오전 (4시간)**
  - Amazon ECS 아키텍처
  - 클러스터, 태스크 정의, 서비스
  - ECS 실행 타입 (EC2, Fargate)
  - ECS 클러스터 생성
- **오후 (4시간)**
  - 태스크 정의 작성
  - 서비스 배포
  - 실습: ECS에 컨테이너 애플리케이션 배포
  - 로드 밸런서 통합

#### Day 33: AWS Fargate
- **오전 (4시간)**
  - AWS Fargate 개요
  - 서버리스 컨테이너
  - Fargate vs EC2 비교
  - Fargate 태스크 정의
- **오후 (4시간)**
  - 실습: Fargate로 서버리스 컨테이너 실행
  - 네트워킹 및 보안 설정
  - 비용 분석
  - 사용 사례 및 모범 사례

#### Day 34: Amazon EKS 소개
- **오전 (4시간)**
  - Amazon EKS 개요
  - EKS 아키텍처
  - EKS vs 자체 관리 Kubernetes
  - EKS 클러스터 생성 준비
- **오후 (4시간)**
  - eksctl 도구 소개
  - kubectl 설정
  - 실습: EKS 클러스터 생성
  - 노드 그룹 구성

#### Day 35: AWS 컨테이너 서비스 실습
- **오전 (4시간)**
  - ECS vs EKS 실전 비교
  - 마이그레이션 시나리오
  - 실습: 동일 애플리케이션을 ECS와 EKS에 배포
  - 성능 및 비용 비교
- **오후 (4시간)**
  - AWS App Mesh 소개
  - 컨테이너 보안 모범 사례
  - 주간 복습 및 Q&A
  - 미니 프로젝트: AWS 컨테이너 서비스 활용

---

### 8주차: AWS 고급 서비스 및 2개월차 종합

#### Day 36: AWS Lambda 및 서버리스
- **오전 (4시간)**
  - AWS Lambda 개요
  - 서버리스 아키텍처
  - Lambda 함수 생성 및 배포
  - 트리거 및 이벤트 소스
- **오후 (4시간)**
  - API Gateway 통합
  - 실습: 서버리스 REST API 구축
  - Lambda 레이어 및 환경 변수
  - 비용 최적화

#### Day 37: AWS 메시징 서비스
- **오전 (4시간)**
  - Amazon SQS (Simple Queue Service)
  - Amazon SNS (Simple Notification Service)
  - Amazon EventBridge
  - 메시징 패턴
- **오후 (4시간)**
  - 실습: SQS + Lambda로 비동기 처리
  - 실습: SNS를 통한 알림 시스템
  - 이벤트 기반 아키텍처 구현
  - 마이크로서비스 통신

#### Day 38: AWS 인프라 자동화 기초
- **오전 (4시간)**
  - AWS CloudFormation 개요
  - 템플릿 구조 (YAML, JSON)
  - 스택 생성 및 관리
  - 파라미터 및 출력
- **오후 (4시간)**
  - 실습: CloudFormation으로 VPC 구성
  - 스택 업데이트 및 롤백
  - 중첩 스택
  - CloudFormation vs Terraform 비교

#### Day 39: AWS 비용 관리 및 최적화
- **오전 (4시간)**
  - AWS 요금 모델
  - AWS Cost Explorer
  - AWS Budgets
  - 비용 할당 태그
- **오후 (4시간)**
  - Reserved Instances vs Savings Plans
  - Spot Instances 활용
  - 실습: 비용 최적화 전략 수립
  - FinOps 기초 개념

#### Day 40: 2개월차 종합 프로젝트
- **오전 (4시간)**
  - 프로젝트: AWS 기반 3-tier 웹 애플리케이션 구축
  - VPC, EC2, RDS, S3, CloudFront 통합
  - Auto Scaling 및 Load Balancing 구성
  - 보안 및 모니터링 설정
- **오후 (4시간)**
  - 프로젝트 완성 및 테스트
  - 아키텍처 다이어그램 작성
  - 프로젝트 발표 및 피드백
  - 2개월차 복습 및 3개월차 준비

---


## 📅 3개월차: Kubernetes 기초 및 실습

### 9주차: Kubernetes 기본 개념

#### Day 41: Kubernetes 소개
- **오전 (4시간)**
  - Kubernetes란 무엇인가?
  - Kubernetes의 역사 (Borg → Kubernetes)
  - 왜 Kubernetes가 필요한가?
  - Kubernetes vs Docker Swarm
- **오후 (4시간)**
  - Kubernetes 아키텍처 개요
  - Control Plane 컴포넌트 (API Server, Scheduler, Controller Manager, etcd)
  - Node 컴포넌트 (Kubelet, Kube-proxy, Container Runtime)
  - Kubernetes 설치 옵션 비교

#### Day 42: Kubernetes 환경 구성
- **오전 (4시간)**
  - Minikube 설치 및 설정
  - kubectl 설치 및 기본 명령어
  - Kubernetes 클러스터 확인
  - 대시보드 설치 및 접근
- **오후 (4시간)**
  - kubectl 기본 명령어 실습
  - 컨텍스트 및 네임스페이스 관리
  - 실습: 첫 번째 애플리케이션 배포
  - YAML 파일 기초

#### Day 43: Pods - Kubernetes의 기본 단위
- **오전 (4시간)**
  - Pod란 무엇인가?
  - Pod 생명주기
  - 단일 컨테이너 Pod vs 멀티 컨테이너 Pod
  - Pod 생성 및 관리
- **오후 (4시간)**
  - Pod YAML 작성
  - 실습: 다양한 Pod 생성
  - Pod 로그 확인 및 디버깅
  - Init Containers 및 Sidecar 패턴

#### Day 44: ReplicaSets 및 Deployments
- **오전 (4시간)**
  - ReplicaSet 개념
  - Deployment 개념 및 필요성
  - Deployment 생성 및 관리
  - 레플리카 수 조정
- **오후 (4시간)**
  - 롤링 업데이트
  - 롤백
  - 실습: 무중단 배포 시나리오
  - Deployment 전략 (Recreate, RollingUpdate)

#### Day 45: Services - 네트워킹 기초
- **오전 (4시간)**
  - Service란 무엇인가?
  - Service 타입 (ClusterIP, NodePort, LoadBalancer, ExternalName)
  - Service Discovery
  - Endpoints
- **오후 (4시간)**
  - 실습: 다양한 Service 타입 생성
  - Service와 Pod 연결
  - 로드 밸런싱
  - 주간 복습 및 실습 프로젝트

---

### 10주차: Kubernetes 핵심 리소스

#### Day 46: ConfigMaps 및 Secrets
- **오전 (4시간)**
  - ConfigMap 개념 및 사용 사례
  - ConfigMap 생성 방법
  - 환경 변수로 주입
  - 볼륨으로 마운트
- **오후 (4시간)**
  - Secret 개념 및 보안
  - Secret 타입 (Opaque, TLS, Docker Registry)
  - 실습: ConfigMap과 Secret 활용
  - 민감 정보 관리 모범 사례

#### Day 47: Volumes 및 Persistent Storage
- **오전 (4시간)**
  - Kubernetes Volume 개념
  - Volume 타입 (emptyDir, hostPath, etc.)
  - PersistentVolume (PV)
  - PersistentVolumeClaim (PVC)
- **오후 (4시간)**
  - StorageClass
  - 동적 프로비저닝
  - 실습: StatefulSet과 영속성 스토리지
  - 데이터베이스 Pod 구성

#### Day 48: Namespaces 및 리소스 관리
- **오전 (4시간)**
  - Namespace 개념 및 사용 사례
  - Namespace 생성 및 관리
  - 리소스 쿼터 (ResourceQuota)
  - 리밋 레인지 (LimitRange)
- **오후 (4시간)**
  - 실습: 멀티 테넌트 환경 구성
  - 네임스페이스 간 통신
  - 리소스 제한 설정
  - 모범 사례

#### Day 49: Labels, Selectors, Annotations
- **오전 (4시간)**
  - Label 개념 및 사용법
  - Selector (Equality-based, Set-based)
  - Annotation
  - 실습: Label을 활용한 리소스 관리
- **오후 (4시간)**
  - 라벨링 전략
  - 실습: 복잡한 Selector 쿼리
  - 메타데이터 활용
  - 조직화 모범 사례

#### Day 50: Kubernetes 네트워킹 심화
- **오전 (4시간)**
  - Kubernetes 네트워킹 모델
  - CNI (Container Network Interface)
  - Pod 간 통신
  - Service 네트워킹
- **오후 (4시간)**
  - Ingress 개념
  - Ingress Controller 설치 (Nginx)
  - 실습: Ingress를 통한 HTTP 라우팅
  - TLS/SSL 설정

---

### 11주차: Kubernetes 고급 리소스

#### Day 51: DaemonSets 및 Jobs
- **오전 (4시간)**
  - DaemonSet 개념 및 사용 사례
  - DaemonSet 생성 및 관리
  - 노드 선택 및 제약
  - 실습: 로깅 에이전트 배포
- **오후 (4시간)**
  - Job 개념
  - CronJob
  - 실습: 배치 작업 실행
  - 병렬 처리 및 완료 조건

#### Day 52: StatefulSets
- **오전 (4시간)**
  - StatefulSet 개념
  - StatefulSet vs Deployment
  - 안정적인 네트워크 ID
  - 순서 보장
- **오후 (4시간)**
  - 실습: StatefulSet으로 데이터베이스 클러스터 구성
  - Headless Service
  - 스케일링 및 업데이트
  - 데이터 영속성

#### Day 53: RBAC (Role-Based Access Control)
- **오전 (4시간)**
  - Kubernetes 인증 및 인가
  - RBAC 개념
  - Role 및 ClusterRole
  - RoleBinding 및 ClusterRoleBinding
- **오후 (4시간)**
  - 실습: 사용자 및 서비스 계정 권한 설정
  - 최소 권한 원칙
  - 보안 모범 사례
  - ServiceAccount

#### Day 54: Resource Limits 및 QoS
- **오전 (4시간)**
  - CPU 및 메모리 요청/제한
  - QoS 클래스 (Guaranteed, Burstable, BestEffort)
  - 리소스 할당 전략
  - 노드 리소스 관리
- **오후 (4시간)**
  - 실습: 리소스 제한 설정 및 테스트
  - HorizontalPodAutoscaler (HPA)
  - VerticalPodAutoscaler (VPA)
  - 클러스터 오토스케일러

#### Day 55: Kubernetes 모니터링 및 로깅
- **오전 (4시간)**
  - Kubernetes 메트릭 서버
  - Prometheus 개요 및 설치
  - Grafana 대시보드
  - 메트릭 수집 및 시각화
- **오후 (4시간)**
  - 로깅 아키텍처
  - 실습: EFK Stack (Elasticsearch, Fluentd, Kibana)
  - 중앙 집중식 로깅
  - 주간 복습 및 실습

---

### 12주차: Kubernetes 공식 문서 Deep Dive

#### Day 56: Kubernetes Concepts - Workloads
- **오전 (4시간)**
  - Kubernetes 공식 문서 구조 탐색
  - Workloads 개념 전체 리뷰
  - Pods, Controllers 심화
  - 문서 기반 실습
- **오후 (4시간)**
  - Pod Lifecycle 상세
  - Pod Disruption Budget
  - 실습: 고가용성 워크로드 구성
  - 문서 읽기 및 적용 연습

#### Day 57: Kubernetes Concepts - Services & Networking
- **오전 (4시간)**
  - Services 공식 문서 Deep Dive
  - Network Policies
  - DNS for Services and Pods
  - Ingress 심화
- **오후 (4시간)**
  - 실습: Network Policy 구성
  - 마이크로서비스 네트워킹
  - 서비스 메시 준비
  - 트래픽 관리

#### Day 58: Kubernetes Concepts - Storage & Configuration
- **오전 (4시간)**
  - Storage 공식 문서 Deep Dive
  - Volume Snapshots
  - CSI (Container Storage Interface)
  - 스토리지 클래스 심화
- **오후 (4시간)**
  - Configuration 관리 심화
  - 실습: 복잡한 구성 시나리오
  - 시크릿 관리 고급
  - 외부 시크릿 관리 도구 (Vault 소개)

#### Day 59: Kubernetes Concepts - Security & Policies
- **오전 (4시간)**
  - Security 공식 문서 Deep Dive
  - Pod Security Standards
  - Security Context
  - Network Policies 심화
- **오후 (4시간)**
  - 실습: 보안 강화된 클러스터 구성
  - Admission Controllers
  - OPA (Open Policy Agent) 소개
  - 컴플라이언스

#### Day 60: 3개월차 종합 프로젝트
- **오전 (4시간)**
  - 프로젝트: Kubernetes 기반 마이크로서비스 배포
  - 멀티 티어 애플리케이션 구성
  - Ingress, Service, ConfigMap, Secret 통합
  - 모니터링 및 로깅 설정
- **오후 (4시간)**
  - 프로젝트 완성 및 테스트
  - 고가용성 및 확장성 검증
  - 프로젝트 발표
  - 3개월차 복습 및 Q&A

---


## 📅 4개월차: Kubernetes 심화 및 Service Mesh

### 13주차: 클라우드 네이티브 Kubernetes

#### Day 61: Amazon EKS 심화
- **오전 (4시간)**
  - EKS 아키텍처 상세
  - EKS 클러스터 생성 (eksctl, Terraform)
  - 관리형 노드 그룹 vs 자체 관리 노드
  - Fargate 프로필
- **오후 (4시간)**
  - 실습: EKS 클러스터 구성 및 애플리케이션 배포
  - AWS Load Balancer Controller
  - EBS CSI Driver
  - EKS와 AWS 서비스 통합

#### Day 62: EKS 네트워킹 및 보안
- **오전 (4시간)**
  - VPC CNI 플러그인
  - Security Groups for Pods
  - IAM Roles for Service Accounts (IRSA)
  - Pod Identity
- **오후 (4시간)**
  - 실습: IRSA 구성
  - EKS 보안 모범 사례
  - Secrets Manager 통합
  - 네트워크 정책

#### Day 63: Google Kubernetes Engine (GKE)
- **오전 (4시간)**
  - GKE 개요 및 특징
  - GKE 클러스터 생성
  - Autopilot vs Standard 모드
  - GKE 네트워킹
- **오후 (4시간)**
  - 실습: GKE 클러스터 구성
  - Workload Identity
  - GKE와 GCP 서비스 통합
  - EKS vs GKE 비교

#### Day 64: Azure Kubernetes Service (AKS)
- **오전 (4시간)**
  - AKS 개요 및 특징
  - AKS 클러스터 생성
  - Azure CNI vs Kubenet
  - AKS 네트워킹
- **오후 (4시간)**
  - 실습: AKS 클러스터 구성
  - Azure Active Directory 통합
  - AKS와 Azure 서비스 통합
  - 클라우드 제공자 비교 정리

#### Day 65: Kubernetes 배포 시 AWS 고려사항
- **오전 (4시간)**
  - EKS 비용 구조 분석
  - 컴퓨팅 비용 최적화 (Spot, Savings Plans)
  - 스토리지 비용 최적화
  - 네트워크 비용 고려사항
- **오후 (4시간)**
  - AWS 서비스로 대체 가능한 Kubernetes 기능
  - ALB Ingress vs Nginx Ingress
  - EBS vs EFS 선택
  - 실습: 비용 효율적인 EKS 클러스터 구성

---

### 14주차: Kubernetes 고급 운영

#### Day 66: Helm - Kubernetes 패키지 관리자
- **오전 (4시간)**
  - Helm 개요 및 필요성
  - Helm 아키텍처 (Chart, Release, Repository)
  - Helm 설치 및 기본 명령어
  - Helm Chart 구조
- **오후 (4시간)**
  - 실습: Helm으로 애플리케이션 배포
  - Chart 커스터마이징 (values.yaml)
  - Helm Repository 관리
  - 실습: 자체 Helm Chart 생성

#### Day 67: Kubernetes Operators
- **오전 (4시간)**
  - Operator 패턴 개념
  - Custom Resource Definitions (CRD)
  - Operator Framework
  - 일반적인 Operator 예제
- **오후 (4시간)**
  - 실습: Prometheus Operator 배포
  - 실습: MySQL Operator 사용
  - Operator 개발 기초
  - Operator Hub 탐색

#### Day 68: Kubernetes 고급 스케줄링
- **오전 (4시간)**
  - Node Selector
  - Node Affinity/Anti-Affinity
  - Pod Affinity/Anti-Affinity
  - Taints and Tolerations
- **오후 (4시간)**
  - 실습: 고급 스케줄링 시나리오
  - Topology Spread Constraints
  - Priority Classes
  - 리소스 최적화

#### Day 69: Kubernetes 트러블슈팅
- **오전 (4시간)**
  - 일반적인 Kubernetes 문제
  - Pod 상태 진단
  - 네트워크 문제 해결
  - 스토리지 문제 해결
- **오후 (4시간)**
  - 실습: 다양한 장애 시나리오
  - kubectl 디버깅 명령어
  - 로그 분석
  - 성능 문제 진단

#### Day 70: Kubernetes 업그레이드 및 유지보수
- **오전 (4시간)**
  - Kubernetes 버전 정책
  - 클러스터 업그레이드 전략
  - 노드 업그레이드
  - 애플리케이션 마이그레이션
- **오후 (4시간)**
  - 실습: 클러스터 업그레이드
  - 백업 및 복구 (Velero)
  - 재해 복구 계획
  - 주간 복습

---

### 15주차: Istio Service Mesh

#### Day 71: Service Mesh 개념 및 Istio 소개
- **오전 (4시간)**
  - Service Mesh란?
  - Service Mesh의 필요성
  - Istio 아키텍처 (Control Plane, Data Plane)
  - Envoy Proxy
- **오후 (4시간)**
  - Istio 설치 (istioctl)
  - Istio 프로필
  - 실습: Istio 설치 및 검증
  - Sidecar Injection

#### Day 72: Istio 트래픽 관리
- **오전 (4시간)**
  - Virtual Service
  - Destination Rule
  - Gateway
  - 트래픽 라우팅
- **오후 (4시간)**
  - 실습: 카나리 배포
  - 실습: A/B 테스팅
  - 트래픽 미러링
  - 타임아웃 및 재시도

#### Day 73: Istio 보안
- **오전 (4시간)**
  - mTLS (Mutual TLS)
  - 인증 정책
  - 인가 정책
  - JWT 인증
- **오후 (4시간)**
  - 실습: mTLS 구성
  - 실습: 세밀한 접근 제어
  - 보안 모범 사례
  - 인증서 관리

#### Day 74: Istio 관찰성
- **오전 (4시간)**
  - Istio 텔레메트리
  - Kiali (서비스 메시 시각화)
  - Jaeger (분산 추적)
  - Prometheus 및 Grafana 통합
- **오후 (4시간)**
  - 실습: Istio 관찰성 스택 구성
  - 서비스 메시 모니터링
  - 트래픽 분석
  - 성능 최적화

#### Day 75: Istio 고급 기능 및 실전
- **오전 (4시간)**
  - Circuit Breaking
  - Fault Injection
  - Rate Limiting
  - 멀티 클러스터 메시
- **오후 (4시간)**
  - 실습: 복원력 패턴 구현
  - Istio 성능 튜닝
  - 프로덕션 배포 고려사항
  - Istio 트러블슈팅

---

### 16주차: Kubernetes 실전 프로젝트

#### Day 76: 프로젝트 계획 및 설계
- **오전 (4시간)**
  - 프로젝트 요구사항 분석
  - 마이크로서비스 아키텍처 설계
  - Kubernetes 리소스 계획
  - Istio 통합 계획
- **오후 (4시간)**
  - 인프라 설계 (EKS)
  - 네트워킹 설계
  - 보안 설계
  - 모니터링 및 로깅 계획

#### Day 77: 프로젝트 구현 - 인프라
- **오전 (4시간)**
  - EKS 클러스터 구성
  - VPC 및 네트워킹 설정
  - IAM 역할 및 정책
  - 스토리지 구성
- **오후 (4시간)**
  - Istio 설치 및 구성
  - 모니터링 스택 배포
  - 로깅 스택 배포
  - 인프라 검증

#### Day 78: 프로젝트 구현 - 애플리케이션
- **오전 (4시간)**
  - 마이크로서비스 배포
  - Helm Chart 작성
  - ConfigMap 및 Secret 구성
  - 서비스 간 통신 설정
- **오후 (4시간)**
  - Istio 트래픽 관리 구성
  - 보안 정책 적용
  - 오토스케일링 설정
  - 애플리케이션 테스트

#### Day 79: 프로젝트 최적화 및 테스트
- **오전 (4시간)**
  - 성능 테스트
  - 부하 테스트
  - 장애 시나리오 테스트
  - 복원력 검증
- **오후 (4시간)**
  - 비용 최적화
  - 리소스 튜닝
  - 보안 강화
  - 문서화

#### Day 80: 프로젝트 발표 및 4개월차 복습
- **오전 (4시간)**
  - 프로젝트 발표 준비
  - 아키텍처 다이어그램 작성
  - 데모 시연
  - 프로젝트 발표
- **오후 (4시간)**
  - 피드백 및 개선
  - 4개월차 전체 복습
  - 핵심 개념 정리
  - 5개월차 준비

---


## 📅 5개월차: CI/CD 및 GitOps

### 17주차: CI/CD 기초

#### Day 81: CI/CD 개념 및 원칙
- **오전 (4시간)**
  - CI (Continuous Integration) 개념
  - CD (Continuous Delivery vs Continuous Deployment)
  - CI/CD의 이점
  - CI/CD 파이프라인 구성 요소
- **오후 (4시간)**
  - CI/CD 모범 사례
  - 파이프라인 설계 원칙
  - 브랜치 전략 (Git Flow, GitHub Flow, Trunk-Based)
  - 실습: Git 브랜치 전략 적용

#### Day 82: CI 단계 - 빌드 및 테스트
- **오전 (4시간)**
  - 소스 코드 관리
  - 자동화된 빌드
  - 단위 테스트
  - 통합 테스트
- **오후 (4시간)**
  - 코드 품질 검사 (Linting, Static Analysis)
  - 테스트 커버리지
  - 실습: 테스트 자동화 구성
  - 빌드 아티팩트 관리

#### Day 83: CI 단계 - 보안 및 품질
- **오전 (4시간)**
  - 보안 스캔 (SAST, DAST)
  - 의존성 스캔
  - 컨테이너 이미지 스캔
  - 라이선스 검사
- **오후 (4시간)**
  - 실습: 보안 스캔 통합
  - 코드 리뷰 자동화
  - 품질 게이트
  - SonarQube 소개

#### Day 84: CD 단계 - 배포 전략
- **오전 (4시간)**
  - 배포 전략 개요
  - 블루-그린 배포
  - 카나리 배포
  - 롤링 배포
- **오후 (4시간)**
  - A/B 테스팅
  - 피처 플래그
  - 실습: 다양한 배포 전략 구현
  - 롤백 전략

#### Day 85: CD 단계 - 환경 관리
- **오전 (4시간)**
  - 환경 분리 (Dev, Staging, Production)
  - 환경별 구성 관리
  - 프로모션 전략
  - 승인 프로세스
- **오후 (4시간)**
  - 실습: 멀티 환경 파이프라인
  - 환경 동기화
  - 구성 드리프트 방지
  - 주간 복습

---

### 18주차: CI/CD 도구 실습

#### Day 86: GitHub Actions 기초
- **오전 (4시간)**
  - GitHub Actions 개요
  - Workflow 구조
  - Events, Jobs, Steps
  - Actions Marketplace
- **오후 (4시간)**
  - 실습: 첫 번째 Workflow 작성
  - 환경 변수 및 시크릿
  - Matrix 빌드
  - 실습: Docker 이미지 빌드 및 푸시

#### Day 87: GitHub Actions 심화
- **오전 (4시간)**
  - 재사용 가능한 Workflow
  - Composite Actions
  - 조건부 실행
  - 병렬 처리
- **오후 (4시간)**
  - 실습: Kubernetes 배포 자동화
  - Self-hosted Runners
  - 캐싱 전략
  - 비용 최적화

#### Day 88: Jenkins 기초
- **오전 (4시간)**
  - Jenkins 개요 및 설치
  - Jenkins 아키텍처
  - Job 생성 및 관리
  - Pipeline as Code (Jenkinsfile)
- **오후 (4시간)**
  - Declarative vs Scripted Pipeline
  - 실습: Jenkins Pipeline 작성
  - 플러그인 관리
  - Jenkins와 Git 통합

#### Day 89: Jenkins 심화
- **오전 (4시간)**
  - Multibranch Pipeline
  - Shared Libraries
  - Jenkins Agent 구성
  - 분산 빌드
- **오후 (4시간)**
  - 실습: Kubernetes에서 Jenkins 실행
  - Jenkins X 소개
  - Blue Ocean UI
  - Jenkins 보안

#### Day 90: 기타 CI/CD 도구
- **오전 (4시간)**
  - CircleCI 개요 및 실습
  - GitLab CI/CD 개요 및 실습
  - TeamCity 소개
  - Drone CI 소개
- **오후 (4시간)**
  - CI/CD 도구 비교 (기능, 비용, 성능)
  - 도구 선택 기준
  - 실습: 동일 프로젝트를 다른 도구로 구성
  - 마이그레이션 고려사항

---

### 19주차: CI/CD 최적화 및 모범 사례

#### Day 91: CI/CD 파이프라인 최적화
- **오전 (4시간)**
  - 빌드 시간 단축 기법
  - 캐싱 전략
  - 병렬화 및 분산 빌드
  - 증분 빌드
- **오후 (4시간)**
  - 실습: 파이프라인 성능 최적화
  - 리소스 효율화
  - 비용 최적화
  - 성능 모니터링

#### Day 92: CI/CD 보안
- **오전 (4시간)**
  - 파이프라인 보안 모범 사례
  - 시크릿 관리
  - 공급망 보안 (Supply Chain Security)
  - SBOM (Software Bill of Materials)
- **오후 (4시간)**
  - 실습: 보안 강화된 파이프라인
  - 서명 및 검증
  - 취약점 관리
  - 컴플라이언스

#### Day 93: CI/CD 모니터링 및 관찰성
- **오전 (4시간)**
  - 파이프라인 메트릭
  - 배포 빈도 및 리드 타임
  - 실패율 및 복구 시간
  - DORA 메트릭
- **오후 (4시간)**
  - 실습: CI/CD 대시보드 구성
  - 알림 및 경고
  - 로그 분석
  - 지속적 개선

#### Day 94: CI/CD 주의사항 및 트러블슈팅
- **오전 (4시간)**
  - 일반적인 CI/CD 안티패턴
  - 파이프라인 장애 대응
  - 디버깅 기법
  - 롤백 시나리오
- **오후 (4시간)**
  - 실습: 장애 시나리오 대응
  - 파이프라인 복원력
  - 재시도 전략
  - 사후 분석 (Post-mortem)

#### Day 95: Docker Image Registry 심화
- **오전 (4시간)**
  - GitHub Container Registry (GHCR) 심화
  - AWS ECR 심화
  - Harbor 소개
  - 프라이빗 레지스트리 운영
- **오후 (4시간)**
  - 실습: 멀티 레지스트리 전략
  - 이미지 복제 및 동기화
  - 레지스트리 보안
  - 주간 복습

---

### 20주차: GitOps 및 ArgoCD

#### Day 96: GitOps 개념 및 원칙
- **오전 (4시간)**
  - GitOps란?
  - GitOps 원칙
  - Push vs Pull 배포 모델
  - GitOps의 이점
- **오후 (4시간)**
  - GitOps 워크플로우
  - Git을 Single Source of Truth로
  - 선언적 구성
  - 실습: GitOps 리포지토리 구조

#### Day 97: ArgoCD 기초
- **오전 (4시간)**
  - ArgoCD 개요 및 아키텍처
  - ArgoCD 설치
  - Application 개념
  - Sync 전략
- **오후 (4시간)**
  - 실습: ArgoCD로 첫 애플리케이션 배포
  - ArgoCD UI 탐색
  - CLI 사용법
  - 자동 동기화 vs 수동 동기화

#### Day 98: ArgoCD 심화
- **오전 (4시간)**
  - ApplicationSet
  - App of Apps 패턴
  - 멀티 클러스터 관리
  - 프로젝트 및 RBAC
- **오후 (4시간)**
  - 실습: 복잡한 GitOps 워크플로우
  - Helm과 ArgoCD 통합
  - Kustomize와 ArgoCD 통합
  - 시크릿 관리 (Sealed Secrets, External Secrets)

#### Day 99: ArgoCD 고급 기능
- **오전 (4시간)**
  - Progressive Delivery (Argo Rollouts)
  - 카나리 배포 자동화
  - 블루-그린 배포 자동화
  - 분석 및 메트릭 기반 프로모션
- **오후 (4시간)**
  - 실습: Argo Rollouts 구성
  - Notifications 및 Webhooks
  - ArgoCD Image Updater
  - 모니터링 및 관찰성

#### Day 100: 5개월차 종합 프로젝트
- **오전 (4시간)**
  - 프로젝트: 완전 자동화된 CI/CD 파이프라인
  - GitHub Actions + ArgoCD 통합
  - 멀티 환경 배포
  - 보안 및 품질 게이트
- **오후 (4시간)**
  - 프로젝트 완성 및 테스트
  - 프로젝트 발표
  - 5개월차 복습
  - 6개월차 준비

---


## 📅 6개월차: Terraform 및 FinOps

### 21주차: Terraform 기초

#### Day 101: Infrastructure as Code 개념
- **오전 (4시간)**
  - Infrastructure as Code (IaC)란?
  - IaC의 이점
  - 선언형 vs 명령형
  - IaC 도구 비교 (Terraform, CloudFormation, Pulumi, Ansible)
- **오후 (4시간)**
  - Terraform 개요
  - Terraform 아키텍처
  - Terraform 설치 및 설정
  - 첫 번째 Terraform 구성

#### Day 102: Terraform 기본 문법
- **오전 (4시간)**
  - HCL (HashiCorp Configuration Language)
  - Providers
  - Resources
  - Data Sources
- **오후 (4시간)**
  - Variables
  - Outputs
  - 실습: 간단한 AWS 리소스 생성
  - Terraform 명령어 (init, plan, apply, destroy)

#### Day 103: Terraform State 관리
- **오전 (4시간)**
  - Terraform State란?
  - Local vs Remote State
  - State Locking
  - S3 Backend 구성
- **오후 (4시간)**
  - 실습: Remote State 구성
  - State 명령어 (list, show, mv, rm)
  - State 파일 보안
  - State 백업 및 복구

#### Day 104: Terraform 모듈
- **오전 (4시간)**
  - 모듈 개념 및 필요성
  - 모듈 구조
  - 모듈 입력 및 출력
  - 로컬 모듈 vs 원격 모듈
- **오후 (4시간)**
  - 실습: 첫 번째 모듈 작성
  - Terraform Registry
  - 모듈 버전 관리
  - 모듈 재사용 전략

#### Day 105: Terraform 워크스페이스 및 환경 관리
- **오전 (4시간)**
  - Workspace 개념
  - 환경 분리 전략
  - 변수 파일 (.tfvars)
  - 환경별 구성 관리
- **오후 (4시간)**
  - 실습: 멀티 환경 구성
  - 조건부 리소스 생성
  - 동적 블록
  - 주간 복습

---

### 22주차: Terraform 심화

#### Day 106: Terraform 고급 기능
- **오전 (4시간)**
  - Count vs For_each
  - Dynamic Blocks
  - Locals
  - Functions
- **오후 (4시간)**
  - 실습: 고급 Terraform 패턴
  - Terraform Console
  - 표현식 및 연산자
  - 타입 제약

#### Day 107: Terraform과 AWS 통합
- **오전 (4시간)**
  - AWS Provider 심화
  - IAM 역할 및 정책 관리
  - VPC 및 네트워킹
  - EC2 및 Auto Scaling
- **오후 (4시간)**
  - 실습: Terraform으로 3-tier 아키텍처 구축
  - RDS 및 데이터베이스
  - S3 및 CloudFront
  - Route 53

#### Day 108: Terraform 모범 사례
- **오전 (4시간)**
  - 코드 구조화
  - 네이밍 컨벤션
  - 문서화
  - 버전 관리
- **오후 (4시간)**
  - 보안 모범 사례
  - 시크릿 관리
  - 실습: 프로덕션 레벨 Terraform 프로젝트
  - 코드 리뷰 체크리스트

#### Day 109: Terraform 테스팅
- **오전 (4시간)**
  - Terraform Validate
  - Terraform Plan 분석
  - Terraform Test (실험적 기능)
  - Terratest 소개
- **오후 (4시간)**
  - 실습: Terraform 코드 테스트
  - 정적 분석 (tflint, tfsec)
  - 정책 검증 (Sentinel, OPA)
  - CI/CD 통합

#### Day 110: Terraform 장단점 및 사용 케이스
- **오전 (4시간)**
  - Terraform의 장점
  - Terraform의 한계
  - 선언형이 좋을 때
  - 명령형이 좋을 때
- **오후 (4시간)**
  - Terraform vs CloudFormation
  - Terraform vs Pulumi
  - 하이브리드 접근법
  - 실습: 도구 선택 시나리오

---

### 23주차: Terraform 실전 프로젝트

#### Day 111: AWS Core Services - VPC 및 네트워킹
- **오전 (4시간)**
  - VPC 모듈 설계
  - 서브넷, 라우팅 테이블, 게이트웨이
  - 보안 그룹 및 NACL
  - VPC Peering 및 Transit Gateway
- **오후 (4시간)**
  - 실습: Terraform으로 VPC 구축
  - 멀티 AZ 구성
  - 네트워크 보안
  - 비용 최적화

#### Day 112: AWS Core Services - 컴퓨팅 및 스토리지
- **오전 (4시간)**
  - EC2 인스턴스 모듈
  - Auto Scaling 그룹
  - Load Balancer
  - Launch Template
- **오후 (4시간)**
  - 실습: Terraform으로 컴퓨팅 리소스 배포
  - EBS 볼륨 관리
  - S3 버킷 구성
  - 백업 및 스냅샷

#### Day 113: AWS Core Services - 데이터베이스 및 캐싱
- **오전 (4시간)**
  - RDS 모듈
  - DynamoDB
  - ElastiCache
  - 데이터베이스 보안
- **오후 (4시간)**
  - 실습: Terraform으로 데이터베이스 배포
  - 백업 및 복원 자동화
  - 읽기 전용 복제본
  - 성능 최적화

#### Day 114: AWS Core Services - 컨테이너 및 서버리스
- **오전 (4시간)**
  - ECS/EKS 클러스터
  - Fargate
  - Lambda 함수
  - API Gateway
- **오후 (4시간)**
  - 실습: Terraform으로 EKS 클러스터 배포
  - 컨테이너 서비스 구성
  - 서버리스 아키텍처
  - 통합 테스트

#### Day 115: Terraform 모듈화 프로젝트
- **오전 (4시간)**
  - 서비스별 모듈 설계
  - 모듈 인터페이스 정의
  - 의존성 관리
  - 모듈 문서화
- **오후 (4시간)**
  - 실습: 재사용 가능한 모듈 작성
  - 모듈 테스트
  - 모듈 버전 관리
  - 주간 복습

---

### 24주차: Terraform Import 및 FinOps

#### Day 116: Terraform Import 기초
- **오전 (4시간)**
  - Terraform Import 개념
  - Import 워크플로우
  - 리소스 식별
  - Import 명령어
- **오후 (4시간)**
  - 실습: 기존 AWS 리소스 Import
  - Import 후 State 정리
  - 구성 파일 생성
  - Import 자동화

#### Day 117: Terraform Import 고급
- **오전 (4시간)**
  - 복잡한 리소스 Import
  - 모듈 Import
  - 대량 Import 전략
  - Import 블록 (Terraform 1.5+)
- **오후 (4시간)**
  - 실습: 전체 인프라 Import
  - Import 검증
  - Drift 감지 및 해결
  - 문서화

#### Day 118: FinOps 개념 및 원칙
- **오전 (4시간)**
  - FinOps란?
  - FinOps 프레임워크
  - 클라우드 재무 관리
  - FinOps 팀 구조
- **오후 (4시간)**
  - AWS 비용 구조 이해
  - 비용 가시성
  - 비용 할당 및 차지백
  - FinOps 문화

#### Day 119: AWS 비용 최적화
- **오전 (4시간)**
  - AWS Cost Explorer 심화
  - AWS Budgets 및 알림
  - Cost Anomaly Detection
  - Savings Plans vs Reserved Instances
- **오후 (4시간)**
  - 실습: 비용 분석 및 최적화
  - 리소스 라이트사이징
  - Spot Instances 활용
  - 스토리지 최적화

#### Day 120: FinOps 도구 및 자동화
- **오전 (4시간)**
  - AWS Cost and Usage Report
  - Terraform으로 비용 관리
  - 태깅 전략
  - 비용 최적화 자동화
- **오후 (4시간)**
  - 실습: FinOps 대시보드 구축
  - 비용 알림 자동화
  - 리소스 정리 자동화
  - 6개월차 복습

---


### 25주차: 최종 프로젝트 및 취업 준비

#### Day 121: 최종 프로젝트 기획
- **오전 (4시간)**
  - 프로젝트 요구사항 정의
  - 아키텍처 설계 (MSA, Kubernetes, AWS)
  - 기술 스택 선정
  - 팀 구성 및 역할 분담
- **오후 (4시간)**
  - 인프라 설계 (Terraform)
  - CI/CD 파이프라인 설계
  - GitOps 워크플로우 설계
  - 프로젝트 일정 수립

#### Day 122: 최종 프로젝트 - 인프라 구축
- **오전 (4시간)**
  - Terraform으로 AWS 인프라 구축
  - VPC, 네트워킹, 보안 설정
  - EKS 클러스터 배포
  - 모니터링 및 로깅 인프라
- **오후 (4시간)**
  - Istio Service Mesh 설치
  - ArgoCD 설치 및 구성
  - 인프라 검증 및 테스트
  - 문서화

#### Day 123: 최종 프로젝트 - 애플리케이션 배포
- **오전 (4시간)**
  - 마이크로서비스 컨테이너화
  - Helm Chart 작성
  - GitOps 리포지토리 구성
  - ArgoCD Application 생성
- **오후 (4시간)**
  - CI/CD 파이프라인 구축
  - 자동화된 테스트
  - 보안 스캔 통합
  - 배포 자동화

#### Day 124: 최종 프로젝트 - 운영 및 최적화
- **오전 (4시간)**
  - 모니터링 대시보드 구성
  - 알림 및 경고 설정
  - 로그 분석 시스템
  - 성능 테스트
- **오후 (4시간)**
  - 비용 최적화
  - 보안 강화
  - 고가용성 검증
  - 재해 복구 테스트

#### Day 125: 최종 프로젝트 발표 및 피드백
- **오전 (4시간)**
  - 프로젝트 발표 준비
  - 데모 시연 리허설
  - 아키텍처 다이어그램 완성
  - 문서 정리
- **오후 (4시간)**
  - 최종 프로젝트 발표
  - 질의응답
  - 피드백 및 개선 사항
  - 프로젝트 회고

---

### 26주차: 취업 준비 및 과정 마무리

#### Day 126: DevOps 엔지니어 취업 준비
- **오전 (4시간)**
  - DevOps 엔지니어 직무 이해
  - 이력서 작성 가이드
  - 포트폴리오 구성
  - GitHub 프로필 최적화
- **오후 (4시간)**
  - 기술 면접 준비
  - 일반적인 면접 질문
  - 실습: 모의 면접
  - 면접 팁 및 전략

#### Day 127: 기술 면접 대비 - Docker & Kubernetes
- **오전 (4시간)**
  - Docker 핵심 개념 복습
  - Docker 면접 질문 및 답변
  - Kubernetes 핵심 개념 복습
  - Kubernetes 면접 질문 및 답변
- **오후 (4시간)**
  - 실전 문제 풀이
  - 트러블슈팅 시나리오
  - 모의 면접
  - 피드백

#### Day 128: 기술 면접 대비 - AWS & Terraform
- **오전 (4시간)**
  - AWS 핵심 서비스 복습
  - AWS 면접 질문 및 답변
  - Terraform 핵심 개념 복습
  - IaC 면접 질문 및 답변
- **오후 (4시간)**
  - 실전 문제 풀이
  - 아키텍처 설계 문제
  - 모의 면접
  - 피드백

#### Day 129: 기술 면접 대비 - CI/CD & DevOps
- **오전 (4시간)**
  - CI/CD 핵심 개념 복습
  - CI/CD 면접 질문 및 답변
  - DevOps 문화 및 실천 방법
  - 소프트 스킬 면접 준비
- **오후 (4시간)**
  - 실전 문제 풀이
  - 시스템 설계 문제
  - 모의 면접
  - 피드백

#### Day 130: 과정 수료 및 향후 학습 계획
- **오전 (4시간)**
  - 6개월 과정 전체 복습
  - 핵심 개념 정리
  - 학습 성과 평가
  - 수료증 수여
- **오후 (4시간)**
  - 향후 학습 로드맵
  - 추가 학습 자료 소개
  - 커뮤니티 및 네트워킹
  - 수료식 및 마무리

---

## 📊 평가 및 프로젝트

### 월별 평가
- **1개월차**: Docker 기반 멀티 컨테이너 애플리케이션 구축
- **2개월차**: AWS 3-tier 웹 애플리케이션 아키텍처 구축
- **3개월차**: Kubernetes 기반 마이크로서비스 배포
- **4개월차**: Istio Service Mesh를 활용한 고급 트래픽 관리
- **5개월차**: 완전 자동화된 CI/CD 파이프라인 구축
- **6개월차**: Terraform을 활용한 전체 인프라 자동화

### 최종 프로젝트
**주제**: 클라우드 네이티브 마이크로서비스 플랫폼 구축

**요구사항**:
- Docker로 컨테이너화된 3개 이상의 마이크로서비스
- AWS EKS 기반 Kubernetes 클러스터
- Istio Service Mesh 적용
- Terraform으로 전체 인프라 코드화
- GitHub Actions + ArgoCD를 통한 GitOps 구현
- Prometheus + Grafana 모니터링
- EFK Stack 로깅
- 보안 스캔 및 품질 게이트
- 비용 최적화 전략 적용

---

## 📚 추가 학습 주제 (선택)

### 고급 주제
- **Kubernetes 고급**
  - Custom Controllers 개발
  - Operator SDK
  - Service Mesh 비교 (Istio, Linkerd, Consul)
  - Multi-cluster 관리

- **클라우드 고급**
  - Multi-cloud 전략
  - Hybrid Cloud
  - Cloud Migration 전략
  - Disaster Recovery

- **보안**
  - DevSecOps
  - Zero Trust Architecture
  - Secrets Management (Vault)
  - Compliance as Code

- **관찰성**
  - OpenTelemetry
  - Distributed Tracing
  - APM (Application Performance Monitoring)
  - SRE 원칙

- **자동화**
  - Ansible
  - Python for DevOps
  - Bash Scripting
  - Infrastructure Testing

---

## 🎯 학습 목표 및 성과

### 기술 역량
- Docker 및 컨테이너 기술 숙련
- Kubernetes 클러스터 운영 능력
- AWS 클라우드 아키텍처 설계 및 구현
- Terraform을 활용한 IaC 구현
- CI/CD 파이프라인 구축 및 운영
- GitOps 방법론 적용
- Service Mesh 이해 및 활용
- 클라우드 비용 최적화

### 실무 역량
- 문제 해결 능력
- 트러블슈팅 능력
- 문서화 능력
- 협업 및 커뮤니케이션
- 지속적 학습 태도

### 취업 목표
- DevOps 엔지니어
- Cloud Engineer
- SRE (Site Reliability Engineer)
- Platform Engineer
- Infrastructure Engineer

---

## 📖 참고 자료

### 공식 문서
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [Istio Documentation](https://istio.io/latest/docs/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)

### 온라인 학습 플랫폼
- Kubernetes Official Tutorials
- AWS Training and Certification
- HashiCorp Learn
- CNCF (Cloud Native Computing Foundation)

### 커뮤니티
- Kubernetes Slack
- AWS Community
- DevOps Korea
- HashiCorp Community

---

## 💡 학습 팁

1. **실습 중심**: 이론보다 실습에 더 많은 시간을 투자하세요
2. **문서화**: 학습한 내용을 블로그나 GitHub에 정리하세요
3. **프로젝트**: 개인 프로젝트를 통해 실전 경험을 쌓으세요
4. **커뮤니티**: 온라인 커뮤니티에 참여하여 네트워킹하세요
5. **최신 트렌드**: 기술 블로그와 뉴스를 통해 최신 동향을 파악하세요
6. **인증**: AWS, Kubernetes 관련 인증 취득을 고려하세요
7. **영어**: 공식 문서는 대부분 영어이므로 영어 실력을 향상시키세요
8. **오픈소스**: 오픈소스 프로젝트에 기여해보세요

---

## ✅ 체크리스트

### 1개월차 완료 후
- [ ] Docker 기본 명령어 숙지
- [ ] Dockerfile 작성 능력
- [ ] Docker Compose 활용
- [ ] 컨테이너 네트워킹 이해
- [ ] MSA 기본 개념 이해

### 2개월차 완료 후
- [ ] AWS 핵심 서비스 이해
- [ ] VPC 및 네트워킹 구성
- [ ] EC2, RDS, S3 활용
- [ ] AWS 컨테이너 서비스 비교
- [ ] 기본적인 AWS 아키텍처 설계

### 3개월차 완료 후
- [ ] Kubernetes 아키텍처 이해
- [ ] kubectl 명령어 숙지
- [ ] Kubernetes 리소스 관리
- [ ] Helm 활용
- [ ] 클라우드 네이티브 Kubernetes 이해

### 4개월차 완료 후
- [ ] EKS 클러스터 운영
- [ ] Istio Service Mesh 구현
- [ ] Kubernetes 고급 기능 활용
- [ ] 모니터링 및 로깅 구성
- [ ] 트러블슈팅 능력

### 5개월차 완료 후
- [ ] CI/CD 파이프라인 구축
- [ ] GitHub Actions 활용
- [ ] Jenkins 파이프라인 작성
- [ ] ArgoCD를 통한 GitOps 구현
- [ ] 배포 자동화

### 6개월차 완료 후
- [ ] Terraform 코드 작성
- [ ] AWS 리소스 자동화
- [ ] Terraform 모듈 개발
- [ ] 기존 리소스 Import
- [ ] FinOps 개념 이해 및 적용

---

## 🎓 수료 후 진로

### 취업 분야
- 스타트업 DevOps 엔지니어
- 중견/대기업 클라우드 엔지니어
- MSP (Managed Service Provider)
- 컨설팅 회사
- 글로벌 IT 기업

### 추가 학습 방향
- 특정 클라우드 전문화 (AWS, GCP, Azure)
- 특정 도구 전문화 (Kubernetes, Terraform)
- SRE 방향
- DevSecOps 방향
- Platform Engineering 방향

### 인증 취득
- AWS Certified Solutions Architect
- AWS Certified DevOps Engineer
- Certified Kubernetes Administrator (CKA)
- Certified Kubernetes Application Developer (CKAD)
- HashiCorp Certified: Terraform Associate

---

**본 커리큘럼은 공식 문서를 기반으로 작성되었으며, 실무 중심의 교육을 목표로 합니다.**

**마지막 업데이트**: 2026년 2월

