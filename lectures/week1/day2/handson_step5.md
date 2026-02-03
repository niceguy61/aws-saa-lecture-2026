# Hands-on Lab - Step 5

## Step 5: 코드 변경 감지

**목표**: 실시간 코드 변경이 컨테이너에 반영되는지 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
# src/index.js 파일 수정 후
docker logs -f node-dev
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
코드 변경 후 재시작 로그 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs node-dev | grep 'restarted'
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 변경 무시 → 'docker exec node-dev ls /app'로 파일 상태 확인
- 문제: 재시작 실패 → 'docker restart node-dev' 명령 실행

</details>

