# Week 3 - Domain 3: Design High-Performing Architectures (24%)

## Goals

- 성능 병목(컴퓨트/스토리지/네트워크/DB/캐시)을 진단하고, 서비스 선택과 튜닝의 근거를 설명한다.

## Service Inventory (Domain 3)

- Compute: EC2 instance families, Auto Scaling, placement concepts
- Edge: CloudFront, Global Accelerator (개념)
- Storage: EBS (gp3/io1/io2), EFS performance modes
- Databases: Aurora performance patterns, DynamoDB (partitioning, indexes), DAX
- Cache: ElastiCache (Redis/Memcached)
- Serverless: Lambda, API Gateway (성능/쿼터)
- Containers (SAA 범위): ECS/EKS 개념 비교

## Top Focus Services (10-15)

- EC2 instance selection + Auto Scaling
- CloudFront caching
- Aurora vs RDS performance tradeoffs
- DynamoDB partition design + indexes
- ElastiCache
- Lambda concurrency/limits

## Day Plan (5 days)

- Day 01: Perf thinking + EC2 sizing patterns
- Day 02: CloudFront/GA + network performance basics
- Day 03: Storage performance (EBS/EFS) patterns
- Day 04: DB performance (Aurora/DynamoDB) + caching
- Day 05: Special Lecture + Week Summary (Top 서비스 비교/함정/대안 + 통합 미니 랩 + 케이스 퀴즈)

## Special Lecture Pack (Top Services Deep Dive)

- `aws-saa/special-lectures/domain03-high-performing-top-services.md`
