# Hands-on Lab - Step 6

## Step 6: Docker Compose로 서비스 관리

**목표**: docker-compose.yml 파일로 서비스 관리

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker-compose -f - <<EOF
version: '3'
services:
  web:
    build: .
    ports:
      - '3000:3000'
    volumes:
      - .:/app
    command: sh -c "npm install && npm run dev"
EOF
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
docker-compose 서비스 정의 완료
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

- 문제: YML 문법 오류 -> 해결: docker-compose --validate 명령어 사용
- 문제: 파일 생성 실패 -> 해결: nano docker-compose.yml 파일 직접 작성

</details>

