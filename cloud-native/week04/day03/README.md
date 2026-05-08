# 4주차 3일차 - Storage와 State

## 목표

상태를 가진 애플리케이션이 운영 규칙을 어떻게 바꾸는지 이해한다.

## 오늘 배울 내용

- Volume, PersistentVolume, PersistentVolumeClaim, StatefulSet 개념
- Stateless와 stateful workload의 차이
- Backup과 restore가 필요한 이유
- State를 가볍게 다룰 때 생기는 문제

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | 트래픽과 애플리케이션 정체성 복습 |
| 10:00-10:50 | 2교시 | Stateless와 Stateful workload |
| 11:00-11:50 | 3교시 | Kubernetes Storage 용어 |
| 12:00-12:50 | 4교시 | 강사 데모: 상태와 데이터 손실 위험 |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | Volume 생명주기 가이드 |
| 15:00-15:50 | 6교시 | 미션: 안전한 State 처리 방식 고르기 |
| 16:00-16:50 | 7교시 | Backup과 restore 토론 |
| 17:00-17:50 | 8교시 | 정리와 Scheduling 예고 |

## 랩/미션/데모

상태를 잘못 다루면 데이터가 사라지거나 숨는 모습을 보고 더 안전한 패턴을 선택한다.

## 보충/심화 자료

- Stateless vs Stateful 비교표
- Storage 용어 지도
- 심화: StatefulSet identity
