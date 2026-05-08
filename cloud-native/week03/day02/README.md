# 3주차 2일차 - Pod와 Deployment

## 목표

Pod에서 Deployment와 rollout으로 이어지는 기본 workload 흐름을 익힌다.

## 오늘 배울 내용

- Pod, ReplicaSet, Deployment, Container의 관계
- Rollout과 rollback 개념
- Label이 Object를 연결하는 방식
- Kubernetes가 실패한 인스턴스를 대체하는 방식

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | Desired state 복습 |
| 10:00-10:50 | 2교시 | Pod 개념 모델 |
| 11:00-11:50 | 3교시 | Deployment와 ReplicaSet |
| 12:00-12:50 | 4교시 | 강사 데모: 배포, 확장, 업데이트 |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | 실습: 애플리케이션 배포 |
| 15:00-15:50 | 6교시 | 실습: 업데이트와 롤백 |
| 16:00-16:50 | 7교시 | 진단: 이미지 또는 label 실수 |
| 17:00-17:50 | 8교시 | 정리와 설정 예고 |

## 랩/미션/데모

애플리케이션을 배포하고 scale, image update, rollback을 수행한다.

## 보충/심화 자료

- Deployment 생명주기 다이어그램
- Label과 Selector 노트
- 심화: ReplicaSet 소유 관계
