# Day 05 - Special Lecture + Week Summary (Domain 4)

비용 최적화를 “비용 드라이버 식별 + 대안 비교(트레이드오프)”로 정리하고, 케이스 문제로 선택 기준을 고정한다.

## Outcomes

- SP/RI/Spot, NAT vs Endpoint, DynamoDB capacity modes 같은 선택 기준을 비교표로 정리한다.
- 케이스 기반 미니 시뮬레이션으로 S3 lifecycle/Intelligent-Tiering 기반 비용 최적화 설정 흐름을 따라간다.
- “요구사항(성능/가용성/보안) vs 비용” 트레이드오프를 문장으로 설명한다.

## Services In Scope (Top set)

- EC2 pricing (Savings Plans/RI/Spot) (concept)
- S3 storage classes + lifecycle + Intelligent-Tiering
- NAT Gateway vs VPC endpoints (concept)
- DynamoDB on-demand vs provisioned (concept)
- Cost Explorer/Budgets (optional, 권한 있을 때)

## Timebox (4h)

- Special lecture + case walkthrough (theory): 3h 30m
- Case quiz + review: 30m

## Reading

- Pack: `aws-saa/special-lectures/domain04-cost-optimized-top-services.md`

## Exam-Style Design Questions

- “프라이빗 서브넷에서 S3 접근” 시 NAT 비용을 줄이려면 무엇을 고려할까?
- S3 storage class 선택을 “액세스 패턴/복구 시간”으로 설명할 수 있는가?
- DynamoDB에서 on-demand vs provisioned는 어떤 기준으로 고를까?
