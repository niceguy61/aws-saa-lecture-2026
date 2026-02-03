# Hands-on Lab - Step 2

## Step 2: Docker Compose 구성

**목표**: bind mount 및 watch 모드 설정

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# docker-compose.yml 파일 작성
version: '3.8'
services:
  web:
    build: .
    volumes:
      - type: bind
        source: ./src/web
        target: /app/web
        read_only: false
      - type: bind
        source: ./package.json
        target: /app/package.json
        read_only: false
    command: npm start
    environment:
      - NODE_ENV=development
    ports:
      - "3000:3000"
    watch:
      - action: sync
        path: ./src/web
        target: /app/web
      - action: sync+restart
        path: ./package.json
        target: /app/package.json
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

