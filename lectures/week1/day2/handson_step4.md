# Hands-on Lab - Step 4

## Step 4: 컨테이너 실행

**목표**: 포트 매핑 및 바인드 마운트 설정

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker run -d -p 3000:3000 --mount type=bind,src=./,target=/app myapp-image
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Container ID 출력됨
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps | grep myapp
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 포트 충돌 → docker ps | grep 3000로 확인
- 문제: 마운트 실패 → 권한 설정 확인: docker run --rm -it --user root myapp-image sh

</details>

