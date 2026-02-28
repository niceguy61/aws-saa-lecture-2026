# CloudWatch로 성능 병목 1차 진단하기

## 소개 (이게 뭔가요?)

- CloudWatch는 AWS 리소스의 지표/로그/알람을 모으는 기본 관측(Observability) 계층이고, 시험에서는 “무엇을 먼저 확인할지”를 자주 묻는다.

## 고객 사례 (스토리, 600~1000자)

![고객 사례 삽화 - CloudWatch로 병목 찾기](../../assets/scenario_image/w3d1s2.png)

서비스가 느려졌다는 신고가 들어오면, 팀은 보통 CPU 그래프부터 연다. 실제로 CPUUtilization이 높으면 원인이 단순한 편이라 “인스턴스 스펙 업”으로 끝날 때도 있다. 문제는 CPU가 낮은데도 느린 케이스다. 이때 경험이 부족하면 “그럼 더 큰 인스턴스면 되겠지”로 가고, 비용만 늘어난다.

한 번은 배치 작업이 시작될 때마다 지연이 튀었는데, CPU는 30% 수준이었다. CloudWatch를 더 보니 EBS VolumeQueueLength가 올라가고, VolumeWriteBytes가 꾸준히 늘었다. 즉 병목은 CPU가 아니라 디스크 I/O였다. 또 다른 날엔 T 계열 인스턴스에서 CPU는 70%대로 유지되다가, CPUCreditBalance가 바닥나면서 지연이 급격히 악화됐다. “CPU가 높다”가 아니라 “크레딧이 소진돼 스로틀링된다”가 정답 신호였던 셈이다.

또 중요한 포인트는 “지표 1개”가 아니라 “세트”로 보는 습관이다. CPU가 높으면 네트워크도 같이 포화인지(NetworkIn/Out), 디스크 큐가 같이 늘었는지(QueueLength), 크레딧이 같이 떨어졌는지(CPUCreditBalance)를 같이 본다. 이렇게 보면 “원인처럼 보이는 현상”과 “진짜 병목”을 분리하기가 훨씬 쉬워진다.

결국 CloudWatch는 정답을 ‘맞히는’ 도구가 아니라, 병목 축을 ‘좁혀가는’ 도구다. CPU만 보지 말고, 스토리지/네트워크/크레딧 지표로 교차 확인하면 “정말 컴퓨트가 문제인지”를 빠르게 가를 수 있다. 지금 문제에서 힌트는 CPU 그래프일까요, 아니면 I/O/크레딧 같은 보조 지표일까요?

## Impact 범위 (어디에 영향을 주나?)

- Operations: 진단 속도/알람 품질이 운영 난이도를 좌우한다.
- Performance: 병목 축을 잘못 잡는 실수를 줄인다.
- Cost: 불필요한 스펙 업/과한 확장을 막는다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-3-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-Perf%20diagnosis-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: CloudWatch](https://img.shields.io/badge/Service-CloudWatch-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 3: Design High-Performing Architectures
- Objectives: 컴퓨트/스토리지/네트워크 병목을 지표로 구분할 수 있는지

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- 시험은 “무엇을 먼저 확인하나”를 통해, 병목 축을 제대로 잡는지 확인한다.

## Core Concepts

- 기본 진단 루틴(시험형)
  - CPU: `CPUUtilization`
  - T 계열: `CPUCreditBalance`, `CPUCreditUsage`
  - EBS: `VolumeReadOps/WriteOps`, `VolumeQueueLength`, `VolumeReadBytes/WriteBytes`
  - Network: `NetworkIn`, `NetworkOut`

```mermaid
flowchart LR
  Problem[성능 이슈] --> CW[CloudWatch 지표]
  CW --> CPU[CPU 높음?]
  CW --> IO["EBS Queue/지연?"]
  CW --> NET[네트워크 포화?]
  CW --> T[T 크레딧 소진?]
```

## Deep Dive

### 1차 진단 루틴: “병목 축”을 빠르게 좁히기

시험에서 CloudWatch는 “정답 지표 1개”를 묻기보다, **무엇을 먼저 보고 어떤 축으로 결론을 내리는지**를 본다. 다음처럼 축을 나누면 소거가 쉬워진다.

| 신호(문장/지표) | 가능성이 큰 병목 축 | CloudWatch에서 먼저 볼 것 |
|---|---|---|
| CPU가 지속적으로 높음 | 컴퓨트 | `CPUUtilization` |
| CPU는 낮은데 느림 + 큐가 증가 | 스토리지 I/O | `VolumeQueueLength`, Read/WriteBytes |
| T 계열 + 특정 시점부터 급격히 느림 | 크레딧 스로틀링 | `CPUCreditBalance`, `CPUCreditUsage` |
| 특정 시간대만 느림 + 네트워크 급증 | 네트워크/대역 | `NetworkIn/Out` |

### Best Practices (시험 포인트로 자주 등장)

- CPU가 높지 않다고 해서 “컴퓨트가 아니다”로 끝내지 말고, **크레딧(T 계열)** 같은 “숨은 제한”을 같이 확인한다.
- “지표 1개로 결론”을 내리면 함정에 빠진다. **CPU + I/O + Network**를 같이 보며 교차 검증하는 선택지가 보이면 정답 후보가 된다.
- CloudWatch Alarm은 “이상 감지 후 알림”의 기본 도구다. 문제에서 “자동 알림/임계치”가 나오면 Alarm을 떠올리는 흐름이 자연스럽다.

### 지표(Metrics) vs 로그(Logs) vs 알람(Alarms)

- “값이 숫자(시계열)로 측정된다” → Metrics/Alarms 축
- “문장/이벤트를 검색해서 원인을 찾는다” → Logs/Logs Insights 축

시험은 이 둘을 섞어 “알람은 로그로 만든다”처럼 보이게 하는 선택지를 낼 수 있으니, 데이터 형태로 분리해두면 소거가 빨라진다.

### 핵심 정리 (Deep Dive)

- CloudWatch는 병목을 ‘맞히는’ 도구가 아니라, 병목 축을 ‘좁히는’ 도구다.
- “CPU만” 보지 말고 **I/O/네트워크/크레딧**으로 교차 확인한다.

## Exam Traps (확장)

- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`
- CPUUtilization 하나만으로 병목을 단정하는 선택지
- T 계열인데 크레딧 지표를 무시하는 선택지
- EBS 병목 신호인데 “네트워크”로만 몰아가는 선택지

## Exam Trap Drill (O/X, 1~3분)

- “CPU는 30%인데, VolumeQueueLength가 크게 올라간다” → 병목은 CPU일까요, 스토리지 I/O일까요?

## TL;DR (한 줄 정리)

- CloudWatch는 **CPU만 보는 게 아니라 크레딧/스토리지/네트워크 지표로 교차 확인**해서 병목 축을 빠르게 좁히는 게 핵심이다.

## References

- References index: `../../references/README.md`
- Exam guide (SAA-C03): `../../references/exam-guide.md`
- Glossary: `../../references/glossary.md`
- AWS services list: `../../references/aws-services.md`
- Exam keypoints: `../../exam-keypoints.md`
- Exam trap bank: `../../exam-trap-bank.md`

## Back

- `./README.md`
