# Integrated Mini Lab (Console): SNS -> SQS Fan-out + DLQ

## Goal

- 팬아웃(SNS) + 내구 큐(SQS) 조합을 구성한다.
- DLQ(redrive)로 실패 메시지 격리를 설정한다.

## Prereqs

- SNS/SQS 생성 권한
- Region: 수업 기본 리전

## Cost Notes

- SNS/SQS는 소규모 사용 시 비용이 미미하지만, 정리(Cleanup) 수행.

## Steps

### A) Console Steps

#### 1) SQS 큐 2개 + DLQ 2개 생성

1. SQS에서 표준(Standard) 큐 생성
  - Queue A: `saa-week2-q-a`
  - DLQ A: `saa-week2-dlq-a`
2. Queue B: `saa-week2-q-b`
  - DLQ B: `saa-week2-dlq-b`

#### 2) Queue A/B에 Redrive policy(DLQ) 설정

1. Queue A 편집 -> Dead-letter queue 설정
2. DLQ A 선택, maxReceiveCount 예: 3
3. Queue B도 동일하게 DLQ B 연결

#### 3) SNS Topic 생성 + SQS 구독(Subscription) 2개

1. SNS에서 Topic 생성: `saa-week2-fanout`
2. Subscriptions 추가:
  - Protocol: SQS, Endpoint: Queue A ARN
  - Protocol: SQS, Endpoint: Queue B ARN
3. SQS Queue A/B의 “Access policy”에 SNS publish 허용이 자동 반영되는지 확인(필요 시 수동 추가)

#### 4) 메시지 발행 -> 두 큐에 도착 확인

1. SNS Topic에서 “Publish message”
2. 메시지 본문 예: `order_id=123`
3. SQS Queue A/B에서 “Poll for messages”로 수신 확인

#### 5) (옵션) DLQ 흐름 확인

1. Queue A에서 메시지를 받은 뒤 “Delete”하지 않고 가시성 타임아웃 이후 재수신을 반복
2. maxReceiveCount 초과 시 DLQ A로 이동하는지 확인

### B) Optional: CLI Equivalents (for validation/automation)

- CLI로 `sns publish` 후 `sqs receive-message`로 확인 가능(수업은 콘솔 기준).

## Validation Checklist

- SNS 1회 publish로 Queue A/B 모두 메시지를 받는다.
- (옵션) 재처리 실패가 누적되면 DLQ로 이동한다.

## Common Errors

- SNS -> SQS 권한(policy) 미설정: subscription은 됐는데 메시지가 안 들어온다.
- FIFO/표준 큐 혼동: FIFO는 제약이 많으므로 학습용은 표준 큐 권장.

## Cleanup

1. SNS subscription 삭제
2. SNS topic 삭제
3. SQS 큐 A/B 및 DLQ A/B 삭제

