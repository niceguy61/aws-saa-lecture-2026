# Week 1 - Domain 1: Design Secure Architectures (30%)

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-1-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Service: IAM](https://img.shields.io/badge/Service-IAM-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: STS](https://img.shields.io/badge/Service-STS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: KMS](https://img.shields.io/badge/Service-KMS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: CloudTrail](https://img.shields.io/badge/Service-CloudTrail-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Organizations](https://img.shields.io/badge/Service-Organizations-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: VPC%20Endpoints](https://img.shields.io/badge/Service-VPC%20Endpoints-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

> 주차 뱃지는 “하이라이트(최대 6개)”만 보여준다. Day별 서비스 범위는 각 Day 문서 상단 `Exam Guide (Badges)`를 기준으로 본다.

## Goals

- IAM 중심으로 “권한 경계”를 설계하고, 암호화/감사/네트워크 경계를 함께 묶어 보안 아키텍처를 설명한다.

## Service Inventory (Domain 1)

- Identity & access: IAM, STS, IAM Identity Center
- Org governance: Organizations, Control Tower
- Data protection: KMS, Secrets Manager, SSM Parameter Store, ACM
- Detection & audit: CloudTrail, Config, GuardDuty, Security Hub, Inspector
- Network security: Security Group, NACL, VPC Endpoints, PrivateLink
- Edge/app protection: WAF, Shield
- Storage security: S3 encryption/policies/block public access, CloudFront OAC/OAI

## Top Focus Services (10-15)

- IAM (policies, roles, permission boundaries)
- STS (AssumeRole, session policy)
- KMS (key policies, grants)
- Secrets Manager vs Parameter Store
- CloudTrail vs Config (무엇을 기록하는가)
- Organizations (SCP) / Control Tower (개념 수준)
- Security Groups / NACLs
- VPC Endpoints / PrivateLink
- S3 security (bucket policy, encryption, block public access)
- WAF (L7) / Shield (DDoS)
- GuardDuty / Security Hub (탐지/집계)
- ACM (TLS 인증서)

## Special Lecture Pack (Top Services Deep Dive)

- `aws-saa/special-lectures/domain01-secure-top-services.md`

## Day Plan (5 days)

- [Day 01](day01/README.md): IAM/STS, least privilege, policy evaluation
- [Day 02](day02/README.md): KMS + Secrets (암호화, 키 정책, 시크릿 패턴)
- [Day 03](day03/README.md): CloudTrail/Config + detection services (감사/탐지)
- [Day 04](day04/README.md): VPC security (SG/NACL) + Private connectivity (Endpoints/PrivateLink)
- [Day 05](day05/README.md): Special Lecture + Week Summary (Top 서비스 비교/함정/대안 + 케이스 퀴즈)
