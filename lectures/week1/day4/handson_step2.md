# Hands-on Lab - Step 2

## Step 2: 로그 확인과 컨테이너 내부 진입(`logs`, `exec`)

**목표**: 컨테이너 문제가 생겼을 때 가장 먼저 하는 "로그 확인"과, 필요한 경우 컨테이너 내부를 확인하는 `exec`를 익힌다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 최근 로그 확인
docker logs --tail 5 loggy

# 2) 실시간으로 따라가기(10초 정도 보고 Ctrl+C)
docker logs -f loggy

# 3) 컨테이너 내부에서 프로세스/파일 확인
docker exec loggy ps
docker exec loggy sh -c 'echo "inside container"; ls -la /'
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
tick=123
tick=124
tick=125
...

PID  USER   TIME  COMMAND
  1 root   0:00  sh -c i=0; while true; do ...
...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# loggy가 아직 running인지 확인
docker ps --filter name=loggy
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `Error response from daemon: Container ... is not running` -> `docker ps -a`로 상태 확인 후, 필요하면 재실행
- `docker exec`에서 쉘이 없음 -> 이미지에 따라 `sh`만 있거나 아예 없을 수 있음(알파인/BusyBox는 보통 `sh`)

</details>
