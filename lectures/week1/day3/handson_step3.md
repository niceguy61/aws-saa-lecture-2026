# Hands-on Lab - Step 3

## Step 3: 컨테이너 실행

**목표**: 포트 매핑 및 bind mount 설정으로 컨테이너 실행

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker run -d --name dev-container -p 3000:3000 \
  -v $(pwd):/app \
  my-node-app
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Container ID 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps | grep dev-container
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 포트 충돌 → 'docker ps --format "{{.Port}}"'로 포트 확인
- 문제: 파일 권한 → 'docker run -v $(pwd):/app:z'로 SELinux 설정

</details>

