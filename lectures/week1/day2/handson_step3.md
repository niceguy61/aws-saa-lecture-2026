# Hands-on Lab - Step 3

## Step 3: nginx 컨테이너 실행 + 포트 매핑

**목표**: 웹 서버 컨테이너를 백그라운드로 실행하고, 호스트 포트를 통해 접근합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker pull nginx:alpine
docker run -d --name web -p 8080:80 nginx:alpine

# 접속 테스트
curl -I http://localhost:8080
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
HTTP/1.1 200 OK
Server: nginx
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `bind: address already in use` -> 다른 호스트 포트 사용(예: `-p 8081:80`) 또는 점유 프로세스 종료
- `curl: (7) Failed to connect` -> 컨테이너 상태/포트 매핑 확인(`docker ps`, `docker logs`)

</details>

