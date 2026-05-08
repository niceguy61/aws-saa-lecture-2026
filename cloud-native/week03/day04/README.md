# 3주차 4일차 - Service와 Namespace

## 목표

변하는 Pod 뒤에 안정적인 접근 지점을 제공하는 Service와 기본 Namespace 구성을 이해한다.

## 오늘 배울 내용

- Service, Selector, Endpoint, ClusterIP
- Pod IP가 안정적인 주소가 아닌 이유
- Namespace를 초급 조직 경계로 쓰는 방법
- Label이 트래픽 라우팅에 미치는 영향

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | 건강한 workload 복습 |
| 10:00-10:50 | 2교시 | Service 개념 모델 |
| 11:00-11:50 | 3교시 | Selector와 Endpoint 관계 |
| 12:00-12:50 | 4교시 | 강사 데모: Cluster 내부 노출 |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | 실습: Service 생성과 확인 |
| 15:00-15:50 | 6교시 | 실습: Namespace와 Service 접근 |
| 16:00-16:50 | 7교시 | 진단: selector mismatch |
| 17:00-17:50 | 8교시 | 정리와 Debugging day 예고 |

## 랩/미션/데모

Cluster 내부에서 애플리케이션을 노출하고 어떤 Pod가 트래픽을 받는지 증명한다.

## 보충/심화 자료

- Service와 Endpoint 다이어그램
- Namespace 워크시트
- 심화: kube-proxy 개요
