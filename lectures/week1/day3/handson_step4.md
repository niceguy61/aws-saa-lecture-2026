# Hands-on Lab - Step 4

## Step 4: 로그 확인

**목표**: nodemon 로그를 통해 개발 서버 실행 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker logs -f dev-container
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
nodemon -L src/index.js 로그 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs dev-container | head -n 20
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 로그 없음 → 'docker logs --tail 100 dev-container'로 전체 로그 확인
- 문제: 컨테이너 정지 → 'docker start dev-container'로 재시작

</details>

