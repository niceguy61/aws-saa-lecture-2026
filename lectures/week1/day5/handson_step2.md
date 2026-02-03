# Hands-on Lab - Step 2

## Step 2: 컨테이너 포트 맵핑 설정

**목표**: 포트 맵핑을 통해 호스트와 컨테이너 통신 설정

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker run -d --name web-app -p 8080:80 -p 3000:3000 node:20-alpine sh -c "npm install && npm run dev" # 포트 맵핑 및 앱 실행
docker ps # 실행 중인 컨테이너 확인
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
8080:80, 3000:3000 포트 맵핑 확인
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
curl http://localhost:8080
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 포트 충돌 → docker ps --format "{{.Ports}}" 확인
- 문제: 앱 실행 실패 → docker logs web-app 확인

</details>

