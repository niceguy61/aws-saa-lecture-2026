# Day 02 - Theory Index (데이터 보호: KMS/Secrets/S3 SSE-KMS)

> 이 문서는 Day 이론 “인덱스”다. 서비스별 theory는 `theory/*.md`에서 각각 읽는다.

## 소개 (이게 뭔가요?)

- KMS는 “키를 직접 들고 다니지 않게” 해주는 중앙 키 관리 계층이다.
- Secrets Manager/Parameter Store는 “시크릿을 코드 밖으로” 빼서 안전하게 보관/회수/회전하게 돕는다.

## 고객 사례 (스토리)

신규 서비스가 오픈되자마자 “비밀번호가 깃에 올라갔다”는 이슈가 터졌다. 급하게 `.env`로 옮겼지만, 배포 서버가 늘면서 파일이 복제되고, 누가 언제 바꿨는지 추적도 안 된다. 게다가 보안팀은 “DB 비밀번호는 분기마다 교체(rotate)하고, 사고 나면 즉시 폐기”를 요구한다. S3에 올리는 고객 파일도 암호화가 기본이어야 한다.

환경이 dev/stage/prod로 나뉘면 상황은 더 골치 아프다. 각 환경의 자격 증명이 달라서 “서버에 들어가서 바꾸는 작업”이 반복되고, 작업자가 한 명이면 휴가도 마음 편히 못 간다. “누가 이 시크릿을 조회했지?” 같은 질문이 나오면, 답할 근거도 필요하다.

처음엔 애플리케이션에서 직접 암호화 라이브러리를 붙이려 했지만, 키를 어디에 둘지가 또 문제다. 여기서 Secrets Manager를 “시크릿 금고”, Parameter Store를 “설정 값 서랍”처럼 나누면 관리가 쉬워진다. 둘 다 KMS로 암호화할 수 있고, 특히 Secrets Manager는 회전/버전 관리가 정답인 문제가 많다. S3는 SSE-KMS로 ‘저장 시 암호화’를 켜면 되지만, 이때 AccessDenied가 나오면 S3 정책보다 KMS key policy를 먼저 의심해야 한다(서비스가 KMS를 대신 호출하기 때문).

지금 상황이 “보관/회전/추적”까지 포함한다면, 시크릿을 어디에 두는 게 가장 안전할까요?

## Impact 범위 (어디에 영향을 주나?)

- Security: 암호화 at-rest + 키/시크릿 접근 통제의 정답을 가른다.
- Operations: `AccessDenied`의 원인이 “S3 권한”이 아니라 “KMS key policy”인 경우가 많다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-1-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-1.3%20Data%20security%20controls-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: KMS](https://img.shields.io/badge/Service-KMS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Secrets%20Manager](https://img.shields.io/badge/Service-Secrets%20Manager-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Parameter%20Store](https://img.shields.io/badge/Service-Parameter%20Store-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: S3](https://img.shields.io/badge/Service-S3-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 1: Design Secure Architectures
- Task focus:
  - 1.1 Design secure access to AWS resources (권한/정책 경계)
  - 1.3 Determine appropriate data security controls (암호화/시크릿)

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- KMS는 “IAM Allow가 있는데도” 막힐 수 있다: **key policy**가 최종 관문인 문제가 많다.
- 시크릿을 코드/환경변수/S3에 두라는 선택지는 대개 오답이다(관리형 서비스 우선).

## Core Concepts

- 데이터 보호 통제 3종 세트(시험형 사고)
  - Encryption at rest: KMS/SSE-KMS/Secrets encryption
  - Access control: IAM/리소스 정책/경계
  - Audit: CloudTrail(누가 키/시크릿을 썼는지)
- KMS가 “정책”에 민감한 이유
  - 암호화/복호화는 KMS API 호출로 귀결되고, KMS는 key policy를 중심으로 통제한다.
  - 다른 서비스(S3, EBS, Secrets Manager)가 KMS를 “호출 대행”할 때도 권한 경계가 중요하다.

![KMS envelope encryption and integration intuition](../../assets/core/kms-envelope-encryption.svg)

## Service Chapters (서비스별로 읽기)

- [KMS: key policy가 핵심(그리고 함정)](theory/10-kms.md)
- [Secrets Manager vs Parameter Store(SecureString)](theory/20-secrets-vs-parameter-store.md)
- [S3 SSE-KMS: “S3 권한만 주면 되지 않나요?” 함정](theory/30-s3-sse-kms.md)

> 서비스가 섞이면 문장이 길어져서 헷갈린다. Deep Dive는 챕터로 분리해두고, `01-theory.md`에서는 흐름/규칙을 먼저 잡는다.

## Quick Comparison Table

| Scenario | Best choice | Why | Common trap |
|---|---|---|---|
| 시크릿 rotation 요구 | Secrets Manager | 운영 기능/통합 | Parameter Store만으로 해결하려 함 |
| 단순 설정 값 | Parameter Store | 경량/단순 | 시크릿까지 한곳에 무작정 몰기 |
| S3 객체 보관 암호화 | SSE-KMS | 중앙 키 통제 | S3 권한만 주면 된다고 착각 |

## Exam Traps

- “KMS는 IAM만 보면 된다”는 오답 유도: key policy가 포인트다.
- “SSE-KMS는 S3만 권한 주면 된다”는 오답 유도: KMS decrypt 경로가 있다.
- “시크릿을 S3/코드/환경변수에 저장” 같은 답안이 보이면 거의 오답(요구사항 따라 예외는 있지만 SAA는 대부분 관리형 선택).

## TL;DR (한 줄 정리)

- “암호화/시크릿 + AccessDenied”가 보이면 **KMS key policy(관문) + 적절한 시크릿 저장소(Secrets Manager/Parameter Store) + 서비스 통합 권한(S3 SSE-KMS)** 조합부터 의심한다.
