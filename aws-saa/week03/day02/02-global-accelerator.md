# Global Accelerator: Anycast로 네트워크 경로를 최적화한다

## 소개 (이게 뭔가요?)

- Global Accelerator(GA)는 Anycast 기반 “글로벌 엔트리 포인트”로, TCP/UDP 트래픽의 경로 최적화와 헬스 기반 전환을 제공한다(캐시 서비스가 아니다).

## 고객 사례 (스토리, 600~1000자)

![고객 사례 삽화 - Global Accelerator Anycast 경로](../../assets/scenario_image/w3d2s2.png)

실시간 기능이 있는 서비스(예: 게임, 음성/영상 통신, 거래 시스템)는 “정적 콘텐츠 캐시”만으로는 체감이 좋아지지 않는다. 해외 사용자는 API 응답이 들쭉날쭉하고, ISP/인터넷 구간에서 라우팅이 꼬이는 날엔 지연이 갑자기 늘어난다. 팀은 “CDN을 붙이자”고 하지만, 이 트래픽은 캐시할 성격이 아니고, 무엇보다 고객사가 “고정 IP 화이트리스트”를 요구한다. CloudFront만으로는 요구를 깔끔하게 만족시키기 어렵다.

여기서 GA가 들어온다. 사용자는 가까운 엣지(엔트리 포인트)로 붙고, 이후 구간은 AWS 글로벌 네트워크 백본을 타고 최적 경로로 목적지(멀티 리전 엔드포인트)까지 간다. 게다가 GA는 고정 IP를 제공하고, 엔드포인트 헬스에 따라 트래픽을 전환할 수 있다. 즉 “캐시로 빠르게”가 아니라 “경로를 안정적으로” 빠르게 만드는 방식이다.

또 하나의 힌트는 “전 세계에서 동일한 엔드포인트로 접속해야 한다”는 문장이다. Route 53 라우팅만으로도 어느 정도는 풀 수 있지만, GA는 고정 IP + 백본 경로 최적화라는 성격이 더 강하다. 그래서 “캐시”와는 결이 다르다.

시험에서 GA가 등장하면, 대개 문장 속에 힌트가 있다. “TCP/UDP”, “고정 IP”, “멀티 리전 failover”, “네트워크 경로 최적화” 같은 신호다. 지금 요구는 캐시 문제일까요, 경로/엔트리 포인트 문제일까요?

## Impact 범위 (어디에 영향을 주나?)

- Performance: 글로벌 RTT/라우팅 변동의 영향을 줄인다.
- Reliability: 헬스 기반 전환으로 멀티 리전 가용성을 높일 수 있다.
- Operations: 고정 IP 요구(화이트리스트) 대응이 쉬워진다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-3-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-3.4%20Network%20arch-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Global%20Accelerator](https://img.shields.io/badge/Service-Global%20Accelerator-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 3: Design High-Performing Architectures
- Objectives: 캐시 vs 경로 최적화 요구를 구분할 수 있는지

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- GA를 CloudFront와 같은 “캐시”로 착각하면 바로 오답이 된다.

## Core Concepts

- GA 핵심 키워드(시험형)
  - Anycast 고정 IP
  - TCP/UDP 트래픽
  - AWS 글로벌 네트워크 백본 경로
  - 엔드포인트 헬스 기반 전환

## Quick Comparison Table

| Topic | CloudFront | Global Accelerator |
|---|---|---|
| 목적 | 콘텐츠/응답 캐시 | 네트워크 경로 최적화 |
| 프로토콜 감각 | 주로 HTTP(S) | TCP/UDP |
| 대표 신호 | 정적/캐시 가능, TTL | 고정 IP, 멀티 리전, 경로 |

## Exam Traps (확장)

- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`
- “캐시 가능한 정적 콘텐츠”인데 GA를 고르는 선택지
- “고정 IP 화이트리스트” 요구인데 CloudFront만 제시하는 선택지

## Exam Trap Drill (O/X, 1~3분)

- “고정 IP가 필요하고, 글로벌 사용자에게 TCP 트래픽 지연을 줄이고 싶다” → GA가 먼저 떠오르나요?

## TL;DR (한 줄 정리)

- Global Accelerator는 **캐시가 아니라 Anycast 기반 경로 최적화/고정 IP/헬스 전환**이 핵심이다.

## References

- References index: `../../references/README.md`
- Exam guide (SAA-C03): `../../references/exam-guide.md`
- Glossary: `../../references/glossary.md`
- AWS services list: `../../references/aws-services.md`
- Exam keypoints: `../../exam-keypoints.md`
- Exam trap bank: `../../exam-trap-bank.md`

## Back

- `./README.md`
