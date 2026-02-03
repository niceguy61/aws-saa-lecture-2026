# Hands-on Lab - Step 3

## Step 3: Docker 이미지 빌드

**목표**: Dockerfile을 기반으로 이미지 생성

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 이미지 빌드 명령어
docker build -t my-node-app .
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Successfully built <hash>
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker images | grep my-node-app
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 의존성 설치 실패
해결: 'npm install' 명령어를 별도로 실행해 보고, .dockerignore 파일을 점검

</details>

