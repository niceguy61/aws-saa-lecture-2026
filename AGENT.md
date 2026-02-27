# Main Agent Operating Notes (AWS SAA Materials)

This repository is being used to author AWS SAA (Solutions Architect - Associate) lecture materials.

## Source Of Truth

- Primary: AWS 공식 시험 가이드 PDF (SAA-C03)
  - https://d1.awsstatic.com/ko_KR/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Exam-Guide.pdf
- Secondary: AWS 공식 문서/Well-Architected Framework (필요 시 Deep Dive 근거로 사용)

## Course Shape (Current Decisions)

- 총 4주, 주차별로 도메인 1~4를 순서대로 진행
- 주 5일(총 20세션) 고정
- 1일(세션) 4시간 기준
  - 기본: 이론 2h + 실습 2h
  - 예외: 이론 비중이 큰 날은 이론 3h + 실습 1h 허용
- 모든 세션은 다음을 포함
  - Deep Dive (시험에 나오는 트레이드오프/제약/설계 패턴 포함)
  - 시각화(mermaid 다이어그램 기본)로 흐름을 설명
  - 실습(콘솔 위주, 필요 시 CLI는 Optional로 보조 / Free tier/저비용, 정리(Cleanup) 포함)
  - 실습 후 모의문제(정답/해설/오답 근거 포함)

## Special Lecture (Top 10~15 Services)

- 일반 도메인 강의(주 5일)와 별도로 “특강” 문서를 운영
- 목적: 자주 출제되는 패턴/헷갈리는 비교(유사 서비스) + Best Practice + 대안(트레이드오프)을 한 곳에 모아 Deep Dive
- 위치: `aws-saa/special-lectures/`

## Output Layout (Conventions)

- 코스 루트: `aws-saa/`
- 주차별 폴더: `aws-saa/weekNN-domainXX-*/`
- 일자별 폴더: `aws-saa/weekNN-.../dayDD/`
  - `README.md` (목표/타임박스/서비스 범위)
  - `01-theory.md`
  - `02-handson.md`
  - `03-quiz.md`

## Quality Gates (Definition Of Done)

- 정확성: “언제/왜 이 서비스를 쓰는가”를 설계 관점으로 설명
- 시험 적합성: 도메인 목표(시험 가이드)를 명시적으로 매핑
- 실습: 예상 결과(검증 포인트) + 비용/주의 + Cleanup 포함
- 퀴즈: 정답+해설, 오답이 왜 오답인지 1~2줄로 명확히
- 시각화: 최소 1개 다이어그램(복잡한 날은 2~3개)
- 가독성: TL;DR → 결정 규칙 → 근거/예시 → 정리 흐름 유지(가이드는 `WRITING_GUIDE.md`)
- VAKOG(멀티모달): 세션 단위로 V/A/K/O/G 요소를 최소 1개씩 포함(가이드는 `VAKOG.md`)

## Writing Style (요약)

- 결론을 먼저 쓴다(TL;DR 1줄).
- 기술 핵심(Core)은 짧고 매끈하게, 비유/설명(Explain)은 편안한 대화체로 쓴다(`WRITING_GUIDE.md`).
- 용어는 첫 등장에만 1줄로 정의한다.
- 문단은 3~5줄, 한 문단에 한 주장.
- “무조건/항상” 대신 조건과 예외를 쓴다.

## VAKOG 운영 규칙 (요약)

- 문서는 학습자를 유형으로 분류하지 않는다. VAKOG는 “콘텐츠 설계 체크리스트”로만 사용한다.
- 각 day README에 `## VAKOG` 블록을 추가하고, 해당 day의 theory/handson/quiz에서 실제로 충족되게 만든다.
- Skill(외부) 기반 산출물도 결과물에 VAKOG 섹션을 덧붙여 일관성을 유지한다(상세: `VAKOG.md`).

## Mistake Prevention Log

실수/수정이 발생하면 아래에 기록하고, 관련 문서(주차/일자/템플릿)를 같이 업데이트한다.

### 2026-02-26

- 초기 스캐폴드 생성: 4주 x 5일(총 20세션) 기준으로 구성
- 시험 가이드 도메인/가중치와 주차 매핑 확정(SAA-C03)
- 실습은 콘솔 위주로 전환
- Top 10~15 서비스 Deep Dive는 Special Lecture 문서로 분리
- 각 주차 Day05는 “Special Lecture + Week Summary(이론 2h30 + 미니 랩 1h + 케이스 퀴즈 30m)”로 운영
- OT는 주차 과정이 아니라 “과정 시작 전 1회” 오리엔테이션이다: `aws-ot/README.md` + `aws-ot/assets/`만 유지(weekNN 구조 재발 방지)
