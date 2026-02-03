# Hands-on Lab - Step 3

## Step 3: 이미지 빌드

**목표**: Dockerfile을 기반으로 이미지 생성

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker build -t myapp-image .
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
docker images | grep myapp-image
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 빌드 실패 → docker build --no-cache .로 재시도
- 문제: 권한 오류 → sudo 명령어로 실행

</details>

