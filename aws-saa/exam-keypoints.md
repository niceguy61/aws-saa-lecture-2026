# AWS SAA Exam Keypoints (Must-Know)

시험에서 자주 “정답을 가르는 한 줄”로 쓰이는 제한/선택 기준/함정을 모아둔 치트시트다.

- 연계/고급 함정(Combo / Similar-but-different)은 `aws-saa/exam-trap-bank.md`도 같이 본다.

## Hard Limits (암기 가치 높은 것)

### Lambda

- Max execution time: 15 minutes
  - Signal: “15분 이상 실행”, “장시간 배치”, “긴 ETL” 같은 문장
  - Better answers: Step Functions(오케스트레이션) + ECS/Fargate/Batch(긴 실행), 또는 이벤트 기반 분할
- Concurrency(개념): 동시에 많이 뜨면 throttling 가능
  - Signal: “갑자기 호출 폭증”, “throttling”
  - Better answers: reserved concurrency, SQS로 버퍼링, 비동기 처리

### SQS (Standard/FIFO)

- 메시지 크기: 256 KB
  - Signal: “큰 페이로드”
  - Better answers: S3에 payload 저장 + SQS에는 pointer(키)만
- 메시지 보관(개념): 최대 14일(설정)
  - Signal: “오래 큐에 쌓아둬야”
  - Better answers: 보관 요구가 강하면 다른 저장소(S3/DB)와 조합
- Delivery(개념): 적어도 한 번 전달(at-least-once)로 중복 가능
  - Signal: “중복 처리”
  - Better answers: consumer idempotency + DLQ

### S3

- 단일 객체 최대 크기: 5 TB(멀티파트 업로드 필요)
  - Signal: “수 TB 대용량 업로드”
  - Better answers: multipart upload

## Service Selection Pivots (시험에서 자주 헷갈리는 비교)

### VPC Endpoints

- Gateway endpoints: S3, DynamoDB
- Interface endpoints(PrivateLink): 그 외 대부분의 AWS 서비스 접근 패턴
  - Signal: “프라이빗 서브넷에서 AWS 서비스에 사설로 접근”, “NAT 비용/보안”
  - Trap: “S3를 보안 그룹으로 제어” (S3는 SG 대상 아님)

### ALB vs NLB

- ALB(L7): host/path 라우팅, HTTP/HTTPS 애플리케이션 트래픽
- NLB(L4): TCP/UDP, 고성능/저지연, (케이스에 따라) 고정 IP 요구
  - Signal: “path 기반 라우팅” -> ALB / “TCP, 극저지연” -> NLB

### RDS Multi-AZ vs Read Replica

- Multi-AZ: 가용성(자동 failover)
- Read replica: 읽기 확장(성능)
  - Trap: “Read replica로 HA 달성”으로 유도하는 선택지

### CloudTrail vs Config

- CloudTrail: API 호출/행위(누가 무엇을 했나)
- Config: 구성 상태/변경/준수(리소스가 어떤 상태인가)

### Secrets Manager vs SSM Parameter Store

- Secrets Manager: rotation/시크릿 운영 기능 요구 시 강한 정답 후보
- Parameter Store(SecureString): 단순 구성/파라미터 성격에 적합

### KMS: key policy vs IAM policy

- KMS는 key policy가 gate로 작동하는 문제가 많다.
  - Signal: “IAM에 Allow가 있는데도 AccessDenied”
  - Next check: key policy, grants, kms:Decrypt 권한 범위

### S3 Versioning/Replication

- Replication(SRR/CRR)은 보통 “소스/대상 버킷 모두 versioning on”이 전제
  - Trap: versioning 없이 복제만 설정하는 선택지

### NAT vs S3 Gateway Endpoint (Cost)

- 프라이빗 서브넷 -> S3 접근이 많으면 NAT 비용이 함정이 될 수 있음
- S3 Gateway endpoint는 NAT 의존을 줄이는 대표 답안

## Common Exam Traps (오답 제거 규칙)

- “키 공유”가 답처럼 보이면 의심: 대부분 STS AssumeRole이 정답 후보
- “무조건 캐시/무조건 CloudFront”: 캐시 가능/일관성 요구/개인화 여부가 관건
- “무조건 스케일업”: 병목이 CPU가 아닐 수 있다(IO/DB/네트워크)
- “모든 데이터를 Glacier”: 복구 시간/복구 비용 트레이드오프 무시 가능

## How To Maintain

- 숫자/쿼터는 변동될 수 있으니, 변경이 의심되면 공식 문서 기준으로 업데이트한다.
- 이 파일의 항목을 “특강 Day05” 비교표/함정 섹션에 역링크로 연결한다.
