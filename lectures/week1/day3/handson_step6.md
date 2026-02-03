# Hands-on Lab - Step 6

## Step 6: 실시간 동기화 검증

**목표**: 파일 변경 시 컨테이너 반영 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
echo "console.log('test');" >> src/index.js
docker logs -f dev-container
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
console.log('test'); 로그 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker exec dev-container ls -l /app/src
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 파일 변경 감지 실패 → 해결: docker-compose.yml에서 watch: true 확인
- 문제: 권한 문제 → 해결: docker exec dev-container chown -R app:app /app 명령어로 권한 변경

</details>

