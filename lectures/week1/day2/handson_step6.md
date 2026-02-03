# Hands-on Lab - Step 6

## Step 6: 이미지 재빌드

**목표**: package.json 변경 시 이미지 재빌드 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
# package.json 수정 후
docker-compose build --no-cache
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Rebuilding 'node-app' 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker images | grep node-app
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 캐시 문제 → '--no-cache' 옵션 강제 재빌드
- 문제: 빌드 실패 → 'docker-compose build --force-recreate'

</details>

