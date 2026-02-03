# Hands-on Lab - Step 3

## Step 3: 바인드 마운트 설정

**목표**: 호스트 디렉토리와 컨테이너 디렉토리 연결

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker run -d --name web-app -v ./app:/app node:20-alpine sh -c "npm install && npm run dev" # 바인드 마운트 적용
docker inspect web-app | grep Mounts # 마운트 정보 확인
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Host Path: ./app, Container Path: /app 표시
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker exec -it web-app ls /app
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 파일 접근 오류 → docker run 명령어에 --user $(id -u):$(id -g) 추가
- 문제: 마운트 실패 → docker volume ls 확인

</details>

