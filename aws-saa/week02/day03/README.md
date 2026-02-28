# Day 03 - Storage resilience (Resilience: Storage backup/replication)

![고객 사례 삽화 - S3 Versioning 복구](../../assets/scenario_image/w2d3s1.png)

## Outcomes

- S3 versioning이 “실수/삭제 복구”에 왜 유리한지 설명한다.
- S3 replication(SRR/CRR) 선택 기준(규제/DR/내구)을 설명한다.
- EBS snapshot이 어떤 용도(백업/복구/복제)로 쓰이는지 설명한다.

## Services In Scope

- S3 (versioning, replication)
- EBS snapshots (개념)
- (개념) EFS resilience

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [S3 Versioning (실수 복구의 기본기)](01-s3-versioning.md)
- [S3 Replication (SRR/CRR: 다른 곳에도 같은 데이터)](02-s3-replication.md)
- [EBS Snapshot (블록 스토리지 백업의 기본 단위)](03-ebs-snapshot.md)

## Core Concepts

- “실수 복구”와 “재해 복구(DR)”는 다르다
  - 실수 복구: 덮어쓰기/삭제/운영 실수 -> Versioning/PITR 같은 롤백 기능
  - DR: 리전/계정 수준 장애/규제 -> Replication/백업/다중 리전 설계
- S3에서 자주 나오는 규칙 1개
  - Replication(SRR/CRR)의 전제조건: 소스/대상 버킷 모두 Versioning ON

![S3 versioning and replication prerequisites](../../assets/core/s3-versioning-replication.svg)

## Exam Traps (확장)

- 복제를 원하는데 versioning을 언급하지 않는 답안
- 단일 버킷에만 의존하는 DR(요구사항이 리전 장애라면 추가 설계 필요)
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- “실수로 삭제/덮어쓰기” 방지를 위해 S3에서 어떤 기능이 정답 후보인가?
- “다른 버킷/리전에 복제”가 요구되면 어떤 설정이 필수인가?
- 백업은 RPO/RTO 요구와 어떤 식으로 연결되는가?

## TL;DR (한 줄 정리)

- “실수 복구”면 **S3 Versioning**, “원격/규제/리전 DR”이면 **SRR/CRR(+ Versioning 전제)**, 블록 스토리지는 **EBS snapshot**이 기본이다.
