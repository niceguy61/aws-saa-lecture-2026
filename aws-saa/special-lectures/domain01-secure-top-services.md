# Special Lecture - Domain 1: Secure Architectures (Top Services)

## Why This Matters On The Exam

- “키 공유/퍼블릭 오픈” 같은 안티패턴을 배제하고, 역할/정책/암호화/감사/네트워크 경계를 조합해 가장 안전한 선택지를 고르는 문제가 반복된다.
- 헷갈리는 포인트는 “정책 종류(Identity vs Resource)”, “상한선(SCP/Boundary)”, “암호화 제어(KMS key policy/Grants)”에서 자주 나온다.

## Services In Scope (Draft Top 10~15)

- IAM, STS
- Organizations (SCP), Control Tower(개념)
- KMS
- Secrets Manager, SSM Parameter Store
- CloudTrail, Config
- GuardDuty, Security Hub, Inspector
- VPC Endpoints/PrivateLink
- S3 security (bucket policy, encryption, block public access)
- WAF, Shield
- ACM

## Core Patterns (Exam-Heavy)

- Pattern: “Cross-account access without key sharing”
  - Role + trust policy + STS AssumeRole
  - (3rd party) ExternalId 조건
- Pattern: “Private access to AWS services”
  - VPC Endpoint + policy, S3 bucket policy 조건(필요 시)
- Pattern: “Encryption with centralized control”
  - KMS CMK + key policy, envelope encryption, rotation

## Confusing Similar Cases (Choose-This-Not-That)

| Scenario | Best choice | Why | Common wrong choice | Why it's wrong |
|---|---|---|---|---|
| 교차 계정 운영 | AssumeRole | 키 공유 제거 + 임시 세션 | 액세스 키 공유 | 유출/회수/감사 측면 취약 |
| 멀티계정 정책 강제 | SCP | 계정/OU 상한선 | IAM allow만 추가 | SCP에서 막히면 무효 |
| 시크릿 관리 | Secrets Manager | rotation/보안 기능 | Parameter Store(일반) | rotation/관리 기능 부족 |
| 감사 vs 구성 추적 | CloudTrail + Config | API 로그 vs 리소스 변경 | CloudTrail만 | 구성 변화/준수 평가가 약함 |

## Deep Dive (Stubs)

### IAM/STS

- TODO: policy evaluation, session policy, permission boundaries

### KMS

- TODO: key policy vs IAM policy, grants, encryption context

### S3 Security

- TODO: block public access, bucket policy conditions, OAC/OAI

## Best Practices (Actionable)

- TODO: “최소 권한”은 정책 조건/태그(ABAC)로 유지보수성을 확보
- TODO: 루트 사용자 보호(MFA) + break-glass 최소화

## Alternatives (Tradeoffs)

- TODO: Secrets Manager vs Parameter Store vs KMS direct encryption

## Drill (Mini Mock)

### Q1

**Scenario:** 외부 파트너가 고객 계정의 역할을 AssumeRole 해야 한다. 고객은 confused deputy 위험을 줄이고 싶다. 어떤 설계가 가장 적절한가?

A. 액세스 키를 전달하고 주기적으로 교체한다  
B. AssumeRole trust policy에 ExternalId 조건을 추가한다  
C. S3 버킷을 퍼블릭으로 열어 데이터만 공유한다  
D. 루트 사용자로 접근하도록 허용한다  

**Answer:** B  
**Explanation:** ExternalId 조건은 제3자 AssumeRole 시 confused deputy 완화에 사용된다.  
**Tags:** `domain:1` `services:STS,IAM`

## References

- Internal references:
  - [References index](../references/README.md)
  - [Exam guide (SAA-C03)](../references/exam-guide.md)
  - [Glossary](../references/glossary.md)
  - [AWS services list](../references/aws-services.md)
  - [Exam keypoints](../exam-keypoints.md)
  - [Exam trap bank](../exam-trap-bank.md)

- Official AWS documentation:
  - [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
  - [STS API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
  - [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
  - [Search: Service Control Policies (SCP)](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Service%20Control%20Policies%20SCP%20AWS%20Organizations)
  - [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
  - [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
  - [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
  - [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
  - [Search: VPC endpoints](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=VPC%20endpoints)
  - [AWS PrivateLink User Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
  - [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
  - [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
