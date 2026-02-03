# Hands-on Lab - Step 2

## Step 2: 이미지 빌드

**목표**: Dockerfile을 기반으로 이미지 생성

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker build -t node-app:latest .
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
docker images | grep node-app
```

</details>

