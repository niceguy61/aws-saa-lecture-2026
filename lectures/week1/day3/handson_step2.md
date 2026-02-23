# Hands-on Lab - Step 2

## Step 2: 이미지 실행 및 웹 응답 확인

**목표**: Step 1에서 만든 이미지를 컨테이너로 실행하고, 로컬 포트 바인딩으로 실제 응답을 확인한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 컨테이너 실행(백그라운드) + 포트 바인딩
docker run --rm -d --name img-web -p 8080:80 img-lab:web-v1

# 상태 확인
docker ps --filter name=img-web

# 브라우저 또는 curl로 응답 확인
curl -s http://localhost:8080 | head

# 컨테이너 내부 파일 확인(선택)
docker exec img-web ls -la /usr/share/nginx/html
docker exec img-web cat /usr/share/nginx/html/index.html
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
CONTAINER ID   IMAGE            COMMAND                  STATUS          PORTS                  NAMES
...            img-lab:web-v1   "/docker-entrypoint.…"   Up ... seconds  0.0.0.0:8080->80/tcp   img-web

<h1>Hello Docker Image</h1>
...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 응답 코드만 확인
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080

# nginx 프로세스가 살아있는지 확인(선택)
docker exec img-web ps
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `bind: address already in use` -> 8080 포트를 사용 중인 프로세스가 있는지 확인 후 다른 포트로 실행(예: `-p 18080:80`)
- `curl: (7) Failed to connect` -> 컨테이너가 바로 종료되었는지 `docker ps -a`로 확인, 방화벽/프록시 환경 점검
- `Conflict. The container name "/img-web" is already in use` -> 기존 컨테이너 제거(`docker rm -f img-web`) 후 재시도

</details>
