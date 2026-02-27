# Auto Scaling = “확장 + 복구”의 엔진

## 구성요소

- Launch template/config: 인스턴스 표준(AMI/타입/보안그룹/user data)
- Auto Scaling group: min/desired/max, AZ 분산
- Health checks: EC2 + (옵션) ELB health check

## 시험 함정

- “원하는 가용성”이 있으면 Multi-AZ + ASG가 기본 정답 후보
- 헬스체크 실패 시 “교체/제외”를 통해 자가 치유가 일어난다

## Exam must-know (포인트 + Why + 대안)

- Key point: “장애 자동 복구” 문장은 ASG + health check(EC2/ELB) 조합으로 푸는 경우가 많다.
- Why: 실패한 인스턴스를 자동으로 감지하고 교체할 수 있는 메커니즘이 있어야 ‘운영자가 수동으로 재기동’ 패턴을 제거할 수 있다.
- Alternative: 워크로드가 서버리스면(예: Lambda) 인스턴스 복구가 아니라 “동시성/재시도/큐”로 복원력을 설계한다.

## TL;DR (한 줄 정리)

- 자가 치유는 **헬스체크 → 제외/교체** 흐름으로 만든다(ASG + health check).

## Back

- `../01-theory.md`
