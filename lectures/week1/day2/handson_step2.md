# Hands-on Lab - Step 2

## Step 2: Dockerfile 작성

**목표**: node:24-alpine 기반 Dockerfile 생성

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
cat > Dockerfile <<EOF
FROM node:24-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
EXPOSE 3000
CMD ["sh", "-c", "npm install && npm run dev"]
EOF
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Dockerfile 파일 생성됨
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
ls -l Dockerfile
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 파일 생성 실패 → cat 명령어 사용법 확인
- 문제: 문법 오류 → nano Dockerfile로 편집

</details>

