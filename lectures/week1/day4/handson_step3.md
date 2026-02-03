# Hands-on Lab - Step 3

## Step 3: 컨테이너 실행 및 로그 모니터링

**목표**: bind mount 및 포트 매핑으로 개발 서버 실행

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker run -d --name myapp-container \
  -p 3000:3000 \
  --mount type=bind,src=.,target=/app \
  myapp:dev \
  sh -c "npm install && npm run dev"
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
nodemon 로그 출력 (Hello Docker! 메시지 포함)
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs -f myapp-container
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 컨테이너 실행 실패 -> 해결: docker ps -a 확인 후 docker start 명령어 사용
- 문제: 포트 충돌 -> 해결: docker kill myapp-container 후 재실행

</details>

