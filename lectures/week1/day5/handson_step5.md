# Hands-on Lab - Step 5

## Step 5: 네트워크 격리와 연결(`connect`) 체감하기

**목표**: 서로 다른 네트워크에 있는 컨테이너는 기본적으로 통신이 안 되며, 필요할 때만 명시적으로 연결해야 함을 확인한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 두 번째 네트워크 생성
docker network create labnet2

# 2) labnet2에만 붙은 web2 실행
docker run -d --name web2 --label lab=week1-day5 --network labnet2 nginx:alpine

# 3) client(=labnet)에서 web2로 접근 시도(실패가 정상)
docker run --rm --name client2 --label lab=week1-day5 --network labnet busybox sh -c 'wget -qO- http://web2 2>/dev/null || echo "FAILED: not reachable"'

# 4) web2를 labnet에도 추가 연결(connect)한 뒤 다시 시도(성공 기대)
docker network connect labnet web2
docker run --rm --name client3 --label lab=week1-day5 --network labnet busybox sh -c 'wget -qO- http://web2 | head -n 3'
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
FAILED: not reachable

<!DOCTYPE html>
<html>
<head>
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# web2가 어떤 네트워크에 붙었는지 확인
docker inspect web2 --format "Networks={{json .NetworkSettings.Networks}}"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `web2`가 이미 다른 이름으로 존재 -> `docker rm -f web2` 후 재시도
- `wget`이 없음 -> busybox 이미지를 사용했는지 확인(또는 alpine에 curl을 설치해야 하지만 네트워크가 필요)

</details>
