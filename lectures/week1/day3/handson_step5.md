# Hands-on Lab - Step 5

## Step 5: 실시간 동기화 테스트

**목표**: src/index.js 수정 후 컨테이너 반영 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
echo "console.log('변경됨');" >> src/index.js
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
docker logs에서 변경 사항 반영 확인
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs dev-container | grep '변경됨'
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 변경 사항 없음 → 'docker exec dev-container ls /app'로 파일 확인
- 문제: 파일 손실 → 'docker commit dev-container my-node-app'로 컨테이너 저장

</details>

