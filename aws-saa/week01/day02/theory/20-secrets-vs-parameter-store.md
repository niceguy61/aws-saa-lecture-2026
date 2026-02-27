# Secrets Manager vs Parameter Store(SecureString)

## Deep Dive

- Secrets Manager가 시험에서 자주 정답인 이유
  - rotation/통합 관리(요구사항에 rotation이 있으면 강력 힌트)
  - 시크릿 수명/교체 운영을 “서비스”로 처리
- Parameter Store(SecureString)의 포지션
  - 단순 구성 값/파라미터에 적합(특히 애플리케이션 설정)
  - 시크릿 운영 기능이 요구되면 Secrets Manager가 더 자연스럽다.
- Exam must-know (포인트 + Why + 대안)
  - Key point: “자동 rotation/통합 운영” 요구가 있으면 Secrets Manager가 정답 후보가 된다.
  - Why: rotation은 단순 저장이 아니라 교체/검증/롤백까지 포함한 운영 기능이며, 문제 문장에 “주기적 교체”가 등장하면 의도적으로 분리해 묻는 경우가 많다.
  - Alternative: “경량 파라미터”만 요구하면 Parameter Store로 충분하지만, 시크릿 수명 관리가 요구되면 Secrets Manager로 전환한다.

## TL;DR (한 줄 정리)

- “rotation/운영” 신호가 있으면 **Secrets Manager**, 단순 설정값이면 **Parameter Store**가 자연스럽다.

## Back

- `../01-theory.md`
