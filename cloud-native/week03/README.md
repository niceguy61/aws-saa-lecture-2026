# 3주차 - Kubernetes Core

## 목표

Kubernetes를 명령어 묶음이 아니라 원하는 상태를 계속 맞추는 시스템으로 이해한다.

## 일별 계획

| 일차 | 주제 | 활동 |
|---|---|---|
| [1일차](day01/README.md) | Kubernetes 큰 그림 | 로컬 Kubernetes Cluster를 관찰하고 Node, Namespace, 기본 Object를 식별한다. |
| [2일차](day02/README.md) | Pod와 Deployment | 애플리케이션을 배포하고 scale, image update, rollback을 수행한다. |
| [3일차](day03/README.md) | 설정과 Health Check | 설정, probe, events를 확인해 실패한 rollout을 복구한다. |
| [4일차](day04/README.md) | Service와 Namespace | Cluster 내부에서 애플리케이션을 노출하고 어떤 Pod가 트래픽을 받는지 증명한다. |
| [5일차](day05/README.md) | Kubernetes 디버깅 | 고장난 Kubernetes workload를 진단하고 증상, 근거, 원인, 수정 방법을 제출한다. |

## 주차 산출물

- Kubernetes desired state 다이어그램
- Deployment 생명주기 다이어그램
- kubectl 문제 해결 가이드
- 스틱맨 이미지: replica를 유지하려는 controller
