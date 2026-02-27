# Day 02 - Theory Index (Resilience: ELB + Auto Scaling)

> 이 문서는 Day 이론 “인덱스”다. 서비스별 theory는 Day 폴더 바로 아래 `01-*.md`에서 각각 읽는다.

## 소개 (이게 뭔가요?)

- ELB는 “앞단에서 건강한 서버로만 보내는 관제탑”이고, Auto Scaling은 “서버를 자동으로 늘리고(스케일) 갈아끼우는(치유) 엔진”이다.
- 헬스체크는 이 둘을 연결하는 트리거다(정상/비정상 판단의 기준).

## 고객 사례 (스토리)

프로모션 날이 다가오자 팀이 긴장했다. 평소에는 문제 없는데, 이벤트 시작 10분 만에 응답이 느려지고 502가 튀었다. 개발자는 한 명이 야근하면서 인스턴스를 수동으로 늘렸고, 이벤트가 끝나면 다시 줄였다. 문제는 “늘리는 타이밍”도 어렵고, “잘못 늘린 인스턴스”가 섞이면 오히려 장애가 커진다는 것이다. 운영팀은 “장애가 나면 자동으로 빼고, 트래픽이 늘면 자동으로 늘리는 구조”를 요구한다.

이때 생각을 바꾸면 편해진다. 사용자는 한 곳으로 들어오게 만들고(Load Balancer), 뒤에서는 정상 서버만 받게 한다(Target group + health check). 인스턴스는 ‘개별’이 아니라 ‘그룹’으로 관리한다(Auto Scaling group). 헬스체크가 실패하면 타겟에서 제외하고, 계속 실패하면 인스턴스를 교체한다. 그리고 ALB/NLB 선택은 “HTTP 라우팅 규칙이 필요하냐(ALB)” vs “TCP/초고성능/고정 IP 같은 신호가 있냐(NLB)”로 갈린다. 수동 스케일은 ‘사람이 스위치를 누르는’ 방식이라면, ASG+ELB는 ‘온도 조절기’처럼 자동으로 균형을 맞춘다.

지금 요구가 “트래픽 스파이크 + 자동 복구”라면, 가장 먼저 어떤 조합을 떠올려야 할까요?

## Impact 범위 (어디에 영향을 주나?)

- Reliability: 자가 치유(health check 기반 제외/교체)와 HA 구성의 핵심
- Performance: L7/L4 선택(ALB/NLB)이 지연/처리량에 영향을 줌
- Operations: 수동 개입을 줄이고 표준화된 복구 루틴을 만든다

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-2-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-2.1%20Scale%20%26%20decouple-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: ELB](https://img.shields.io/badge/Service-ELB-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Auto%20Scaling](https://img.shields.io/badge/Service-Auto%20Scaling-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: EC2](https://img.shields.io/badge/Service-EC2-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 2: Design Resilient Architectures
- Task focus:
  - 2.1 Scalable and loosely coupled architectures
  - 2.2 Highly available and/or fault-tolerant architectures

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- “헬스체크 실패 → 제외/교체” 흐름을 이해하면, ALB/NLB/ASG 문제에서 정답이 빨라진다.

## Core Concepts

- “가용성”은 대개 한 서비스로 끝나지 않는다
  - 진입점: Load Balancer (헬스체크/라우팅)
  - 복구/확장: Auto Scaling (교체/스케일)
  - 상태 분리: stateless + 외부 저장소(DB/캐시)
- 시험에서 가장 많이 섞이는 축 2개
  - L7 기능 필요 여부(라우팅 규칙/HTTP): ALB
  - L4/정적 IP/초고성능: NLB

![ALB vs NLB and ASG self-healing](../../assets/core/lb-and-asg-resilience.svg)

## Service Theories (서비스별로 읽기)

- [ALB vs NLB (L7 라우팅 vs L4 성능/프로토콜)](01-alb-vs-nlb.md)
- [Auto Scaling (확장 + 자가 치유)](02-auto-scaling.md)

> 로드밸런서 선택과 자가 치유(ASG)는 서로 다른 축이라, 챕터로 나눠놓으면 복습이 쉬워진다.

## Exam Traps

- “L7 기능이 필요한데 NLB를 선택”하는 오답
- “단일 AZ ASG”로 HA를 달성할 수 있다고 착각
- 보안 그룹/타겟 그룹 포트 불일치로 헬스체크 실패(실습에서도 자주)

## TL;DR (한 줄 정리)

- “스파이크 + 자동 복구”는 **ELB + ASG + health check**로 풀고, 라우팅/프로토콜 신호로 **ALB vs NLB**를 고른다.
