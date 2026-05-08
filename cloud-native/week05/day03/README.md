# 5주차 3일차 - AWS 네트워킹과 외부 노출

## 목표

Kubernetes exposure 개념을 AWS 네트워킹과 public access 결정으로 연결한다.

## 오늘 배울 내용

- VPC, Subnet, Security Group, Load Balancer, Route 53, ACM
- Public 노출과 private 보호의 차이
- Security Group 규칙이 중요한 이유
- HTTP 트래픽이 Cloud 애플리케이션에 도달하는 방식

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | AWS compute 선택 복습 |
| 10:00-10:50 | 2교시 | VPC와 Subnet 개념 모델 |
| 11:00-11:50 | 3교시 | Security Group과 Load Balancer |
| 12:00-12:50 | 4교시 | Route 53과 ACM 개념 walkthrough |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | 미션: 외부 노출 경로 선택 |
| 15:00-15:50 | 6교시 | 미션: 보안 경계 설명 |
| 16:00-16:50 | 7교시 | 팀별 debrief |
| 17:00-17:50 | 8교시 | 정리와 managed service 예고 |

## 랩/미션/데모

간단한 애플리케이션의 안전한 외부 노출 경로를 선택하고 private로 남겨야 할 영역을 설명한다.

## 보충/심화 자료

- AWS 트래픽 경로 다이어그램
- Security Group 워크시트
- 심화: Public/Private Subnet 패턴
