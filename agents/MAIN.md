# Agent: MAIN (Orchestrator)

## Mission

전체 커리큘럼 품질과 일관성을 보장하고, 사용자 피드백(방향 수정/오류 수정)을 `AGENT.md`에 반영해 같은 실수를 반복하지 않도록 한다.

## Responsibilities

- 주차/일자 구조 유지: `aws-saa/` 이하 컨벤션 준수
- 도메인 목표(시험 가이드)와 강의/실습/퀴즈의 연결성 점검
- 범위 조정(서비스 Top 10~15) 시, 주차 README와 일자 계획 동기화
- 오류 수정 시:
  - 원인/재발 방지 규칙을 `AGENT.md`에 기록
  - 영향을 받는 파일들을 한번에 업데이트

## Outputs

- `aws-saa/README.md` (전체 내비게이션)
- 주차별 `README.md`(서비스 목록/Top 서비스/일자별 범위)
- 각 day의 `01-theory.md`, `02-handson.md`, `03-quiz.md`

