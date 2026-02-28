# Day 01 - IAM/STS foundations (접근 제어: IAM/STS/Organizations)

![고객 사례 삽화 - IAM 권한 템플릿](../../assets/scenario_image/w1d1s1.png)

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

- Theory + mini-action: 4h

## Flow (읽는 순서)

- 왜 IAM/STS가 시험에서 “정답을 가르는 단서”가 자주 되는지 → 정책 평가 규칙 3개 → AssumeRole 패턴 → 상한선(SCP/boundary) → 예시로 손에 붙이기

## Reading (서비스별 theory)

- [IAM (정책 평가 + 최소 권한)](01-iam.md)
- [STS (AssumeRole: 임시 자격 증명)](02-sts.md)
- [Organizations + OU/SCP (멀티계정 거버넌스)](03-organizations-scp.md)
- [IAM Identity Center (SSO: 사용자 입구 표준화)](04-identity-center.md)

> 먼저 규칙(Decision Rules)을 읽고, 필요한 챕터를 골라 깊게 들어가면 흐름이 덜 끊긴다.

## Decision Rules (정답을 가르는 규칙 3개)

1. 기본은 Deny다. → **Allow가 없으면 무조건 Deny**
2. Explicit Deny는 항상 이긴다. → Allow가 10개 있어도 Deny 하나면 끝
3. 상한선은 뚫을 수 없다. → **SCP/boundary에 막히면 IAM Allow로는 풀 수 없다**

![IAM policy evaluation (order and boundaries)](../../assets/core/iam-evaluation.svg)

## Smell Test (헷갈리는 지점 / 레드 플래그)

- “키를 공유하자”가 보이면 거의 틀렸다 → 보통 **AssumeRole**이 정답 방향
- “SCP로 Allow했으니 됐다” → SCP는 부여가 아니라 **상한선**이다
- “trust policy에 S3 권한을 넣자” → trust는 “누가 Assume”, permission은 “Assume 후 무엇을”
- “S3를 SG로 막자” → S3는 SG 대상이 아니다(정책/엔드포인트 관점)

## Quick Comparison Table

| Topic | Option 1 | Option 2 | Notes |
|---|---|---|---|
| 권한 부여 단위 | IAM Role | IAM User | 운영/워크로드는 Role 우선, 장기 키 최소화 |
| 정책 부착 위치 | Identity policy | Resource policy | 교차계정/리소스 단위 공유는 resource policy가 유리 |
| 권한 상한선 | SCP | Permission boundary | SCP는 계정/OU 단위, boundary는 identity 단위 |
| 임시 권한 | STS AssumeRole | 액세스 키 공유 | 시험 정답은 거의 STS 쪽 |

## Exam Traps (확장)

- SCP를 적용했는데 “정책을 붙였는데도” 안 된다: SCP는 상한선, IAM Allow가 별도로 필요
- S3 접근을 막고 싶은데 security group으로 해결하려 함: S3는 SG 대상이 아님(대신 bucket policy/VPC endpoint policy)
- Cross-account에서 “액세스 키 공유”가 정답처럼 보이면 의심: 대부분 AssumeRole + trust policy
- Role trust policy와 permission policy를 혼동: trust는 “누가 Assume”, permission은 “Assume 후 무엇을”
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam Trap Drill (O/X, 1~2분)

아래 문장 2개를 “정답/오답”으로만 판정해보자(이유는 한 줄로).

1) “SCP에서 Allow 했으니 이제 접근 가능하다.”  
2) “교차 계정 운영은 access key 공유가 가장 단순하다.”

## Exam-Style Design Questions

- “교차 계정 액세스”가 필요할 때, 사용자 액세스 키 공유 없이 어떻게 설계할까?
- “특정 S3 prefix만 읽기” 같은 요구사항에서 identity policy vs bucket policy 중 무엇을 선택할까?
- Organizations에서 SCP를 적용했는데도 액세스가 안 풀린다. 무엇을 먼저 확인할까?
- 임시 크레덴셜을 써야 하는 이유(키 유출/수명/감사)와 설계 상의 장점은?

## TL;DR (한 줄 정리)

- 키 공유가 보이면 대부분 오답이다: **Role + STS AssumeRole + (필요 시) boundary/SCP**로 “최소 권한 + 임시 자격 증명”을 만든다.
