# Day 05 - Special Lecture + Week Summary (Domain 3)

성능을 “병목(컴퓨트/스토리지/DB/네트워크/캐시)” 관점으로 정리하고, 자주 출제되는 선택 기준과 함정을 비교표로 회수한다.

## Outcomes

- CloudFront/GA, ElastiCache/DAX, DynamoDB/Aurora 같은 비교 포인트를 정리한다.
- 통합 미니 랩으로 CloudFront + S3(OAC) 캐싱 패턴을 콘솔로 구성한다.
- 성능 문제를 “어디를 먼저 의심할지” 진단 순서로 설명한다.

## Services In Scope (Top set)

- CloudFront (cache behavior)
- EC2 sizing (review)
- EBS/EFS performance (review)
- DynamoDB (partitioning/index), Aurora/RDS (review)
- ElastiCache, DAX (concept)
- Lambda concurrency/limits (review)

## Timebox (4h)

- Special lecture (theory): 2h 30m
- Integrated mini lab (console): 1h
- Case quiz + review: 30m

## Reading

- Pack: `aws-saa/special-lectures/domain03-high-performing-top-services.md`

## Exam-Style Design Questions

- “전 세계 사용자” 지연시간 이슈에서 CloudFront vs Global Accelerator 중 무엇을 고를까?
- DynamoDB 성능 이슈를 “키 설계/GSI/핫 파티션” 관점으로 진단할 수 있는가?
- Lambda 동시성 제한이 성능/가용성에 미치는 영향을 설명할 수 있는가?

