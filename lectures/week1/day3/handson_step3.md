# Hands-on Lab - Step 3

## Step 3: 컨테이너 실행 및 포트 매핑

**목표**: 포트 3000 매핑 및 바인드 마운트 설정

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker run -d -p 3000:3000 -v $(pwd):/app --name dev-container my-node-app:latest
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Container ID 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps --format "{{.ID}} {{.Status}} {{.Ports}}"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 포트 충돌 → 해결: docker ps | grep 3000 명령어로 확인 후 포트 변경
- 문제: 마운트 실패 → 해결: docker inspect dev-container | grep Mounts 확인

</details>

