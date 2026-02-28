# AWS Services (SAA-C03) — 서비스 목록 + 한 줄 설명 + 공식 링크

이 문서는 **AWS 공식 SAA-C03 자료의 “범위 내 AWS 서비스 및 기능” 목록**을 기준으로, 서비스별로 “시험 관점 한 줄”과 공식 문서 링크를 붙여둔 인덱스다.

- Source of truth:
  - In-scope AWS services & features (AWS Certification): https://docs.aws.amazon.com/ko_kr/aws-certification/latest/examguides/saa-03-in-scope-services.html
  - Exam guide PDF 링크는 `exam-guide.md` 참고

> 목록/분류는 변경될 수 있다. 실제 강의 노트의 theory 링크는 이 레포의 구성에 따라 일부만 제공한다.

## Analytics

- Amazon Athena — S3에 대해 서버리스 SQL 쿼리. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Athena))
- AWS Data Pipeline — (레거시) 데이터 워크플로/이동 오케스트레이션. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Data%20Pipeline))
- Amazon EMR — 관리형 Hadoop/Spark 빅데이터 처리. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20EMR))
- AWS Glue — 서버리스 ETL + 데이터 카탈로그. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Glue))
- Amazon Kinesis — 스트리밍 데이터 수집/처리. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Kinesis))
- Amazon OpenSearch Service — 관리형 검색/로그 분석. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20OpenSearch%20Service))
- Amazon QuickSight — BI 대시보드/시각화. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20QuickSight))
- Amazon Redshift — 데이터 웨어하우스. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Redshift))

## Application Integration

- Amazon EventBridge — 이벤트 버스/라우팅. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20EventBridge))
- Amazon MQ — 관리형 메시지 브로커(ActiveMQ/RabbitMQ). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20MQ))
- Amazon Simple Notification Service (Amazon SNS) — pub/sub 알림/팬아웃. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20SNS))
- Amazon Simple Queue Service (Amazon SQS) — 메시지 큐로 decouple. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20SQS))
- AWS Step Functions — 워크플로 오케스트레이션. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Step%20Functions))

## Blockchain

- Amazon Managed Blockchain — 관리형 블록체인 네트워크. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Managed%20Blockchain))

## Compute

- AWS Batch — 배치 작업 큐/스케줄링. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Batch))
- Amazon Elastic Compute Cloud (Amazon EC2) — 가상 서버 컴퓨트. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20EC2), [Theory](../week03/day01/01-ec2.md))
- Amazon EC2 Auto Scaling — 스케일아웃 + 자가 치유. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20EC2%20Auto%20Scaling), [Theory](../week02/day02/02-auto-scaling.md))
- AWS Elastic Beanstalk — 애플리케이션 배포/운영 자동화(PaaS). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Elastic%20Beanstalk))
- AWS Lambda — 서버리스 함수 실행. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Lambda))
- AWS Outposts — 온프렘 확장형 AWS(하이브리드). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Outposts))
- AWS Serverless Application Repository — 서버리스 앱 템플릿/배포. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Serverless%20Application%20Repository))
- AWS Systems Manager — 운영 자동화/패치/세션/인벤토리. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Systems%20Manager))

## Containers

- Amazon Elastic Container Registry (Amazon ECR) — 컨테이너 이미지 레지스트리. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20ECR))
- Amazon Elastic Container Service (Amazon ECS) — 컨테이너 오케스트레이션. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20ECS))
- Amazon Elastic Kubernetes Service (Amazon EKS) — 관리형 Kubernetes. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20EKS))
- AWS Fargate — 서버리스 컨테이너 실행(ECS/EKS). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Fargate))

## Customer Engagement

- Amazon Connect — 클라우드 컨택센터. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Connect))
- Amazon Simple Email Service (Amazon SES) — 이메일 발송. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20SES))

## Database

- Amazon Aurora — RDS 호환 고성능 DB(읽기 확장/아키텍처가 포인트). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Aurora), [Theory](../week03/day04/03-aurora.md))
- Amazon DocumentDB (with MongoDB compatibility) — 관리형 Document DB. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20DocumentDB))
- Amazon DynamoDB — 관리형 NoSQL(파티션/인덱스가 포인트). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20DynamoDB), [Theory](../week03/day04/01-dynamodb.md))
- Amazon ElastiCache — 캐시(반복 읽기 핫패스). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20ElastiCache), [Theory](../week03/day04/02-elasticache.md))
- Amazon Keyspaces (for Apache Cassandra) — 관리형 Cassandra. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Keyspaces))
- Amazon Neptune — 그래프 DB. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Neptune))
- Amazon Relational Database Service (Amazon RDS) — 관리형 관계형 DB(HA vs 확장 구분). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20RDS), [Theory](../week02/day04/01-rds-aurora-multi-az-vs-rr.md))
- Amazon Redshift — 데이터 웨어하우스. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Redshift))

## Developer Tools

- AWS Command Line Interface (AWS CLI) — AWS CLI. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CLI))
- AWS Cloud Development Kit (AWS CDK) — IaC(코드로 인프라). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CDK))
- AWS CloudShell — 브라우저 내 쉘. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CloudShell))
- AWS CodeArtifact — 패키지 저장소. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CodeArtifact))
- AWS CodeBuild — CI 빌드. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CodeBuild))
- AWS CodeCommit — Git 리포지토리. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CodeCommit))
- AWS CodeDeploy — 배포 자동화. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CodeDeploy))
- AWS CodePipeline — CI/CD 파이프라인. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CodePipeline))
- AWS CodeStar — 프로젝트 템플릿/통합. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CodeStar))
- AWS Tools and SDKs — SDK/도구 모음. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20SDK))

## Frontend Web and Mobile

- AWS Amplify — 프론트엔드/풀스택 호스팅/백엔드 구성. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Amplify))
- Amazon API Gateway — API 프록시/관리(인증/쓰로틀링). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20API%20Gateway))
- AWS AppSync — GraphQL API. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20AppSync))
- AWS Device Farm — 모바일 테스트. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Device%20Farm))
- Amazon Cognito — 사용자 인증/연동. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Cognito))

## Management and Governance

- AWS Auto Scaling — 여러 서비스의 오토스케일링 통합. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Auto%20Scaling))
- AWS CloudFormation — IaC(템플릿). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CloudFormation))
- AWS CloudTrail — API 호출 감사(누가 무엇을 했나). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CloudTrail), [Theory](../week01/day03/01-cloudtrail.md))
- Amazon CloudWatch — 지표/로그/알람(관측). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20CloudWatch), [Theory](../week03/day01/02-cloudwatch.md))
- AWS Compute Optimizer — 리소스 추천. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Compute%20Optimizer))
- AWS Config — 구성/준수(리소스 상태). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Config), [Theory](../week01/day03/02-config.md))
- AWS Control Tower — 멀티 계정 랜딩존. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Control%20Tower))
- AWS Cost Explorer — 비용 분석/분해. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Cost%20Explorer), [Theory](../week04/day01/01-cost-explorer.md))
- AWS License Manager — 라이선스 관리. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20License%20Manager))
- AWS Managed Services — 운영 대행(관리형). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Managed%20Services))
- AWS Organizations — 멀티계정 거버넌스 + SCP. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Organizations), [Theory](../week01/day01/03-organizations-scp.md))
- AWS Resource Access Manager (AWS RAM) — 리소스 공유(교차 계정). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Resource%20Access%20Manager))
- AWS Service Catalog — 표준화된 프로비저닝. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Service%20Catalog))
- AWS Trusted Advisor — 베스트 프랙티스 체크. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Trusted%20Advisor))
- AWS Well-Architected Tool — WA 리뷰/워크로드 평가. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Well-Architected%20Tool))

## Machine Learning

- Amazon Comprehend — NLP(감정/엔티티). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Comprehend))
- Amazon Kendra — 엔터프라이즈 검색. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Kendra))
- Amazon Lex — 챗봇. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Lex))
- Amazon Polly — TTS. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Polly))
- Amazon Rekognition — 이미지/비디오 분석. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Rekognition))
- Amazon SageMaker — ML 모델 빌드/학습/배포. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20SageMaker))
- Amazon Textract — 문서 OCR/추출. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Textract))
- Amazon Transcribe — STT. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Transcribe))
- Amazon Translate — 번역. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Translate))

## Migration and Transfer

- AWS Application Discovery Service — 마이그레이션 발견/인벤토리. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Application%20Discovery%20Service))
- AWS Application Migration Service — 서버 마이그레이션(MGN). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Application%20Migration%20Service))
- AWS DataSync — 대용량 데이터 전송/동기화. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20DataSync))
- AWS Database Migration Service (AWS DMS) — DB 마이그레이션. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Database%20Migration%20Service))
- AWS Migration Hub — 마이그레이션 추적/허브. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Migration%20Hub))
- AWS Snow Family — 오프라인/엣지 데이터 전송. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Snow%20Family))
- AWS Transfer Family — SFTP/FTPS/FTP 관리형. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Transfer%20Family))

## Networking and Content Delivery

- Amazon CloudFront — CDN/캐시/엣지. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20CloudFront), [Theory](../week03/day02/01-cloudfront.md))
- AWS Direct Connect — 전용 회선. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Direct%20Connect))
- Elastic Load Balancing (ELB) — 로드 밸런서(ALB/NLB). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Elastic%20Load%20Balancing), [Theory](../week02/day02/01-alb-vs-nlb.md))
- AWS Global Accelerator — Anycast 기반 경로 최적화. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Global%20Accelerator), [Theory](../week03/day02/02-global-accelerator.md))
- AWS PrivateLink — VPC 간 서비스 노출(인터페이스 엔드포인트). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20PrivateLink), [Theory](../week01/day04/02-vpc-endpoints-privatelink.md))
- Amazon Route 53 — DNS + 라우팅 정책/헬스체크. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Route%2053), [Theory](../week02/day01/01-route53-routing.md))
- Amazon Virtual Private Cloud (Amazon VPC) — 네트워크 격리 경계. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20VPC))
- AWS VPN — VPN 연결(사이트투사이트/클라이언트). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20VPN))

## Security, Identity, and Compliance

- AWS Artifact — 컴플라이언스 보고서. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Artifact))
- AWS Audit Manager — 감사 증적 수집/평가. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Audit%20Manager))
- AWS Certificate Manager (ACM) — TLS 인증서. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Certificate%20Manager))
- AWS CloudHSM — 전용 HSM. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20CloudHSM))
- Amazon Cognito — 사용자 인증/연동. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Cognito))
- Amazon Detective — 조사/상관분석(보안). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Detective))
- AWS Directory Service — 관리형 디렉터리(AD). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Directory%20Service))
- AWS Firewall Manager — 방화벽/WAF 정책 관리. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Firewall%20Manager))
- Amazon GuardDuty — 위협 탐지(findings). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20GuardDuty), [Theory](../week01/day03/03-detection-services.md))
- AWS IAM Identity Center — SSO(구: AWS SSO). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20IAM%20Identity%20Center), [Theory](../week01/day01/04-identity-center.md))
- AWS Identity and Access Management (IAM) — 접근 제어(정책/role). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Identity%20and%20Access%20Management), [Theory](../week01/day01/01-iam.md))
- AWS Key Management Service (AWS KMS) — 키 관리/암호화 API(정책이 관문). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Key%20Management%20Service), [Theory](../week01/day02/01-kms.md))
- Amazon Macie — S3 민감 정보 탐지. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20Macie))
- AWS Network Firewall — VPC 네트워크 방화벽. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Network%20Firewall))
- AWS Resource Access Manager (AWS RAM) — 리소스 공유(교차 계정). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Resource%20Access%20Manager))
- AWS Secrets Manager — 시크릿 저장/회전. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Secrets%20Manager), [Theory](../week01/day02/02-secrets-vs-parameter-store.md))
- AWS Security Hub — 보안 결과 집계. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Security%20Hub), [Theory](../week01/day03/03-detection-services.md))
- AWS Shield — DDoS 보호. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Shield))
- AWS Single Sign-On — (구 명칭) IAM Identity Center. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Single%20Sign-On))
- AWS WAF — L7 웹 방화벽. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20WAF))

## Storage

- AWS Backup — 백업 오케스트레이션. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Backup))
- Amazon Elastic Block Store (Amazon EBS) — 블록 스토리지(IOPS/처리량 튜닝). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20EBS), [Theory](../week03/day03/01-ebs.md))
- Amazon Elastic File System (Amazon EFS) — 공유 파일시스템. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20EFS), [Theory](../week03/day03/02-efs.md))
- Amazon FSx — 관리형 파일시스템(Windows/Lustre/ONTAP/OpenZFS). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20FSx))
- Amazon Simple Storage Service (Amazon S3) — 객체 스토리지(보안/버저닝/라이프사이클). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20S3), [Theory](../week02/day03/01-s3-versioning.md))
- Amazon S3 Glacier — S3 아카이브 계열(복구 시간/비용 트레이드오프). ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20S3%20Glacier), [Theory](../week04/day03/01-s3-storage-classes.md))
- AWS Storage Gateway — 하이브리드 스토리지 게이트웨이. ([Docs](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Storage%20Gateway))
