# Hands-on Lab - Step 5

## Step 5: 실시간 파일 동기화 테스트

**목표**: src/web 디렉토리 수정 후 재구성 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# src/web 디렉토리에 파일 추가 또는 수정
echo "console.log('Test');" >> src/web/test.js

# 변경사항 확인
docker-compose restart web
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
애플리케이션 자동 재시작 및 변경된 파일 반영
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs -f <container-id>
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 변경사항 반영 안 될 때: `docker-compose down && docker-compose up -d` 재시도
- 문제: 파일 권한 문제 시: `chmod -R 777 src/web` 실행

</details>

