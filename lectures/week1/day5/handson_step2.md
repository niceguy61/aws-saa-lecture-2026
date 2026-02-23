# Hands-on Lab - Step 2

## Step 2: 컨테이너 이름으로 다른 컨테이너 접근(DNS + 같은 네트워크)

**목표**: 같은 네트워크(`labnet`) 위에서 컨테이너 이름 `web`을 DNS로 해석해 HTTP 요청을 보낸다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# busybox 클라이언트 컨테이너로 web에 요청(컨테이너는 --rm로 자동 삭제)
docker run --rm --name client --label lab=week1-day5 --network labnet busybox sh -c 'wget -qO- http://web | head -n 5'
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# client 컨테이너가 같은 네트워크에 있을 때만 이름(web)로 접근 가능
docker network inspect labnet | head -n 80
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `wget: bad address 'web'` -> web이 `labnet`에 붙어있는지 확인(`docker inspect web`), client도 `--network labnet`인지 확인
- `wget: can't connect to remote host` -> web 컨테이너가 running인지 확인(`docker ps --filter name=web`), web 내부 서비스가 떠있는지 로그 확인

</details>
