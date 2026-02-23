# Hands-on Lab - Step 6

## Step 6: 멀티스테이지 빌드로 "런타임 이미지"를 슬림하게 만들기(Go 예제)

**목표**: 빌드에 필요한 도구(Go 컴파일러 등)는 builder 스테이지에만 두고, 최종 이미지는 실행에 필요한 산출물만 포함하도록 구성한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) Go 예제 폴더 준비
mkdir -p docker-image-basics/go
cd docker-image-basics/go

# 2) 아래 3개 파일을 생성하세요
# go.mod
# module example.com/imglab
# go 1.22
#
# main.go
# (아래 참고)
#
# Dockerfile
# (아래 참고)

# main.go (예시)
# package main
# import (
#   "fmt"
#   "log"
#   "net/http"
# )
# func main() {
#   http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
#     fmt.Fprintln(w, "hello from multi-stage image")
#   })
#   log.Fatal(http.ListenAndServe(":8081", nil))
# }
#
# Dockerfile (멀티스테이지 예시)
# FROM golang:1.22-alpine AS builder
# WORKDIR /src
# COPY go.mod ./
# COPY main.go ./
# RUN go build -trimpath -ldflags="-s -w" -o /out/app ./main.go
#
# FROM alpine:3.19
# RUN adduser -D -H app
# USER app
# COPY --from=builder /out/app /app
# EXPOSE 8081
# ENTRYPOINT ["/app"]

# 3) 멀티스테이지 이미지 빌드
docker build -t img-lab:go-ms .

# 4) 실행 후 응답 확인
docker run --rm -d --name img-go -p 8081:8081 img-lab:go-ms
curl -s http://localhost:8081

# 5) 크기 비교(빌더 이미지 vs 최종 이미지)
docker image ls | head -n 30
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
hello from multi-stage image

REPOSITORY   TAG    IMAGE ID     CREATED        SIZE
img-lab      go-ms  ...          ...            (상대적으로 작음)
golang       1.22-alpine ...     ...            (상대적으로 큼)
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 컨테이너가 떠있는지 확인
docker ps --filter name=img-go

# 이미지가 만들어졌는지 확인
docker image ls img-lab:go-ms
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `failed to solve: ...`에서 베이스 이미지 pull 실패 -> 네트워크/프록시 설정 확인, 회사 내부 미러/레지스트리 사용 여부 확인
- `bind: address already in use` -> 8081 포트를 사용 중이면 다른 포트로 실행(예: `-p 18081:8081`)
- 빌드가 오래 걸림 -> 첫 pull/첫 빌드는 시간이 걸릴 수 있음. 이후 캐시가 적용되는지 확인

</details>
