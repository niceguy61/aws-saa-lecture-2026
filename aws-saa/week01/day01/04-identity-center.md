# IAM Identity Center (SSO: 사용자 입구 표준화)

## 소개 (이게 뭔가요?)

- IAM Identity Center는 “사내 사용자/그룹을 AWS 계정에 SSO로 연결”하는 출입구다.
- 시험에서는 “IAM User를 잔뜩 만들지 말고, 중앙 SSO로 통제”하라는 신호로 자주 등장한다.

## 고객 사례 (스토리, 600~1000자)

회사가 성장하면서 AWS 계정이 몇 개로 늘었다. 팀원 입사/퇴사가 잦아지자, 계정마다 IAM User를 만드는 방식은 금방 한계가 왔다. 한 사람이 퇴사하면 “모든 계정에서 사용자 삭제했는지”를 확인해야 하고, 누락이 생기면 그대로 권한이 남는다. 게다가 파트타임/외주 인력이 들어오면 “기간 제한”도 필요하다. 보안팀은 말한다. “사내 계정(예: AD/Okta)로 로그인하고, 권한은 중앙에서 할당/회수해야 해요. 계정이 늘어나도 같은 방식이어야 하고요.”

이때 Identity Center를 쓰면 ‘사용자 관리’를 AWS 계정마다 반복하지 않아도 된다. 사용자는 SSO로 한 번 로그인하고, 어떤 계정에 어떤 역할로 들어갈지(권한 세트/권한 템플릿)만 중앙에서 관리한다. 계정이 1개든 20개든 “입구”가 하나로 통일되니 운영이 단순해지고, 퇴사/권한 회수도 중앙에서 처리된다. 핵심은 “사용자 신원은 IdP/SSO에서, 권한은 Role/정책에서”라는 분리다. 결국 IAM User를 늘리는 대신, SSO + Role 기반 접근으로 관리 포인트를 줄이는 게 더 안전하고 운영 친화적이다.

당신 조직이 지금 IAM User를 계속 늘리고 있다면, 그 이유는 “편해서”일까요, 아니면 “SSO 설계가 없어서”일까요?

## Impact 범위 (어디에 영향을 주나?)

- Security: 퇴사/권한 회수 누락을 줄이고 중앙 통제를 강화
- Operations: 계정이 늘어도 사용자/그룹 운영을 일관되게 유지

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-1-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-1.1%20Security%20access%20design-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Identity%20Center](https://img.shields.io/badge/Service-Identity%20Center-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 1: Design Secure Architectures
- Task focus: SSO/연합(페더레이션) 기반 접근 설계(개념)

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- “사내 IdP로 SSO”는 Identity Center로 연결하라는 신호다.
- “여러 계정에 동일 권한을 중앙에서 할당”도 같은 축이다.

## VAKOG Anchors

- V(Visual): “사용자(SSO) → 계정 선택 → Role” 흐름을 한 줄로 그려본다.
- A(Auditory): “사용자는 SSO, 권한은 Role”을 말로 고정한다.
- O(Olfactory, smell test): 계정마다 IAM User를 계속 만드는 운영은 냄새가 난다.
- G(Gustatory, taste test): ‘퇴사 처리’ 체크리스트를 1분으로 써본다.

## Core Concepts

- SSO는 “인증(누구인가)”을 통일한다.
- 권한은 Role/정책(권한 세트 포함)으로 분리한다.

## Deep Dive

### 시험형 신호

- “사내 IdP(예: AD/Okta)로 SSO” → Identity Center 후보
- “여러 계정에 동일 권한을 중앙에서 할당” → Identity Center + Organizations(계정/OU) 흐름

## Quick Comparison Table

| Topic | Option 1 | Option 2 | Notes |
|---|---|---|---|
| 사용자 관리 | Identity Center (SSO) | IAM User 다수 | 계정이 늘면 IAM User는 운영 비용 폭발 |

## Exam Traps (5-8)

- “SSO 요구”인데 IAM User를 추가로 만들라는 선택지

## Taste Test (1~3분)

- “사내 계정으로 AWS 콘솔 접근 + 중앙 권한 할당” → 어떤 서비스가 먼저 떠오르나요?

## TL;DR (한 줄 정리)

- 사용자는 **SSO로 들어오고**, 실제 권한은 **Role/정책(권한 세트 포함)**로 통제한다고 생각하면 된다.

## Back

- `./00-theory-index.md`
