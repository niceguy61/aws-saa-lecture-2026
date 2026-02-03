# Hands-on Lab - Step 4

## Step 4: 로그 확인

**목표**: 애플리케이션 실행 상태 모니터링

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker logs -f node-dev
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
nodemon 시작 로그 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs node-dev | grep 'nodemon'
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 로그 없음 → 'docker logs --tail 100 node-dev'로 전체 로그 확인
- 문제: 실시간 로그 없음 → '--tail -1' 옵션 추가

</details>

