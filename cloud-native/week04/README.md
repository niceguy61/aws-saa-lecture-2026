# 4주차 - Kubernetes 네트워킹과 운영

## 목표

Kubernetes 안에서 트래픽이 이동하는 방식과 운영 중 나타나는 증상을 연결해서 이해한다.

## 일별 계획

| 일차 | 주제 | 활동 |
|---|---|---|
| [1일차](day01/README.md) | Kubernetes 네트워킹 모델 | 한 Pod에서 Service까지 요청이 이동하는 경로를 추적하고 어디서 깨질 수 있는지 표시한다. |
| [2일차](day02/README.md) | Ingress와 HTTP Routing | HTTP 트래픽을 Service로 라우팅하고 브라우저에서 Pod까지의 경로를 설명한다. |
| [3일차](day03/README.md) | Storage와 State | 상태를 잘못 다루면 데이터가 사라지거나 숨는 모습을 보고 더 안전한 패턴을 선택한다. |
| [4일차](day04/README.md) | Scheduling과 Scaling | 작은 workload로 scheduling과 scaling 동작을 관찰한다. |
| [5일차](day05/README.md) | 운영 리뷰 | 증상, 영향, 원인, 수정, 예방, cleanup을 포함한 미니 incident review를 진행한다. |

## 주차 산출물

- Pod-Service-Ingress 트래픽 다이어그램
- DNS와 Service 문제 해결 흐름도
- 운영 체크리스트
- 스틱맨 이미지: Pod 사이에서 길을 잃은 요청
