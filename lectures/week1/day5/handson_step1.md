# Hands-on Lab - Step 1

## 실습 개요

**제목**: Docker 네트워킹 기초 실습: 유저 정의 브리지, DNS(이름 기반 통신), 포트 퍼블리시

**목적**: Docker 네트워킹에서 가장 자주 헷갈리는 3가지를 실습으로 정리합니다.

1. 컨테이너 간 통신은 "같은 네트워크" 위에서 "이름(DNS)"으로 한다
2. 호스트에서 컨테이너로 접근하려면 `-p`로 포트를 퍼블리시해야 한다
3. 컨테이너 내부의 `localhost`는 "자기 자신"이다

**학습 목표**:
- 유저 정의 브리지 네트워크를 만들고 컨테이너를 연결한다
- 컨테이너 이름 기반으로 다른 컨테이너에 HTTP 요청을 보낸다
- 포트 퍼블리시(`-p`)로 호스트에서 컨테이너 서비스를 접근한다
- `network inspect/connect/disconnect`로 연결 관계를 확인/변경한다

**예상 소요 시간**: 60-90분

**난이도**: Beginner/Intermediate

### 실습 흐름도

```mermaid
flowchart LR
  A[labnet 생성] --> B[web 컨테이너 실행]
  B --> C[client 컨테이너로 web 접근]
  C --> D[-p로 호스트 공개]
  D --> E[inspect로 IP/DNS 확인]
  E --> F[connect/disconnect로 격리 체감]
  F --> G[정리(cleanup)]
```

## 사전 요구사항

<details>
<summary>사전 요구사항 보기</summary>

- Docker Desktop 설치(Windows/macOS)
  - 공식: https://docs.docker.com/desktop/install/
- (Linux) Docker Engine 설치
  - 공식: https://docs.docker.com/engine/install/
- 네트워크/포트 관련 문서
  - 네트워킹 개요(공식): https://docs.docker.com/network/
  - bridge 드라이버(공식): https://docs.docker.com/network/drivers/bridge/
  - `docker network`(공식): https://docs.docker.com/reference/cli/docker/network/
  - `docker run` 포트 퍼블리시(공식): https://docs.docker.com/reference/cli/docker/container/run/#publish-or-expose-port--p---expose
- HTTP 확인 도구(선택: curl)
  - 공식: https://curl.se/docs/

</details>

## 환경 설정

<details>
<summary>환경 설정 보기</summary>

- Docker 동작 확인: `docker info`
  - 공식: https://docs.docker.com/reference/cli/docker/system/info/
- 안전한 정리를 위한 라벨 사용
  - 본 실습 컨테이너에는 `--label lab=week1-day5`를 부여합니다.

</details>

---

## Step 1: 유저 정의 브리지 네트워크 생성 + 웹 컨테이너 실행

**목표**: 유저 정의 브리지 네트워크 `labnet`을 만들고, 같은 네트워크에 nginx 웹 컨테이너를 실행한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 네트워크 생성
docker network create labnet

# 2) 네트워크 목록 확인
docker network ls | head -n 20

# 3) web 컨테이너 실행(포트 퍼블리시는 아직 하지 않음)
docker run -d --name web --label lab=week1-day5 --network labnet nginx:alpine

# 4) 상태 확인
docker ps --filter name=web
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
NETWORK ID     NAME      DRIVER    SCOPE
...            labnet    bridge    local

CONTAINER ID   IMAGE         STATUS         NAMES
...            nginx:alpine  Up ...         web
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# web이 labnet에 붙었는지 확인
docker inspect web --format "Networks={{json .NetworkSettings.Networks}}"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `network create`에서 이름 충돌 -> 기존 네트워크 삭제 또는 다른 이름 사용: `docker network rm labnet`
- `Unable to find image 'nginx:alpine' locally` 이후 pull 실패 -> 네트워크/프록시 확인(공식: https://docs.docker.com/network/proxy/)

</details>
