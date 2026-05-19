# Cloud Native DevOps 강의

이 과정은 비전공 대학생도 따라올 수 있도록 Docker, Docker Compose, Kubernetes, AWS를 단계적으로 배우는 6주 강의입니다.

AWS는 컨테이너 기반 애플리케이션을 실제 Cloud 환경에서 배포하고 운영하기 위한 맥락으로 다룹니다.

## 대상 학습자

- Cloud, DevOps, Platform Engineering을 처음 접하는 비전공 대학생
- 로컬 애플리케이션이 Cloud 서비스가 되는 흐름을 이해하고 싶은 초급 개발자
- 고급 아키텍처보다 용어, 그림, 데모, 작은 실습이 먼저 필요한 학습자

## 과정 목표

과정을 마치면 학습자는 다음을 할 수 있어야 합니다.

- 로컬 애플리케이션이 Container, Kubernetes, AWS로 이어지는 흐름을 설명한다.
- Docker와 Docker Compose로 간단한 애플리케이션을 실행한다.
- Kubernetes의 Workload, Service, Ingress, 설정, 기본 운영 흐름을 이해한다.
- AWS를 안전하게 사용하는 기본 습관과 Cloud Native 배포 선택지를 설명한다.
- 로그, 메트릭, 대시보드, 실패 증상을 초급 수준에서 읽는다.
- 작은 랩과 미션을 통해 시스템을 관찰하고 문제를 설명한다.

## 6주 커리큘럼

| 주차 | 주제 | 핵심 질문 |
|---|---|---|
| 01 | OT와 컴퓨팅 기초 | Docker와 Cloud Native를 배우기 전에 무엇을 알아야 할까? |
| 02 | Docker와 Docker Compose | 애플리케이션을 어떻게 같은 방식으로 포장하고 실행할까? |
| 03 | Kubernetes Core | Kubernetes는 애플리케이션을 어떻게 계속 실행 상태로 유지할까? |
| 04 | Kubernetes 네트워킹과 운영 | 트래픽은 어떻게 이동하고, 운영 중 문제는 어떻게 읽을까? |
| 05 | AWS 기반 Cloud Native 애플리케이션 | Cloud 서비스는 컨테이너 애플리케이션을 어떻게 도와줄까? |
| 06 | Observability, 보안, 최종 통합 | 실행 중인 시스템을 어떻게 이해하고 안전하게 설명할까? |

## 바로가기

- [6주 전체 시간표](schedule.md)
- [학습 설계 가이드](LEARNING_DESIGN.md)
- [1주차 - OT와 컴퓨팅 기초](week01/README.md)
- [2주차 - Docker와 Docker Compose](week02/README.md)
- [3주차 - Kubernetes Core](week03/README.md)
- [4주차 - Kubernetes 네트워킹과 운영](week04/README.md)
- [5주차 - AWS 기반 Cloud Native 애플리케이션](week05/README.md)
- [6주차 - Observability, 보안, 최종 통합](week06/README.md)

## 공통 시나리오

과정 전체는 하나의 반복 시나리오를 계속 확장합니다.

> 작은 제품 팀이 노트북에서만 실행되던 웹 API를 Cloud Native 플랫폼으로 옮긴다. 팀은 안정적인 배포, 안전한 트래픽 노출, 명확한 보안 경계, 장애를 설명할 수 있는 관측 가능성이 필요하다.

이 시나리오는 이론, 랩, 미션, 다이어그램, 강사 노트, 스틱맨 이미지에 반복해서 등장합니다.

## 시각 자료 방향

- 시스템 구조, 트래픽 흐름, 생명주기, 문제 해결 경로는 Mermaid 다이어그램으로 표현합니다.
- 배포 압박, 네트워크 장애, Secret 유출, 장애 회고 같은 사람 중심 장면은 스틱맨 이미지로 표현합니다.

자세한 내용은 [design/visual-direction.md](design/visual-direction.md)를 참고합니다.
