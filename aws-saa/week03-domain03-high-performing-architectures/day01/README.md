# Day 01 - Performance thinking + EC2 sizing

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

- Theory: 2h 30m
- Hands-on (console): 1h 30m

## Exam-Style Design Questions

- “지속적인 고CPU” 워크로드에서 T 계열이 오답이 되는 신호는?
- “처리량”을 높여야 할 때 스케일업 vs 스케일아웃 중 어떤 선택이 자연스러운가?
- 성능 문제에서 CloudWatch로 무엇을 먼저 확인할까?

