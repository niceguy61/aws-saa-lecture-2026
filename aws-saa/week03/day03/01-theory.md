# Theory

## Exam Guide Mapping

- Domain: Domain 3: Design High-Performing Architectures
- Task focus:
  - 3.1 Determine high-performing and/or scalable storage solutions

## Core Concepts

- 스토리지 성능은 “용량”이 아니라 “IOPS/throughput/공유 여부”로 결정되는 경우가 많다.
- 시험에서 자주 나오는 신호
  - “IOPS/일관된 성능” -> io1/io2 후보
  - “용량은 그대로인데 성능만 튜닝” -> gp3 후보
  - “여러 인스턴스가 공유 파일” -> EFS 후보

![Storage performance axes](../../assets/core/storage-performance-axes.svg)

## Deep Dive

### EBS: IOPS/Throughput이 핵심 축

- gp3: 성능(IOPS/throughput)과 용량을 분리해서 조정 가능(시험에서 장점으로 등장)
- io1/io2: 프로비저닝 IOPS 중심(요구 문장에 “높은 IOPS/일관성” 힌트가 있으면)
- 병목 신호
  - VolumeQueueLength 증가
  - 높은 Read/Write latency(환경에 따라)

#### Exam must-know (포인트 + Why + 대안)

- Key point: “성능 병목” 문장에 IOPS/큐/지연 힌트가 있으면 ‘EBS 타입 선택/튜닝’이 정답 후보가 된다.
- Why: 블록 스토리지는 성능 축(IOPS/throughput)이 명확하고, 특히 gp3는 용량과 성능을 분리해 조정하는 장점이 있다.
- Alternative: “공유 파일 시스템” 요구면 EBS가 아니라 EFS로 간다(블록은 공유 목적이 아님).

```mermaid
flowchart LR
  EC2[EC2] --> EBS[EBS Volume]
  EBS --> CW[CloudWatch metrics]
```

### EFS: 공유 파일 시스템

- When to use
  - 여러 인스턴스가 같은 파일을 읽고/쓰는 요구(공유)
  - POSIX 파일 시스템 요구
- When not to use
  - 단일 인스턴스 로컬 고성능 디스크처럼 쓰려는 요구(요구에 따라 EBS/Instance store가 더 적절)
- 성능/처리량 모드(개념)
  - 워크로드에 따라 선택지가 문제로 출제될 수 있음(용어 수준)

#### Exam must-know (포인트 + Why + 대안)

- Key point: “여러 인스턴스가 같은 파일을 읽고/쓴다” 문장이 있으면 EFS가 정답 후보가 된다.
- Why: EFS는 NFS 기반 공유 파일시스템이고, EBS는 인스턴스에 붙는 블록 스토리지라 공유 모델이 다르다.
- Alternative: 단일 인스턴스의 초고성능 로컬 디스크 요구면 instance store/EBS(io2) 같은 선택지가 더 맞다.

## Exam Traps

- “공유 파일 시스템”인데 EBS를 고르는 오답(블록 스토리지는 공유 목적이 아님)
- “IOPS 병목”인데 스케일업만 고르는 오답(스토리지 성능 조정이 정답일 수 있음)
