# EBS Snapshot (블록 스토리지 백업의 기본 단위)

## 소개 (이게 뭔가요?)

- EBS snapshot은 EBS 볼륨의 백업/복구 기본 단위로 등장한다.

## 고객 사례 (스토리, 600~1000자)

![고객 사례 삽화 - EBS Snapshot 백업](../../assets/scenario_image/w2d3s3.png)

애플리케이션이 상태를 디스크에 쓰는 워크로드였다. 업데이트를 하다가 디스크가 꼬여 롤백이 필요해졌다. 팀은 “S3는 버전 관리가 쉬운데, 이 디스크는 어떻게 복구하지?”를 고민한다. 인스턴스를 새로 띄워도 디스크 데이터가 없으면 의미가 없다. 결국 필요한 건 ‘볼륨 수준’의 백업이다.

이때 EBS snapshot이 기본 단위가 된다. 시험에서도 AMI/스냅샷/백업이 섞여 나오는데, 디스크 데이터 복구가 핵심이면 snapshot이 자연스럽다. 리전 DR까지 요구되면 더 큰 전략(백업 복제/DR 메뉴)로 확장되지만, 기본기는 snapshot이다.

그리고 운영 현실에서는 “한 번 떠놓고 끝”이 아니라 “주기적으로 떠놓고, 복구가 되는지 확인”까지가 세트다. 스냅샷이 있으면 새 볼륨을 만들어 인스턴스에 붙이거나(복구), 새로운 AMI/환경으로 이어가는 선택지가 열리지만, 없으면 결국 ‘다시 만들기’밖에 남지 않는다. 그래서 시험에서도 “데이터가 EBS에 있다”는 문장이 나오면, 서버(인스턴스)보다 **볼륨(스냅샷)**을 먼저 떠올리는 게 정답에 가깝다.

그리고 이 반복 작업은 결국 자동화(정기 스냅샷)로 운영 부담을 줄이는 쪽이 자연스럽다.

지금 문제는 “서버 교체”인가요, 아니면 “디스크 데이터 복구”인가요?

## Impact 범위 (어디에 영향을 주나?)

- Reliability/Operations: 볼륨 단위 복구/롤백 절차

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-2-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-2.2%20Backup%20%26%20DR-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: EBS](https://img.shields.io/badge/Service-EBS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

## Why This Matters (시험/실무에서 걸리는 지점)

- “볼륨/디스크 복구” 신호가 있으면 snapshot이 기본 후보로 올라간다.

## Core Concepts

- 스냅샷은 백업/복구의 기본 단위로 등장
- “장애 대비”에서 AMI/스냅샷/백업 전략이 섞여 출제될 수 있음

## Deep Dive

### Snapshot이 “왜” 정답이 되는가

시험에서 EBS Snapshot은 단순 기능 문제가 아니라 **복구 단위(Unit of recovery)**를 고르는 문제로 자주 나온다.

- **객체/파일 단위 복구**: S3 Versioning, EFS 등
- **서버(인스턴스) 단위 복구**: AMI/이미지 기반 재배포
- **디스크(블록) 단위 복구**: **EBS Snapshot**

문장에 “데이터가 인스턴스 로컬이 아니라 EBS에 있다”, “디스크가 꼬였다”, “볼륨을 복구해야 한다”가 있으면 스냅샷이 자연스럽다.

### Best Practices (실무/시험에 자주 나오는 디테일)

- 스냅샷은 일반적으로 **증분(incremental)** 형태로 이해하는 게 안전하다(매번 전체를 다시 뜨는 개념으로만 보면 비용/시간 감각이 흔들림).
- 운영 관점에서는 “한 번 떠놓기”가 아니라 **정기 스냅샷 + 보존 정책 + 복구 리허설**이 세트다.
- “다른 리전에도 백업이 있어야 한다” 같은 문장이 있으면 **Snapshot Copy(리전 간 복사)**까지 떠올려야 한다.
- 암호화(EBS/KMS)가 걸려 있다면, 복구/복사 시에도 **키 정책/권한**이 따라온다(권한이 막히면 복구 자체가 실패할 수 있음).

### AMI와의 관계(시험 단골)

| 무엇을 복구하려는가 | 자연스러운 1순위 | 왜 |
|---|---|---|
| “볼륨 데이터” | **EBS Snapshot** | 블록 스토리지 복구 단위 |
| “인스턴스를 동일 구성으로 재배포” | AMI | OS/구성까지 포함한 이미지 |

즉, “서버를 다시 띄우면 끝”이 아니라 “데이터가 디스크에 남아야 한다”는 문장이 보이면 스냅샷 축으로 답이 좁혀진다.

### 핵심 정리 (Deep Dive)

- 디스크(블록) 데이터 복구는 **EBS Snapshot**이 기본 단위다.
- “다른 리전에도 백업”이 붙으면 Snapshot Copy/DR 메뉴로 확장해서 본다.

## TL;DR (한 줄 정리)

- 블록 스토리지 백업/복구는 **EBS snapshot**이 기본 단위다.

## References

- Internal references:
  - [References index](../../references/README.md)
  - [Exam guide (SAA-C03)](../../references/exam-guide.md)
  - [Glossary](../../references/glossary.md)
  - [AWS services list](../../references/aws-services.md)
  - [Exam keypoints](../../exam-keypoints.md)
  - [Exam trap bank](../../exam-trap-bank.md)

- Official AWS documentation:
  - [Search: Amazon EBS](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=Amazon%20EBS)

## Back

- `./README.md`
