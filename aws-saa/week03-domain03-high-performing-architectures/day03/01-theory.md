# Theory

## Exam Guide Mapping

- Domain: Domain 3: Design High-Performing Architectures
- Task focus:
  - 3.1 Determine high-performing and/or scalable storage solutions

## Deep Dive

### EBS: IOPS/Throughput이 핵심 축

- gp3: 성능(IOPS/throughput)과 용량을 분리해서 조정 가능(시험에서 장점으로 등장)
- io1/io2: 프로비저닝 IOPS 중심(요구 문장에 “높은 IOPS/일관성” 힌트가 있으면)
- 병목 신호
  - VolumeQueueLength 증가
  - 높은 Read/Write latency(환경에 따라)

```mermaid
flowchart LR
  EC2[EC2] --> EBS[(EBS Volume)]
  EBS --> CW[CloudWatch: Ops/Bytes/QueueLength]
```

### EFS: 공유 파일 시스템

- When to use
  - 여러 인스턴스가 같은 파일을 읽고/쓰는 요구(공유)
  - POSIX 파일 시스템 요구
- When not to use
  - 단일 인스턴스 로컬 고성능 디스크처럼 쓰려는 요구(요구에 따라 EBS/Instance store가 더 적절)
- 성능/처리량 모드(개념)
  - 워크로드에 따라 선택지가 문제로 출제될 수 있음(용어 수준)

## Exam Traps

- “공유 파일 시스템”인데 EBS를 고르는 오답(블록 스토리지는 공유 목적이 아님)
- “IOPS 병목”인데 스케일업만 고르는 오답(스토리지 성능 조정이 정답일 수 있음)

