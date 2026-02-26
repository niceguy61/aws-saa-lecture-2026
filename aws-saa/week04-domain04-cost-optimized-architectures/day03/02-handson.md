# Hands-on Lab (Console): Prefix 기반 Lifecycle 2개 만들기 + Intelligent-Tiering

## Goal

- 한 버킷에서 prefix별로 서로 다른 lifecycle 정책을 만든다.
- Intelligent-Tiering을 적용하는 기준을 설명할 수 있다.

## Prereqs

- S3 버킷 생성/설정 권한
- Region: 수업 기본 리전

## Cost Notes

- 전환은 시간이 지나야 적용된다(실습 중 즉시 변화는 보이지 않을 수 있음).

## Steps

### A) Console Steps

#### 1) 버킷 생성 + 샘플 업로드

1. 버킷 생성: `saa-week4-storage-<랜덤>`
2. 업로드:
  - `logs/2026-01-01.log`
  - `logs/2026-01-02.log`
  - `app/releases/v1.zip`

#### 2) Lifecycle rule #1 (logs/)

1. Management -> Lifecycle rules -> Create
2. Scope: prefix `logs/`
3. Transition(예시):
  - 30일 후 Standard-IA
  - 90일 후 Glacier 계열(조직 정책에 맞게)
4. Expiration(예시):
  - 365일 후 만료

#### 3) Lifecycle rule #2 (app/ -> Intelligent-Tiering)

1. 새 rule 생성
2. Scope: prefix `app/`
3. Transition:
  - (조직 정책에 따라) Intelligent-Tiering으로 전환하거나 업로드 시 클래스로 선택

#### 4) (설명 체크) 왜 prefix로 나누나

- 로그/릴리즈/아카이브는 액세스/복구 요구가 다르다.

### B) Optional: CLI Equivalents (for validation/automation)

- 수업은 콘솔이 1순위.

## Validation Checklist

- prefix `logs/`와 `app/`에 서로 다른 정책을 적용했다.
- Intelligent-Tiering이 적합한 신호(예측 어려움)를 설명할 수 있다.

## Cleanup

1. lifecycle rules 삭제(선택)
2. 오브젝트 삭제 후 버킷 삭제

