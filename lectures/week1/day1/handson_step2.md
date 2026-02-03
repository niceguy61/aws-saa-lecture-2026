# Hands-on Lab - Step 2

## Step 2: Dockerfile 작성

**목표**: Node.js 기반 컨테이너 이미지 정의

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
cat > Dockerfile <<EOF
FROM node:18
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
EOF
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Dockerfile 파일 생성 및 내용 확인
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
cat Dockerfile
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 문법 오류 → Dockerfile 공식 문서 참고
- 문제: 파일 생성 실패 → 파일 권한 확인

</details>

