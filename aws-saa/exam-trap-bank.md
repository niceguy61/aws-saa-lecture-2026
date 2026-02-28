# AWS SAA Exam Trap Bank (Combo / Similar-but-Different / Advanced)

기존의 짧은 확인 섹션 대신, “연계되는 서비스 조합”과 “비슷하지만 다른 것”, “고급 구현 포인트”까지 포함해서 Exam Trap을 확장한 모음집이다.

## How to use

- 문제의 **요구 조건(신호어)** 을 먼저 표시하고, 아래 함정에서 “오답 제거”를 한다.
- 한 문제에 **2개 이상의 서비스가 등장**하면 “단독 서비스 지식”보다 **연계 함정**이 정답을 가른다.
- “가장 비용 효율”, “운영 부담 최소”, “최소 변경”, “가장 안전”, “가장 빠른 복구” 같은 문장은 거의 항상 선택 기준을 고정한다.

## Identity & Security

- Trap: `AccessDenied` → 무조건 IAM Allow 추가
  - Signal: “Allow 했는데도 안 됨”
  - Next check: `ExplicitDeny`, `SCP`, `permissions boundary`, `KMS key policy`, (교차계정이면) `resource policy`
- Trap: “키 공유/장기 자격 증명 공유”가 정답처럼 보이게 유도
  - Signal: “외부/다른 계정이 접근해야”, “임시 접근”, “감사/회수”
  - Better answers: `STS AssumeRole` (+ trust policy), 필요 시 `ExternalId`
- Trap: `trust policy`(누가 Assume)와 `permission policy`(Assume 후 무엇을)를 섞어 쓰는 선택지
  - Signal: “role을 만들었는데 권한이…”, “assume은 되는데 액션이…”
  - Fix: trust에 principal/condition, permission에 action/resource
- Trap: `Organizations SCP`를 “권한 부여(Allow)”로 착각
  - Signal: “SCP로 허용했으니 됨”
  - Reality: SCP는 상한선(guardrail)이라 **IAM Allow가 별도로 필요**
- Trap: “S3를 security group으로 막자/열자”
  - Signal: “S3 접근 제어” + “SG”
  - Better answers: S3는 SG 대상 아님 → `bucket policy`, `VPC endpoint policy`, `CloudFront OAC/OAI`
- Trap: `KMS`는 IAM만 있으면 된다고 착각
  - Signal: “kms:Decrypt Allow가 있는데도 안 됨”
  - Next check: `key policy`(gate), `grants`, (S3/EBS/RDS 등) **서비스가 KMS를 호출하는 주체**가 누구인지

## Logging / Audit / Compliance (CloudTrail / Config / CloudWatch)

- Trap: `CloudTrail`로 “리소스 구성 상태/준수”를 해결하려는 선택지
  - Signal: “준수/구성 변경을 평가”, “drift”, “규정 위반 감지”
  - Better answers: `AWS Config` rules / conformance packs
- Trap: `Config`로 “누가 무엇을 했나(API 호출)”를 풀려는 선택지
  - Signal: “누가 변경했는지”, “API 호출 추적”
  - Better answers: `CloudTrail` (+ 조직/멀티리전 trail), 필요 시 `CloudWatch Logs` 연동
- Trap: `CloudWatch Logs`와 `CloudWatch Metrics/Alarm`의 역할 혼동
  - Signal: “로그에서 특정 패턴이 나오면 알림”
  - Better answers: logs → metric filter로 metric 생성 → alarm
- Trap: “모든 이벤트는 CloudTrail data events로 켜자” 같은 비용 무시 선택지
  - Signal: “S3 object-level”, “Lambda invoke-level” + “항상 켜자”
  - Reality: data events는 비용/볼륨이 커질 수 있어 **필요 범위만 선택**

## Networking (VPC / Endpoints / Routing / Load Balancing)

- Trap: `NACL`을 stateful처럼 다루는 선택지
  - Signal: “NACL에 인바운드만 열면 됨”
  - Reality: NACL은 stateless → **인/아웃 둘 다** + ephemeral port 고려
- Trap: “프라이빗 서브넷 → S3 접근”을 NAT로만 해결
  - Signal: “NAT 비용”, “S3 트래픽 많음”
  - Better answers: `S3 Gateway Endpoint` (S3/DynamoDB는 gateway), 그 외는 `Interface Endpoint(PrivateLink)`
- Trap: `Interface Endpoint`에 대해 “Gateway endpoint처럼” 이해
  - Signal: “보안그룹”, “private DNS”, “ENI”
  - Reality: interface는 ENI + SG, gateway는 라우트 테이블 기반
- Trap: `PrivateLink` vs `VPC Peering` 혼동
  - Signal: “서로 다른 VPC에서 서비스 접근”
  - Pivot: peering은 네트워크 연결(대칭, 라우팅/SG), PrivateLink는 **서비스 노출**(producer/consumer)
- Trap: `ALB` vs `NLB`를 “이름”으로만 외우는 선택지
  - Signal: “path/host 기반”, “HTTP 헤더”, “WebSocket”
  - Pivot: L7 기능/라우팅은 ALB, 초저지연 TCP/고정 IP 요구는 NLB가 자주 정답
- Trap: “글로벌 가속 = CloudFront”로 단정
  - Signal: “동적 트래픽”, “TCP/UDP”, “Anycast”, “헬스체크 기반 region failover”
  - Pivot: `Global Accelerator`는 L4/Anycast 가속, `CloudFront`는 CDN 캐시(정적/캐시 가능한 동적)
- Trap: Route 53 라우팅 정책을 “지리”로만 착각
  - Signal: “다중 리전”, “failover”, “latency”, “가중치”
  - Pivot: failover(헬스체크), latency(최저 지연), weighted(비율), geolocation(사용자 위치 기반)

## Edge / Content (CloudFront / S3 / WAF)

- Trap: `CloudFront` 캐시가 안 되는데 “CloudFront를 쓰면 자동으로 빨라진다”
  - Signal: “개인화”, “쿠키/헤더/쿼리스트링”
  - Pivot: cache key에 포함하면 히트율 급락 → **필요 최소만 포함** / signed cookie/url / origin cache-control
- Trap: “S3를 퍼블릭으로 열고 CloudFront로 가린다”는 선택지
  - Signal: “S3 static hosting” + “보안”
  - Better answers: S3는 private + `OAC/OAI`로 CloudFront만 접근
- Trap: 무조건 “invalidation”을 정답처럼 고르는 선택지
  - Signal: “콘텐츠 갱신”
  - Pivot: TTL/버전드 오브젝트(파일명 변경)로 해결이 더 깔끔한 경우가 많음(비용/규모)

## Storage (S3 / Lifecycle / Replication)

- Trap: `S3 replication`에서 versioning 전제를 놓치는 선택지
  - Signal: “CRR/SRR 설정”
  - Must: 소스/대상 **둘 다 versioning**
- Trap: “기존 객체도 자동으로 복제된다”로 유도
  - Signal: “이미 쌓인 데이터도 복제”
  - Reality: 기본은 신규 객체 중심 → 기존 객체 복제는 별도 옵션/배치 고려
- Trap: Glacier 계열/아카이브로 옮기면 “복구가 즉시”라고 착각
  - Signal: “아카이브 + 즉시 복구”
  - Pivot: retrieval time/fee, 최소 보관 기간(minimum storage duration)
- Trap: Intelligent-Tiering을 “무조건 최저 비용”으로 고정
  - Signal: “알아서 최적화”
  - Reality: 모니터링/오버헤드, access 패턴, archive tier 사용 조건을 확인
- Trap: Lifecycle로 자주 접근하는 데이터를 너무 빨리 cold tier로 내리는 선택지
  - Signal: “최근 데이터도 자주 조회”
  - Pivot: 조회 빈도/지연/요금(early deletion)까지 같이 본다

## Compute / Scaling (EC2 / ASG / Lambda)

- Trap: “스케일업”을 항상 정답처럼 고르는 선택지
  - Signal: “성능 문제”
  - Pivot: 병목이 CPU가 아닐 수 있다(DB/IO/네트워크) → scale out/캐시/비동기 고려
- Trap: `ASG`가 “멀티 AZ 고가용성”을 자동 보장한다고 착각
  - Signal: “HA 필요”
  - Reality: 멀티 AZ 배치/헬스체크/ELB 연동을 명시적으로 구성해야 한다는 힌트가 자주 나옴
- Trap: Lambda로 “15분 이상”을 풀게 만드는 선택지
  - Signal: “장시간 실행”, “긴 배치”
  - Better answers: `Step Functions` + `ECS/Fargate/Batch`
- Trap: `EC2 Spot`을 “무조건 가장 싸다”로만 선택
  - Signal: “중단 허용 여부”가 애매함
  - Pivot: interruption 허용/대체 가능하면 Spot, 아니면 RI/Savings Plans/On-Demand 혼합
- Trap: `EBS`와 `Instance Store` 혼동
  - Signal: “재부팅/종료 후에도 데이터 유지”
  - Pivot: Instance store는 휘발, 내구성/복구 요구면 EBS(+snapshot)

## Databases (RDS / Aurora / DynamoDB / ElastiCache)

- Trap: `RDS Read Replica`로 HA를 달성하는 선택지
  - Signal: “장애 시 자동 전환”
  - Better answers: `Multi-AZ`(자동 failover), read replica는 읽기 확장
- Trap: `DynamoDB`에서 “키 설계” 없이 성능을 해결하려는 선택지
  - Signal: “특정 파티션만 핫”, “throttling”
  - Better answers: 파티션 키 분산, GSI/적절한 access pattern, 필요 시 DAX
- Trap: `ElastiCache`를 “DB 대체/영구 저장”으로 쓰게 유도
  - Signal: “영구 저장”, “정합성”
  - Pivot: 캐시는 캐시(보조), 소스 오브 트루스는 DB
- Trap: Redis vs Memcached 선택 기준을 무시
  - Signal: “멀티 AZ”, “persistence”, “pub/sub”
  - Pivot: 기능/내구성 필요하면 Redis 쪽이 자주 정답
- Trap: `Aurora`를 “그냥 RDS”로 취급
  - Signal: “빠른 failover”, “읽기 확장”, “글로벌”
  - Pivot: Aurora replica/클러스터 아키텍처, 필요하면 `Aurora Global Database`

## Cost / Billing / Governance

- Trap: “비용 최적화”인데 데이터 전송/NAT/크로스 AZ 비용을 무시
  - Signal: “많은 트래픽”, “프라이빗 서브넷”, “S3 접근”
  - Pivot: endpoint/NAT, region/az 설계, 캐시 전략
- Trap: `Cost Explorer`와 `Budgets` 역할 혼동
  - Signal: “예산 초과 알림”
  - Pivot: 알림/액션은 `Budgets`, 분석/시각화는 `Cost Explorer`
- Trap: `Cost allocation tags`는 “태깅만 하면 바로 비용이 잡힌다”
  - Signal: “태그 기반 비용 추적”
  - Reality: 활성화(activate) + 반영 지연(리포트) 가능
