# Special Lecture + Week Summary (Domain 3)

## Exam Guide Mapping

- Domain: Domain 3: Design High-Performing Architectures
- Task focus:
  - 3.1 Storage
  - 3.2 Compute
  - 3.3 Database
  - 3.4 Network
  - 3.5 Data ingestion/transformation

## Week 3 Diagnosis Order (시험에서 통하는 순서)

1. 캐시(CloudFront/ElastiCache)로 불필요한 호출을 줄일 수 있는가
2. DB/키/인덱스/파티션이 병목인가
3. 스토리지 IOPS/throughput이 부족한가(EBS/EFS)
4. 컴퓨트가 부족한가(EC2/Lambda concurrency)
5. 네트워크 경로/엣지/리전 선택이 문제인가

## Core Concepts

- Domain 3는 “성능 최적화”를 단일 서비스 선택이 아니라 “병목 진단 순서”로 푸는 문제로 자주 나온다.

![Caching layers](../../assets/core/caching-layers.svg)

## Confusing Similar Cases

| Scenario | Best choice | Why | Common wrong choice | Why it's wrong |
|---|---|---|---|---|
| 글로벌 정적 콘텐츠 | CloudFront | 캐시/엣지 | 단일 리전 S3만 | RTT/지연 증가 |
| 고정 IP 가속(개념) | Global Accelerator | Anycast | CloudFront | L7 캐시 목적과 다름 |
| DynamoDB 지연 | 키 설계/GSI | 핫 파티션 회피 | 무조건 DAX | 근본 키 설계 문제는 남음 |
| DB 읽기 성능 | 캐시/인덱스 | 반복 조회 최적화 | 스케일업만 | 비용 증가/한계 |

## Exam-Heavy Pattern: CloudFront + Private S3 (OAC)

```mermaid
flowchart LR
  U[Users] --> CF[CloudFront]
  CF --> S3[S3 Bucket - private]
  CF -. signed as OAC .-> S3
```

- S3는 퍼블릭이 아니고, CloudFront만 접근하도록 bucket policy를 제한한다.
- 캐시 키/TTL/무효화(invalidation)가 선택지로 등장한다.

## Exam must-know (요약)

- Key point: 캐시 가능하면 캐시(CloudFront/ElastiCache)가 1순위 후보, 키/인덱스/IOPS 신호가 있으면 그 축으로 들어간다.
- Why: 성능 문제의 원인은 CPU보다 네트워크 RTT/캐시 히트율/DB 액세스 패턴/스토리지 I/O에 있는 경우가 많다.
- Alternative: 요구가 “복원력” 중심이면(Domain 2) DR/ASG/큐로, “비용” 중심이면(Domain 4) 티어링/구매 옵션/전송 비용으로 전환한다.

## Reference Pack

- `aws-saa/special-lectures/domain03-high-performing-top-services.md`
