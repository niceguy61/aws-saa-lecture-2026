# 1주차 2일차 - Cloud Native를 위한 컴퓨팅 기초

## 목표

컨테이너와 웹 서비스를 이해하는 데 필요한 프로세스, 포트, 파일, 환경 변수, 로그 개념을 익힌다.

이 과정에서 웹앱을 다루는 이유는 웹 개발 자체를 깊게 배우기 위해서가 아니다. Cloud Native에서 Docker, Kubernetes, AWS가 실제로 운영하는 대상이 대부분 “요청을 받고 응답하는 서비스”이기 때문이다. 작은 웹앱은 그 서비스를 가장 작고 안전하게 관찰하기 위한 실습 모델이다.

## 오늘 배울 내용

- 프로그램과 프로세스의 차이
- localhost와 포트의 의미
- 파일, 환경 변수, 로그의 역할
- 로컬 애플리케이션을 안전하게 관찰하는 방법

## 사전 준비

- [Python 설치와 확인](00-python-setup.md)

Day2 실습 앱은 Python 3로 실행한다. 터미널에서 `python3 --version`, `python --version`, 또는 `py --version` 중 하나가 동작해야 한다.

## 일일 시간표

| 시간 | 교시 | 인덱스 |
|---|---|---|
| 09:00-09:50 | 1교시 | [전날 복습과 프로그램/프로세스 개념](01-review-process.md) |
| 10:00-10:50 | 2교시 | [포트, localhost, 브라우저 요청](02-port-localhost-request.md) |
| 11:00-11:50 | 3교시 | [파일, 환경 변수, 로그](03-files-env-logs.md) |
| 12:00-12:50 | 4교시 | [작은 웹앱 구조 보기](04-small-webapp-structure.md) |
| 13:00-14:00 | 점심 | 점심시간 |
| 14:00-14:50 | 5교시 | [실습 준비: 작은 웹앱 실행](05-lab-run-small-webapp.md) |
| 15:00-15:50 | 6교시 | [실습: 포트, 요청, 로그 확인](06-lab-port-request-log.md) |
| 16:00-16:50 | 7교시 | [진단: 앱이 열리지 않는 이유 찾기](07-diagnose-app-not-opening.md) |
| 17:00-17:50 | 8교시 | [Day2 핵심 정리와 Docker 개념 Live QA](08-docker-concept-preview.md) |

## 랩/미션/데모

작은 로컬 웹 애플리케이션을 실행하고, 프로세스, 포트, 요청 경로, 로그를 확인한다.

오늘 실습 앱은 프로젝트 결과물이 아니라 관찰 도구다. 브라우저 화면보다 중요한 것은 서버 프로세스, 포트, 요청 경로, 환경 변수, 로그가 어떻게 연결되는지 보는 것이다.

실습 앱:

- [app/server.py](app/server.py)

기본 실행:

```bash
cd cloud-native/week01/day02/app
python3 server.py
```

브라우저에서 `http://localhost:8000`을 연다.

## 보충/심화 자료

- HTTP 기초 노트
- 포트와 localhost 워크시트
- 심화: 프로세스와 소켓 개념
