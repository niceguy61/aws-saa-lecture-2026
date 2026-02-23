# Hands-on Lab - Step 5

## Step 5: 컨테이너 내부 진입(exec)과 파일 확인

**목표**: 컨테이너가 "격리된 프로세스/파일시스템"이라는 감각을 익히고 내부를 점검합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker exec -it web sh

# 컨테이너 안에서 실행
nginx -v
ls -la /usr/share/nginx/html | head -n 10
exit
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
nginx version: nginx/...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker exec web sh -c "ls -la /usr/share/nginx/html | head -n 3"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `sh: not found` -> 이미지에 셸이 없을 수 있음(오늘 실습은 `nginx:alpine` 권장)
- `exec failed` -> 컨테이너가 실행 중인지 확인(`docker ps`)

</details>

