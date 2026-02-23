# Hands-on Lab - Step 3

## Step 3: 이미지 메타데이터/레이어 확인 (`inspect`, `history`)

**목표**: 이미지가 어떤 설정(포트/엔트리포인트 등)을 갖고 있는지 확인하고, 레이어 기반으로 어떻게 쌓였는지 이해한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 이미지 상세(메타데이터) 확인
docker image inspect img-lab:web-v1 | head -n 40

# 레이어 히스토리 확인
docker history img-lab:web-v1

# 다이제스트 표시(환경에 따라 비어 보일 수 있음)
docker image ls --digests | head -n 20
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
[
  {
    "Id": "sha256:....",
    "RepoTags": [
      "img-lab:web-v1"
    ],
...

IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
sha256:...     ...            COPY index.html /usr/share/nginx/html/index...   ...B
<missing>      ...            /bin/sh -c #(nop)  CMD ["nginx" "-g" "daem...    0B
...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 같은 이미지 ID인지 확인(태그 변경/추가와 무관하게 ID가 동일하면 같은 내용)
docker image inspect img-lab:web-v1 --format "{{.Id}}"

# 레이어 수가 Dockerfile 단계(베이스 포함)와 연결됨을 확인
docker history img-lab:web-v1 | head -n 10
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `No such object: img-lab:web-v1` -> Step 1에서 빌드가 성공했는지 확인 후 `docker image ls`로 태그 존재 확인
- `head: command not found`(Windows) -> 출력이 길면 그냥 실행해서 스크롤로 확인하거나, PowerShell에서는 `| Select-Object -First 40` 사용

</details>
