# Deep Dive - 트러블슈팅

## 시나리오 1: 호스트에서 컨테이너 서비스에 접속이 안 된다(포트 퍼블리시/바인딩 혼동)

### 트러블슈팅 흐름도

```mermaid
flowchart TD
  A[컨테이너는 running] --> B{포트 퍼블리시(-p) 했나?}
  B -->|No| C[호스트에서 접근 불가]
  B -->|Yes| D{HOST_PORT가 맞나?}
  D -->|No| E[다른 포트로 접속]
  D -->|Yes| F{컨테이너 내부 서비스가 0.0.0.0에 listen?}
  F -->|No| G[localhost 바인딩 문제]
  F -->|Yes| H[방화벽/프록시/라우팅 확인]
```

### 시나리오 설명

<details>
<summary>문제 상황 보기</summary>

- 증상:
  - 컨테이너는 `Up`인데 브라우저/curl로 `http://localhost:PORT` 접속이 실패한다.
  - `Connection refused` 또는 `Failed to connect`가 발생한다.
- 환경: 로컬 Docker Desktop 또는 Linux Docker Engine
- 에러 메시지(예시):
  - `curl: (7) Failed to connect to localhost port 8080: Connection refused`

</details>

### 원인 분석

<details>
<summary>원인 분석 보기</summary>

가장 흔한 원인은 다음 중 하나입니다.

- `-p HOST_PORT:CONTAINER_PORT`를 누락했다: 컨테이너 내부 포트가 열려 있어도 호스트로 자동 노출되지 않습니다.
- 포트를 잘못 열었다: 예를 들어 컨테이너는 80인데 `-p 8080:8080`으로 열어 접근이 실패합니다.
- 애플리케이션이 `127.0.0.1`에만 바인딩되어 있다: 컨테이너 내부에서만 접근 가능한 상태입니다. 일반적으로 컨테이너에서는 `0.0.0.0`에 바인딩해야 외부(호스트/다른 컨테이너)에서 접근할 수 있습니다.
- 호스트 환경 이슈: 방화벽, 프록시, 이미 다른 프로세스가 포트를 점유하고 있는 경우 등

</details>

### 원인 확인 방법

<details>
<summary>진단 단계 보기</summary>

```bash
# Step 1: 포트 매핑이 있는지 확인
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
docker port <container_name>

# Step 2: 컨테이너 로그로 서버가 정상 기동했는지 확인
docker logs --tail 100 <container_name>

# Step 3: 컨테이너 내부에서 로컬로 접속 가능한지 확인(컨테이너 내부 테스트)
# busybox/alpine 계열이면 wget이 있을 수 있음
docker exec <container_name> sh -c 'wget -qO- http://127.0.0.1:80 | head -n 5 || true'

# Step 4: 호스트 포트 점유 여부 점검(환경별 도구 사용)
```

</details>

### 수정 방법

<details>
<summary>해결 단계 보기</summary>

```bash
# Fix 1: 올바른 포트 퍼블리시로 재실행
docker rm -f <container_name>
docker run -d --name <container_name> -p 8080:80 <image>

# Fix 2: 애플리케이션이 0.0.0.0에 바인딩되도록 설정 수정
# (프레임워크/서버에 따라 다름: listen address를 0.0.0.0으로)
```

</details>

### 정상 확인 방법

<details>
<summary>검증 단계 보기</summary>

```bash
# Verify 1: 포트 매핑 확인
docker ps --filter name=<container_name> --format "Ports={{.Ports}}"

# Verify 2: 호스트에서 응답 확인
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
```

</details>

---

## 시나리오 2: 컨테이너끼리 통신이 안 된다(같은 네트워크가 아님 / DNS 이름 해석 실패)

### 트러블슈팅 흐름도

```mermaid
flowchart LR
  A[client 컨테이너] --> B{web에 접근}
  B --> C{같은 네트워크?}
  C -->|No| D[네트워크에 연결(connect)]
  C -->|Yes| E{이름(DNS) 해석?}
  E -->|Fail| F[유저 정의 브리지 사용]
  E -->|OK| G[포트/방화벽/앱 확인]
```

### 시나리오 설명

<details>
<summary>문제 상황 보기</summary>

- 증상:
  - `client` 컨테이너에서 `http://web` 또는 `ping web`이 실패한다.
  - IP를 직접 쓰면 되기도 하지만 이름으로는 안 되는 경우가 있다.
- 환경: 여러 컨테이너를 띄워 서비스 간 통신을 구성하는 로컬 개발 환경
- 에러 메시지(예시):
  - `wget: bad address 'web'`
  - `ping: bad address 'web'`

</details>

### 원인 분석

<details>
<summary>원인 분석 보기</summary>

대표 원인
- 두 컨테이너가 같은 네트워크에 있지 않다: Docker 네트워크는 기본적으로 격리 단위입니다.
- 기본 `bridge` 네트워크만 쓰면서 이름 기반 통신을 기대했다: 이름 기반 DNS는 유저 정의 브리지에서 더 명확하게 동작합니다(권장).
- 컨테이너 내부에서 `localhost`를 썼다: `localhost`는 자기 자신이므로 다른 컨테이너에 접근할 수 없습니다.

</details>

### 원인 확인 방법

<details>
<summary>진단 단계 보기</summary>

```bash
# Step 1: 컨테이너가 어떤 네트워크에 붙어있는지 확인
docker inspect <client> --format "Networks={{json .NetworkSettings.Networks}}"
docker inspect <web> --format "Networks={{json .NetworkSettings.Networks}}"

# Step 2: 네트워크 목록/상세 확인
docker network ls
docker network inspect <network_name> | head -n 80
```

</details>

### 수정 방법

<details>
<summary>해결 단계 보기</summary>

```bash
# Fix 1: 유저 정의 브리지 네트워크 생성 후 컨테이너를 같은 네트워크에 붙인다
docker network create labnet
docker network connect labnet <client>
docker network connect labnet <web>

# Fix 2: 이름 기반 접근 사용(같은 네트워크라면 컨테이너 이름이 DNS로 해석됨)
# 예: http://web:80
```

</details>

### 정상 확인 방법

<details>
<summary>검증 단계 보기</summary>

```bash
# Verify: client에서 web으로 요청이 되는지 확인(환경에 따라 wget/curl 사용)
docker exec <client> sh -c 'wget -qO- http://web:80 | head -n 5 || true'
```

</details>

---
