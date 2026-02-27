# Day 04 - DB performance + caching (Aurora/DynamoDB/ElastiCache)

## Outcomes

- DB 성능 문제를 “쿼리/인덱스/캐시/모델링” 관점으로 분해한다.
- DynamoDB에서 “파티션 키 설계/핫 파티션”이 성능에 미치는 영향을 설명한다.
- ElastiCache/DAX의 역할을 “읽기 캐시”로 위치시킨다(개념).
- DynamoDB GSI로 “다른 액세스 패턴”을 추가하는 사고 흐름을 설명한다.

## Services In Scope

- DynamoDB (partition key, GSI 개념)
- ElastiCache, DAX (개념)
- Aurora/RDS performance patterns (개념)

## Timebox (4h)

- Theory + mini-action: 4h

## Exam-Style Design Questions

- DynamoDB 지연 문제에서 “무조건 DAX”가 오답이 되는 신호는?
- “다른 조건으로 조회” 요구가 있을 때 GSI가 정답인 신호는?
- 캐시가 정답이 되는 상황과 오답이 되는 상황을 구분할 수 있는가?
