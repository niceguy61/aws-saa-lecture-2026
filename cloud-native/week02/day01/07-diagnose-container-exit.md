# 7교시 - 진단 랩: 컨테이너가 바로 종료되는 이유

## 목표

컨테이너가 바로 종료되는 상황을 일부러 만들고, `docker ps -a`, `docker logs`, exit code를 근거로 원인을 설명한다.

## 한 줄 요약

컨테이너는 내부의 main process가 끝나면 종료된다. 서버처럼 계속 떠 있는 프로세스가 없으면 컨테이너도 계속 떠 있지 않는다.

## 왜 이런 일이 생기나

컨테이너는 VM처럼 "켜진 컴퓨터"가 아니다. 컨테이너의 생명주기는 내부 main process와 강하게 연결된다.

예를 들어 다음 명령은 메시지를 출력하고 끝난다.

```bash
docker run --name w2d1-once nginx:1.27-alpine nginx -v
```

nginx 버전을 출력한 뒤 main process가 끝났으므로 container도 종료된다.

## Step 1. 바로 끝나는 컨테이너 만들기

```bash
docker run --name w2d1-once nginx:1.27-alpine nginx -v
```

예상 결과:

```text
nginx version: nginx/1.27.5
```

공식 nginx 이미지는 시작 전에 `/docker-entrypoint.sh` 로그를 함께 출력할 수 있다. 이 로그가 보여도 이상한 것이 아니다. 핵심은 마지막에 nginx version이 출력되고 컨테이너가 종료된다는 점이다.

## Step 2. Running 목록에서 확인

```bash
docker ps --filter name=w2d1-once
```

예상:

```text
출력이 없거나 header만 보인다.
```

Running 상태가 아니기 때문이다.

## Step 3. 전체 목록에서 확인

```bash
docker ps -a --filter name=w2d1-once
```

예상 결과의 핵심:

```text
STATUS: Exited (0) ...
NAMES: w2d1-once
```

`Exited (0)`은 프로세스가 오류 없이 끝났다는 뜻이다. 실패가 아니라 "할 일을 끝내고 종료"한 것이다.

## Step 4. 로그 확인

```bash
docker logs w2d1-once
```

예상 결과:

```text
nginx version: nginx/1.27.5
```

여기에도 `/docker-entrypoint.sh` 로그가 함께 섞일 수 있다. 로그를 읽을 때는 "entrypoint가 준비 작업을 했고, 마지막에 내가 실행한 명령 결과가 남았다"로 해석한다.

로그는 컨테이너가 종료된 뒤에도 확인할 수 있다. 삭제하면 로그도 함께 사라진다.

## Step 5. 실패하는 컨테이너 만들기

이번에는 일부러 존재하지 않는 nginx option을 실행한다.

```bash
docker run --name w2d1-fail nginx:1.27-alpine nginx --not-a-real-option
```

예상 결과:

```text
nginx: invalid option: "-"
```

nginx는 존재하지 않는 option을 만나면 위와 비슷한 오류를 남기고 종료한다.

전체 목록에서 확인한다.

```bash
docker ps -a --filter name=w2d1-fail
```

예상 결과의 핵심:

```text
STATUS: Exited (1) ...
```

`Exited (1)`은 프로세스가 오류로 끝났다는 신호다.

로그를 확인한다.

```bash
docker logs w2d1-fail
```

## Step 6. 비교 정리

| 컨테이너 | 실행한 명령 | 상태 | 의미 |
|---|---|---|---|
| `w2d1-once` | `nginx -v` | `Exited (0)` | 정상 종료 |
| `w2d1-fail` | 잘못된 option | `Exited (1)` | 오류 종료 |
| `w2d1-web` | nginx server | `Up` | 계속 실행 중 |

## Cleanup

오늘 만든 진단용 컨테이너를 삭제한다.

```bash
docker rm w2d1-once
docker rm w2d1-fail
```

만약 `w2d1-web`이 남아 있다면 함께 정리한다.

```bash
docker stop w2d1-web
docker rm w2d1-web
```

정리 확인:

```bash
docker ps -a --filter name=w2d1-
```

출력이 없으면 오늘 실습 컨테이너가 정리된 것이다.

## 진단 보고 문장

아래 형식으로 오늘의 진단 결과를 한 문장으로 써본다.

```text
컨테이너 ________은/는 ________ 명령을 실행했고,
docker ps -a에서 ________ 상태였으며,
logs에는 ________가 남아 있었으므로
원인은 ________이다.
```

## 다음 교시 연결

오늘은 이미 준비된 image를 실행했다. 내일은 우리가 직접 Dockerfile을 작성해서 image를 만든다.
