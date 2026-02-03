# Hands-on Lab - Step 3

## Step 3: 컨테이너 실행

**목표**: 포트 매핑 및 바인드 마운트 설정으로 개발 서버 실행

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker run -d --name node-dev -p 3000:3000 -v $(pwd):/app node-app:latest
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
docker ps | grep node-dev
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 포트 충돌 → '-p 3001:3000'으로 포트 변경
- 문제: 마운트 실패 → 'docker run --privileged' 추가

</details>

