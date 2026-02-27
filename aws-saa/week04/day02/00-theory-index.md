# Day 02 - Theory Index (컴퓨트 비용: 구매 옵션 + right sizing/Auto Scaling)

> 이 문서는 Day 이론 “인덱스”다. 상세 이론은 Day 폴더 바로 아래 `01-*.md` 서비스별 문서로 분리한다.

## 소개 (이 Day는 무엇을 묶나?)

- Day 02는 컴퓨트 비용 최적화를 “스펙 줄이기”가 아니라 **요구 신호에 맞는 요금 모델 선택 + 측정 기반 right sizing**으로 정리한다.
- 시험은 보통 “예측 가능/중단 허용/스파이크” 같은 문장 신호로 RI/SP/Spot/ASG를 고르게 만든다.

## 고객 사례 (스토리, 600~1000자)

서비스가 안정되자 비용이 문제다. EC2가 가장 큰 비중을 차지하는데, 팀은 “일단 작은 인스턴스로 바꾸자”로 접근한다. 그런데 몇 번 바꾸고 나면 장애가 나거나, 다시 스펙을 올리는 일이 반복된다. 결국 비용만 줄이고 성능/가용성을 깨는 ‘최적화’가 된다.

여기서부터는 순서가 중요하다. 첫째, 워크로드가 steady state(1~3년 예측 가능)인지, 중단을 허용하는 배치인지, 아니면 스파이크가 심한지 문장 신호로 분류한다. 예측 가능하면 할인 모델(Savings Plans/RI)이 정답 후보로 올라가고, 중단 허용이면 Spot이 강력하다. 스파이크가 있으면 On-Demand를 기본으로 두고 Auto Scaling으로 피크만 대응하는 흐름이 자연스럽다.

둘째, right sizing은 ‘감’이 아니라 측정이다. CPU/메모리/네트워크/I/O 지표(CloudWatch)와 p95/p99 같은 앱 지표로 “진짜 필요한 만큼”을 확인해야 한다. 그리고 비피크가 명확하면 Scheduled scaling으로 “야간 0” 같은 패턴이 비용 효율을 크게 만든다.

지금 문제 문장에는 “예측 가능”이 있나요, “중단 허용”이 있나요, 아니면 “스파이크”가 더 강한가요?

## Impact 범위 (어디에 영향을 주나?)

- Cost: 구매 옵션 선택과 스케줄 축소가 가장 큰 레버리지인 경우가 많다.
- Reliability: Spot/스펙 다운은 중단/성능 요구를 위반하면 바로 오답이다.
- Operations: 측정 기반 right sizing이 없으면 ‘왔다 갔다’만 반복한다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-4-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-4.2%20Compute%20solutions-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: EC2](https://img.shields.io/badge/Service-EC2-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Auto%20Scaling](https://img.shields.io/badge/Service-Auto%20Scaling-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 4: Design Cost-Optimized Architectures
- Task focus:
  - 4.2 Design cost-optimized compute solutions

</details>

## Core Concepts

- 비용 절감은 “요구 신호”에서 시작한다
  - 예측 가능(steady state) → 할인 모델(RI/Savings Plans)
  - 중단 허용 → Spot
  - 변동/스파이크 → On-Demand + Auto Scaling
- right sizing은 감이 아니라 측정이다(CloudWatch, p95/p99, utilization)

![구매 옵션 결정](../../assets/core/purchase-options-decision.svg)

## Service Theories (서비스별로 읽기)

- [EC2 구매 옵션(RI/SP/Spot): 문장 신호로 고른다](01-ec2-purchase-options.md)
- [Right sizing + Auto Scaling: 측정하고, 비피크를 줄인다](02-right-sizing-autoscaling.md)

## Decision Rules (정답을 가르는 규칙 3개)

1. “1~3년 예측 가능”이면 **RI/SP**, “중단 허용 배치”면 **Spot**이 먼저다.
2. “스파이크/변동”이면 **On-Demand + Auto Scaling**(특히 Scheduled scaling)이 자연스럽다.
3. right sizing은 **지표로 측정**하고, “더 큰 1대”로만 끝내는 답은 조심한다.

## Smell Test (레드 플래그 3~5)

- 중단 불가인데 Spot을 고르는 답
- 예측 가능인데 On-Demand만 고집하는 답
- right sizing을 “감”으로 결정하는 답(측정/지표가 없다)

## TL;DR (한 줄 정리)

- 컴퓨트 비용은 **요구 신호(예측/중단/스파이크) → 요금 모델 선택 → 측정 기반 right sizing/스케줄 축소** 순서로 푼다.
