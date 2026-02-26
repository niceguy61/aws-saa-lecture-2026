# Special Lecture - Domain 4: Cost-Optimized Architectures (Top Services)

## Why This Matters On The Exam

- 비용 최적화는 “요구사항 충족 + 비용 드라이버 제거”의 설계 문제로 나온다.
- 헷갈리는 포인트는 “SP/RI/Spot 선택”, “S3 storage class”, “NAT 비용 vs VPC endpoint”다.

## Services In Scope (Draft Top 10~15)

- EC2 pricing (Savings Plans, RIs, Spot)
- S3 storage classes + lifecycle
- Budgets/Cost Explorer(개념)
- NAT Gateway vs VPC endpoints
- DynamoDB capacity modes

## Confusing Similar Cases (Choose-This-Not-That)

| Scenario | Best choice | Why | Common wrong choice | Why it's wrong |
|---|---|---|---|---|
| S3 비용 최적화 | lifecycle + storage class | 자동 전환 | 무조건 Standard | 장기 보관에 비효율 |
| 프라이빗 S3 접근 비용 | Gateway endpoint(S3) | NAT egress 제거 | NAT Gateway | 시간/트래픽에 따라 급증 |

## Deep Dive (Stubs)

- TODO

