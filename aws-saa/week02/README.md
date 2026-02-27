# Week 2 - Domain 2: Design Resilient Architectures (26%)

## Goals

- 장애를 “전제로” 가용성/복구 전략을 설계하고, 단일 장애 지점을 제거하는 패턴을 설명한다.

## Service Inventory (Domain 2)

- DNS/traffic: Route 53, health checks, routing policies
- Load balancing & scaling: ALB/NLB, Auto Scaling
- Storage resilience: S3 versioning/replication, EBS snapshots, EFS
- Databases: RDS/Aurora Multi-AZ, DynamoDB
- Messaging: SQS, SNS, EventBridge
- Backup/DR: AWS Backup, pilot light / warm standby / multi-site

## Top Focus Services (10-15)

- Route 53 routing policies (failover/latency/weighted)
- ALB/NLB + Auto Scaling
- Multi-AZ patterns (EC2, RDS/Aurora)
- S3 versioning + replication
- DynamoDB HA concepts (multi-AZ by design, global tables 개념)
- SQS (decoupling), SNS fan-out
- AWS Backup

## Day Plan (5 days)

- Day 01: Resilience fundamentals + Route 53 routing
- Day 02: ALB/NLB + Auto Scaling + health checks
- Day 03: Storage resilience (S3/EBS/EFS) + backup
- Day 04: Database resilience (RDS/Aurora/DynamoDB)
- Day 05: Special Lecture + Week Summary (Top 서비스 비교/함정/대안 + 통합 미니 랩 + 케이스 퀴즈)

## Special Lecture Pack (Top Services Deep Dive)

- `aws-saa/special-lectures/domain02-resilient-top-services.md`
