# 스토리지 복원력: S3/EBS/EFS + 백업

## 소개 (이게 뭔가요?)

- 스토리지 문제는 “장애”보다 “실수(삭제/덮어쓰기)”로 먼저 터지는 경우가 많다.
- S3의 Versioning/Replication과 EBS snapshot은 시험에서 ‘복구’ 힌트를 가장 자주 만든다.

## 고객 사례 (스토리)

운영 중인 서비스에서 사고가 났다. 배치 작업이 로그 파일을 정리하다가, 중요한 객체까지 같이 지워버렸다. 다행히 서버는 멀쩡하지만 데이터가 사라졌다. “백업은 있나요?”라는 질문에, 팀은 “어… 어제 ZIP 떠둔 게 있긴 한데…” 정도였다. 데이터가 하루만 날아가도 큰 손실인데, 담당자는 한 명이라 매번 수동 백업을 챙기기도 어렵다. 게다가 신규 고객은 “다른 리전에도 복제해달라(규제/DR)”는 요구까지 덧붙였다.

이때 S3 Versioning은 ‘실수 복구’의 기본기다. 삭제가 곧바로 사라지는 게 아니라 delete marker가 붙는 모델이라, 이전 버전을 되돌릴 수 있다. 그리고 “다른 곳에도 같은 데이터가 있어야 한다”는 요구가 나오면 SRR/CRR 같은 Replication이 후보가 된다(전제 조건이 Versioning ON이라는 함정도 같이 따라온다). 블록 스토리지(EBS) 쪽은 snapshot이 백업/복구의 기본 단위로 등장한다. 결국 스토리지는 “정말 재해(리전 장애)까지 대비하나?” vs “실수/운영 복구가 목적이냐?”를 먼저 가르고, 그에 맞는 기능을 고르면 된다.

지금 요구가 “실수 복구”에 가깝다면, 복제보다 먼저 켜야 하는 기능은 무엇일까요?

## Impact 범위 (어디에 영향을 주나?)

- Reliability: 삭제/덮어쓰기/운영 실수 복구(롤백) 메커니즘에 직결
- Operations: 수동 백업을 줄이고 복구 절차를 표준화
- Cost: Replication/장기 보관(아카이브)은 비용 구조가 달라진다

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-2-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-2.2%20Backup%20%26%20DR-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: S3](https://img.shields.io/badge/Service-S3-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: EBS](https://img.shields.io/badge/Service-EBS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: EFS](https://img.shields.io/badge/Service-EFS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 2: Design Resilient Architectures
- Task focus:
  - 2.2 Highly available and/or fault-tolerant architectures

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- “accidental deletion/overwrite”가 보이면 S3 Versioning, “다른 곳에도 복제”가 보이면 Replication을 먼저 떠올리면 된다.

## Core Concepts

- “실수 복구”와 “재해 복구(DR)”는 다르다
  - 실수 복구: 덮어쓰기/삭제/운영 실수 -> Versioning/PITR 같은 롤백 기능
  - DR: 리전/계정 수준 장애/규제 -> Replication/백업/다중 리전 설계
- S3에서 자주 나오는 규칙 1개
  - Replication(SRR/CRR)의 전제조건: 소스/대상 버킷 모두 Versioning ON

![S3 versioning and replication prerequisites](../../assets/core/s3-versioning-replication.svg)

## Service Chapters (서비스별로 읽기)

- [S3 Versioning: “실수 복구”의 기본기](theory/10-s3-versioning.md)
- [S3 Replication (SRR/CRR): 데이터 복제 요구 대응](theory/20-s3-replication.md)
- [EBS Snapshot (개념)](theory/30-ebs-snapshot.md)

> 스토리지는 “실수 복구(Versioning)”와 “DR/규제(Replication)”를 분리해서 읽으면 선택이 빨라진다.

## Exam Traps

- 복제를 원하는데 versioning을 언급하지 않는 답안
- 단일 버킷에만 의존하는 DR(요구사항이 리전 장애라면 추가 설계 필요)

## TL;DR (한 줄 정리)

- “실수 복구”면 **S3 Versioning**, “원격/규제/리전 DR”이면 **SRR/CRR(+ Versioning 전제)**, 블록 스토리지는 **EBS snapshot**이 기본이다.
