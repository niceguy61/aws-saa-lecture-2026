# 6교시 - 핸즈온 2: logs, exec, stop, remove

## 목표

실행 중인 컨테이너를 관찰하고 안전하게 중지/삭제한다. 운영에서 중요한 것은 "컨테이너가 있다"가 아니라 "어떤 증거로 상태를 판단했는가"다.

## 성공 기준

- `docker logs`로 HTTP 요청 로그를 확인한다.
- `docker exec`로 컨테이너 내부에서 명령을 실행한다.
- `docker stop`으로 정상 중지한다.
- `docker rm`으로 stopped container를 삭제한다.
- 삭제 전후 상태를 `docker ps -a`로 확인한다.

## Prerequisites

5교시에서 만든 컨테이너가 실행 중이어야 한다.

```bash
docker ps --filter name=w2d1-web
```

실행 중이 아니라면 다시 실행한다.

```bash
docker run -d --name w2d1-web -p 8080:80 nginx:1.27-alpine
```

## Step 1. 요청을 만들어 로그 재료 만들기

브라우저에서 `http://localhost:8080`을 새로고침하거나 다음 명령을 실행한다.

```bash
curl http://localhost:8080
```

## Step 2. 로그 확인

```bash
docker logs --tail 20 w2d1-web
```

예상 결과의 핵심:

```text
"GET / HTTP/1.1" 200
```

로그에서 확인할 것:

- 요청 method: `GET`
- 요청 path: `/`
- 응답 status code: `200`
- user agent: `curl` 또는 브라우저 정보

## Step 3. 컨테이너 내부 명령 실행

nginx 버전을 확인한다.

```bash
docker exec w2d1-web nginx -v
```

예상 결과:

```text
nginx version: nginx/1.27.5
```

실행 중인 프로세스도 확인한다.

```bash
docker exec w2d1-web ps
```

예상 결과에는 nginx master process와 worker process가 보인다.

```text
PID   USER     TIME  COMMAND
1     root      ...  nginx: master process nginx -g daemon off;
```

## Step 4. 컨테이너 중지

```bash
docker stop w2d1-web
```

예상 결과:

```text
w2d1-web
```

Running 목록에서는 사라진다.

```bash
docker ps --filter name=w2d1-web
```

하지만 모든 컨테이너 목록에는 남아 있다.

```bash
docker ps -a --filter name=w2d1-web
```

예상 상태:

```text
STATUS: Exited ...
```

## Step 5. 컨테이너 삭제

삭제 전 이름을 다시 확인한다.

```bash
docker ps -a --filter name=w2d1-web
```

삭제한다.

```bash
docker rm w2d1-web
```

예상 결과:

```text
w2d1-web
```

삭제 확인:

```bash
docker ps -a --filter name=w2d1-web
```

출력이 없으면 삭제된 것이다.

## rm 명령 주의

여기서 사용하는 명령은 `docker rm`이다. Docker가 관리하는 stopped container 객체를 삭제한다.

Linux의 `rm`은 파일을 삭제하는 명령이다. 특히 `rm -rf /`처럼 root 경로를 대상으로 하는 명령은 시스템을 망가뜨릴 수 있으므로 절대 실행하지 않는다. 수업 중 삭제가 필요하면 먼저 "무엇을 삭제하는 명령인가"를 말로 설명한 뒤 실행한다.

## Troubleshooting

| 증상 | 원인 후보 | 해결 |
|---|---|---|
| `No such container` | 이름이 다르거나 이미 삭제됨 | `docker ps -a`로 이름 확인 |
| `You cannot remove a running container` | 아직 실행 중 | `docker stop w2d1-web` 후 삭제 |
| `docker exec` 실패 | 컨테이너가 실행 중이 아님 | `docker ps`로 상태 확인 |
| 로그가 비어 있음 | 아직 요청을 보내지 않음 | 브라우저 접속 또는 `curl` 실행 |

## 오늘의 운영 관점

운영에서 "컨테이너가 이상합니다"라는 말은 부족하다. 다음처럼 증거를 붙여야 한다.

```text
w2d1-web 컨테이너는 현재 Exited 상태다.
nginx 요청 로그는 200까지 남았고,
stop 이후에는 docker ps에서 사라졌지만 docker ps -a에는 Exited로 남았다.
```
