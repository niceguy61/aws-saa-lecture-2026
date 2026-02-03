# Hands-on Lab - Step 2

## Step 2: docker-compose.yml 작성

**목표**: 실시간 코드 동기화 기능을 활성화한 docker-compose.yml 구성

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 서비스 정의
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - type: bind
        source: ./web
        target: /app/web
        watch: true
    command: npm start
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
docker-compose.yml 파일 생성 완료
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
cat docker-compose.yml
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 'volumes' 설정 시 경로 오류
해결: 'web' 디렉토리가 존재하는지 확인 후 경로 수정

</details>

