# Day 04 - Database resilience (Resilience: Database)

![고객 사례 삽화 - Multi-AZ vs Read Replica](../../assets/scenario_image/w2d4s1.png)

## Outcomes

- RDS/Aurora에서 “가용성(Multi-AZ)”과 “읽기 확장(Read replica)”을 구분한다.
- DynamoDB의 복원력(관리형, AZ 내구) 특징을 개념으로 설명한다.
- DynamoDB PITR(시점 복구)을 켜는 이유와 “복구/복원” 흐름을 이해한다.

## Services In Scope

- RDS/Aurora (Multi-AZ vs Read replica 개념)
- DynamoDB (PITR/backup 개념)

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [RDS/Aurora: Multi-AZ vs Read Replica](01-rds-aurora-multi-az-vs-rr.md)
- [DynamoDB Resilience + PITR (실수 롤백)](02-dynamodb-resilience.md)

## Core Concepts

- DB 문제는 보통 “가용성”과 “확장”을 분리해서 묻는다
  - HA/자동 장애 조치: Multi-AZ
  - 읽기 확장: Read replica
  - “둘 다 필요”면 둘을 같이 쓴다
- 시험의 핵심은 목적 매칭
  - “failover”가 문장에 있으면 Multi-AZ
  - “read-heavy”가 문장에 있으면 Read replica

![RDS Multi-AZ vs Read Replica](../../assets/core/rds-multi-az-vs-read-replica.svg)

## Exam Traps (확장)

- “Multi-AZ = 읽기 확장” 착각
- 관계형/NoSQL 요구를 구분하지 못하고 아무 DB나 고르는 실수
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- “가용성” 요구가 있을 때 Multi-AZ가 정답인 신호는?
- “읽기 성능 확장” 요구가 있을 때 Read replica가 정답인 신호는?
- NoSQL이 필요한 요구(키-값/저지연/탄력)와 관계형이 필요한 요구(조인/트랜잭션)를 어떻게 구분할까?

## TL;DR (한 줄 정리)

- “failover/HA”면 **Multi-AZ**, “read-heavy”면 **Read replica**, “실수 롤백”이면 **DynamoDB PITR**처럼 목적을 먼저 분리한다.
