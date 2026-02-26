# Integrated Mini Lab (Console): S3 Lifecycle + Intelligent-Tiering

## Goal

- S3 비용 최적화의 기본 패턴(라이프사이클/스토리지 클래스)을 콘솔에서 구성한다.
- “액세스 패턴에 따라 자동 전환” 설계를 설명한다.

## Prereqs

- S3 버킷/라이프사이클 규칙 생성 권한
- Region: 수업 기본 리전

## Cost Notes

- 라이프사이클 전환은 시간이 지나야 적용된다(실습 중 즉시 비용 절감이 보이진 않는다).

## Steps

### A) Console Steps

#### 1) S3 버킷 생성 + 샘플 오브젝트 업로드

1. 버킷 생성(예: `saa-week4-lifecycle-<랜덤>`)
2. 샘플 업로드
  - `logs/2026-01-01.log`
  - `app/releases/v1.zip`

#### 2) Lifecycle rule 생성(전환 + 만료)

1. 버킷 -> Management -> Lifecycle rules -> Create rule
2. Rule scope
  - Prefix로 범위 제한: `logs/`
3. Transitions(예시)
  - 30일 후: Standard-IA
  - 90일 후: Glacier Instant Retrieval(또는 조직 정책에 맞는 Glacier 계열)
4. Expiration(예시)
  - 365일 후 만료(로그 정책에 맞게 조정)

#### 3) (옵션) Intelligent-Tiering 적용

1. `app/` 같은 “액세스 패턴이 예측 어려운” 데이터에 Intelligent-Tiering을 고려한다.
2. 동일 버킷에 규칙을 하나 더 만들거나, 업로드 시 스토리지 클래스를 Intelligent-Tiering으로 선택한다(조직 가이드에 맞게).

### B) Optional: CLI Equivalents (for validation/automation)

- `aws s3api put-bucket-lifecycle-configuration`로도 설정 가능(수업은 콘솔 기준).

## Validation Checklist

- prefix 범위(`logs/`)에만 lifecycle이 적용되도록 구성했다.
- 스토리지 클래스 선택을 “액세스 패턴/복구 시간/비용”으로 설명할 수 있다.

## Common Errors

- 모든 오브젝트에 전환 적용: 자주 접근하는 데이터까지 전환되어 성능/비용이 악화될 수 있다.
- Glacier 계열 선택 시 복구 시간/요금(요청/복구)을 고려하지 않음.

## Cleanup

1. Lifecycle rules 삭제(선택)
2. 오브젝트 삭제 후 버킷 삭제

