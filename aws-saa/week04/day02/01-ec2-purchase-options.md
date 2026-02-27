# EC2 구매 옵션(RI/SP/Spot): 문장 신호로 고른다

## 소개 (이 서비스/주제는 무엇인가?)

- EC2 비용 최적화의 핵심은 “어떤 인스턴스를 쓰나”보다 **어떤 구매/할인 모델을 고르나**인 경우가 많다.

## 고객 사례 (스토리, 600~1000자)

서비스가 안정되면서 트래픽이 크게 변하지 않는데, 매달 EC2 비용은 꾸준히 크다. 팀은 인스턴스를 조금 줄여보지만, 성능 여유가 줄어들 뿐 비용 절감 폭은 작다. 반대로 배치 작업은 매일 밤 몇 시간만 돌고, 중간에 끊겨도 재시도하면 되는 성격인데도 On-Demand로 돌리고 있다. “지금 돈을 가장 많이 먹는 방식이 무엇인가?”를 보려면 스펙이 아니라 요금 모델을 봐야 한다.

여기서 문장 신호가 정답을 가른다. “1~3년 사용량이 예측 가능(steady state)”이면 RI나 Savings Plans가 후보로 올라간다. “중단 허용, 배치, fault-tolerant” 같은 표현이 있으면 Spot이 강력하다. 반대로 “중단 불가/고가용성” 요구가 강하면 Spot은 오답 후보가 된다. 스파이크가 심하면 On-Demand를 기본으로 두고 Auto Scaling으로 피크만 대응하는 답이 자연스럽다.

그리고 같은 “할인”이라도 조건이 다르다. steady state는 장기 약정의 근거가 되고, 중단 허용은 스팟의 근거가 된다. 반대로 “항상 켜져 있어야 한다”는 요구가 있으면 할인보다 가용성/안정성이 우선이다. 이 기준이 고정되면, 옵션을 외우지 않아도 문장만 읽고 후보가 좁혀진다.

시험은 이 신호를 거의 문장에 직접 넣는다. 그래서 구매 옵션 문제는 ‘암기’가 아니라 ‘키워드 매칭’이다. 지금 시나리오는 예측 가능한가요, 중단을 허용하나요?

## Impact 범위 (어디에 영향을 주나?)

- Cost: 할인 모델/Spot은 절감 폭이 크다.
- Reliability: Spot은 중단을 허용할 때만 정답이 된다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-4-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-4.2%20Compute%20pricing-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: EC2](https://img.shields.io/badge/Service-EC2-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Concept: Savings%20Plans](https://img.shields.io/badge/Concept-Savings%20Plans-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Concept: Reserved%20Instances](https://img.shields.io/badge/Concept-Reserved%20Instances-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Concept: Spot](https://img.shields.io/badge/Concept-Spot-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 4: Design Cost-Optimized Architectures
- Objectives: 예측 가능/중단 허용 신호로 구매 옵션을 고를 수 있는지

</details>

## VAKOG Anchors

- V(Visual): 아래 결정 트리로 신호를 분류한다.
- A(Auditory): “예측 가능=RI/SP, 중단 허용=Spot, 스파이크=On-Demand+ASG”를 말로 고정한다.
- O(Olfactory, smell test): 중단 불가인데 Spot을 고르면 냄새가 난다.
- G(Gustatory, taste test): 문장 1개로 옵션을 고른다.

## Core Concepts

```mermaid
flowchart TB
  Sig[Workload signals] --> Steady[예측 가능 1~3년 -> RI or SP]
  Sig --> Burst[스파이크/변동 -> On-Demand + ASG]
  Sig --> Batch[중단 허용 -> Spot]
```

## Deep Dive

### EC2 구매 옵션 전체 정리(누락 없이)

> 표준/대표 선택지는 **굵게** 표시했다.

| 옵션 | 언제 쓰나(문장 신호) | 제약/리스크 | 비용 효율 포인트 |
|---|---|---|---|
| **On-Demand** | 스파이크/변동, 예측 어려움 | 할인 적음 | 유연성 최우선(기본값) |
| **Savings Plans(SP)** | steady state, 1~3년 예측 가능 | 약정(커밋) 필요 | 예측 가능할수록 비용 효율↑ |
| Reserved Instances(RI) | steady state, 특정 타입/리전 고정 성향 | 제약이 더 큼(설계에 따라) | 조건이 맞으면 절감 효과 |
| Spot | 중단 허용 배치/내결함 | 인터럽트 가능 | 중단 허용이면 큰 절감 |

### 비용 드라이버 체크(컴퓨트 관점)

- “할인”은 곧 “조건”이다: 예측 가능/중단 허용 신호가 없는데 할인만 노리면 함정이 된다.
- 큰 절감은 종종 “옵션”보다 “운영 패턴(ASG/스케줄 축소)”과 결합될 때 나온다.

## Exam Traps (5-8)

- “중단 허용 배치”인데 On-Demand만 고르는 선택지
- “steady state”인데 On-Demand만 고집하는 선택지
- “중단 불가”인데 Spot을 고르는 선택지

## Taste Test (1~3분)

- “배치 작업, 중단 가능, 재시도 가능” → 어떤 옵션이 먼저 떠오르나요?

## TL;DR (한 줄 정리)

- “예측 가능”이면 **RI/SP**, “중단 허용”이면 **Spot**, “스파이크”면 **On-Demand+ASG**가 신호다.

## Back

- `./00-theory-index.md`
