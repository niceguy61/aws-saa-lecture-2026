# Hands-on Lab - Step 5

## Step 5: 빌드 캐시와 `.dockerignore` 체감하기

**목표**: "무엇이 바뀌면 어떤 단계의 캐시가 깨지는지"를 직접 확인하고, `.dockerignore`로 빌드 컨텍스트를 줄이는 이유를 이해한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
cd docker-image-basics/web

# 1) 같은 내용으로 재빌드(캐시 확인)
DOCKER_BUILDKIT=1 docker build --progress=plain -t img-lab:web-v1 .

# 2) index.html 내용 일부를 수정한 뒤 재빌드 (COPY 단계만 다시 실행되는지 관찰)
DOCKER_BUILDKIT=1 docker build --progress=plain -t img-lab:web-v1 .

# 3) (선택) 컨텍스트가 커지면 느려지는 것을 보기 위해 더미 파일 생성
# Linux/macOS:
#   dd if=/dev/zero of=junk.bin bs=1M count=5
# Windows PowerShell:
#   fsutil file createnew junk.bin 5242880

# 4) .dockerignore 생성/수정 (에디터로 아래 내용을 저장)
# .git
# node_modules
# dist
# target
# *.log
# junk.bin

# 5) 다시 빌드하여 "transferring context"가 줄어드는지 관찰
DOCKER_BUILDKIT=1 docker build --progress=plain -t img-lab:web-v1 .
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
...
 => [internal] load .dockerignore
 => => transferring context: ...KB
 => CACHED [1/2] FROM docker.io/library/nginx:alpine
 => [2/2] COPY index.html /usr/share/nginx/html/index.html
...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 캐시가 잘 먹으면, 두 번째 빌드에서 CACHED가 많이 나타난다
DOCKER_BUILDKIT=1 docker build --progress=plain -t img-lab:web-v1 .

# .dockerignore 파일 존재 확인
ls -la .dockerignore
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `DOCKER_BUILDKIT=1`이 동작하지 않음 -> 환경에 따라 기본이 BuildKit일 수 있으니 그냥 `docker build`로 진행(출력 형식만 다를 수 있음)
- `.dockerignore`를 만들었는데도 컨텍스트가 커 보임 -> 제외 패턴이 맞는지 확인(파일/폴더명 오타, 경로 기준은 "컨텍스트 루트"임)

</details>
