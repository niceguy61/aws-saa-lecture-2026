# Hands-on Lab - Step 6

## Step 6: 실시간 파일 동기화(watch 모드)

**목표**: 파일 변경 시 자동 재빌드 설정

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker run -d --name dev-env -v ./app:/app -e CHOKIDAR_USEPOLLING=true node:20-alpine sh -c "npm install && npm run dev" # watch 모드 활성화
docker logs -f dev-env # 로그 모니터링
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
파일 변경 시 'File changed' 로그 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
echo "test" >> ./app/test.txt
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 변경 감지 실패 → CHOKIDAR_USEPOLLING=true 설정 확인
- 문제: 로그 출력 없음 → docker logs --tail 100 dev-env 확인

</details>

