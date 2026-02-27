# Secrets Manager vs Parameter Store(SecureString)

## 소개 (이게 뭔가요?)

- 둘 다 “시크릿/설정 값을 코드 밖에서 안전하게 보관”하는 도구다.
- 시험에서는 보통 “저장”이 아니라 **운영 기능(회전/교체/통합)** 유무로 정답이 갈린다.

## 고객 사례 (스토리, 600~1000자)

팀이 `.env`로 시크릿을 관리하다가 사고를 겪었다. 개발/스테이징/운영 환경이 늘어나자 파일 복사로 시크릿이 퍼지고, 누가 바꿨는지 추적도 어렵다. 보안팀은 “DB 비밀번호는 주기적으로 교체해야 한다(rotate)”고 요구한다. 여기서 문제가 커진다. 교체는 단순히 값 하나 바꾸는 게 아니라, 애플리케이션이 새 값으로 안전하게 전환되고, 실패하면 롤백할 수 있어야 한다. 담당자가 한 명이면 더 버겁다.

이럴 때 Secrets Manager는 “시크릿 운영”까지 포함한 금고에 가깝다. 회전 요구가 있으면 강력한 신호가 된다. 반면 Parameter Store(SecureString)는 단순한 구성 값(설정 파라미터)을 안전하게 보관하는 ‘서랍’에 가깝다. 둘 다 KMS로 암호화할 수 있지만, 시험은 “회전/교체/통합 운영이 필요하냐”를 먼저 묻는다. 결국 선택 기준은 ‘값이 민감하냐’만이 아니라, ‘수명 관리가 필요하냐’다.

특히 운영에서 “새 시크릿 적용”이 자동화돼야 하면, 저장소 선택이 곧 운영 난이도 선택이 된다. 그래서 문제 문장에 rotation, 자동 교체, 통합 관리 같은 단어가 있으면 그냥 지나치면 안 된다.

지금 요구사항에 “정기 교체/회전/자동화”가 들어 있나요? 그렇다면 어떤 쪽이 더 자연스러울까요?

## Impact 범위 (어디에 영향을 주나?)

- Security: 시크릿이 코드/파일/깃에 퍼지는 경로를 제거
- Operations: 회전/교체 같은 운영 요구가 있으면 선택이 달라진다

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-1-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-1.3%20Data%20security%20controls-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Secrets%20Manager](https://img.shields.io/badge/Service-Secrets%20Manager-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 1: Design Secure Architectures
- Task focus: 시크릿 저장소 선택(회전/운영 기능 힌트)

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- “rotation”이 문장에 있으면 Secrets Manager가 강한 정답 후보가 된다.
- “단순 설정 값”이면 Parameter Store가 충분한 경우가 많다.

## VAKOG Anchors

- V(Visual): 아래 비교표를 보고 10초 안에 선택한다.
- A(Auditory): “회전이면 SM, 설정이면 PS”를 말로 고정한다.
- O(Olfactory, smell test): “시크릿을 S3/코드/환경변수에 저장”은 냄새가 난다.
- G(Gustatory, taste test): 문장 1개 보고 바로 선택해본다.

## Core Concepts

- “시크릿 운영(회전/교체/버전)”이 요구되면 Secrets Manager 쪽이 자연스럽다.
- “경량 파라미터/설정”이면 Parameter Store(SecureString)로 충분할 수 있다.

## Deep Dive

- Secrets Manager가 시험에서 자주 정답인 이유
  - rotation/통합 관리(요구사항에 rotation이 있으면 강력 힌트)
  - 시크릿 수명/교체 운영을 “서비스”로 처리
- Parameter Store(SecureString)의 포지션
  - 단순 구성 값/파라미터에 적합(특히 애플리케이션 설정)
  - 시크릿 운영 기능이 요구되면 Secrets Manager가 더 자연스럽다.
- Exam must-know (포인트 + Why + 대안)
  - Key point: “자동 rotation/통합 운영” 요구가 있으면 Secrets Manager가 정답 후보가 된다.
  - Why: rotation은 단순 저장이 아니라 교체/검증/롤백까지 포함한 운영 기능이다.
  - Alternative: “경량 파라미터”만 요구하면 Parameter Store로 충분하지만, 수명 관리가 요구되면 Secrets Manager로 전환한다.

## Quick Comparison Table

| Scenario | Best choice | Why | Common trap |
|---|---|---|---|
| 시크릿 rotation 요구 | Secrets Manager | 운영 기능/통합 | Parameter Store만으로 해결하려 함 |
| 단순 설정 값 | Parameter Store | 경량/단순 | 시크릿까지 한곳에 무작정 몰기 |

## Exam Traps (5-8)

- “rotation 요구”가 있는데 Parameter Store만 고르는 답
- “시크릿을 파일로 배포”하는 답안

## Taste Test (1~3분)

- “DB 비밀번호를 30일마다 자동 교체” 요구가 있으면 무엇이 먼저 떠오르나요?

## TL;DR (한 줄 정리)

- “rotation/운영” 신호가 있으면 **Secrets Manager**, 단순 설정값이면 **Parameter Store**가 자연스럽다.

## Back

- `../01-theory.md`
