# DR Strategy Menu (RPO/RTO로 고르는 복구 전략)

## 소개 (이게 뭔가요?)

- DR은 “재해(리전/대규모 장애)까지 포함한 복구 전략”이고, 선택 기준은 RPO/RTO다.

## 고객 사례 (스토리, 600~1000자)

경영진이 질문한다. “리전 장애가 나면 얼마나 빨리 복구돼야 하나요?” 팀은 대답이 막힌다. 평소 장애 대응은 인스턴스 재기동이나 롤백 정도였는데, 리전 단위 장애는 차원이 다르다. 고객 데이터가 얼마나 유실돼도 되는지(RPO), 서비스가 얼마나 빨리 살아나야 하는지(RTO)가 계약/규제와 연결된다. 그런데 이 요구는 기술만의 문제가 아니라 비용 문제다. “항상 두 곳에서 완전히 돌아가게(Active/Active)” 하면 빠르지만 비싸다. “백업만” 두면 싸지만 느리다.

그래서 DR은 메뉴처럼 고른다. Backup/Restore는 비용이 낮지만 RTO가 크다. Pilot light는 핵심만 상시 유지해 중간 정도다. Warm standby는 축소된 운영 환경을 유지해 RTO를 더 줄인다. Active/Active는 가장 빠르지만 비용이 가장 크다. 시험은 이 ‘트레이드오프’를 읽는 문제다. 문장에 RPO/RTO 숫자나 “몇 분 내 복구” 같은 강한 신호가 나오면, 백업만으로 끝나는 답은 오답이 되기 쉽다.

또 하나의 포인트는 “DR은 운영 계획”이라는 점이다. 단순히 리소스를 만들어두는 게 아니라, 장애 시나리오에서 어떤 순서로 전환/복구할지, 그리고 그걸 정기적으로 연습할지까지 포함한다. 시험에서도 ‘계획’과 ‘요구’의 일치 여부를 보는 문장이 섞여 나온다.

당신 서비스의 RPO/RTO 요구를 한 문장으로 말해본다면, 어떤 전략이 자연스러울까요?

## Impact 범위 (어디에 영향을 주나?)

- Reliability: 재해 상황에서 서비스/데이터 복구의 정답을 가른다
- Cost: 요구가 강할수록(Active/Active) 비용이 크게 증가한다

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-2-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-2.2%20Backup%20%26%20DR-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: DR](https://img.shields.io/badge/Service-DR-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 2: Design Resilient Architectures
- Task focus: RPO/RTO 기반 DR 전략 선택(개념)

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- DR 문제는 “정답 서비스”가 아니라 “요구 강도(RPO/RTO) ↔ 비용” 매칭 문제다.

## VAKOG Anchors

- V(Visual): 아래 메뉴 다이어그램으로 선택지를 고정한다.
- A(Auditory): “RPO는 데이터, RTO는 시간”을 말로 고정한다.
- O(Olfactory, smell test): RTO가 짧은데 “백업만” 고르는 답은 냄새가 난다.
- G(Gustatory, taste test): 숫자 신호만 보고 전략을 고른다.

## Core Concepts

- Backup/Restore: 비용 낮음, RTO 큼
- Pilot light: 핵심만 상시 유지, RTO 중간
- Warm standby: 축소된 운영 환경 유지, RTO 작음
- Multi-site active/active: 비용 큼, RTO 매우 작음

```mermaid
flowchart TB
  Req[RPO and RTO requirement] --> Menu{Pick strategy}
  Menu --> BR[Backup restore]
  Menu --> PL[Pilot light]
  Menu --> WS[Warm standby]
  Menu --> AA[Active active]
```

## Deep Dive

- “요구가 강할수록 비용이 올라간다”를 읽어내는 문제가 많다.

## Quick Comparison Table

| Strategy | Cost | RTO |
|---|---|---|
| Backup/Restore | Low | High |
| Warm standby | Medium~High | Low |
| Active/Active | Highest | Lowest |

## Exam Traps (5-8)

- RTO가 매우 짧은데 Backup/Restore만 고르는 답

## Taste Test (1~3분)

- “몇 분 내 복구, 데이터 손실 거의 0” → 어떤 전략 쪽이 더 자연스러운가?

## TL;DR (한 줄 정리)

- RPO/RTO 요구가 강할수록 **Warm standby → Active/Active**로 올라가며, 비용도 같이 올라간다.

## Back

- `../01-theory.md`
