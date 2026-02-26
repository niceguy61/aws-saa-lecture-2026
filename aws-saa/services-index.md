# Services Index (Draft)

도메인별 서비스 목록은 “주차 README”가 1차 기준이며, 여기서는 중복을 허용하고 빠르게 검색할 수 있도록만 정리한다.

## Domain 1: Secure Architectures

- IAM, STS, IAM Identity Center
- Organizations, Control Tower
- KMS, Secrets Manager, SSM Parameter Store
- CloudTrail, Config
- GuardDuty, Security Hub, Inspector
- WAF, Shield, ACM
- VPC Security (SG/NACL), VPC Endpoints/PrivateLink
- S3 Security (Bucket policy, encryption, OAC/OAI)

## Domain 2: Resilient Architectures

- Route 53, ELB (ALB/NLB)
- Auto Scaling, EC2
- S3 (versioning/replication), EBS snapshots, EFS
- RDS/Aurora Multi-AZ, DynamoDB
- SQS, SNS, EventBridge
- AWS Backup, DR strategies

## Domain 3: High-Performing Architectures

- EC2 instance selection, EBS/EFS performance
- CloudFront, Global Accelerator
- DynamoDB/DAX, Aurora performance patterns
- ElastiCache
- Lambda, API Gateway
- ECS/EKS basics (SAA 범위 중심)

## Domain 4: Cost-Optimized Architectures

- Pricing models (On-Demand/RIs/Savings Plans/Spot)
- S3 storage classes + lifecycle + Intelligent-Tiering
- Right sizing + Auto Scaling
- Data transfer, NAT vs VPC Endpoints
- Budgets/Cost Explorer/CUR

