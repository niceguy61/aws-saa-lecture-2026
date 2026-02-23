# Hands-on Lab - Step 6

## Step 6: `inspect`/필터/라벨로 운영 관점 조회하기

**목표**: 컨테이너/볼륨이 많아졌을 때 "내가 찾는 대상만" 안전하게 조회하고, 설정을 정확히 확인하는 패턴(라벨 + 필터 + inspect)을 익힌다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 라벨로 실습용 컨테이너만 조회
docker ps -a --filter label=lab=week1-day4

# 2) 특정 컨테이너의 핵심 정보만 빠르게 확인
docker inspect loggy --format "Name={{.Name}} Status={{.State.Status}} Image={{.Config.Image}}"
docker inspect limits --format "Memory={{.HostConfig.Memory}} NanoCpus={{.HostConfig.NanoCpus}}"

# 3) 프로세스 목록(top) 확인(운영에서 자주 사용)
docker top loggy

# 4) 종료/정지 후 상태 확인
docker stop loggy
docker ps -a --filter name=loggy
docker start loggy
docker ps --filter name=loggy
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Name=/loggy Status=running Image=busybox
...
UID   PID   PPID  C  STIME  TTY  TIME     CMD
root  ...   ...   0  ...    ?    00:00:00 sh -c i=0; while true; do ...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# stop/start 이후에도 컨테이너가 살아있고, 로그가 계속 찍히는지 확인
docker logs --tail 5 loggy
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `docker top`이 비어 보임 -> 컨테이너가 실행 중인지 먼저 확인(`docker ps`), 일부 환경에서는 제한적으로 보일 수 있음
- `docker start` 후 바로 exited -> PID 1이 지속 실행인지 확인(일회성 커맨드면 start하자마자 종료 가능)

</details>
