# Day 03 - Theory Index (감사/준수/탐지)

> 이 문서는 Day 이론 “인덱스”다. 서비스별 theory는 Day 폴더 바로 아래 `01-*.md`에서 각각 읽는다.

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

## Service Theories (서비스별로 읽기)

- [CloudTrail (누가/언제/무엇을 했나: 행위의 근거)](01-cloudtrail.md)
- [AWS Config (구성 상태 + 준수/규칙 위반)](02-config.md)
- [Detection services (GuardDuty / Security Hub / Inspector)](03-detection-services.md)

> “행위(CloudTrail) vs 상태(Config) vs 탐지/집계(GuardDuty/Security Hub)”를 분리해서 읽어야 시험형 문장도 깔끔해진다.

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
