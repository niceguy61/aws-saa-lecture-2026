# EBS: gp3/io2로 IOPS/처리량을 맞춘다

## 소개 (이게 뭔가요?)

- EBS는 EC2에 붙는 블록 스토리지이고, 시험에서는 “용량이 아니라 성능 축(IOPS/처리량)”을 맞추는지 본다.

## 고객 사례 (스토리, 600~1000자)

![고객 사례 삽화 - EBS 튜닝(gp3/io2)](../../assets/scenario_image/w3d3s1.png)

팀이 운영하는 내부 분석 시스템은 “가끔 느리다”가 아니라 “항상 답답하다”는 불만이 나온다. CPU는 여유가 있는데 쿼리/배치가 시작되면 응답이 뚝뚝 끊긴다. 개발자는 인스턴스를 키웠는데도 차이가 없어서 당황한다. 로그를 보면 디스크 읽기/쓰기 대기가 늘어나는 느낌인데, “디스크는 용량만 충분하면 되는 거 아닌가?”라는 선입견 때문에 방향을 못 잡는다.

여기서 EBS 성능 축을 잡아야 한다. 블록 스토리지는 **랜덤 I/O(=IOPS)**와 **연속 처리량(MB/s)**이 핵심이다. CloudWatch에서 VolumeQueueLength가 올라가거나 I/O 관련 지표가 과하게 흔들리면, 컴퓨트가 아니라 스토리지 I/O 병목일 가능성이 높다. 이때 gp3는 용량과 성능(IOPS/처리량)을 분리해서 조절할 수 있어 “용량은 그대로, 성능만 튜닝” 신호에 잘 맞는다. 반대로 “높은 IOPS”와 “일관된 성능”이 강하면 프로비저닝 IOPS 기반의 io2(io1)가 후보가 된다.

그리고 시험은 종종 “볼륨 타입을 바꾸면 해결된다”를 쉽게 주지 않는다. “QueueLength가 증가한다”, “IO wait가 늘어난다”, “랜덤 I/O가 많다” 같은 간접 힌트로 스토리지 병목임을 알아채게 만든다. 이 신호를 못 잡으면 인스턴스만 계속 키우게 되고, 비용만 올라간다.

정리하면, EBS 문제는 “더 큰 디스크”가 아니라 “어떤 축을 올릴지”를 고르는 문제다. 지금 문장은 IOPS/큐/지연 같은 신호를 주고 있나요?

## Impact 범위 (어디에 영향을 주나?)

- Performance: I/O 병목이 풀리면 체감 성능이 크게 개선될 수 있다.
- Cost: io2는 비용이 빠르게 상승할 수 있어 신호가 명확할 때만 고른다.
- Operations: 지표 기반 튜닝(gp3)으로 운영 안정성이 올라간다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-3-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-3.1%20Storage%20perf-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: EBS](https://img.shields.io/badge/Service-EBS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: CloudWatch](https://img.shields.io/badge/Service-CloudWatch-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 3: Design High-Performing Architectures
- Objectives: I/O 병목 신호를 보고 EBS 타입/튜닝으로 풀 수 있는지

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- “느린데 CPU는 낮다”가 나오면, 시험은 스토리지/네트워크 쪽으로 시선을 돌리라고 신호를 준다.

## Core Concepts

- gp3: 용량과 성능(IOPS/처리량)을 분리해서 조절 가능
- io1/io2: 프로비저닝 IOPS(높은/일관된 IOPS 요구에 적합)
- 병목 신호(시험/실무)
  - `VolumeQueueLength` 증가
  - I/O 관련 지표의 지속적 포화

```mermaid
flowchart LR
  App[App on EC2] --> EBS[EBS Volume]
  EBS --> CW[CloudWatch metrics]
```

## Deep Dive

### EBS 볼륨 타입 전체 정리(누락 없이)

> 표준/대표 선택지는 **굵게** 표시했다.

| 타입 | 성격(한 줄) | 언제 쓰나(문장 신호) | 비용 효율 포인트 |
|---|---|---|---|
| **gp3** | 범용 SSD(튜닝 가능) | “용량은 그대로, 성능만 조절” | 기본값으로 비용 효율이 좋은 경우가 많다(성능/용량 분리) |
| gp2 | 레거시 범용 SSD | “기존 gp2 사용” 같은 힌트 | 신규 설계는 보통 gp3가 더 자연스럽다 |
| **io2** | 프로비저닝 IOPS(일관성) | “높은/일관된 IOPS”, “지연 민감” | 비용↑, 신호가 명확할 때만 |
| io1 | 이전 세대 프로비저닝 IOPS | “io1”이 명시되거나 기존 구성 | 보통 io2가 후보가 되기 쉽다 |
| st1 | HDD(처리량 중심) | “대용량 순차 처리/로그 처리” | SSD보다 저렴, 랜덤 I/O엔 부적합 |
| sc1 | HDD(콜드) | “거의 안 읽는 대용량” | 더 저렴, 성능 요구 낮을 때 |
| standard(magnetic) | 구형 | 거의 레거시/트랩 | 시험/실무에서 표준 선택지로는 드묾 |

### 비용 드라이버/비용 효율 포인트(스토리지 관점)

- “싸게”는 곧 “요구 신호를 만족하면서”다: 랜덤 IOPS가 병목인데 HDD(st1/sc1)를 고르면 비용은 싸도 정답이 아니다.
- gp3는 성능(IOPS/처리량)을 따로 조절할 수 있어, right sizing처럼 “필요한 만큼만” 맞추는 방향으로 설명하기 좋다.
- io2는 성능/일관성 신호가 강할 때만: 그렇지 않으면 비용만 올라갈 수 있다.

- Exam must-know
  - Key point: IOPS/큐/지연 힌트가 있으면 “EBS 타입 선택/튜닝”이 정답 후보가 된다.
  - Why: 블록 스토리지는 성능 축이 명확하고, gp3는 튜닝 여지가 크다.
  - Alternative: “공유 파일시스템” 요구면 EBS가 아니라 EFS로 간다.

## Quick Comparison Table

| Signal | Best choice | Notes |
|---|---|---|
| 용량은 그대로, 성능만 | gp3 | IOPS/처리량 조절 |
| 높은/일관된 IOPS | io2/io1 | 비용↑ 가능 |

## Exam Traps (확장)

- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`
- “공유 파일시스템”인데 EBS를 고르는 선택지
- “IOPS 병목”인데 스케일업만 고르는 선택지

## Exam Trap Drill (O/X, 1~3분)

- “VolumeQueueLength가 올라가고, 읽기/쓰기 지연이 커진다” → gp3 튜닝/ io2 중 무엇이 먼저 떠오르나요?

## TL;DR (한 줄 정리)

- EBS는 **용량이 아니라 IOPS/처리량**이 핵심이고, “튜닝”이면 **gp3**, “일관된 고IOPS”면 **io2**가 신호다.

## References

- References index: `../../references/README.md`
- Exam guide (SAA-C03): `../../references/exam-guide.md`
- Glossary: `../../references/glossary.md`
- AWS services list: `../../references/aws-services.md`
- Exam keypoints: `../../exam-keypoints.md`
- Exam trap bank: `../../exam-trap-bank.md`

## Back

- `./README.md`
