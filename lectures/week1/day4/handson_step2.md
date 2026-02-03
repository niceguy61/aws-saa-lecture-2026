# Hands-on Lab - Step 2

## Step 2: Docker 이미지 빌드

**목표**: Docker 이미지 생성 및 버전 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker build -t myapp:dev .
docker images | grep myapp
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
myapp:dev 이미지 생성 완료
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker images | grep myapp
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 빌드 실패 -> 해결: docker build --no-cache --progress plain
- 문제: 경로 오류 -> 해결: docker build -t myapp:dev . 명령어 재실행

</details>

