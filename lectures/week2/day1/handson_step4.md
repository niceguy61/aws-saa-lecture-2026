# Hands-on Lab - Step 4

## Step 4: 컨테이너 실행 및 로그 확인

**목표**: 애플리케이션 실행 및 실시간 재구성 테스트

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# Docker Compose로 서비스 실행
docker-compose up -d

# 로그 확인 (nodemon 시작 시까지 대기)
docker logs -f <container-id>
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
nodemon 로그 출력: `nodemon -L src/index.js`
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs <container-id>
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 컨테이너 시작 실패 시: `docker-compose logs` 실행
- 문제: 로그 출력 없을 때: `docker-compose up --build` 재시도

</details>

