# 👉 Hands-on Lab - Step 3

## 👉 Step 3: Dockerfile 작성

**목표**: Node.js 이미지 구성

**명령어**:

```bash
echo 'FROM node:24-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
CMD ["sh", "-c", "npm install && npm run dev"]' > Dockerfile

```

**예상 출력**:

```

Dockerfile 파일 생성됨

```

**확인 방법**:

```bash
cat Dockerfile

```

**문제 해결**:
- 문제: 파일 생성 실패
  해결: sudo 권한으로 다시 시도

