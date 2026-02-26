# Day 05 - Special Lecture + Week Summary (Domain 2)

Top 서비스(라우팅/로드밸런싱/디커플링/DR)를 “선택 기준 + 함정 + 대안”으로 정리하고, 통합 미니 랩과 케이스 문제로 회수한다.

## Outcomes

- SQS/SNS/EventBridge, Multi-AZ/Read replica, ALB/NLB 같은 헷갈리는 비교를 정리한다.
- 통합 미니 랩으로 SNS -> SQS fan-out + DLQ 패턴을 콘솔로 구성한다.
- DR 시나리오에서 RPO/RTO 기반 선택 논리를 설명한다.

## Services In Scope (Top set)

- Route 53 (routing review)
- ELB (ALB/NLB), Auto Scaling (review)
- SQS, SNS, EventBridge (핵심 비교)
- RDS/Aurora Multi-AZ vs Read replica (review)
- AWS Backup / DR strategy (concept)

## Timebox (4h)

- Special lecture (theory): 2h 30m
- Integrated mini lab (console): 1h
- Case quiz + review: 30m

## Reading

- Pack: `aws-saa/special-lectures/domain02-resilient-top-services.md`

## Exam-Style Design Questions

- “버퍼링/재시도” 요구사항에서 SQS vs SNS vs EventBridge 중 무엇이 정답이 되는가?
- Multi-AZ가 필요한 상황과 Read replica가 필요한 상황을 어떻게 구분할까?
- 장애 시나리오에서 RPO/RTO에 맞는 DR 전략을 어떻게 선택할까?

