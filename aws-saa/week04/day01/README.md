# Day 01 - Cost drivers + tagging + Budgets/Cost Explorer (Cost drivers + 가시성)

![고객 사례 삽화 - 비용 드라이버 가시화](../../assets/scenario_image/w4d1s0.png)

## Outcomes

- 비용을 “사용량 x 단가”로 분해하고, 주요 비용 드라이버(컴퓨트/스토리지/전송)를 식별한다.
- 태깅 전략이 비용 가시성(차지백/쇼백)에 왜 중요한지 설명한다.
- Cost Explorer/Budgets가 각각 무엇을 하는지(분석 vs 알림/통제) 구분한다.
- Budget 알림 흐름(예산 → 알림 → 대응)을 설계 관점으로 설명한다.

## Services In Scope

- Cost Explorer (분석)
- AWS Budgets (알림/통제)
- (개념) Cost allocation tags

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [Cost Explorer: 비용을 “분해해서” 본다](01-cost-explorer.md)
- [AWS Budgets: 초과를 “알림/통제”한다](02-budgets.md)
- [Cost allocation tags: 팀/프로젝트 비용을 나눠 본다](03-cost-allocation-tags.md)

## Core Concepts

- 비용 = 사용량(시간/요청/GB) × 단가
- 최적화 = “요구사항을 유지하면서” 드라이버를 줄이는 설계
- 가시화 없이는 최적화가 없다
  - 태그/계정/서비스/리전 차원으로 “어디서 돈이 나가는지”부터 본다

![비용 드라이버 맵](../../assets/core/cost-drivers-map.svg)

## Decision Rules (정답을 가르는 규칙 3개)

1. “팀/프로젝트별 비용”이면 **태그 표준화(또는 계정 분리)**가 먼저다.
2. “원인 분석/추세/그룹핑”이면 **Cost Explorer**, “초과 알림/임계치”면 **Budgets**다.
3. 비용은 우선 **Compute/Storage/Network** 3축으로 분해하고, 드라이버를 하나씩 제거한다.

## Smell Test (레드 플래그 3~5)

- 태그 없이 “팀별 비용”을 정확히 본다고 하는 답
- NAT/데이터 전송 비용을 무시하고 컴퓨트만 줄이는 답
- “최적화=무조건 cheapest”로 가서 요구사항(성능/가용성/보안)을 깨는 답

## TL;DR (한 줄 정리)

- Domain 4의 출발은 **가시화(태그) → 분석(Cost Explorer) → 알림(Budgets)**이고, 그 다음에야 ‘줄일 곳’이 보인다.

## Exam-Style Design Questions

- “비용을 팀/프로젝트별로 나눠 보고 싶다”는 요구에서 가장 먼저 해야 할 일은?
- “비용 급증을 빨리 감지”하려면 어떤 도구 조합이 적절한가?
- “데이터 전송”이 비용 함정이 되는 케이스는 어떤 문장으로 나타나는가?
