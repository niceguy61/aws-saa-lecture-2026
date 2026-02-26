# Hands-on Lab (Console): DynamoDB 테이블 + GSI로 액세스 패턴 추가

## Goal

- DynamoDB 테이블을 만들고(Partition key + Sort key), 예시 데이터를 넣는다.
- GSI를 추가해 “다른 조회 조건”을 지원한다.
- Query(키 기반)와 Scan(전체 탐색)의 차이를 콘솔에서 확인한다.

## Prereqs

- DynamoDB 생성/설정 권한
- Region: 수업 기본 리전

## Cost Notes

- 소량 테스트는 비용이 작지만, 테이블은 정리한다.

## Steps

### A) Console Steps

#### 1) 테이블 생성

1. DynamoDB -> Create table
2. Table name: `saa-week3-orders`
3. Partition key: `pk` (String)
4. Sort key: `sk` (String)
5. Capacity: On-demand(학습용)
6. Create

#### 2) 예시 아이템 10~20개 생성

1. Explore items -> Create item
2. 예시 패턴
  - `pk=customer#1`, `sk=order#1001`, `status=PAID`
  - `pk=customer#1`, `sk=order#1002`, `status=CANCELED`
  - `pk=customer#2`, `sk=order#2001`, `status=PAID`

#### 3) Query로 조회(키 기반)

1. Explore items에서 Query 선택
2. Partition key에 `customer#1` 입력
3. 결과가 해당 파티션 범위로 제한되는지 확인

#### 4) Scan으로 조회(전체)

1. Scan 선택
2. 전체를 읽는 동작임을 확인(데이터가 커질수록 비용/시간 증가)

#### 5) GSI 추가(status로 조회)

1. Table -> Indexes -> Create index
2. Index name: `gsi_status`
3. Partition key: `status` (String)
4. Projection: All(학습용)
5. Create

#### 6) GSI로 Query

1. Explore items에서 Index를 `gsi_status`로 선택
2. Query: `status=PAID`로 조회

### B) Optional: CLI Equivalents (for validation/automation)

- `ReturnConsumedCapacity`를 켜면 Query vs Scan의 비용 차이를 더 선명하게 볼 수 있다(선택).

## Validation Checklist

- Query는 키 기반으로 제한된 조회임을 설명할 수 있다.
- Scan은 전체 탐색이며 비용/성능 함정이 될 수 있음을 설명할 수 있다.
- GSI로 다른 액세스 패턴을 추가할 수 있다.

## Common Errors

- GSI 생성은 즉시 반영되지 않을 수 있다(Creating 상태).
- 키 설계를 못 잡고 “원하는 모든 조건 검색”을 기대하는 실수(시험에서 함정).

## Cleanup

1. 테이블 삭제(인덱스 포함)

