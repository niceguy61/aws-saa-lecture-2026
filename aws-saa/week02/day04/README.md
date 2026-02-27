# Day 04 - Database resilience (RDS/Aurora/DynamoDB)

## Outcomes

- RDS/Aurora에서 “가용성(Multi-AZ)”과 “읽기 확장(Read replica)”을 구분한다.
- DynamoDB의 복원력(관리형, AZ 내구) 특징을 개념으로 설명한다.
- DynamoDB PITR(시점 복구)을 켜는 이유와 “복구/복원” 흐름을 이해한다.

## Services In Scope

- RDS/Aurora (Multi-AZ vs Read replica 개념)
- DynamoDB (PITR/backup 개념)

## Timebox (4h)

- Theory + mini-action: 4h

## Exam-Style Design Questions

- “가용성” 요구가 있을 때 Multi-AZ가 정답인 신호는?
- “읽기 성능 확장” 요구가 있을 때 Read replica가 정답인 신호는?
- NoSQL이 필요한 요구(키-값/저지연/탄력)와 관계형이 필요한 요구(조인/트랜잭션)를 어떻게 구분할까?
