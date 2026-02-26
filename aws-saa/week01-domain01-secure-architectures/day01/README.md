# Day 01 - IAM/STS foundations

## Outcomes

- IAM policy evaluation 로직(Explicit deny, 조건, 우선순위)을 설명한다.
- 사용자/그룹/역할/리소스 정책을 구분하고, 언제 무엇을 쓰는지 판단한다.
- STS AssumeRole 기반의 역할 전환(임시 자격 증명)의 목적과 보안 포인트(ExternalId 등)를 설명한다.
- 멀티계정(Organizations/SCP)에서 “권한 경계”가 어떻게 만들어지는지 개념적으로 연결한다.

## Services In Scope

- IAM (Users/Groups/Roles/Policies, permission boundaries, policy conditions)
- STS (AssumeRole, temporary credentials, session policy)
- Organizations (SCP 개념, multi-account strategy)
- IAM Identity Center(개념: federation/SSO 관점)

## Timebox (4h)

- Theory: 2h 30m
- Hands-on: 1h 30m

## Exam-Style Design Questions

- “교차 계정 액세스”가 필요할 때, 사용자 액세스 키 공유 없이 어떻게 설계할까?
- “특정 S3 prefix만 읽기” 같은 요구사항에서 identity policy vs bucket policy 중 무엇을 선택할까?
- Organizations에서 SCP를 적용했는데도 액세스가 안 풀린다. 무엇을 먼저 확인할까?
- 임시 크레덴셜을 써야 하는 이유(키 유출/수명/감사)와 설계 상의 장점은?

