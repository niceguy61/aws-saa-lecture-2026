# Day 01 - IAM/STS foundations

## TL;DR (한 줄 결론)

- 키 공유가 보이면 대부분 오답이다: **Role + STS AssumeRole + (필요 시) boundary/SCP**로 “최소 권한 + 임시 자격 증명”을 만든다.

## Outcomes

- IAM 정책 평가(기본 Deny, Explicit Deny 우선, 경계/상한선)를 “말로” 풀어 설명한다.
- User/Group/Role, identity policy/resource policy를 구분하고, 상황별로 선택한다.
- STS AssumeRole이 왜 필요한지(임시/감사/회수)와 보안 포인트(ExternalId, session policy)를 짚는다.
- Organizations/SCP, permissions boundary가 “권한 상한선”을 만든다는 감각을 잡는다.

## Services In Scope

- IAM (Users/Groups/Roles/Policies, permission boundaries, policy conditions)
- STS (AssumeRole, temporary credentials, session policy)
- Organizations (SCP 개념, multi-account strategy)
- IAM Identity Center(개념: federation/SSO 관점)

## Timebox (4h)

- Theory: 2h 30m
- Hands-on: 1h 30m

## Flow (읽는 순서)

- 왜 IAM/STS가 시험에서 “정답을 가르는 단서”가 자주 되는지 → 정책 평가 규칙 3개 → AssumeRole 패턴 → 상한선(SCP/boundary) → 실습으로 손에 붙이기

## Exam-Style Design Questions

- “교차 계정 액세스”가 필요할 때, 사용자 액세스 키 공유 없이 어떻게 설계할까?
- “특정 S3 prefix만 읽기” 같은 요구사항에서 identity policy vs bucket policy 중 무엇을 선택할까?
- Organizations에서 SCP를 적용했는데도 액세스가 안 풀린다. 무엇을 먼저 확인할까?
- 임시 크레덴셜을 써야 하는 이유(키 유출/수명/감사)와 설계 상의 장점은?
