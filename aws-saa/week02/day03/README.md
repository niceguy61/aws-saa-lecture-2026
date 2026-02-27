# Day 03 - Storage resilience (S3/EBS/EFS) + backup

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

## Exam-Style Design Questions

- “실수로 삭제/덮어쓰기” 방지를 위해 S3에서 어떤 기능이 정답 후보인가?
- “다른 버킷/리전에 복제”가 요구되면 어떤 설정이 필수인가?
- 백업은 RPO/RTO 요구와 어떤 식으로 연결되는가?
