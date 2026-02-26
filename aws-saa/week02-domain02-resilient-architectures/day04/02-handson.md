# Hands-on Lab (Console): DynamoDB PITR로 실수 복구 시나리오

## Goal

- DynamoDB 테이블을 만들고 PITR을 활성화한다.
- 아이템을 변경/삭제한 뒤, “복원(restore)”로 새 테이블을 만들어 데이터를 복구하는 흐름을 확인한다.

## Prereqs

- DynamoDB 생성/설정 권한
- Region: 수업 기본 리전

## Cost Notes

- DynamoDB는 소량 사용 시 비용이 작지만, 불필요한 테이블은 삭제한다.

## Steps

### A) Console Steps

#### 1) 테이블 생성

1. DynamoDB -> Create table
2. Table name: `saa-week2-pitr`
3. Partition key: `pk` (String)
4. Capacity: On-demand(학습용)
5. Create

#### 2) 아이템 2개 추가

1. Explore items -> Create item
2. 예: `pk=order#1`, `status=PAID`
3. 예: `pk=order#2`, `status=PAID`

#### 3) PITR 활성화

1. Table -> Backups 탭
2. Point-in-time recovery 활성화(Enable)

#### 4) “실수” 재현(삭제/변경)

1. `order#2` 아이템 삭제
2. `order#1`의 status를 `CANCELED`로 변경

#### 5) Restore 수행(새 테이블로)

1. Backups/PITR에서 Restore 선택
2. 복원 시점: 실수 이전 시각으로 지정(콘솔 선택)
3. 새 테이블 이름: `saa-week2-pitr-restore`
4. Restore

#### 6) 복원 테이블에서 데이터 확인

1. `saa-week2-pitr-restore` 테이블에서 아이템 확인
2. 실수 이전 상태가 복구되었는지 확인

### B) Optional: CLI Equivalents (for validation/automation)

- 수업은 콘솔이 1순위.

## Validation Checklist

- PITR 활성화 상태를 확인했다.
- 삭제/변경 후, restore로 새 테이블에 이전 상태가 복구됨을 확인했다.

## Common Errors

- PITR 켠 직후 복원 시점 선택이 제한될 수 있다(일정 시간 필요할 수 있음).
- restore는 “원본 테이블 롤백”이 아니라 “새 테이블 생성” 흐름이 기본이다.

## Cleanup

1. `saa-week2-pitr` 테이블 삭제
2. `saa-week2-pitr-restore` 테이블 삭제

