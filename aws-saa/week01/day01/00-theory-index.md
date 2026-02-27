# Day 01 - Theory Index (접근 제어: IAM/STS/Organizations)

> 이 문서는 Day 이론 “인덱스”다. 서비스별 theory는 Day 폴더 바로 아래 `01-*.md`에서 각각 읽는다.

## 소개 (이게 뭔가요?)

- IAM은 “누가 무엇을 할 수 있는지”를 정책으로 정의하는 접근 제어 계층이다.
- STS는 역할(Role)을 Assume 해서 “임시 자격 증명”으로 접근하게 만들어 키 공유를 없앤다.

## 고객 사례 (스토리)

보안팀에서 연락이 왔다. “관리 콘솔에 권한 기능 꼭 넣어주세요. 팀마다 다르고, 프로젝트별로도 달라요.” 처음엔 애플리케이션 DB에 role 테이블을 만들고, 화면마다 if 문으로 막으면 될 것 같았다. 그런데 AWS 리소스(예: S3, EC2) 권한까지 들어오자 얘기가 달라졌다. 사용자 1명, 기능 1개마다 예외가 생기고, 담당자는 나 혼자다.

권한이 조금만 꼬이면 화면은 멀쩡한데 API가 `AccessDenied`로 떨어진다. “왜 안 돼요?” 질문이 쌓일수록, 내가 만든 권한 로직은 점점 더 복잡해진다.

게다가 본사-지사, 자회사까지 계정이 늘어난다. “본사 보안팀이 만든 권한 템플릿을 지사 계정에도 똑같이 적용하고, 필요하면 딱 한 기능만 추가/회수”해야 한다. 여기서 IAM의 managed policy를 ‘권한 템플릿’처럼 쓰고, Role을 ‘직무 카드’처럼 빌려 쓰는 구조로 바꾸면 일이 단순해진다. Organizations의 OU/SCP로 “절대 하면 안 되는 것”을 상한선으로 걸어두고, 사용자는 Identity Center로 로그인(SSO)만 한다. 실제 작업은 STS AssumeRole로 받은 임시 자격 증명으로 처리한다. 은행 OTP처럼 시간 지나면 만료되니, 영구 키를 들고 다닐 이유가 없다.

이 요구사항이라면, “사용자 계정 만들기”보다 먼저 어떤 Role/정책/경계를 설계해볼까요?

## Impact 범위 (어디에 영향을 주나?)

- Security: 최소 권한/키 공유 금지/감사(CloudTrail)까지 설계에 직결
- Operations: AccessDenied 트러블슈팅(정책 평가/경계/리소스 정책)을 좌우
- Reliability/Cost/Performance: 직접 기능은 아니지만, “권한/설정 실수”가 장애/비용 폭탄으로 이어질 수 있음

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-1-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-1.1%20Security%20access%20design-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: IAM](https://img.shields.io/badge/Service-IAM-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: STS](https://img.shields.io/badge/Service-STS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Organizations](https://img.shields.io/badge/Service-Organizations-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 1: Design Secure Architectures
- Task focus: 1.1 AWS 리소스에 대한 보안 액세스 설계 (IAM, STS, 교차 계정, SCP, 리소스 정책)

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- 시험 문제는 자주 이렇게 출제된다: “Allow를 줬는데 왜 안 돼요?” → 정답은 대개 **Explicit Deny / SCP / permissions boundary / resource policy / trust policy** 쪽에 있다.
- 실무에서도 키 공유는 사고로 이어진다. 그래서 “Role + STS 임시 자격 증명”이 기본 패턴이다.

## Core Concepts

IAM을 외우는 가장 쉬운 방식은 “용어”가 아니라 “질문”으로 잡는 것이다.

- 인증(Authentication): “누구인가?” (예: Identity Center로 SSO)
- 인가(Authorization): “무엇을 할 수 있나?” (예: IAM 정책 평가)

정책은 크게 4종류가 핵심이다(시험 빈출).

- Identity-based policy: 사용자/그룹/역할에 부착
- Resource-based policy: 리소스에 부착 (예: S3 bucket policy, KMS key policy)
- Permissions boundary: **identity의 최대 권한 상한선**(부여가 아니라 제한)
- SCP(Organizations): **계정/OU의 최대 권한 상한선**(부여가 아니라 제한)

![IAM policy evaluation (order and boundaries)](../../assets/core/iam-evaluation.svg)

## Decision Rules (정답을 가르는 규칙 3개)

1. 기본은 Deny다. → **Allow가 없으면 무조건 Deny**
2. Explicit Deny는 항상 이긴다. → Allow가 10개 있어도 Deny 하나면 끝
3. 상한선은 뚫을 수 없다. → **SCP/boundary에 막히면 IAM Allow로는 풀 수 없다**

## Service Theories (서비스별로 읽기)

- [IAM (정책 평가 + 최소 권한)](01-iam.md)
- [STS (AssumeRole: 임시 자격 증명)](02-sts.md)
- [Organizations + OU/SCP (멀티계정 거버넌스)](03-organizations-scp.md)
- [IAM Identity Center (SSO: 사용자 입구 표준화)](04-identity-center.md)

> Deep Dive는 서비스별 챕터로 분리했다. 먼저 규칙(Decision Rules)을 읽고, 필요한 챕터를 골라 깊게 들어가면 흐름이 끊기지 않는다.

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

## Exam Traps

- SCP를 적용했는데 “정책을 붙였는데도” 안 된다: SCP는 상한선, IAM Allow가 별도로 필요
- S3 접근을 막고 싶은데 security group으로 해결하려 함: S3는 SG 대상이 아님(대신 bucket policy/VPC endpoint policy)
- Cross-account에서 “액세스 키 공유”가 정답처럼 보이면 의심: 대부분 AssumeRole + trust policy
- Role trust policy와 permission policy를 혼동: trust는 “누가 Assume”, permission은 “Assume 후 무엇을”

## Taste Test (1~2분)

아래 문장 2개를 “정답/오답”으로만 판정해보자(이유는 한 줄로).

1) “SCP에서 Allow 했으니 이제 접근 가능하다.”  
2) “교차 계정 운영은 access key 공유가 가장 단순하다.”

## TL;DR (한 줄 정리)

- IAM은 “Allow 목록”이 아니라 **정책 평가 규칙 + 상한선(SCP/boundary) + 리소스 정책**의 조합이다. 그래서 AccessDenied는 대부분 “Allow를 더 붙이면 된다”가 아니다.
