# Hands-on Lab - Step 6

## Step 6: 컨테이너 안의 `localhost` 함정 피하기

**목표**: 컨테이너 내부에서 `localhost`는 "자기 자신"이라는 점을 확인하고, 다른 컨테이너에 접근할 때는 이름(web)을 사용해야 함을 확실히 한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# client 컨테이너에서 localhost로 접근(대부분 실패가 정상: client 자신에게 웹서버가 없음)
docker run --rm --name client-local --label lab=week1-day5 --network labnet busybox sh -c 'wget -qO- http://localhost 2>/dev/null || echo "FAILED: localhost is client itself"'

# 같은 client 컨테이너에서 web으로 접근(성공이 정상)
docker run --rm --name client-web --label lab=week1-day5 --network labnet busybox sh -c 'wget -qO- http://web | head -n 3'
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
FAILED: localhost is client itself

<!DOCTYPE html>
<html>
<head>
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 실전 정리:
# - 호스트에서 접근: http://localhost:8085 (포트 퍼블리시 필요)
# - 컨테이너 간 접근: http://web:80 (같은 네트워크 + 이름)
docker ps --filter name=web
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- web이 내려가 있음 -> `docker ps --filter name=web`로 확인 후 재시작/재실행
- `web` 이름 해석 실패 -> client가 `--network labnet`인지, web이 `labnet`에 붙었는지 확인

</details>
