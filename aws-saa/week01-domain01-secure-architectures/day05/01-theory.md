# Special Lecture + Week Summary (Domain 1)

## Exam Guide Mapping

- Domain: Domain 1: Design Secure Architectures
- Task focus:
  - 1.1 Design secure access to AWS resources
  - 1.2 Design secure workloads and applications
  - 1.3 Determine appropriate data security controls

## Agenda (2h 30m)

1. Top 서비스 “선택 기준” 15분
2. 헷갈리는 비교(Choose-this-not-that) 40분
3. 설계 패턴 4종(시험 빈출) 55분
4. 함정/오답 제거 규칙 20분
5. Day05 미니 랩 브리핑 20분

## Week 1 Decision Rules (암기 대신 규칙)

- 키 공유가 보이면 AssumeRole(=STS)이 정답 후보 1순위다.
- “누가 Assume?”은 trust policy, “Assume 후 무엇?”은 permission policy다.
- 상한선이 있는지 먼저 확인한다: SCP/Permissions boundary가 있으면 IAM Allow로 뚫을 수 없다.
- 데이터 보호 요구가 있으면 “암호화(키 관리) + 접근 제어 + 감사”를 같이 묻는 문제다.

## Confusing Similar Cases

| Scenario | Best choice | Why | Common wrong choice | Why it's wrong |
|---|---|---|---|---|
| 교차 계정 운영 | Role + STS AssumeRole | 임시/회수/감사 | 액세스 키 공유 | 유출 시 회수/추적 어려움 |
| 상위 거버넌스 | SCP | 계정/OU 상한선 | IAM Allow만 추가 | SCP Deny는 항상 이김 |
| 시크릿 관리 | Secrets Manager | rotation/통합 기능 | Parameter Store(일반) | rotation/관리 기능 약함 |
| 감사/구성 추적 | CloudTrail + Config | API 호출 vs 구성 변화 | CloudTrail만 | 구성/준수 관점 누락 |
| DDoS/웹 보호 | Shield/WAF | L3/4 vs L7 | SG/NACL | 엣지 공격/봇 대응 불가 |

## Exam-Heavy Patterns (4)

### Pattern 1: Cross-account access without key sharing

- Role trust policy로 “누가 Assume 가능한지” 정의
- 필요 시 ExternalId 조건(3rd party)
- 세션 정책(session policy)으로 “추가 제한” 가능

### Pattern 2: Centralized encryption control (KMS)

- KMS는 “키 사용 권한”이 핵심이다.
- key policy는 KMS에서 특히 중요(리소스 정책 성격).
- 애플리케이션 암호화는 보통 envelope encryption(개념)로 설명한다.

### Pattern 3: Secret retrieval for workloads

- 앱은 장기 키 대신 role 기반으로 시크릿을 읽는다.
- 시크릿은 KMS로 보호되고, CloudTrail로 “누가/언제 읽었는지” 감사한다.

```mermaid
flowchart LR
  App[Workload (Role)] --> SM[Secrets Manager]
  SM --> KMS[KMS CMK]
  App -. API calls .-> CT[CloudTrail (Event history / Trail)]
  SM -. API calls .-> CT
```

### Pattern 4: Audit + Detection linkage

- CloudTrail: “API 호출” 로그(누가 무엇을 했나)
- Config: “리소스 구성” 변화(어떤 상태였나)
- GuardDuty/Security Hub는 “탐지/집계” 층에서 활용(개념)

## Traps (오답 제거)

- “SCP로 Allow를 줬다”는 문장 자체가 함정이다: SCP는 상한선(Allow의 의미가 다름)
- “KMS는 IAM policy만으로 제어한다”는 오답 유도: key policy가 핵심
- “시크릿을 S3에 저장” 같은 안티패턴은 거의 오답

## Reference Pack

- `aws-saa/special-lectures/domain01-secure-top-services.md`

