# Hands-on Lab - Step 6

## Step 6: 컨테이너/이미지 정리 (stop, rm, rmi)

**목표**: 실습 후 자원을 정리하는 습관을 들이고 컨테이너와 이미지의 차이를 다시 확인합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker stop web
docker rm web

docker images | head -n 10
docker rmi nginx:alpine
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
web
web
Untagged: nginx:alpine
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps -a
docker images | grep nginx || true
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `image is being used by running container` -> 먼저 컨테이너 stop/rm 후 rmi
- `grep: command not found` -> Git Bash/WSL 사용 또는 `docker images`에서 확인

</details>

