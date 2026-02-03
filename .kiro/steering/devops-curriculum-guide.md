---
inclusion: always
---

# DevOps 교육 과정 Steering Guide (EARS 패턴)

## 🎯 과정 개요

**WHEN** 사용자가 DevOps, Docker, Kubernetes, AWS, Terraform, CI/CD 관련 질문을 하면,
**THE SYSTEM SHALL** 이 6개월 교육 커리큘럼을 참조하여 답변한다.

**WHEN** 사용자가 특정 주차나 일차의 학습 내용을 요청하면,
**THE SYSTEM SHALL** 해당 주차/일차의 상세 커리큘럼을 제공한다.

---

## 📅 과정 구조 (26주, 130일)

### 1개월차 (1-4주): Docker & MSA 기초
**WHERE** Docker 컨테이너 기술을 학습할 때,
**THE SYSTEM SHALL** 다음 순서로 진행한다:
- Week 1: DevOps 이론, Docker 기초, 이미지, 컨테이너, 네트워킹
- Week 2: Dockerfile 최적화, Registry, Docker Compose, Docker Swarm
- Week 3: Docker 보안, MSA 개념, 통신 패턴, MSA 구현
- Week 4: 모니터링, 성능 최적화, 트러블슈팅, 실전 운영

**IF** 사용자가 Docker 관련 질문을 하면,
**THEN** 1-4주차 커리큘럼을 참조한다.

### 2개월차 (5-8주): AWS 클라우드
**WHERE** AWS 클라우드 서비스를 학습할 때,
**THE SYSTEM SHALL** 다음 순서로 진행한다:
- Week 5: AWS 기본, EC2, S3, RDS, VPC
- Week 6: Load Balancing, Auto Scaling, Route 53, CloudFront, 보안, 모니터링
- Week 7: ECS, Fargate, EKS, ECR (컨테이너 서비스)
- Week 8: Lambda, 메시징, CloudFormation, 비용 관리

**IF** 사용자가 AWS 관련 질문을 하면,
**THEN** 5-8주차 커리큘럼을 참조한다.

### 3개월차 (9-12주): Kubernetes 기초
**WHERE** Kubernetes를 학습할 때,
**THE SYSTEM SHALL** 다음 순서로 진행한다:
- Week 9: K8s 개념, 환경 구성, Pods, Deployments, Services
- Week 10: ConfigMaps, Secrets, Volumes, Namespaces, Labels
- Week 11: DaemonSets, Jobs, StatefulSets, RBAC, Resource Limits, 모니터링
- Week 12: K8s 공식 문서 Deep Dive (Workloads, Networking, Storage, Security)

**IF** 사용자가 Kubernetes 기초 질문을 하면,
**THEN** 9-12주차 커리큘럼을 참조한다.

### 4개월차 (13-16주): Kubernetes 심화 & Istio
**WHERE** 클라우드 네이티브 Kubernetes와 Service Mesh를 학습할 때,
**THE SYSTEM SHALL** 다음 순서로 진행한다:
- Week 13: EKS, GKE, AKS 비교 및 실습, AWS 통합
- Week 14: Helm, Operators, 고급 스케줄링, 트러블슈팅, 업그레이드
- Week 15: Istio 개념, 트래픽 관리, 보안, 관찰성, 고급 기능
- Week 16: 종합 프로젝트 (EKS + Istio)

**IF** 사용자가 EKS, Istio, Service Mesh 질문을 하면,
**THEN** 13-16주차 커리큘럼을 참조한다.

### 5개월차 (17-20주): CI/CD & GitOps
**WHERE** CI/CD 파이프라인을 학습할 때,
**THE SYSTEM SHALL** 다음 순서로 진행한다:
- Week 17: CI/CD 개념, 빌드/테스트, 보안/품질, 배포 전략, 환경 관리
- Week 18: GitHub Actions, Jenkins, CircleCI, TeamCity 실습
- Week 19: 파이프라인 최적화, 보안, 모니터링, 트러블슈팅, Registry
- Week 20: GitOps 개념, ArgoCD 기초/심화, Argo Rollouts

**IF** 사용자가 CI/CD, GitOps, ArgoCD 질문을 하면,
**THEN** 17-20주차 커리큘럼을 참조한다.

### 6개월차 (21-26주): Terraform & FinOps
**WHERE** Infrastructure as Code를 학습할 때,
**THE SYSTEM SHALL** 다음 순서로 진행한다:
- Week 21: IaC 개념, Terraform 기본, State, 모듈, Workspace
- Week 22: Terraform 고급, AWS 통합, 모범 사례, 테스팅, 장단점
- Week 23: AWS Core Services 배포 (VPC, 컴퓨팅, DB, 컨테이너), 모듈화
- Week 24: Terraform Import, FinOps 개념, 비용 최적화, 자동화
- Week 25: 최종 프로젝트 (전체 통합)
- Week 26: 취업 준비, 기술 면접, 과정 마무리

**IF** 사용자가 Terraform, IaC, FinOps 질문을 하면,
**THEN** 21-26주차 커리큘럼을 참조한다.

---

## 🔑 핵심 학습 원칙

**WHEN** 교육 내용을 설명할 때,
**THE SYSTEM SHALL** 다음 원칙을 따른다:
- 오전 4시간: 이론 및 개념
- 오후 4시간: 실습 및 프로젝트
- 공식 문서 기반 학습
- 실무 중심 접근

**WHERE** 실습이 필요한 경우,
**THE SYSTEM SHALL** 단계별 가이드를 제공한다.

**IF** 사용자가 특정 기술의 공식 문서를 요청하면,
**THEN** 다음 링크를 제공한다:
- Docker: https://docs.docker.com/
- Kubernetes: https://kubernetes.io/docs/
- AWS: https://docs.aws.amazon.com/
- Terraform: https://www.terraform.io/docs/
- Istio: https://istio.io/latest/docs/
- ArgoCD: https://argo-cd.readthedocs.io/

---

## 📊 일별 상세 커리큘럼

### 1주차: DevOps 기본 이론 및 환경 구성

**Day 1: DevOps 개요 및 문화**
- 오전: DevOps란?, 역사와 필요성, CALMS 모델, 전통적 개발 vs DevOps
- 오후: DevOps 생명주기, 도구 생태계, 실습 환경 구성, Git 기본

**Day 2: 컨테이너 기술 개요 및 Docker 소개**
- 오전: 가상화 vs 컨테이너화, Docker 아키텍처, Docker 설치
- 오후: Docker Hub, 첫 컨테이너 실행, 기본 명령어, 웹 서버 실습

**Day 3: Docker 이미지 기초**
- 오전: 이미지 개념, 레이어 구조, Docker Hub 활용, 태그 관리
- 오후: Dockerfile 기본 문법, 첫 Dockerfile 작성, Node.js 이미지 빌드

**Day 4: Docker 컨테이너 관리**
- 오전: 생명주기 관리, 포트 매핑, 볼륨 마운트, 환경 변수
- 오후: 로그 확인, 컨테이너 접속, 리소스 제한, DB 컨테이너 실습

**Day 5: Docker 네트워킹 기초**
- 오전: 네트워크 종류, 사용자 정의 네트워크, 컨테이너 간 통신
- 오후: 멀티 컨테이너 애플리케이션 실습, 주간 복습, 미니 프로젝트

### 2주차: Docker 심화

**Day 6: Dockerfile 최적화**
- 오전: 멀티 스테이지 빌드, 이미지 크기 최적화, 레이어 캐싱, .dockerignore
- 오후: 베이스 이미지 선택, 보안 모범 사례, 프로덕션 Dockerfile, 이미지 스캔

**Day 7: Docker Registry 및 이미지 배포**
- 오전: Docker Hub 심화, 프라이빗 레지스트리, 태깅 전략, 푸시/풀
- 오후: GHCR, AWS ECR, 프라이빗 레지스트리 배포, 버전 관리

**Day 8: Docker Compose 기초**
- 오전: Compose 개념, YAML 구조, 서비스/네트워크/볼륨, 기본 명령어
- 오후: 환경 변수, 의존성 관리, 웹+DB+Redis 구성, 헬스체크

**Day 9: Docker Compose 심화**
- 오전: 멀티 컨테이너 오케스트레이션, 고급 설정, 스케일링, 오버라이드
- 오후: 환경 분리, MSA 구성, 로깅/모니터링, Compose 프로젝트 관리

**Day 10: Docker Swarm 소개**
- 오전: Swarm 개념, Swarm vs K8s, 클러스터 구성, 초기화
- 오후: 서비스 배포, 스택 배포, 롤링 업데이트, Swarm 실습

### 3주차: Docker 실전 프로젝트 및 MSA 기초

**Day 11: Docker 보안**
- 오전: 보안 모범 사례, 루트리스 컨테이너, 시크릿 관리, 네트워크 보안
- 오후: 이미지 서명/검증, 보안 스캔 도구, 보안 강화 실습, 컴플라이언스

**Day 12: MSA 개요**
- 오전: 모놀리식 vs MSA, 장단점, 설계 원칙, 서비스 분해
- 오후: MSA 디자인 패턴, 데이터 관리, 이벤트 기반 아키텍처, MSA 설계

**Day 13: MSA 통신 패턴**
- 오전: 동기/비동기 통신, 서비스 간 인증, API 버저닝
- 오후: REST API 마이크로서비스, 서비스 메시, 분산 트랜잭션, 에러 핸들링

**Day 14: Docker 기반 MSA 구현**
- 오전: 마이크로서비스 컨테이너화, API Gateway, 서비스 디스커버리, 로드 밸런싱
- 오후: 3개 이상 마이크로서비스 구성, 서비스 간 통신, 중앙 로깅, 분산 추적

**Day 15: 1개월차 종합 프로젝트**
- 오전: 요구사항 분석, 아키텍처 설계, 서비스 분해, Compose 작성
- 오후: 구현 및 테스트, 디버깅, 발표 및 코드 리뷰, 복습

### 4주차: Docker 고급 주제 및 실전 운영

**Day 16: Docker 모니터링 및 로깅**
- 오전: 메트릭 수집, 모니터링 도구, 로깅 드라이버, ELK Stack
- 오후: Prometheus + Grafana 실습, 알림 설정, 로그 분석, 성능 튜닝

**Day 17: Docker 성능 최적화**
- 오전: 리소스 제한, CPU/메모리 최적화, 스토리지 드라이버, 네트워크 최적화
- 오후: 빌드 캐시, 이미지 레이어 최적화, 성능 벤치마킹, 병목 분석

**Day 18: Docker 트러블슈팅**
- 오전: 일반적 문제 해결, 디버깅 기법, 네트워크 문제, 스토리지 문제
- 오후: 로그 분석 진단, 트러블슈팅 시나리오, 성능 문제, 복구 전략

**Day 19: Docker 실전 운영 사례**
- 오전: 프로덕션 운영, CI/CD 파이프라인, 블루-그린 배포, 카나리 배포
- 오후: 백업/복구, 재해 복구, 무중단 배포 실습, 운영 자동화

**Day 20: 1개월차 최종 평가**
- 오전: 전체 복습, 핵심 개념 정리, 실전 문제, 모의 면접
- 오후: 최종 프로젝트 발표, 피드백, 2개월차 소개, 로드맵 점검

### 5주차: AWS 기본 이해 및 핵심 서비스

**Day 21: AWS 클라우드 개요**
- 오전: 클라우드 컴퓨팅, AWS 소개, 리전/AZ/엣지, 계정 생성
- 오후: Management Console, AWS CLI, IAM 기초, 사용자/권한 설정

**Day 22: EC2**
- 오전: EC2 개요, 인스턴스 타입, AMI, 인스턴스 생성
- 오후: 보안 그룹, 키 페어, 웹 서버 구성, 모니터링

**Day 23: AWS 스토리지**
- 오전: S3 개요, 버킷, 스토리지 클래스, 버전 관리, 보안
- 오후: EBS 볼륨, 스냅샷, S3 정적 웹사이트, EBS 연결

**Day 24: AWS 데이터베이스**
- 오전: RDS 개요, 엔진, 인스턴스 생성, 다중 AZ
- 오후: 백업/복원, 읽기 전용 복제본, RDS MySQL 실습, DynamoDB

**Day 25: VPC**
- 오전: VPC 개요, 서브넷, 라우팅 테이블, 인터넷 게이트웨이
- 오후: NAT 게이트웨이, 보안 그룹 vs NACL, VPC 생성, 3-tier 네트워크

### 6주차: AWS 네트워킹 및 로드 밸런싱

**Day 26: AWS 로드 밸런싱**
- 오전: ELB 개요, ALB, NLB, CLB
- 오후: 타겟 그룹, 헬스체크, ALB 실습, SSL/TLS

**Day 27: Auto Scaling**
- 오전: Auto Scaling 개요, Launch Template, ASG 생성, 스케일링 정책
- 오후: ASG 구성 실습, ALB 통합, 스케일링 테스트, 비용 최적화

**Day 28: Route 53 및 CloudFront**
- 오전: Route 53 개요, DNS, 호스팅 영역, 라우팅 정책
- 오후: CloudFront 개요, CDN, 배포 생성, S3 + CloudFront

**Day 29: AWS 보안**
- 오전: 공동 책임 모델, IAM 심화, KMS, Secrets Manager
- 오후: WAF, Shield, 보안 강화 실습, 모범 사례

**Day 30: 모니터링 및 로깅**
- 오전: CloudWatch 개요, 메트릭/알람, Logs, Dashboards
- 오후: CloudTrail, Config, 모니터링 대시보드, 로그 분석

### 7주차: AWS 컨테이너 서비스

**Day 31: AWS 컨테이너 서비스 개요**
- 오전: ECS/EKS/Fargate 비교, 장단점, 오케스트레이션, 로드맵
- 오후: ECR, 리포지토리 생성, 이미지 푸시/풀, ECR 배포

**Day 32: ECS 기초**
- 오전: ECS 아키텍처, 클러스터/태스크/서비스, 실행 타입, 클러스터 생성
- 오후: 태스크 정의, 서비스 배포, ECS 배포 실습, 로드 밸런서

**Day 33: Fargate**
- 오전: Fargate 개요, 서버리스 컨테이너, Fargate vs EC2, 태스크 정의
- 오후: Fargate 실습, 네트워킹/보안, 비용 분석, 사용 사례

**Day 34: EKS 소개**
- 오전: EKS 개요, 아키텍처, EKS vs 자체 관리, 클러스터 준비
- 오후: eksctl, kubectl 설정, EKS 클러스터 생성, 노드 그룹

**Day 35: AWS 컨테이너 실습**
- 오전: ECS vs EKS 비교, 마이그레이션, 동일 앱 배포, 성능/비용
- 오후: App Mesh, 컨테이너 보안, 주간 복습, 미니 프로젝트

### 8주차: AWS 고급 서비스

**Day 36: Lambda 및 서버리스**
- 오전: Lambda 개요, 서버리스 아키텍처, 함수 생성, 트리거
- 오후: API Gateway, 서버리스 REST API, Lambda 레이어, 비용 최적화

**Day 37: 메시징 서비스**
- 오전: SQS, SNS, EventBridge, 메시징 패턴
- 오후: SQS + Lambda 실습, SNS 알림, 이벤트 기반 아키텍처, MSA 통신

**Day 38: 인프라 자동화 기초**
- 오전: CloudFormation 개요, 템플릿 구조, 스택 관리, 파라미터
- 오후: CloudFormation VPC 실습, 업데이트/롤백, 중첩 스택, vs Terraform

**Day 39: 비용 관리**
- 오전: 요금 모델, Cost Explorer, Budgets, 태그
- 오후: RI vs Savings Plans, Spot Instances, 비용 최적화, FinOps 기초

**Day 40: 2개월차 종합 프로젝트**
- 오전: 3-tier 웹 애플리케이션, VPC/EC2/RDS/S3/CloudFront, Auto Scaling/LB, 보안/모니터링
- 오후: 프로젝트 완성, 아키텍처 다이어그램, 발표, 복습

### 9주차: Kubernetes 기본 개념

**Day 41: Kubernetes 소개**
- 오전: K8s란?, 역사, 필요성, vs Docker Swarm
- 오후: 아키텍처, Control Plane, Node 컴포넌트, 설치 옵션

**Day 42: 환경 구성**
- 오전: Minikube 설치, kubectl, 클러스터 확인, 대시보드
- 오후: kubectl 명령어, 컨텍스트/네임스페이스, 첫 배포, YAML 기초

**Day 43: Pods**
- 오전: Pod 개념, 생명주기, 단일/멀티 컨테이너, 생성/관리
- 오후: Pod YAML, 다양한 Pod 생성, 로그/디버깅, Init/Sidecar

**Day 44: ReplicaSets 및 Deployments**
- 오전: ReplicaSet, Deployment 개념, 생성/관리, 레플리카 조정
- 오후: 롤링 업데이트, 롤백, 무중단 배포, Deployment 전략

**Day 45: Services**
- 오전: Service 개념, 타입, Service Discovery, Endpoints
- 오후: 다양한 Service 실습, Pod 연결, 로드 밸런싱, 주간 복습

### 10주차: Kubernetes 핵심 리소스

**Day 46: ConfigMaps 및 Secrets**
- 오전: ConfigMap 개념, 생성 방법, 환경 변수, 볼륨 마운트
- 오후: Secret 개념, 타입, ConfigMap/Secret 실습, 민감 정보 관리

**Day 47: Volumes 및 Persistent Storage**
- 오전: Volume 개념, 타입, PV, PVC
- 오후: StorageClass, 동적 프로비저닝, StatefulSet 실습, DB Pod

**Day 48: Namespaces 및 리소스 관리**
- 오전: Namespace 개념, 생성/관리, ResourceQuota, LimitRange
- 오후: 멀티 테넌트 실습, 네임스페이스 간 통신, 리소스 제한, 모범 사례

**Day 49: Labels, Selectors, Annotations**
- 오전: Label 개념, Selector, Annotation, Label 활용
- 오후: 라벨링 전략, 복잡한 Selector, 메타데이터, 조직화

**Day 50: 네트워킹 심화**
- 오전: 네트워킹 모델, CNI, Pod 간 통신, Service 네트워킹
- 오후: Ingress 개념, Ingress Controller, HTTP 라우팅, TLS/SSL

### 11주차: Kubernetes 고급 리소스

**Day 51: DaemonSets 및 Jobs**
- 오전: DaemonSet 개념, 생성/관리, 노드 선택, 로깅 에이전트
- 오후: Job 개념, CronJob, 배치 작업, 병렬 처리

**Day 52: StatefulSets**
- 오전: StatefulSet 개념, vs Deployment, 네트워크 ID, 순서 보장
- 오후: DB 클러스터 실습, Headless Service, 스케일링, 영속성

**Day 53: RBAC**
- 오전: 인증/인가, RBAC 개념, Role/ClusterRole, RoleBinding
- 오후: 사용자/서비스 계정 권한, 최소 권한, 보안 모범 사례, ServiceAccount

**Day 54: Resource Limits 및 QoS**
- 오전: CPU/메모리 요청/제한, QoS 클래스, 리소스 할당, 노드 관리
- 오후: 리소스 제한 실습, HPA, VPA, 클러스터 오토스케일러

**Day 55: 모니터링 및 로깅**
- 오전: 메트릭 서버, Prometheus, Grafana, 메트릭 수집
- 오후: 로깅 아키텍처, EFK Stack, 중앙 로깅, 주간 복습

### 12주차: Kubernetes 공식 문서 Deep Dive

**Day 56: Workloads**
- 오전: 공식 문서 구조, Workloads 리뷰, Pods/Controllers, 문서 실습
- 오후: Pod Lifecycle, Pod Disruption Budget, 고가용성, 문서 적용

**Day 57: Services & Networking**
- 오전: Services Deep Dive, Network Policies, DNS, Ingress 심화
- 오후: Network Policy 실습, MSA 네트워킹, 서비스 메시 준비, 트래픽 관리

**Day 58: Storage & Configuration**
- 오전: Storage Deep Dive, Volume Snapshots, CSI, 스토리지 클래스
- 오후: Configuration 심화, 복잡한 구성, 시크릿 고급, Vault

**Day 59: Security & Policies**
- 오전: Security Deep Dive, Pod Security Standards, Security Context, Network Policies
- 오후: 보안 강화 클러스터, Admission Controllers, OPA, 컴플라이언스

**Day 60: 3개월차 종합 프로젝트**
- 오전: K8s 마이크로서비스 배포, 멀티 티어, Ingress/Service/ConfigMap/Secret, 모니터링/로깅
- 오후: 프로젝트 완성, 고가용성/확장성, 발표, 복습

### 13주차: 클라우드 네이티브 Kubernetes

**Day 61: EKS 심화**
- 오전: EKS 아키텍처, 클러스터 생성, 관리형/자체 관리 노드, Fargate 프로필
- 오후: EKS 구성 실습, AWS Load Balancer Controller, EBS CSI Driver, AWS 통합

**Day 62: EKS 네트워킹 및 보안**
- 오전: VPC CNI, Security Groups for Pods, IRSA, Pod Identity
- 오후: IRSA 구성, EKS 보안 모범 사례, Secrets Manager, 네트워크 정책

**Day 63: GKE**
- 오전: GKE 개요, 클러스터 생성, Autopilot vs Standard, 네트워킹
- 오후: GKE 구성, Workload Identity, GCP 통합, EKS vs GKE

**Day 64: AKS**
- 오전: AKS 개요, 클러스터 생성, Azure CNI vs Kubenet, 네트워킹
- 오후: AKS 구성, Azure AD 통합, Azure 통합, 클라우드 비교

**Day 65: K8s 배포 시 AWS 고려사항**
- 오전: EKS 비용 구조, 컴퓨팅 최적화, 스토리지 비용, 네트워크 비용
- 오후: AWS 서비스 대체, ALB vs Nginx, EBS vs EFS, 비용 효율적 EKS

### 14주차: Kubernetes 고급 운영

**Day 66: Helm**
- 오전: Helm 개요, 아키텍처, 설치, Chart 구조
- 오후: Helm 배포, values.yaml, Repository 관리, Chart 생성

**Day 67: Operators**
- 오전: Operator 패턴, CRD, Operator Framework, 예제
- 오후: Prometheus Operator, MySQL Operator, Operator 개발, Hub

**Day 68: 고급 스케줄링**
- 오전: Node Selector, Node Affinity/Anti-Affinity, Pod Affinity, Taints/Tolerations
- 오후: 고급 스케줄링 실습, Topology Spread, Priority Classes, 최적화

**Day 69: 트러블슈팅**
- 오전: 일반적 문제, Pod 진단, 네트워크 문제, 스토리지 문제
- 오후: 장애 시나리오, kubectl 디버깅, 로그 분석, 성능 진단

**Day 70: 업그레이드 및 유지보수**
- 오전: 버전 정책, 클러스터 업그레이드, 노드 업그레이드, 마이그레이션
- 오후: 클러스터 업그레이드 실습, Velero 백업, 재해 복구, 주간 복습

### 15주차: Istio Service Mesh

**Day 71: Service Mesh 및 Istio 소개**
- 오전: Service Mesh란?, 필요성, Istio 아키텍처, Envoy Proxy
- 오후: Istio 설치, 프로필, 설치 검증, Sidecar Injection

**Day 72: Istio 트래픽 관리**
- 오전: Virtual Service, Destination Rule, Gateway, 트래픽 라우팅
- 오후: 카나리 배포, A/B 테스팅, 트래픽 미러링, 타임아웃/재시도

**Day 73: Istio 보안**
- 오전: mTLS, 인증 정책, 인가 정책, JWT 인증
- 오후: mTLS 구성, 세밀한 접근 제어, 보안 모범 사례, 인증서 관리

**Day 74: Istio 관찰성**
- 오전: 텔레메트리, Kiali, Jaeger, Prometheus/Grafana
- 오후: 관찰성 스택 구성, 서비스 메시 모니터링, 트래픽 분석, 성능 최적화

**Day 75: Istio 고급 기능**
- 오전: Circuit Breaking, Fault Injection, Rate Limiting, 멀티 클러스터
- 오후: 복원력 패턴, 성능 튜닝, 프로덕션 배포, 트러블슈팅

### 16주차: Kubernetes 실전 프로젝트

**Day 76: 프로젝트 계획**
- 오전: 요구사항 분석, MSA 설계, K8s 리소스 계획, Istio 통합
- 오후: 인프라 설계, 네트워킹, 보안, 모니터링/로깅

**Day 77: 인프라 구현**
- 오전: EKS 클러스터, VPC/네트워킹, IAM, 스토리지
- 오후: Istio 설치, 모니터링 스택, 로깅 스택, 검증

**Day 78: 애플리케이션 구현**
- 오전: 마이크로서비스 배포, Helm Chart, ConfigMap/Secret, 서비스 통신
- 오후: Istio 트래픽 관리, 보안 정책, 오토스케일링, 테스트

**Day 79: 최적화 및 테스트**
- 오전: 성능 테스트, 부하 테스트, 장애 시나리오, 복원력 검증
- 오후: 비용 최적화, 리소스 튜닝, 보안 강화, 문서화

**Day 80: 프로젝트 발표**
- 오전: 발표 준비, 아키텍처 다이어그램, 데모, 발표
- 오후: 피드백, 4개월차 복습, 핵심 개념, 5개월차 준비

### 17주차: CI/CD 기초

**Day 81: CI/CD 개념**
- 오전: CI 개념, CD 개념, 이점, 파이프라인 구성 요소
- 오후: 모범 사례, 설계 원칙, 브랜치 전략, Git 브랜치 실습

**Day 82: CI - 빌드 및 테스트**
- 오전: 소스 코드 관리, 자동화 빌드, 단위 테스트, 통합 테스트
- 오후: 코드 품질 검사, 테스트 커버리지, 테스트 자동화, 아티팩트 관리

**Day 83: CI - 보안 및 품질**
- 오전: 보안 스캔, 의존성 스캔, 컨테이너 스캔, 라이선스 검사
- 오후: 보안 스캔 통합, 코드 리뷰 자동화, 품질 게이트, SonarQube

**Day 84: CD - 배포 전략**
- 오전: 배포 전략 개요, 블루-그린, 카나리, 롤링
- 오후: A/B 테스팅, 피처 플래그, 배포 전략 실습, 롤백

**Day 85: CD - 환경 관리**
- 오전: 환경 분리, 환경별 구성, 프로모션, 승인 프로세스
- 오후: 멀티 환경 파이프라인, 환경 동기화, 드리프트 방지, 주간 복습

### 18주차: CI/CD 도구 실습

**Day 86: GitHub Actions 기초**
- 오전: GitHub Actions 개요, Workflow 구조, Events/Jobs/Steps, Marketplace
- 오후: 첫 Workflow, 환경 변수/시크릿, Matrix 빌드, Docker 이미지 빌드

**Day 87: GitHub Actions 심화**
- 오전: 재사용 Workflow, Composite Actions, 조건부 실행, 병렬 처리
- 오후: K8s 배포 자동화, Self-hosted Runners, 캐싱, 비용 최적화

**Day 88: Jenkins 기초**
- 오전: Jenkins 개요/설치, 아키텍처, Job 관리, Jenkinsfile
- 오후: Declarative vs Scripted, Pipeline 작성, 플러그인, Git 통합

**Day 89: Jenkins 심화**
- 오전: Multibranch Pipeline, Shared Libraries, Agent 구성, 분산 빌드
- 오후: K8s에서 Jenkins, Jenkins X, Blue Ocean, 보안

**Day 90: 기타 CI/CD 도구**
- 오전: CircleCI 실습, GitLab CI/CD 실습, TeamCity, Drone CI
- 오후: 도구 비교, 선택 기준, 동일 프로젝트 다른 도구, 마이그레이션

### 19주차: CI/CD 최적화

**Day 91: 파이프라인 최적화**
- 오전: 빌드 시간 단축, 캐싱, 병렬화, 증분 빌드
- 오후: 성능 최적화 실습, 리소스 효율화, 비용 최적화, 모니터링

**Day 92: CI/CD 보안**
- 오전: 파이프라인 보안, 시크릿 관리, 공급망 보안, SBOM
- 오후: 보안 강화 파이프라인, 서명/검증, 취약점 관리, 컴플라이언스

**Day 93: 모니터링 및 관찰성**
- 오전: 파이프라인 메트릭, 배포 빈도/리드 타임, 실패율/복구 시간, DORA
- 오후: CI/CD 대시보드, 알림/경고, 로그 분석, 지속적 개선

**Day 94: 주의사항 및 트러블슈팅**
- 오전: 안티패턴, 파이프라인 장애 대응, 디버깅, 롤백
- 오후: 장애 시나리오, 파이프라인 복원력, 재시도, Post-mortem

**Day 95: Docker Image Registry 심화**
- 오전: GHCR 심화, AWS ECR 심화, Harbor, 프라이빗 레지스트리
- 오후: 멀티 레지스트리, 이미지 복제/동기화, 레지스트리 보안, 주간 복습

### 20주차: GitOps 및 ArgoCD

**Day 96: GitOps 개념**
- 오전: GitOps란?, 원칙, Push vs Pull, 이점
- 오후: GitOps 워크플로우, Git as Single Source of Truth, 선언적 구성, 리포지토리 구조

**Day 97: ArgoCD 기초**
- 오전: ArgoCD 개요/아키텍처, 설치, Application, Sync 전략
- 오후: 첫 애플리케이션 배포, UI 탐색, CLI, 자동/수동 동기화

**Day 98: ArgoCD 심화**
- 오전: ApplicationSet, App of Apps, 멀티 클러스터, 프로젝트/RBAC
- 오후: 복잡한 GitOps 워크플로우, Helm 통합, Kustomize 통합, 시크릿 관리

**Day 99: ArgoCD 고급**
- 오전: Progressive Delivery, Argo Rollouts, 카나리 자동화, 블루-그린 자동화, 메트릭 기반 프로모션
- 오후: Argo Rollouts 구성, Notifications/Webhooks, Image Updater, 모니터링

**Day 100: 5개월차 종합 프로젝트**
- 오전: 완전 자동화 CI/CD, GitHub Actions + ArgoCD, 멀티 환경, 보안/품질 게이트
- 오후: 프로젝트 완성, 발표, 5개월차 복습, 6개월차 준비

### 21주차: Terraform 기초

**Day 101: IaC 개념**
- 오전: IaC란?, 이점, 선언형 vs 명령형, 도구 비교
- 오후: Terraform 개요, 아키텍처, 설치/설정, 첫 구성

**Day 102: Terraform 기본 문법**
- 오전: HCL, Providers, Resources, Data Sources
- 오후: Variables, Outputs, AWS 리소스 생성, Terraform 명령어

**Day 103: State 관리**
- 오전: State란?, Local vs Remote, State Locking, S3 Backend
- 오후: Remote State 구성, State 명령어, State 보안, 백업/복구

**Day 104: 모듈**
- 오전: 모듈 개념, 구조, 입력/출력, 로컬/원격 모듈
- 오후: 첫 모듈 작성, Terraform Registry, 버전 관리, 재사용 전략

**Day 105: Workspace 및 환경 관리**
- 오전: Workspace 개념, 환경 분리, .tfvars, 환경별 구성
- 오후: 멀티 환경 구성, 조건부 리소스, 동적 블록, 주간 복습

### 22주차: Terraform 심화

**Day 106: 고급 기능**
- 오전: Count vs For_each, Dynamic Blocks, Locals, Functions
- 오후: 고급 패턴 실습, Terraform Console, 표현식/연산자, 타입 제약

**Day 107: AWS 통합**
- 오전: AWS Provider 심화, IAM, VPC/네트워킹, EC2/Auto Scaling
- 오후: 3-tier 아키텍처 실습, RDS/DB, S3/CloudFront, Route 53

**Day 108: 모범 사례**
- 오전: 코드 구조화, 네이밍 컨벤션, 문서화, 버전 관리
- 오후: 보안 모범 사례, 시크릿 관리, 프로덕션 프로젝트, 코드 리뷰

**Day 109: 테스팅**
- 오전: Terraform Validate, Plan 분석, Terraform Test, Terratest
- 오후: 코드 테스트 실습, 정적 분석, 정책 검증, CI/CD 통합

**Day 110: 장단점 및 사용 케이스**
- 오전: Terraform 장점, 한계, 선언형이 좋을 때, 명령형이 좋을 때
- 오후: vs CloudFormation, vs Pulumi, 하이브리드, 도구 선택

### 23주차: Terraform 실전

**Day 111: VPC 및 네트워킹**
- 오전: VPC 모듈 설계, 서브넷/라우팅/게이트웨이, 보안 그룹/NACL, VPC Peering/Transit Gateway
- 오후: Terraform VPC 실습, 멀티 AZ, 네트워크 보안, 비용 최적화

**Day 112: 컴퓨팅 및 스토리지**
- 오전: EC2 모듈, Auto Scaling, Load Balancer, Launch Template
- 오후: 컴퓨팅 리소스 배포, EBS 관리, S3 구성, 백업/스냅샷

**Day 113: 데이터베이스 및 캐싱**
- 오전: RDS 모듈, DynamoDB, ElastiCache, DB 보안
- 오후: 데이터베이스 배포, 백업/복원 자동화, 읽기 전용 복제본, 성능 최적화

**Day 114: 컨테이너 및 서버리스**
- 오전: ECS/EKS 클러스터, Fargate, Lambda, API Gateway
- 오후: EKS 클러스터 배포, 컨테이너 서비스, 서버리스 아키텍처, 통합 테스트

**Day 115: 모듈화 프로젝트**
- 오전: 서비스별 모듈 설계, 인터페이스 정의, 의존성 관리, 문서화
- 오후: 재사용 가능 모듈, 모듈 테스트, 버전 관리, 주간 복습

### 24주차: Terraform Import 및 FinOps

**Day 116: Terraform Import 기초**
- 오전: Import 개념, 워크플로우, 리소스 식별, Import 명령어
- 오후: 기존 AWS 리소스 Import, State 정리, 구성 파일 생성, 자동화

**Day 117: Import 고급**
- 오전: 복잡한 리소스 Import, 모듈 Import, 대량 Import, Import 블록
- 오후: 전체 인프라 Import, Import 검증, Drift 감지/해결, 문서화

**Day 118: FinOps 개념**
- 오전: FinOps란?, 프레임워크, 클라우드 재무 관리, FinOps 팀
- 오후: AWS 비용 구조, 비용 가시성, 비용 할당/차지백, FinOps 문화

**Day 119: AWS 비용 최적화**
- 오전: Cost Explorer 심화, Budgets/알림, Cost Anomaly Detection, Savings Plans vs RI
- 오후: 비용 분석/최적화, 라이트사이징, Spot Instances, 스토리지 최적화

**Day 120: FinOps 도구 및 자동화**
- 오전: Cost and Usage Report, Terraform 비용 관리, 태깅 전략, 비용 최적화 자동화
- 오후: FinOps 대시보드, 비용 알림 자동화, 리소스 정리 자동화, 6개월차 복습

### 25주차: 최종 프로젝트

**Day 121: 프로젝트 기획**
- 오전: 요구사항 정의, 아키텍처 설계, 기술 스택, 팀 구성
- 오후: 인프라 설계, CI/CD 설계, GitOps 설계, 일정 수립

**Day 122: 인프라 구축**
- 오전: Terraform AWS 인프라, VPC/네트워킹/보안, EKS 클러스터, 모니터링/로깅
- 오후: Istio 설치, ArgoCD 구성, 인프라 검증, 문서화

**Day 123: 애플리케이션 배포**
- 오전: 마이크로서비스 컨테이너화, Helm Chart, GitOps 리포지토리, ArgoCD Application
- 오후: CI/CD 파이프라인, 자동화 테스트, 보안 스캔, 배포 자동화

**Day 124: 운영 및 최적화**
- 오전: 모니터링 대시보드, 알림/경고, 로그 분석, 성능 테스트
- 오후: 비용 최적화, 보안 강화, 고가용성 검증, 재해 복구

**Day 125: 프로젝트 발표**
- 오전: 발표 준비, 데모 리허설, 아키텍처 다이어그램, 문서 정리
- 오후: 최종 발표, 질의응답, 피드백, 프로젝트 회고

### 26주차: 취업 준비

**Day 126: DevOps 취업 준비**
- 오전: 직무 이해, 이력서 작성, 포트폴리오, GitHub 프로필
- 오후: 기술 면접 준비, 면접 질문, 모의 면접, 면접 팁

**Day 127: 면접 대비 - Docker & Kubernetes**
- 오전: Docker 핵심 복습, Docker 면접 질문, K8s 핵심 복습, K8s 면접 질문
- 오후: 실전 문제, 트러블슈팅 시나리오, 모의 면접, 피드백

**Day 128: 면접 대비 - AWS & Terraform**
- 오전: AWS 핵심 복습, AWS 면접 질문, Terraform 핵심 복습, IaC 면접 질문
- 오후: 실전 문제, 아키텍처 설계, 모의 면접, 피드백

**Day 129: 면접 대비 - CI/CD & DevOps**
- 오전: CI/CD 핵심 복습, CI/CD 면접 질문, DevOps 문화, 소프트 스킬
- 오후: 실전 문제, 시스템 설계, 모의 면접, 피드백

**Day 130: 과정 수료**
- 오전: 6개월 전체 복습, 핵심 개념 정리, 학습 성과 평가, 수료증
- 오후: 향후 학습 로드맵, 추가 자료, 커뮤니티/네트워킹, 수료식

---

## 📊 주요 학습 주제 매핑

### Docker 관련
**WHEN** Docker 질문이 들어오면,
**THE SYSTEM SHALL** 위의 Day 1-20 상세 커리큘럼을 참조한다.

### AWS 관련
**WHEN** AWS 질문이 들어오면,
**THE SYSTEM SHALL** 위의 Day 21-40 상세 커리큘럼을 참조한다.

### Kubernetes 관련
**WHEN** Kubernetes 질문이 들어오면,
**THE SYSTEM SHALL** 위의 Day 41-80 상세 커리큘럼을 참조한다.

### CI/CD 관련
**WHEN** CI/CD 질문이 들어오면,
**THE SYSTEM SHALL** 위의 Day 81-100 상세 커리큘럼을 참조한다.

### Terraform 관련
**WHEN** Terraform 질문이 들어오면,
**THE SYSTEM SHALL** 위의 Day 101-120 상세 커리큘럼을 참조한다.

### 최종 프로젝트 및 취업 준비
**WHEN** 최종 프로젝트나 취업 준비 질문이 들어오면,
**THE SYSTEM SHALL** 위의 Day 121-130 상세 커리큘럼을 참조한다.

---

## 🎓 프로젝트 가이드

**WHEN** 사용자가 프로젝트 구현을 요청하면,
**THE SYSTEM SHALL** 다음 단계를 제안한다:

### 월별 프로젝트
1. **1개월차**: Docker 기반 멀티 컨테이너 애플리케이션
2. **2개월차**: AWS 3-tier 웹 애플리케이션
3. **3개월차**: Kubernetes 마이크로서비스 배포
4. **4개월차**: Istio Service Mesh 통합
5. **5개월차**: CI/CD 파이프라인 자동화
6. **6개월차**: Terraform 전체 인프라 자동화

### 최종 프로젝트 요구사항
**WHERE** 최종 프로젝트를 진행할 때,
**THE SYSTEM SHALL** 다음을 포함한다:
- Docker 컨테이너화된 마이크로서비스 (3개 이상)
- AWS EKS 클러스터
- Istio Service Mesh
- Terraform IaC
- GitHub Actions + ArgoCD GitOps
- Prometheus + Grafana 모니터링
- EFK Stack 로깅
- 보안 스캔 및 품질 게이트
- 비용 최적화

---

## 💡 학습 지원 규칙

**IF** 사용자가 특정 일차의 내용을 요청하면,
**THEN** 해당 일차의 오전/오후 커리큘럼을 상세히 제공한다.

**IF** 사용자가 실습 가이드를 요청하면,
**THEN** 단계별 실습 절차를 제공한다.

**IF** 사용자가 트러블슈팅을 요청하면,
**THEN** 해당 기술의 일반적인 문제와 해결 방법을 제공한다.

**IF** 사용자가 면접 준비를 요청하면,
**THEN** Day 126-129의 면접 준비 내용을 참조한다.

**WHERE** 공식 문서를 참조해야 할 때,
**THE SYSTEM SHALL** 최신 공식 문서 링크를 제공한다.

**WHEN** 사용자가 학습 순서를 질문하면,
**THE SYSTEM SHALL** 선수 학습이 필요한 내용을 먼저 안내한다.

---

## 🔍 빠른 참조

### 주차별 핵심 키워드
- **Week 1-4**: Docker, Container, Compose, Swarm, MSA
- **Week 5-8**: AWS, EC2, S3, RDS, VPC, ECS, EKS
- **Week 9-12**: Kubernetes, Pods, Services, Volumes, RBAC
- **Week 13-16**: EKS, GKE, AKS, Istio, Service Mesh
- **Week 17-20**: CI/CD, GitHub Actions, Jenkins, ArgoCD, GitOps
- **Week 21-26**: Terraform, IaC, Import, FinOps, 최종 프로젝트

### 기술 스택 의존성
**WHEN** 학습 순서를 결정할 때,
**THE SYSTEM SHALL** 다음 의존성을 고려한다:
- Docker → Kubernetes
- AWS 기초 → EKS
- Kubernetes → Istio
- Git → CI/CD → GitOps
- AWS → Terraform AWS Provider
- 모든 기술 → 최종 프로젝트

---

## 📚 참고 문서 위치

**전체 커리큘럼**: `DevOps_6개월_교육과정_커리큘럼.md`

**WHEN** 사용자가 상세 커리큘럼을 요청하면,
**THE SYSTEM SHALL** 위 파일을 참조하여 답변한다.

