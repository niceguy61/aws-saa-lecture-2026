# EBS Snapshot (블록 스토리지 백업의 기본 단위)

## 소개 (이게 뭔가요?)

- EBS snapshot은 EBS 볼륨의 백업/복구 기본 단위로 등장한다.

## 고객 사례 (스토리, 600~1000자)

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

## VAKOG Anchors

- V(Visual): snapshot=볼륨 백업 단위로 기억한다.
- A(Auditory): “디스크는 snapshot”을 말로 고정한다.
- O(Olfactory, smell test): 디스크 복구를 S3만으로 해결하려는 답은 냄새가 난다.
- G(Gustatory, taste test): 문장 하나 보고 snapshot을 떠올린다.

## Core Concepts

- 스냅샷은 백업/복구의 기본 단위로 등장
- “장애 대비”에서 AMI/스냅샷/백업 전략이 섞여 출제될 수 있음

## Deep Dive

- 시험에서는 “어떤 복구 단위가 필요한가(서버 vs 디스크 vs 객체)”를 구분하는 문제가 많다.

## TL;DR (한 줄 정리)

- 블록 스토리지 백업/복구는 **EBS snapshot**이 기본 단위다.

## Back

- `../01-theory.md`
