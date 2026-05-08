# 2주차 2일차 - Docker Image

## 목표

Docker Image가 어떻게 만들어지고 이름 붙고 재사용되는지 이해한다.

## 오늘 배울 내용

- Dockerfile 구조
- Image layer와 build cache의 초급 개념
- Build context와 .dockerignore
- Tag와 Registry 흐름

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | 컨테이너 생명주기 복습 |
| 10:00-10:50 | 2교시 | Dockerfile 읽기 |
| 11:00-11:50 | 3교시 | Layer, cache, build context |
| 12:00-12:50 | 4교시 | 강사 데모: 작은 API 이미지 빌드 |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | 실습: Dockerfile 작성과 빌드 |
| 15:00-15:50 | 6교시 | 실습: tag 지정과 재실행 |
| 16:00-16:50 | 7교시 | 진단: build cache가 동작한 이유 찾기 |
| 17:00-17:50 | 8교시 | 정리와 런타임 설정 예고 |

## 랩/미션/데모

간단한 API 이미지를 빌드하고 tag를 붙인 뒤 실행한다. Dockerfile의 각 줄이 어떤 역할을 했는지 설명한다.

## 보충/심화 자료

- Dockerfile 체크리스트
- .dockerignore 예시
- 심화: Image layer 저장 방식
