# AWS SAA Glossary (시험 용어)

시험에서 “용어를 정확히 구분하는지”로 정답이 갈리는 것들을 짧게 정리한다.

더 큰 서비스 목록(공식 목록 + 링크)은 `aws-services.md` 참고.

## Official docs (quick links)

- AWS Documentation (search): https://docs.aws.amazon.com/search/doc-search.html
- In-scope AWS services & features (SAA-C03): https://docs.aws.amazon.com/ko_kr/aws-certification/latest/examguides/saa-03-in-scope-services.html
- AWS Well-Architected Framework (official): https://aws.amazon.com/ko/architecture/well-architected/
- IAM User Guide: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
- Amazon VPC User Guide: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
- Amazon S3 User Guide: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html

## Framework & Exam

- **Well-Architected Framework (WAF)** ([reference](./well-architected-framework.md)): 6개 Pillar로 워크로드를 점검/개선하는 AWS의 설계 기준.

## Identity & Security

- **Principal**: “누가 요청했나”(IAM user/role, federated user 등).
- **Authentication vs Authorization**: 인증(누구인가) vs 인가(무엇을 할 수 있나).
- **Identity-based policy**: 사용자/그룹/역할에 붙는 정책.
- **Resource-based policy**: 리소스에 붙는 정책(S3 bucket policy, KMS key policy 등).
- **Explicit Deny**: 어떤 Allow보다 우선한다(시험 단골).
- **Permissions boundary**: identity(사용자/역할) 단위의 “권한 상한선”.
- **SCP (Service Control Policy)** ([theory](../week01/day01/03-organizations-scp.md)): 계정/OU 단위의 “권한 상한선”(권한 부여가 아님).
- **STS AssumeRole** ([theory](../week01/day01/02-sts.md)): 교차 계정/임시 권한의 기본 패턴(“키 공유” 답안은 보통 함정).
- **KMS key policy** ([theory](../week01/day02/01-kms.md)): KMS 접근의 ‘관문’이 되는 경우가 많다(IAM Allow만으로 끝나지 않는 함정).

## Networking

- **Region / AZ**: 리전(지역) / 가용 영역(독립 장애 도메인). “Multi-AZ”는 HA 신호.
- **VPC / Subnet**: VPC는 네트워크 경계, 서브넷은 AZ 내 IP 범위.
- **CIDR**: IP 주소 범위 표기(네트워크 설계 문제에 자주 등장).
- **ENI**: 네트워크 인터페이스(보안 그룹이 붙는 대상).
- **Security Group (SG)** ([theory](../week01/day04/01-sg-vs-nacl.md)): 인스턴스/ENI 단위, stateful.
- **NACL** ([theory](../week01/day04/01-sg-vs-nacl.md)): 서브넷 단위, stateless(인/아웃 규칙 둘 다 필요).
- **VPC Endpoint** ([theory](../week01/day04/02-vpc-endpoints-privatelink.md)): NAT/인터넷 없이 AWS 서비스로 사설 접근.
  - Gateway endpoint: S3, DynamoDB
  - Interface endpoint(PrivateLink): 그 외 다수 서비스 패턴

## Storage (S3)

- **S3 storage class** ([theory](../week04/day03/01-s3-storage-classes.md)): “액세스 패턴/복구 요구/비용”으로 고른다.
- **Lifecycle rule** ([theory](../week04/day03/02-s3-lifecycle.md)): 전환/만료를 정책화(수동 이동은 운영 부채).
- **Versioning** ([theory](../week02/day03/01-s3-versioning.md)): 실수(삭제/덮어쓰기) 복구의 기본기.
- **Replication (SRR/CRR)** ([theory](../week02/day03/02-s3-replication.md)): 다른 버킷/리전에도 동일 데이터(대개 versioning이 전제).
- **Glacier** ([theory](../week04/day03/01-s3-storage-classes.md)): 아카이브(archive) 계열 스토리지 클래스를 가리키는 표현으로 자주 쓰임.
  - 핵심: 저장 비용↓ ↔ 복구 시간/복구 비용/제약↑
  - 함정: “즉시 복구” 요구가 있으면 무조건 Glacier는 오답 후보

## Resilience

- **SPOF**: 단일 장애 지점. 시험에서 제거(분산) 신호가 자주 나온다.
- **RPO / RTO** ([theory](../week02/day01/02-dr-strategies.md)): 데이터 손실 허용 시점(RPO) / 복구 시간(RTO). DR 전략 선택 기준.
- **Multi-AZ**: 가용성(자동 failover) 신호.
- **Read replica** ([theory](../week02/day04/01-rds-aurora-multi-az-vs-rr.md)): 읽기 확장(성능) 신호. “HA를 read replica로” 유도는 함정.
- **Failover routing** ([theory](../week02/day01/01-route53-routing.md)): 장애 감지(health) + 트래픽 전환(라우팅) 조합 신호.

## Performance

- **p95/p99**: 평균이 아니라 tail latency를 보라는 신호.
- **Throughput**: 처리량(req/s, MB/s, IOPS).
- **IOPS** ([theory](../week03/day03/01-ebs.md)): 스토리지 랜덤 I/O 성능 축(EBS 튜닝 문제의 핵심).
- **Cache key** ([theory](../week03/day02/01-cloudfront.md)): CloudFront 캐시 히트율을 좌우(쿠키/헤더/쿼리 포함 여부가 함정 포인트).
- **TTL / Invalidation** ([theory](../week03/day02/01-cloudfront.md)): 신선도 vs 비용/운영 트레이드오프.
- **Anycast** ([theory](../week03/day02/02-global-accelerator.md)): Global Accelerator의 핵심 힌트(캐시가 아니라 경로 최적화).

## Cost

- **Cost allocation tags** ([theory](../week04/day01/03-cost-allocation-tags.md)): 팀/프로젝트별 비용 가시화(태그 활성화/표준화가 전제).
- **Budgets vs Cost Explorer** ([theory](../week04/day01/01-cost-explorer.md), [theory](../week04/day01/02-budgets.md)): 알림/통제(Budgets) vs 분석/분해(Cost Explorer).
- **Data transfer / NAT cost** ([theory](../week04/day04/README.md)): “숨은 비용 드라이버”로 출제 빈도가 높다.
- **RI / Savings Plans / Spot** ([theory](../week04/day02/01-ec2-purchase-options.md)): 예측 가능/중단 허용/스파이크 신호로 고른다.
