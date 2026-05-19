# 1주차 5일차 - Cloud와 DevOps 용어

## 목표

초급 컴퓨팅 개념을 Cloud와 DevOps 용어로 연결한다. 1주차 마지막 날의 목표는 용어를 많이 외우는 것이 아니라, “내 노트북에서 되던 앱이 어떻게 다른 사람이 쓰는 서비스가 되는가”를 설명하는 것이다.

## 오늘 배울 내용

- Cloud, Region, 계정, VM, Container의 의미
- 배포, 릴리스, 롤백의 기본 흐름
- DevOps가 반복 가능성과 피드백을 중시하는 이유
- Docker, Kubernetes, AWS가 이후 수업에서 어떻게 연결되는지
- 코드 변경이 실행 중인 서비스가 되는 과정을 팀별로 설명하는 방법

## 난이도 기준

첫 주 마무리이므로 비전공자도 따라올 수 있게 용어를 쉬운 말로 바꾼다. 오후 팀 미션은 70% 정도가 완성 가능한 수준을 목표로 하되, 빠른 팀은 Docker 이미지/컨테이너까지 연결해본다.

| 수준 | 오늘의 목표 |
|---|---|
| 비전공/고등학생 | Cloud, 배포, 롤백, health check를 쉬운 말로 설명한다 |
| 대학생/부트캠프 수준 | 코드 변경에서 서비스 확인까지의 흐름을 다이어그램으로 만든다 |
| 주니어 엔지니어 | 실패 상황, 로그, 롤백, Docker 연결까지 포함해 설명한다 |

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | [1주차 복습과 용어 워밍업](01-week1-review-terms-warmup.md) |
| 10:00-10:50 | 2교시 | [자격증식 암기 없는 Cloud 기초](02-cloud-basics-no-memorization.md) |
| 11:00-11:50 | 3교시 | [배포, 롤백, 릴리스 이야기](03-deploy-rollback-release.md) |
| 12:00-12:50 | 4교시 | [DevOps 피드백 루프](04-devops-feedback-loop.md) |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | [미션 준비: 배포 설명하기](05-mission-prep-explain-deployment.md) |
| 15:00-15:50 | 6교시 | [팀 미션: 다이어그램과 스토리 만들기](06-team-mission-diagram-story.md) |
| 16:00-16:50 | 7교시 | [팀별 공유와 피드백](07-team-share-feedback.md) |
| 17:00-17:50 | 8교시 | [Week1 핵심 정리와 Docker Live QA](08-week1-quiz-docker-preview.md) |

## 랩/미션/데모

코드 변경이 실행 중인 서비스가 되기까지의 배포 이야기를 팀별로 설명한다. 실패 또는 롤백 상황을 하나 포함한다.

팀 미션 템플릿:

- [mission/deployment-story-template.md](mission/deployment-story-template.md)

핵심 미션:

- 작은 웹앱 변경 상황을 하나 고른다.
- 정상 배포 흐름을 만든다.
- 실패 상황 1개를 포함한다.
- health check, 로그, 설정, 롤백을 포함한다.
- 2주차 Docker와 연결되는 지점을 한 문장으로 적는다.

## 오늘 나오는 핵심 용어

| 용어 | 쉬운 뜻 |
|---|---|
| Cloud | 필요한 컴퓨팅 자원을 빌려 쓰고 API로 다루는 환경 |
| Region | 클라우드 자원이 위치한 큰 지역 |
| VM | 가상의 컴퓨터 |
| Container | 앱 실행 환경을 가볍게 포장한 실행 단위 |
| Deploy | 변경을 실행 환경에 반영하는 일 |
| Release | 사용자가 새 버전을 쓰게 하는 일 |
| Rollback | 문제가 생겼을 때 이전 상태로 되돌리는 일 |
| DevOps | 개발과 운영의 피드백을 짧게 만드는 방식 |

## Docker 이론 세션 위치

1주차에는 Docker를 깊게 실습하지 않는다. 대신 Day1 설치 확인, Day2 개념 미리보기, Day5 8교시 이론 예고로 2주차를 준비한다.

2주차부터는 Docker 명령을 실제로 많이 실행한다. 그래서 Day5 마지막 시간에는 image, container, registry, tag, VM과 container 차이, 안전한 삭제 규칙을 먼저 정리한다.

## 보충/심화 자료

- 초급 Cloud 용어집
- DevOps 루프 다이어그램
- 심화: VM vs Container vs Managed Service
