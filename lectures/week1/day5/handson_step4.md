# Hands-on Lab - Step 4

## Step 4: `network inspect`로 IP/연결 관계 확인하기

**목표**: 네트워크 관점에서 "누가 어디에 붙어 있고, 어떤 IP를 갖는지"를 확인한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 네트워크 상세 확인(컨테이너/IPv4Address 포함)
docker network inspect labnet | head -n 120

# web의 네트워크 설정만 빠르게 보기(따옴표 이스케이프를 피하려고 single quote 사용)
docker inspect web --format 'IP={{(index .NetworkSettings.Networks "labnet").IPAddress}}'

# (선택) web 컨테이너 내부 hosts 확인
docker exec web cat /etc/hosts | head -n 20
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
IP=172.19.0.2
...
172.19.0.2  web
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# labnet에 web이 붙어있는지 확인
docker inspect web --format "Networks={{json .NetworkSettings.Networks}}"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `template parsing error` -> `--format` 구문이 어려우면 `docker inspect web` 전체 출력에서 `NetworkSettings`를 확인
- `head: command not found`(Windows) -> 출력이 길면 스크롤로 확인하거나 PowerShell에서는 `| Select-Object -First 120` 사용

</details>
