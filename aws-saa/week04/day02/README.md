# Day 02 - EC2 pricing models + right sizing/ASG (컴퓨트 비용 최적화)

![고객 사례 삽화 - 컴퓨트 비용 최적화 흐름](../../assets/scenario_image/w4d2s0.png)

## Outcomes

- On-Demand/RI/Savings Plans/Spot의 선택 기준(예측 가능성/중단 허용)을 설명한다.
- right sizing의 목표를 “요구사항 대비 적정”으로 정의할 수 있다.
- Auto Scaling/Scheduled scaling을 비용 최적화 관점(야간 0, 피크만 확장)으로 연결한다.

## Services In Scope

- EC2 purchase options (개념)
- Auto Scaling (scheduled scaling 개념)
- (개념) Spot interruptions, mixed instances

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [EC2 구매 옵션(RI/SP/Spot): 문장 신호로 고른다](01-ec2-purchase-options.md)
- [Right sizing + Auto Scaling: 측정하고, 비피크를 줄인다](02-right-sizing-autoscaling.md)

## Core Concepts

- 비용 절감은 “요구 신호”에서 시작한다
  - 예측 가능(steady state) → 할인 모델(RI/Savings Plans)
  - 중단 허용 → Spot
  - 변동/스파이크 → On-Demand + Auto Scaling
- right sizing은 감이 아니라 측정이다(CloudWatch, p95/p99, utilization)

![구매 옵션 결정](../../assets/core/purchase-options-decision.svg)

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

## Exam-Style Design Questions

- “중단 허용 배치” 문장이 있으면 어떤 구매 옵션이 정답 후보가 되는가?
- “1~3년 사용량이 예측 가능” 문장이 있으면 어떤 옵션이 정답 후보가 되는가?
- right sizing은 “무엇을 보고” 결정해야 하는가(지표/측정)?
