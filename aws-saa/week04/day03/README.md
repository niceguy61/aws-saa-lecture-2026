# Day 03 - S3 storage classes + lifecycle patterns (S3 비용 최적화: 클래스/라이프사이클)

![고객 사례 삽화 - S3 비용 최적화(클래스/라이프사이클)](../../assets/scenario_image/w4d3s0.png)

## Outcomes

- S3 스토리지 클래스 선택을 “액세스 패턴/복구 시간/비용”으로 설명한다.
- Lifecycle rule의 역할(전환/만료)을 설명하고, prefix 기반 분리 설계를 할 수 있다.
- Intelligent-Tiering을 고려해야 하는 신호(예측 어려움)를 설명한다.

## Services In Scope

- S3 storage classes (개념)
- S3 lifecycle, Intelligent-Tiering

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [S3 스토리지 클래스: 액세스/복구 요구로 고른다](01-s3-storage-classes.md)
- [S3 라이프사이클: 전환/만료를 자동화한다](02-s3-lifecycle.md)
- [Intelligent-Tiering: 예측이 어려울 때 자동 최적화](03-intelligent-tiering.md)

## Core Concepts

- 스토리지 비용 최적화는 “액세스 패턴 + 복구 요구”를 같이 본다
  - 자주 접근: Standard
  - 가끔 접근: IA 계열
  - 거의 안 함: Glacier 계열(복구 시간/비용 트레이드오프)
- Lifecycle은 “자동 정책화”다(수동 이동은 운영비를 만든다)

![S3 클래스와 라이프사이클](../../assets/core/s3-storage-class-lifecycle.svg)

## Decision Rules (정답을 가르는 규칙 3개)

1. “장기 보관/거의 안 봄”이면 **Glacier 계열 + 라이프사이클**이 후보가 된다(복구 시간 확인).
2. “복구가 즉시 필요”면 **무조건 Glacier**는 오답 후보가 된다.
3. “패턴 예측 어려움/자동 최적화”면 **Intelligent-Tiering**이 신호다.

## Smell Test (레드 플래그 3~5)

- “모든 데이터를 Glacier”로 옮기는 답(복구 시간/요청/복구 비용 무시)
- 라이프사이클을 “전체 데이터에 일괄 적용”하는 답(핫 데이터까지 전환)
- 복구 요구를 읽지 않고 ‘가장 싼 클래스’만 고르는 답

## TL;DR (한 줄 정리)

- S3 비용 최적화는 **액세스 패턴 + 복구 시간**을 먼저 확인하고, **라이프사이클/티어링**으로 정책화한다.

## Exam-Style Design Questions

- “장기 보관 + 가끔 조회” 요구에서 어떤 클래스가 후보가 되는가?
- “예측하기 어려운 액세스 패턴” 문장이 있으면 어떤 선택지가 후보가 되는가?
- prefix 기반으로 lifecycle을 나누는 이유는?
