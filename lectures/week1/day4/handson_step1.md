# Hands-on Lab - Step 1

## 실습 개요

**제목**: Docker 컨테이너 관리 실습: 상태/로그/재시작/리소스/볼륨/정리까지

**목적**: 컨테이너는 "실행 인스턴스"이므로, 운영 관점에서는 실행/정지뿐 아니라 상태 관찰, 로그 확인, 재시작 정책, 리소스 제한, 데이터 유지(볼륨), 그리고 안전한 정리(cleanup)까지 익혀야 합니다. 이 실습은 그 기본 루틴을 한 번에 묶어서 반복 가능한 체크리스트 형태로 익히는 것이 목표입니다.

**학습 목표**:
- `docker ps`, `docker logs`, `docker exec`, `docker inspect`로 컨테이너 상태/원인을 빠르게 파악한다
- 재시작 정책과 종료 코드(ExitCode)를 이해하고 "바로 종료/재시작 루프"를 진단한다
- CPU/메모리 제한을 설정하고 `docker stats`로 관찰한다
- 볼륨으로 데이터를 분리해 컨테이너 교체에도 데이터가 유지되게 한다

**예상 소요 시간**: 90분

**난이도**: Beginner/Intermediate

### 실습 흐름도

```mermaid
flowchart LR
  A[컨테이너 실행] --> B[상태 확인]
  B --> C[로그/exec로 진단]
  C --> D[재시작 정책 실습]
  D --> E[리소스 제한/관찰]
  E --> F[볼륨으로 데이터 유지]
  F --> G[inspect + 필터링]
  G --> H[안전한 정리]
```

## 사전 요구사항

<details>
<summary>사전 요구사항 보기</summary>

- Docker Desktop 설치(Windows/macOS)
  - 공식: https://docs.docker.com/desktop/install/
- (Linux) Docker Engine 설치
  - 공식: https://docs.docker.com/engine/install/
- 주요 CLI 문서
  - `docker run`: https://docs.docker.com/reference/cli/docker/container/run/
  - `docker logs`: https://docs.docker.com/reference/cli/docker/container/logs/
  - `docker exec`: https://docs.docker.com/reference/cli/docker/container/exec/
  - `docker inspect`: https://docs.docker.com/reference/cli/docker/inspect/
  - `docker stats`: https://docs.docker.com/reference/cli/docker/container/stats/
  - `docker volume`: https://docs.docker.com/reference/cli/docker/volume/

</details>

## 환경 설정

<details>
<summary>환경 설정 보기</summary>

- Docker 동작 확인
  - 명령어: `docker info`
  - 공식: https://docs.docker.com/reference/cli/docker/system/info/
- 안전한 정리를 위해 라벨 사용
  - 본 실습에서는 `--label lab=week1-day4`를 붙여서, 정리 단계에서 "실습용 컨테이너만" 선택적으로 삭제합니다.

</details>

---

## Step 1: 관찰 가능한 컨테이너 실행(로그 생성기)

**목표**: 운영에서 가장 자주 하는 루틴인 "실행 -> 상태 확인 -> 로그 확인"을 바로 할 수 있도록, 지속적으로 로그를 남기는 컨테이너를 준비한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 로그를 계속 찍는 컨테이너 실행
docker run -d --name loggy --label lab=week1-day4 busybox sh -c 'i=0; while true; do echo "tick=$i"; i=$((i+1)); sleep 1; done'

# 2) 실행 중 컨테이너 확인
docker ps --filter name=loggy

# 3) 종료된 컨테이너까지 포함해서 전체 확인
docker ps -a --filter name=loggy
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
CONTAINER ID   IMAGE     COMMAND                  STATUS          NAMES
...            busybox   "sh -c i=0; while..."   Up ... seconds  loggy
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 컨테이너가 running 상태인지 확인
docker inspect loggy --format "Status={{.State.Status}}"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `Unable to find image 'busybox:latest' locally` 이후 pull 실패 -> 네트워크/프록시 확인(공식: https://docs.docker.com/network/proxy/)
- `Conflict. The container name "/loggy" is already in use` -> 기존 컨테이너 제거 후 재시도: `docker rm -f loggy`

</details>
