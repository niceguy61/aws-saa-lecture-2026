# Special Lecture - Domain 2: Resilient Architectures (Top Services)

## Why This Matters On The Exam

- 가용성/복구는 “Multi-AZ/Decouple/Retry” 같은 반복 패턴으로 출제된다.
- 헷갈리는 포인트는 “Route 53 라우팅 정책”, “ALB vs NLB”, “SQS vs SNS vs EventBridge”, “RDS Multi-AZ vs Read replica”다.

## Services In Scope (Draft Top 10~15)

- Route 53 (routing policies, health checks)
- ALB/NLB, Auto Scaling
- S3 (versioning/replication)
- RDS/Aurora Multi-AZ
- DynamoDB (HA 개념)
- SQS, SNS, EventBridge
- AWS Backup

## Confusing Similar Cases (Choose-This-Not-That)

| Scenario | Best choice | Why | Common wrong choice | Why it's wrong |
|---|---|---|---|---|
| 비동기 버퍼/내구 큐 | SQS | pull 기반, 재시도/가시성 | SNS | push/팬아웃 중심 |
| L7 라우팅 | ALB | path/host 기반 | NLB | L4 중심 |
| 가용성(동기) | RDS Multi-AZ | 자동 failover | Read replica | 주로 읽기 확장/비동기 |

## Deep Dive (Stubs)

- TODO

