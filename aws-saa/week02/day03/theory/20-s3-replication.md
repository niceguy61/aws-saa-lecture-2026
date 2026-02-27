# S3 Replication (SRR/CRR): 데이터 복제 요구 대응

- Preconditions(핵심)
  - 소스/대상 버킷 모두 versioning이 켜져 있어야 한다.
- When to use
  - DR/규제/리전 장애 대비/근접 복제 요구
- Traps
  - versioning을 안 켠 채 복제를 “설정했다”는 선택지

## Exam must-know (포인트 + Why + 대안)

- Key point: “리전 장애 대비/규제 준수/원격 복제” 문장이 있으면 CRR/SRR이 정답 후보가 된다.
- Why: 복제는 ‘데이터가 다른 곳에도 존재’해야 의미가 있으며, 버전 기반 복제가 전제라 versioning이 필수다.
- Alternative: 단순 백업 요구면(복제까지는 불필요) Backup/Restore(EBS snapshot, AWS Backup 등) 전략이 더 비용 효율적일 수 있다.

## TL;DR (한 줄 정리)

- “원격 복제/DR/규제” 신호가 있으면 SRR/CRR(+ Versioning 전제)부터 본다.

## Back

- `../01-theory.md`
