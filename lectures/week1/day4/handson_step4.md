# Hands-on Lab - Step 4

## Step 4: 리소스 제한과 관찰(`--memory`, `--cpus`, `stats`, `update`)

**목표**: 컨테이너에 CPU/메모리 제한을 걸고, 설정이 적용되었는지 확인하며, 실행 중에 일부 값을 업데이트하는 방법을 익힌다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 리소스 제한을 건 컨테이너 실행(실제로 부하를 주는 게 목적은 아님)
docker run -d --name limits --label lab=week1-day4 --memory 128m --cpus 0.5 alpine sh -c 'while true; do sleep 1; done'

# 2) 설정 확인(HostConfig)
docker inspect limits --format "Memory={{.HostConfig.Memory}} NanoCpus={{.HostConfig.NanoCpus}}"

# 3) 관찰(10초 정도 보고 Ctrl+C)
docker stats limits

# 4) 실행 중 업데이트(예: 메모리 256MB로)
docker update --memory 256m limits
docker inspect limits --format "Memory={{.HostConfig.Memory}}"
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Memory=134217728 NanoCpus=500000000
...
CONTAINER ID   NAME     CPU %   MEM USAGE / LIMIT   ...
...            limits   0.00%   1.2MiB / 128MiB     ...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps --filter name=limits
docker inspect limits --format "Status={{.State.Status}}"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `docker update`가 일부 옵션에서 실패 -> 모든 자원 제한이 업데이트 가능하진 않습니다. 실행 전에 `docker run`으로 설정하는 것을 기본으로 두세요.
- 제한 값 단위 혼동 -> `--memory 128m`처럼 단위를 명시하고, inspect 값은 바이트 기반으로 보일 수 있습니다.

</details>
