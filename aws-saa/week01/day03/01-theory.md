# CloudTrail/Config + 탐지 서비스(감사/준수/탐지)

## 소개 (이게 뭔가요?)

- CloudTrail은 “누가/언제/무엇을 했는지(행위)”를 남기는 감사 로그 계층이다.
- Config는 “리소스가 어떤 구성 상태인지(상태/준수)”를 추적한다.
- GuardDuty/Security Hub/Inspector는 “탐지 결과를 만들고/모으고/취약점을 찾는” 레이어다.

## 고객 사례 (스토리)

어느 날 새벽, 운영 채널에 알림이 떴다. “S3 버킷이 퍼블릭으로 열렸습니다.” 누가 바꿨는지, 언제부터였는지, 그리고 다른 리소스도 같은 문제가 있는지 바로 답해야 한다. 그런데 로그가 애플리케이션 로그뿐이면 “AWS 콘솔에서 누가 클릭했는지”는 남지 않는다. 보안/감사 팀은 “변경 이력 보관”과 “규정 위반 탐지”를 동시에 요구한다.

감사팀은 “최소 6개월은 근거를 남겨야 한다”고 말하고, 운영팀은 “다음번엔 열리기 전에 알림이 와야 한다”고 한다. 결국 필요한 건 로그 ‘한 줄’이 아니라, 질문을 재구성할 수 있는 “근거”다.

이때 CloudTrail은 “API 호출(행위)의 영수증” 역할을 한다. 누가 보안 그룹을 열었는지, 누가 정책을 바꿨는지는 CloudTrail에서 찾는다. 반면 Config는 “리소스 구성(상태)의 타임라인”이다. 특정 시점에 보안 그룹 규칙이 무엇이었는지, 규정에 어긋났는지는 Config가 더 자연스럽다. 여기에 GuardDuty가 이상 징후를 findings로 만들고, Security Hub가 여러 결과를 모아준다. Inspector는 취약점 관점에서 보완한다(시험에서는 ‘탐지/집계/취약점’을 섞어 묻는다).

“누가 했나”와 “어떤 상태였나” 중, 지금 당신이 먼저 답해야 하는 질문은 무엇인가요?

## Impact 범위 (어디에 영향을 주나?)

- Security/Compliance: 감사(Audit)와 준수(Compliance) 요구를 풀어내는 핵심 도구들이다.
- Operations: “원인 추적/누가 바꿨나”를 못 풀면 장애 대응이 느려진다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-1-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-1.2%20Secure%20workloads%20%26%20apps-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: CloudTrail](https://img.shields.io/badge/Service-CloudTrail-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Config](https://img.shields.io/badge/Service-Config-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: GuardDuty](https://img.shields.io/badge/Service-GuardDuty-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Security%20Hub](https://img.shields.io/badge/Service-Security%20Hub-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Inspector](https://img.shields.io/badge/Service-Inspector-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 1: Design Secure Architectures
- Task focus:
  - 1.2 Design secure workloads and applications (감사/탐지로 운영 보안)
  - 1.3 Determine appropriate data security controls (감사/추적)

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- 시험은 “행위(CloudTrail) vs 상태(Config)”를 섞어서 낚는다. 질문 축을 먼저 고르면 절반은 맞춘다.

## Core Concepts

- Audit vs Compliance vs Detection
  - Audit: “누가/언제/무엇을 했는가”를 재구성할 수 있어야 함(CloudTrail)
  - Compliance/Config state: “리소스가 어떤 구성인지/규칙 위반인지”(Config)
  - Detection: “이상 행위/위협”을 찾아 알림/조치를 연결(GuardDuty/Security Hub 등)

![CloudTrail vs Config vs CloudWatch (audit and observability)](../../assets/core/observability-audit.svg)

## Deep Dive

### CloudTrail: API 활동의 근거 자료

- What it captures(개념)
  - 관리 이벤트(Management events): 대부분의 제어 plane API 호출
  - (필요 시) 데이터 이벤트(Data events): 예: S3 object-level API (요구사항/비용/범위가 다름)
- Event history vs Trail
  - Event history: 콘솔에서 최근 이벤트를 빠르게 확인(기본 제공 범위)
  - Trail: S3로 장기 보관/검색/감사 체계 구축(조직 표준)
- 시험 포인트
  - “누가 삭제했는지/누가 정책을 바꿨는지”는 CloudTrail
  - “S3 데이터 이벤트를 켤지 말지”는 비용/요구사항 트레이드오프
- Exam must-know (포인트 + Why + 대안)
  - Key point: “누가 이 변경을 했나”는 CloudTrail, “현재/과거 구성 상태가 어땠나”는 Config다.
  - Why: CloudTrail은 API 호출(행위)의 증거이고, Config는 리소스 구성(상태)의 스냅샷/이력이다. 둘은 질문의 축이 다르다.
  - Alternative: “탐지/알림” 요구가 명시되면 GuardDuty/Security Hub 같은 탐지/집계 계층을 붙인다(CloudTrail 자체는 탐지 엔진이 아니다).

```mermaid
flowchart LR
  API[API Call] --> CT[CloudTrail]
  CT --> EH[Event history - console]
  CT --> S3[S3 bucket - logs]
  S3 --> ATH[Athena query - optional]
```

### AWS Config: 구성 변화와 준수(Compliance) 관점

- What it captures(개념)
  - 리소스 구성(configuration items) 변경 이력
  - 규칙 기반 준수 평가(Config rules)
- CloudTrail과의 차이(시험형 문장)
  - CloudTrail: “행위(Who did what)”
  - Config: “상태(What is the current/was the configuration)”
- Exam must-know (포인트 + Why + 대안)
  - Key point: “준수/규칙 위반” 문장이 있으면 Config(규칙/준수)가 정답 후보로 올라간다.
  - Why: 준수는 이벤트(행위)보다 리소스의 속성/구성 기준으로 판단된다(예: public S3, 0.0.0.0/0 인바운드 등).
  - Alternative: “누가 그 설정을 바꿨는지”까지 묻는다면 CloudTrail을 함께 써야 한다(둘 중 하나로만 해결하려는 답은 함정일 수 있음).

```mermaid
flowchart TB
  R[Resource state changes] --> CFG[AWS Config]
  CFG --> HIST[Config history]
  CFG --> RULES[Config rules - compliance]
```

### Detection 서비스 연결(개념 수준)

- GuardDuty: 위협 탐지(여러 로그 소스 기반) 후 findings 생성
- Security Hub: 다양한 보안 결과를 집계/표준화/점수화(허브)
- Inspector: 취약점/구성 평가(서비스/에이전트 기반 패턴이 선택지로 출제될 수 있음)

```mermaid
flowchart LR
  CT[CloudTrail] --> GD[GuardDuty findings]
  VPC[VPC signals] --> GD
  DNS[DNS signals] --> GD
  GD --> SH[Security Hub]
  INS[Inspector findings] --> SH
```

## Quick Comparison Table

| Question | Best tool | Why |
|---|---|---|
| 누가 보안 그룹 인바운드를 열었나 | CloudTrail | API 호출 근거 |
| 현재 보안 그룹 규칙이 기준 위반인가 | Config | 구성/준수 |
| 의심스러운 활동을 탐지/알림하고 싶다 | GuardDuty/Security Hub | 탐지/집계 |

## Exam Traps

- CloudTrail과 Config를 “둘 다 로그니까 동일”로 보는 선택지: 기록 목적이 다르다.
- “탐지 서비스가 곧 로그 저장소”라는 오해: 탐지는 소스(CloudTrail 등) 위에서 동작한다.
- 데이터 이벤트/고급 기능을 무조건 켜는 답: 요구사항/비용 트레이드오프를 본다.

## TL;DR (한 줄 정리)

- “누가 했나”는 **CloudTrail**, “구성이 어땠나/준수인가”는 **Config**, “이상 징후를 찾고 모아라”는 **GuardDuty + Security Hub(+ Inspector)**로 푼다.
