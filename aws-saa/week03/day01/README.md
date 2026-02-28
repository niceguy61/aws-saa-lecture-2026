# Day 01 - Performance thinking + EC2 sizing (성능 생각법 + EC2 사이징)

![고객 사례 삽화 - 성능 진단 시작](../../assets/scenario_image/w3d1s0.png)

## Outcomes

- 성능 요구사항을 “지연시간/처리량/동시성/예측 가능성”으로 분해한다.
- EC2 인스턴스 패밀리 선택 기준(컴퓨트/메모리/네트워크/가속기)을 설명한다.
- burstable(T 계열)에서 “크레딧”이 문제로 이어지는 케이스를 식별한다.
- CloudWatch 지표를 보고 병목이 CPU인지(또는 다른 곳인지) 1차 판단한다.

## Services In Scope

- EC2 (instance families, burstable basics)
- CloudWatch (CPUUtilization, CPUCreditBalance 등 지표 관점)
- (개념) Placement/ENA/EBS-optimized

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [EC2 인스턴스 패밀리 선택 + Burstable(T) 함정](01-ec2.md)
- [CloudWatch로 성능 병목 1차 진단하기](02-cloudwatch.md)

## Core Concepts

- 지표로 번역
  - 지연시간(latency): p95/p99 (평균만 보면 함정)
  - 처리량(throughput): req/s, MB/s, IOPS
  - 동시성(concurrency): 동시 요청/동시 실행
  - 일관성(predictability): 스파이크 이후에도 유지되는가
- 병목은 4가지 축으로 수렴
  - CPU / 메모리 / 네트워크 / 스토리지 I/O

![성능 지표와 병목 축](../../assets/core/perf-metrics-and-bottlenecks.svg)

## Exam Traps (확장)

- 성능 문제 = 무조건 더 큰 인스턴스(scale up)로 끝내는 선택지.
- T 계열을 “지속 고부하” 워크로드에 쓰는 선택지(크레딧 소진/스로틀링).
- CPUUtilization 하나만 보고 결론 내리게 유도하는 선택지(추가 지표로 교차 확인).
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- “지속적인 고CPU” 워크로드에서 T 계열이 오답이 되는 신호는?
- “처리량”을 높여야 할 때 스케일업 vs 스케일아웃 중 어떤 선택이 자연스러운가?
- 성능 문제에서 CloudWatch로 무엇을 먼저 확인할까?

## TL;DR (한 줄 정리)

- 성능 문제는 먼저 **지표(p95/p99/처리량/동시성)로 번역**하고, **병목 축(CPU/메모리/네트워크/스토리지 I/O)**을 맞춘 뒤 서비스 선택으로 들어간다.
