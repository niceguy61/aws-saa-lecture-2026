# 3주차 3일차 - 설정과 Health Check

## 목표

Kubernetes에서 Image와 실행 설정, 상태 확인을 분리해서 다루는 방법을 이해한다.

## 오늘 배울 내용

- ConfigMap과 Secret의 초급 개념
- Liveness와 readiness probe
- Resource requests와 limits의 의미
- YAML이 맞아 보여도 rollout이 실패할 수 있는 이유

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | Deployment 생명주기 복습 |
| 10:00-10:50 | 2교시 | ConfigMap과 Secret 개념 |
| 11:00-11:50 | 3교시 | Health check와 resource 기초 |
| 12:00-12:50 | 4교시 | 강사 데모: 실패한 rollout과 정상 rollout |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | 미션 준비: 고장난 rollout |
| 15:00-15:50 | 6교시 | 미션: 설정 또는 probe 문제 복구 |
| 16:00-16:50 | 7교시 | events, describe, logs로 근거 찾기 |
| 17:00-17:50 | 8교시 | 정리와 Service 예고 |

## 랩/미션/데모

설정, probe, events를 확인해 실패한 rollout을 복구한다.

## 보충/심화 자료

- 설정과 Health 체크리스트
- Probe 예시
- 심화: Resource와 Scheduling
