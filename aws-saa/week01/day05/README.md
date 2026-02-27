# Day 05 - Special Lecture + Week Summary (Domain 1)

핵심 서비스(Top 10~15)를 “비교/함정/대안”으로 정리하고, 케이스 문제로 시험형 판단을 회수한다.

## Outcomes

- Domain 1 Top 서비스에서 “선택 기준(when/why)”을 말로 설명한다.
- 헷갈리는 유사 서비스/기능을 비교표로 구분하고 오답 포인트를 피한다.
- Best practice 기반 대안(트레이드오프)을 제시한다.
- 케이스 기반 미니 시뮬레이션으로 KMS + Secrets + IAM 경계를 한 번에 연결한다.

## Services In Scope (Top set)

- IAM, STS (role switching)
- KMS (key policy 개념)
- Secrets Manager (KMS 통합)
- CloudTrail (Event history로 감사 확인)
- (Review) CloudTrail vs Config, Secrets Manager vs Parameter Store, SCP/Boundary

## Timebox (4h)

- Special lecture + case walkthrough (theory): 3h 30m
- Case quiz + review: 30m

## Reading

- Pack: `aws-saa/special-lectures/domain01-secure-top-services.md`

## Exam-Style Design Questions

- 어떤 상황에서 “Secrets Manager”가 “Parameter Store”보다 정답이 되는가?
- KMS에서 “key policy vs IAM policy”의 역할을 어떻게 구분할까?
- 임시 크레덴셜(AssumeRole)이 장기 키보다 안전한 이유를 설계 관점에서 설명할 수 있는가?
- CloudTrail과 Config의 차이를 “기록 대상/용도”로 구분할 수 있는가?
