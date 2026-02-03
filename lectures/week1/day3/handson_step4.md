# Hands-on Lab - Step 4

## Step 4: 실시간 개발 서버 실행

**목표**: nodemon을 통한 실시간 재시작 설정

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker exec -it dev-container sh -c "npm install && npm run dev"
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
nodemon 로그 및 서버 시작 메시지
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs -f dev-container
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 서버 시작 실패 → 해결: docker logs dev-container 확인
- 문제: npm 명령어 오류 → 해결: docker exec -it dev-container sh 명령어로 진입 후 수동 실행

</details>

