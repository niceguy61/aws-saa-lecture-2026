# Intelligent-Tiering: 예측이 어려울 때 자동 최적화

## 소개 (이 서비스/주제는 무엇인가?)

- S3 Intelligent-Tiering은 액세스 패턴이 예측 어려운 데이터에 대해 **자동으로 티어를 이동**해 비용을 최적화하는 옵션이다.

## 고객 사례 (스토리, 600~1000자)

릴리즈 아카이브 파일은 어떤 달엔 많이 내려받고, 어떤 달엔 거의 안 본다. 팀은 Standard-IA로 옮기자니 “갑자기 핫해지면 어떡하지?”가 걱정이고, Standard로 두자니 장기 비용이 아깝다. 액세스 패턴을 예측해서 정책을 만들려 해도, 제품/마케팅 일정에 따라 변동이 커서 정확히 맞추기 어렵다.

이때 Intelligent-Tiering이 후보가 된다. 시험에서 “액세스 패턴이 예측하기 어렵다”, “자동 최적화가 필요하다” 같은 문장이 나오면 이 선택지가 올라온다. 다만 자동이라고 해서 아무 생각 없이 쓰는 건 아니다. 어떤 데이터는 항상 핫이거나, 항상 콜드라서 명시적으로 클래스를 고르는 게 더 낫기도 하다. 결국 신호는 “패턴 예측이 어렵다”다.

실무에서는 “정책을 여러 개로 나눠도 계속 예외가 생긴다”는 순간이 온다. 그때부터는 사람이 규칙을 유지하는 비용이 커지고, 잘못된 전환으로 성능이나 운영이 흔들린다. Intelligent-Tiering은 그 부담을 줄여주는 쪽에 가깝다.

정리하면, Intelligent-Tiering은 “규칙을 못 정하겠다”가 아니라 “규칙을 정해도 자주 틀린다”는 상황에서 비용과 운영 부담을 같이 줄이는 카드다.

지금 데이터는 액세스 패턴을 말로 예측할 수 있나요, 아니면 들쭉날쭉한가요?

## Impact 범위 (어디에 영향을 주나?)

- Cost: 잘못된 클래스 선택으로 생기는 낭비를 줄인다.
- Operations: 수동/복잡한 전환 규칙을 줄인다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-4-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-Auto%20tiering-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Intelligent--Tiering](https://img.shields.io/badge/Service-Intelligent--Tiering-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

## Core Concepts

- 시험 힌트
  - “액세스 패턴이 예측하기 어렵다”
  - “자동 최적화”

## Exam Traps (5-8)

- 패턴이 명확한데도(항상 핫/항상 콜드) 무조건 Intelligent-Tiering을 고르는 선택지
- 복구 시간 요구를 무시하고 ‘자동’만 보는 선택지

## Taste Test (1~3분)

- “액세스가 들쭉날쭉해서 어떤 클래스로 고정하기 어렵다” → 무엇이 먼저 떠오르나요?

## TL;DR (한 줄 정리)

- “예측 어려움/자동 최적화” 신호가 있으면 **Intelligent-Tiering**이 후보다.

## Back

- `./00-theory-index.md`
