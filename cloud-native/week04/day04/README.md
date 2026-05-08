# 4주차 4일차 - Scheduling과 Scaling

## 목표

Kubernetes가 workload를 어디에 배치하는지, resource 설정이 왜 신뢰성에 영향을 주는지 이해한다.

## 오늘 배울 내용

- Requests, limits, node capacity, scheduling
- 수평 확장 개념
- Node pressure 증상
- Resource 설정이 기술이자 운영 판단인 이유

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | State와 신뢰성 복습 |
| 10:00-10:50 | 2교시 | Scheduling 개념 모델 |
| 11:00-11:50 | 3교시 | Requests, limits, node capacity |
| 12:00-12:50 | 4교시 | 강사 데모: scheduling과 resource 증상 |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | 실습: resource 동작 관찰 |
| 15:00-15:50 | 6교시 | 실습: scale과 workload 확인 |
| 16:00-16:50 | 7교시 | 진단: Pending 또는 throttling 증상 |
| 17:00-17:50 | 8교시 | 정리와 운영 리뷰 예고 |

## 랩/미션/데모

작은 workload로 scheduling과 scaling 동작을 관찰한다.

## 보충/심화 자료

- Requests와 limits 워크시트
- Scaling 결정표
- 심화: HPA metrics 흐름
