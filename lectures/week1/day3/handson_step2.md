# Hands-on Lab - Step 2

## Step 2: Docker 이미지 빌드

**목표**: Docker 이미지 생성 및 태그 부여

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker build -t my-node-app:latest .
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

- 문제: 빌드 실패 → 해결: docker build --no-cache --progress plain 명령어로 상세 오류 확인
- 문제: 권한 오류 → 해결: docker build --privileged 옵션 추가

</details>

