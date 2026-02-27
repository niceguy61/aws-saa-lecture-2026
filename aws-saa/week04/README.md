# Week 4 - Domain 4: Design Cost-Optimized Architectures (20%)

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-4-0ea5e9?style=flat&logo=amazonaws&logoColor=white)
![Service: Budgets](https://img.shields.io/badge/Service-Budgets-8b5cf6?style=flat&logo=amazonaws&logoColor=white)
![Service: Cost%20Explorer](https://img.shields.io/badge/Service-Cost%20Explorer-8b5cf6?style=flat&logo=amazonaws&logoColor=white)
![Service: Savings%20Plans](https://img.shields.io/badge/Service-Savings%20Plans-8b5cf6?style=flat&logo=amazonaws&logoColor=white)
![Service: S3](https://img.shields.io/badge/Service-S3-8b5cf6?style=flat&logo=amazonaws&logoColor=white)
![Service: NAT%20Gateway](https://img.shields.io/badge/Service-NAT%20Gateway-8b5cf6?style=flat&logo=amazonaws&logoColor=white)
![Service: VPC%20Endpoints](https://img.shields.io/badge/Service-VPC%20Endpoints-8b5cf6?style=flat&logo=amazonaws&logoColor=white)

## Goals

- 비용 최적화를 “지출 줄이기”가 아니라 “요구사항 대비 합리적 설계”로 설명하고, 비용 드라이버를 식별한다.

## Service Inventory (Domain 4)

- Cost management: Budgets, Cost Explorer, CUR (개념)
- Compute pricing: On-Demand, Savings Plans, Reserved Instances, Spot
- Storage classes: S3 classes + lifecycle + Intelligent-Tiering
- Data transfer: egress, NAT 비용, VPC endpoints tradeoff
- Right sizing: instance selection, Auto Scaling, gp3 전환 등
- DB cost: Aurora/RDS options, DynamoDB capacity modes

## Top Focus Services (10-15)

- EC2 pricing options (SP/RI/Spot)
- S3 storage classes + lifecycle
- Cost Explorer/Budgets
- NAT Gateway cost vs VPC endpoints
- DynamoDB on-demand vs provisioned
- Aurora/RDS right-sizing options

## Day Plan (5 days)

- Day 01: Cost drivers + tagging + Budgets/Cost Explorer
- Day 02: EC2 pricing models + right sizing/ASG
- Day 03: S3 storage classes + lifecycle patterns
- Day 04: Data transfer + NAT vs endpoints + CloudFront caching
- Day 05: Special Lecture + Week Summary (Top 서비스 비교/함정/대안 + 통합 미니 랩 + 케이스 퀴즈)

## Special Lecture Pack (Top Services Deep Dive)

- `aws-saa/special-lectures/domain04-cost-optimized-top-services.md`
