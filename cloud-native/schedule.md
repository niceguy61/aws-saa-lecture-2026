# 6주 강의 시간표

이 문서는 Cloud Native DevOps 6주 이론 과정의 1차 작업 시간표입니다.

## 수업 시간 모델

| 시간 | 교시 |
|---|---|
| 09:00-09:50 | 1교시 |
| 10:00-10:50 | 2교시 |
| 11:00-11:50 | 3교시 |
| 12:00-12:50 | 4교시 |
| 13:00-14:00 | 점심 |
| 14:00-14:50 | 5교시 |
| 15:00-15:50 | 6교시 |
| 16:00-16:50 | 7교시 |
| 17:00-17:50 | 8교시 |

기본 비율:

- 이론과 설명: 5-6교시
- 데모, 영상, 애플리케이션 시연: 1교시
- 랩 또는 미션: 1-2교시
- 정리와 회고: 마지막 20-30분

## 전체 일별 시간표

| 주차 | 일차 | 주제 | 주요 교시 | 랩/미션/데모 |
|---|---:|---|---|---|
| 01 | 01 | 과정 OT, 아이스 브레이킹, 개발 환경 준비 | 자기소개와 기대치 공유, 과정 OT, 1-3주차 흐름, 4-6주차 흐름 | Docker Desktop, VS Code, WSL, AI 도구, CLI coding agent 사용 준비를 점검한다. |
| 01 | 02 | Cloud Native를 위한 컴퓨팅 기초 | 프로그램과 프로세스의 차이, localhost와 포트의 의미 | 작은 로컬 웹 애플리케이션을 실행하고, 프로세스, 포트, 요청 경로, 로그를 확인한다. |
| 01 | 03 | Linux와 터미널 생존법 | 명령어 구조와 옵션 읽는 법, 경로와 현재 작업 디렉터리 | 실패하는 명령어의 원인을 찾고, 에러 메시지를 쉬운 말로 설명한 뒤 올바른 명령어를 작성한다. |
| 01 | 04 | 웹 애플리케이션의 모양 | 클라이언트, API, 데이터베이스, 정적 파일의 역할, 설정과 health check가 필요한 이유 | 강사가 만든 재미있는 앱이 설정 누락, 포트 문제, 의존성 장애로 실패하는 모습을 보고 원인을 추론한다. |
| 01 | 05 | Cloud와 DevOps 용어 | Cloud, Region, 계정, VM, Container의 의미, 배포와 롤백의 기본 흐름 | 코드 변경이 실행 중인 서비스가 되기까지의 배포 이야기를 팀별로 설명한다. 실패 또는 롤백 상황을 하나 포함한다. |
| 02 | 01 | 컨테이너 개념 모델 | Image, Container, Registry, Tag, Runtime의 의미, Image와 실행 중인 Container의 차이 | 간단한 컨테이너를 실행하고 상태, 로그, 내부 접근, 중지, 삭제를 안전하게 연습한다. |
| 02 | 02 | Docker Image | Dockerfile 구조, Image layer와 build cache의 초급 개념 | 간단한 API 이미지를 빌드하고 tag를 붙인 뒤 실행한다. Dockerfile의 각 줄이 어떤 역할을 했는지 설명한다. |
| 02 | 03 | 런타임 설정 | 환경 변수, 포트, 볼륨, 로그, 재시작 동작과 exit code | 시작은 되지만 제대로 동작하지 않는 컨테이너를 로그, 포트 매핑, 환경 변수를 근거로 고친다. |
| 02 | 04 | Docker Compose | Compose service, network, volume, environment 문법, Service 이름이 로컬 DNS처럼 쓰이는 방식 | Docker Compose로 API와 데이터베이스를 실행하고, API가 DB에 도달하는 방식을 증명한다. |
| 02 | 05 | Image 품질과 전달 | 작고 명확한 이미지가 운영에 유리한 이유, 흔한 이미지 실수 | Docker Image를 개선하고 크기, 명확성, 안전성, 반복 가능성 중 어떤 점이 좋아졌는지 설명한다. |
| 03 | 01 | Kubernetes 큰 그림 | Cluster, Node, Control Plane, Workload, kubectl, Desired state와 actual state | 로컬 Kubernetes Cluster를 관찰하고 Node, Namespace, 기본 Object를 식별한다. |
| 03 | 02 | Pod와 Deployment | Pod, ReplicaSet, Deployment, Container의 관계, Rollout과 rollback 개념 | 애플리케이션을 배포하고 scale, image update, rollback을 수행한다. |
| 03 | 03 | 설정과 Health Check | ConfigMap과 Secret의 초급 개념, Liveness와 readiness probe | 설정, probe, events를 확인해 실패한 rollout을 복구한다. |
| 03 | 04 | Service와 Namespace | Service, Selector, Endpoint, ClusterIP, Pod IP가 안정적인 주소가 아닌 이유 | Cluster 내부에서 애플리케이션을 노출하고 어떤 Pod가 트래픽을 받는지 증명한다. |
| 03 | 05 | Kubernetes 디버깅 | get, describe, logs, exec, events 사용 흐름, Pending, CrashLoopBackOff, ImagePullBackOff, NotReady 증상 | 고장난 Kubernetes workload를 진단하고 증상, 근거, 원인, 수정 방법을 제출한다. |
| 04 | 01 | Kubernetes 네트워킹 모델 | Pod IP, Service IP, DNS, Endpoint, kube-proxy 개념, Pod가 Running이어도 트래픽이 실패할 수 있는 이유 | 한 Pod에서 Service까지 요청이 이동하는 경로를 추적하고 어디서 깨질 수 있는지 표시한다. |
| 04 | 02 | Ingress와 HTTP Routing | Ingress, Ingress Controller, Host routing, Path routing, Service와 Ingress의 차이 | HTTP 트래픽을 Service로 라우팅하고 브라우저에서 Pod까지의 경로를 설명한다. |
| 04 | 03 | Storage와 State | Volume, PersistentVolume, PersistentVolumeClaim, StatefulSet 개념, Stateless와 stateful workload의 차이 | 상태를 잘못 다루면 데이터가 사라지거나 숨는 모습을 보고 더 안전한 패턴을 선택한다. |
| 04 | 04 | Scheduling과 Scaling | Requests, limits, node capacity, scheduling, 수평 확장 개념 | 작은 workload로 scheduling과 scaling 동작을 관찰한다. |
| 04 | 05 | 운영 리뷰 | Rollout strategy와 failure drill 기초, Cleanup과 운영 체크리스트 습관 | 증상, 영향, 원인, 수정, 예방, cleanup을 포함한 미니 incident review를 진행한다. |
| 05 | 01 | AWS OT와 안전 | AWS Account, IAM, Region, VPC, Budget의 초급 의미, Credential 안전과 비용 감각 | 위험한 Cloud 사용 습관을 찾아 안전한 수업 규칙으로 바꾼다. |
| 05 | 02 | AWS Container Service | ECR, ECS, EKS, App Runner, Lambda container image 개념, Managed service의 tradeoff | 같은 컨테이너 앱을 여러 AWS 배포 선택지에 매핑하고 장단점을 비교한다. |
| 05 | 03 | AWS 네트워킹과 외부 노출 | VPC, Subnet, Security Group, Load Balancer, Route 53, ACM, Public 노출과 private 보호의 차이 | 간단한 애플리케이션의 안전한 외부 노출 경로를 선택하고 private로 남겨야 할 영역을 설명한다. |
| 05 | 04 | Managed Data와 Integration | RDS, DynamoDB, S3, SQS, Secrets Manager의 개념, 애플리케이션이 DB, Object Storage, Queue, Secret Storage를 필요로 하는 경우 | 샘플 애플리케이션이 managed service를 사용할 때 팀이 직접 운영하지 않아도 되는 것과 여전히 책임져야 하는 것을 구분한다. |
| 05 | 05 | AWS 설계 스튜디오 | 비용, 신뢰성, 운영, 보안 균형 잡기, 배포 대상과 managed service 선택 | 작은 애플리케이션의 Cloud Native 배포 설계를 만들고 선택 이유를 방어한다. |
| 06 | 01 | Observability 기초 | Metrics, logs, traces, events의 차이, Dashboard가 증명할 수 있는 것과 없는 것 | 애플리케이션 로그와 메트릭을 확인하고 어떤 signal이 증상을 가장 잘 설명하는지 말한다. |
| 06 | 02 | Kubernetes 보안 기초 | RBAC, Service Account, Secret 처리, Image 위험, Least privilege가 중요한 이유 | 샘플 workload에서 unsafe default를 찾고 초급 수준에서 더 안전한 대안을 설명한다. |
| 06 | 03 | CI/CD와 GitOps 개념 | Build, test, image push, deploy, rollback, promotion, CI/CD pipeline stage | 강사가 만든 pipeline을 따라 code change부터 deployed workload까지의 흐름을 확인한다. |
| 06 | 04 | Capstone 준비 | 시스템 설명을 구조화하는 방법, Architecture와 traffic flow 그리기 | Architecture, 배포 경로, 실패 사례, 설명 계획을 포함한 최종 시나리오를 준비한다. |
| 06 | 05 | Capstone Day | 시스템 설계를 명확히 전달하는 방법, 증상에서 원인으로 추론하는 방법 | 시스템과 하나의 실패 상황을 설명한다. Architecture, 배포 경로, 증거, 원인, 수정, 예방을 포함한다. |


## 1주차 - OT와 컴퓨팅 기초

목적: 비전공 학생이 Docker, Kubernetes, AWS를 배우기 전에 필요한 최소한의 컴퓨팅 감각과 수업 분위기를 만든다.

| 일차 | 주제 | 주요 흐름 | 랩/미션/데모 |
|---|---|---|---|
| 01 | 과정 OT, 아이스 브레이킹, 개발 환경 준비 | 자기소개와 기대치 공유, 과정 OT, 1-3주차 흐름, 4-6주차 흐름 | Docker Desktop, VS Code, WSL, AI 도구, CLI coding agent 사용 준비를 점검한다. |
| 02 | Cloud Native를 위한 컴퓨팅 기초 | 프로그램과 프로세스의 차이, localhost와 포트의 의미 | 작은 로컬 웹 애플리케이션을 실행하고, 프로세스, 포트, 요청 경로, 로그를 확인한다. |
| 03 | Linux와 터미널 생존법 | 명령어 구조와 옵션 읽는 법, 경로와 현재 작업 디렉터리 | 실패하는 명령어의 원인을 찾고, 에러 메시지를 쉬운 말로 설명한 뒤 올바른 명령어를 작성한다. |
| 04 | 웹 애플리케이션의 모양 | 클라이언트, API, 데이터베이스, 정적 파일의 역할, 설정과 health check가 필요한 이유 | 강사가 만든 재미있는 앱이 설정 누락, 포트 문제, 의존성 장애로 실패하는 모습을 보고 원인을 추론한다. |
| 05 | Cloud와 DevOps 용어 | Cloud, Region, 계정, VM, Container의 의미, 배포와 롤백의 기본 흐름 | 코드 변경이 실행 중인 서비스가 되기까지의 배포 이야기를 팀별로 설명한다. 실패 또는 롤백 상황을 하나 포함한다. |

## 2주차 - Docker와 Docker Compose

목적: 컨테이너를 추상 개념이 아니라 애플리케이션을 같은 방식으로 실행하기 위한 도구로 이해한다.

| 일차 | 주제 | 주요 흐름 | 랩/미션/데모 |
|---|---|---|---|
| 01 | 컨테이너 개념 모델 | Image, Container, Registry, Tag, Runtime의 의미, Image와 실행 중인 Container의 차이 | 간단한 컨테이너를 실행하고 상태, 로그, 내부 접근, 중지, 삭제를 안전하게 연습한다. |
| 02 | Docker Image | Dockerfile 구조, Image layer와 build cache의 초급 개념 | 간단한 API 이미지를 빌드하고 tag를 붙인 뒤 실행한다. Dockerfile의 각 줄이 어떤 역할을 했는지 설명한다. |
| 03 | 런타임 설정 | 환경 변수, 포트, 볼륨, 로그, 재시작 동작과 exit code | 시작은 되지만 제대로 동작하지 않는 컨테이너를 로그, 포트 매핑, 환경 변수를 근거로 고친다. |
| 04 | Docker Compose | Compose service, network, volume, environment 문법, Service 이름이 로컬 DNS처럼 쓰이는 방식 | Docker Compose로 API와 데이터베이스를 실행하고, API가 DB에 도달하는 방식을 증명한다. |
| 05 | Image 품질과 전달 | 작고 명확한 이미지가 운영에 유리한 이유, 흔한 이미지 실수 | Docker Image를 개선하고 크기, 명확성, 안전성, 반복 가능성 중 어떤 점이 좋아졌는지 설명한다. |

## 3주차 - Kubernetes Core

목적: Kubernetes를 명령어 묶음이 아니라 원하는 상태를 계속 맞추는 시스템으로 이해한다.

| 일차 | 주제 | 주요 흐름 | 랩/미션/데모 |
|---|---|---|---|
| 01 | Kubernetes 큰 그림 | Cluster, Node, Control Plane, Workload, kubectl, Desired state와 actual state | 로컬 Kubernetes Cluster를 관찰하고 Node, Namespace, 기본 Object를 식별한다. |
| 02 | Pod와 Deployment | Pod, ReplicaSet, Deployment, Container의 관계, Rollout과 rollback 개념 | 애플리케이션을 배포하고 scale, image update, rollback을 수행한다. |
| 03 | 설정과 Health Check | ConfigMap과 Secret의 초급 개념, Liveness와 readiness probe | 설정, probe, events를 확인해 실패한 rollout을 복구한다. |
| 04 | Service와 Namespace | Service, Selector, Endpoint, ClusterIP, Pod IP가 안정적인 주소가 아닌 이유 | Cluster 내부에서 애플리케이션을 노출하고 어떤 Pod가 트래픽을 받는지 증명한다. |
| 05 | Kubernetes 디버깅 | get, describe, logs, exec, events 사용 흐름, Pending, CrashLoopBackOff, ImagePullBackOff, NotReady 증상 | 고장난 Kubernetes workload를 진단하고 증상, 근거, 원인, 수정 방법을 제출한다. |

## 4주차 - Kubernetes 네트워킹과 운영

목적: Kubernetes 안에서 트래픽이 이동하는 방식과 운영 중 나타나는 증상을 연결해서 이해한다.

| 일차 | 주제 | 주요 흐름 | 랩/미션/데모 |
|---|---|---|---|
| 01 | Kubernetes 네트워킹 모델 | Pod IP, Service IP, DNS, Endpoint, kube-proxy 개념, Pod가 Running이어도 트래픽이 실패할 수 있는 이유 | 한 Pod에서 Service까지 요청이 이동하는 경로를 추적하고 어디서 깨질 수 있는지 표시한다. |
| 02 | Ingress와 HTTP Routing | Ingress, Ingress Controller, Host routing, Path routing, Service와 Ingress의 차이 | HTTP 트래픽을 Service로 라우팅하고 브라우저에서 Pod까지의 경로를 설명한다. |
| 03 | Storage와 State | Volume, PersistentVolume, PersistentVolumeClaim, StatefulSet 개념, Stateless와 stateful workload의 차이 | 상태를 잘못 다루면 데이터가 사라지거나 숨는 모습을 보고 더 안전한 패턴을 선택한다. |
| 04 | Scheduling과 Scaling | Requests, limits, node capacity, scheduling, 수평 확장 개념 | 작은 workload로 scheduling과 scaling 동작을 관찰한다. |
| 05 | 운영 리뷰 | Rollout strategy와 failure drill 기초, Cleanup과 운영 체크리스트 습관 | 증상, 영향, 원인, 수정, 예방, cleanup을 포함한 미니 incident review를 진행한다. |

## 5주차 - AWS 기반 Cloud Native 애플리케이션

목적: AWS를 컨테이너 애플리케이션을 배포하고 운영하는 현실적인 클라우드 환경으로 이해한다.

| 일차 | 주제 | 주요 흐름 | 랩/미션/데모 |
|---|---|---|---|
| 01 | AWS OT와 안전 | AWS Account, IAM, Region, VPC, Budget의 초급 의미, Credential 안전과 비용 감각 | 위험한 Cloud 사용 습관을 찾아 안전한 수업 규칙으로 바꾼다. |
| 02 | AWS Container Service | ECR, ECS, EKS, App Runner, Lambda container image 개념, Managed service의 tradeoff | 같은 컨테이너 앱을 여러 AWS 배포 선택지에 매핑하고 장단점을 비교한다. |
| 03 | AWS 네트워킹과 외부 노출 | VPC, Subnet, Security Group, Load Balancer, Route 53, ACM, Public 노출과 private 보호의 차이 | 간단한 애플리케이션의 안전한 외부 노출 경로를 선택하고 private로 남겨야 할 영역을 설명한다. |
| 04 | Managed Data와 Integration | RDS, DynamoDB, S3, SQS, Secrets Manager의 개념, 애플리케이션이 DB, Object Storage, Queue, Secret Storage를 필요로 하는 경우 | 샘플 애플리케이션이 managed service를 사용할 때 팀이 직접 운영하지 않아도 되는 것과 여전히 책임져야 하는 것을 구분한다. |
| 05 | AWS 설계 스튜디오 | 비용, 신뢰성, 운영, 보안 균형 잡기, 배포 대상과 managed service 선택 | 작은 애플리케이션의 Cloud Native 배포 설계를 만들고 선택 이유를 방어한다. |

## 6주차 - Observability, 보안, 최종 통합

목적: 배포 이후의 동작을 관찰하고, 기본 보안을 적용하며, 전체 시스템을 설명할 수 있게 만든다.

| 일차 | 주제 | 주요 흐름 | 랩/미션/데모 |
|---|---|---|---|
| 01 | Observability 기초 | Metrics, logs, traces, events의 차이, Dashboard가 증명할 수 있는 것과 없는 것 | 애플리케이션 로그와 메트릭을 확인하고 어떤 signal이 증상을 가장 잘 설명하는지 말한다. |
| 02 | Kubernetes 보안 기초 | RBAC, Service Account, Secret 처리, Image 위험, Least privilege가 중요한 이유 | 샘플 workload에서 unsafe default를 찾고 초급 수준에서 더 안전한 대안을 설명한다. |
| 03 | CI/CD와 GitOps 개념 | Build, test, image push, deploy, rollback, promotion, CI/CD pipeline stage | 강사가 만든 pipeline을 따라 code change부터 deployed workload까지의 흐름을 확인한다. |
| 04 | Capstone 준비 | 시스템 설명을 구조화하는 방법, Architecture와 traffic flow 그리기 | Architecture, 배포 경로, 실패 사례, 설명 계획을 포함한 최종 시나리오를 준비한다. |
| 05 | Capstone Day | 시스템 설계를 명확히 전달하는 방법, 증상에서 원인으로 추론하는 방법 | 시스템과 하나의 실패 상황을 설명한다. Architecture, 배포 경로, 증거, 원인, 수정, 예방을 포함한다. |


## 보충/심화 자료 운영

주요 내용이 너무 어려워지는 경우 본문에 모두 넣지 않고 별도 보충/심화 자료로 분리합니다.

보충 자료 후보:

- 터미널 기초
- HTTP와 DNS 기초
- Linux process와 port 기초
- YAML 기초
- 배포를 위한 Git 기초

심화 자료 후보:

- Container image layer
- Kubernetes Control Plane 내부 구조
- CNI와 kube-proxy 상세
- Ingress Controller 내부 구조
- IAM과 AWS 네트워킹 상세
- Prometheus data model과 alert 품질
