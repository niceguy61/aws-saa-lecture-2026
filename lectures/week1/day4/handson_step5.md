# Hands-on Lab - Step 5

## Step 5: 볼륨으로 데이터 유지하기(`volume create`, `-v`)

**목표**: 컨테이너를 지워도 데이터가 남도록, 컨테이너 수명과 데이터를 분리하는 기본 패턴(볼륨)을 실습한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 이름 있는 볼륨 생성
docker volume create labdata

# 2) 첫 컨테이너에서 파일 생성(컨테이너는 --rm로 바로 제거)
docker run --rm --name vol1 --label lab=week1-day4 -v labdata:/data alpine sh -c 'echo "hello volume" > /data/msg.txt; ls -la /data; cat /data/msg.txt'

# 3) 두 번째 컨테이너에서 같은 볼륨을 마운트하여 파일이 남아있는지 확인
docker run --rm --name vol2 --label lab=week1-day4 -v labdata:/data alpine sh -c 'ls -la /data; cat /data/msg.txt'

# 4) 볼륨 목록 확인
docker volume ls | head -n 20
docker volume inspect labdata
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
msg.txt
hello volume
...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 볼륨이 존재하는지 확인
docker volume ls | head
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `permission denied` -> 호스트/OS/파일 시스템 권한 이슈일 수 있음. 우선 named volume으로 진행하고, 바인드 마운트는 경로/권한을 점검
- `volume inspect` 결과가 낯설다 -> 운영에서는 "어떤 컨테이너가 어떤 볼륨을 쓰는지" 추적이 중요하므로, 다음 Step에서 라벨/inspect를 함께 사용

</details>
