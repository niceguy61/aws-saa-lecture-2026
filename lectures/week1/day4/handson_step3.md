# Hands-on Lab - Step 3

## Step 3: 종료 코드와 재시작 정책 체험(`--restart`, `ExitCode`)

**목표**: "컨테이너가 죽으면 왜 죽었는지(ExitCode)"를 확인하고, 재시작 정책이 장애를 어떻게 증폭(또는 완화)시키는지 체감한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 일부러 실패하는 컨테이너 실행(Exit 1)
docker run -d --name crashy --label lab=week1-day4 --restart=on-failure:3 alpine sh -c 'echo "crash now"; exit 1'

# 2) 상태/재시작 횟수 확인
docker ps -a --filter name=crashy
docker inspect crashy --format "Status={{.State.Status}} RestartCount={{.RestartCount}} ExitCode={{.State.ExitCode}}"

# 3) 로그 확인
docker logs crashy
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Status=exited RestartCount=3 ExitCode=1

crash now
crash now
crash now
...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 재시작 정책 확인
docker inspect crashy --format "RestartPolicy={{json .HostConfig.RestartPolicy}}"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `No such container: crashy` -> 재시작 횟수 제한 후 종료 상태로 남아 있어야 함. 이름 오타/이미지 pull 실패 여부 확인
- 재시작 루프 디버깅이 어려움 -> 컨테이너를 제거하고 재시작 정책 없이 실행해 로그/환경을 먼저 확인

</details>
