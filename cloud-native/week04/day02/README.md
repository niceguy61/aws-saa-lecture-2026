# 4주차 2일차 - Ingress와 HTTP Routing

## 목표

HTTP 트래픽이 Cluster 밖에서 들어와 Service에 도달하는 방식을 이해한다.

## 오늘 배울 내용

- Ingress, Ingress Controller, Host routing, Path routing
- Service와 Ingress의 차이
- TLS 개념의 초급 이해
- Routing 실수가 사용자에게 어떻게 보이는지

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | 내부 트래픽 경로 복습 |
| 10:00-10:50 | 2교시 | Ingress 개념 모델 |
| 11:00-11:50 | 3교시 | Host와 Path routing |
| 12:00-12:50 | 4교시 | 강사 데모: Service로 트래픽 라우팅 |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | 실습: 기본 Ingress 구성 |
| 15:00-15:50 | 6교시 | 실습: Route 확인과 수정 |
| 16:00-16:50 | 7교시 | 진단: host, path, service 실수 |
| 17:00-17:50 | 8교시 | 정리와 Storage 예고 |

## 랩/미션/데모

HTTP 트래픽을 Service로 라우팅하고 브라우저에서 Pod까지의 경로를 설명한다.

## 보충/심화 자료

- Service vs Ingress 비교표
- HTTP routing 워크시트
- 심화: Ingress Controller 내부 동작
