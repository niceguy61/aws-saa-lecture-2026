# Hands-on Lab - Step 4

## Step 4: 태깅 전략 이해하기 (`tag`, `latest`, 네임스페이스)

**목표**: 하나의 이미지에 여러 태그를 붙이고(별칭), 태그가 "내용"이 아니라 "포인터"라는 점을 확인한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 같은 이미지에 태그 추가(별칭 만들기)
docker image tag img-lab:web-v1 img-lab:web-latest

# 팀/조직 네임스페이스를 붙인 태그(레지스트리에 올릴 때 흔히 사용)
docker image tag img-lab:web-v1 myteam/img-lab:web-v1

# 태그 목록 확인
docker image ls | head -n 30

# 태그가 바뀌어도 이미지 ID는 같음을 확인
docker image inspect img-lab:web-v1 --format "{{.Id}}"
docker image inspect img-lab:web-latest --format "{{.Id}}"
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
REPOSITORY          TAG         IMAGE ID       CREATED         SIZE
img-lab             web-v1      abcdef123456   ...             ...
img-lab             web-latest  abcdef123456   ...             ...
myteam/img-lab      web-v1      abcdef123456   ...             ...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 서로 다른 태그가 같은 IMAGE ID를 가리키면 "같은 내용"이다
docker image ls img-lab
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `invalid reference format` -> 태그 형식이 `name:tag`인지 확인(공백/대문자/특수문자 포함 여부 점검)
- `No such image: img-lab:web-v1` -> Step 1 빌드 성공 여부 확인 후 태그명 오타 점검

</details>
