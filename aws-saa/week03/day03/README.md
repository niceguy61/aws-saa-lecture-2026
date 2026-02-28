# Day 03 - Storage performance (스토리지 성능: EBS vs EFS)

![고객 사례 삽화 - 스토리지 성능 축 맞추기](../../assets/scenario_image/w3d3s0.png)

## Outcomes

- EBS 볼륨 타입(gp3/io1/io2)의 핵심 축(IOPS/throughput)을 설명한다.
- EBS QueueLength 같은 지표로 “디스크 병목”을 의심할 수 있다.
- EFS가 적합한 케이스(공유 파일 시스템)와 성능 모드(개념)를 설명한다.

## Services In Scope

- EBS (gp3 tuning 개념)
- EFS (performance/throughput mode 개념)
- CloudWatch 지표 관점

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [EBS: gp3/io2로 IOPS/처리량을 맞춘다](01-ebs.md)
- [EFS: 여러 인스턴스가 공유하는 파일시스템](02-efs.md)

## Core Concepts

- 시험 신호(패턴 매칭)
  - “높은/일관된 IOPS” → EBS io2/io1
  - “용량은 그대로, 성능만 올리고 싶다” → EBS gp3
  - “여러 인스턴스가 같은 파일을 공유한다” → EFS

![스토리지 성능 축](../../assets/core/storage-performance-axes.svg)

## Exam Traps (확장)

- “공유 파일시스템”인데 EBS를 고르는 선택지(공유 모델이 다르다).
- “IOPS 병목”인데 인스턴스만 키우는 선택지(스토리지 축 튜닝이 정답일 수 있다).
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- “IOPS가 병목” 문장에 어떤 선택지가 매핑되는가?
- “공유 파일 시스템” 요구가 있을 때 EBS가 아니라 EFS가 되는 이유는?
- gp3의 장점(비용/성능 분리)을 설명할 수 있는가?

## TL;DR (한 줄 정리)

- 스토리지는 **용량이 아니라 IOPS/처리량/공유**가 신호다: “일관 IOPS”면 io2, “튜닝”이면 gp3, “공유 파일”이면 EFS.
