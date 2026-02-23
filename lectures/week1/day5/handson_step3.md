# Hands-on Lab - Step 3

## Step 3: 호스트에서 접근하려면 `-p`로 포트를 퍼블리시해야 한다

**목표**: 컨테이너가 running이어도, 호스트에서 접근하려면 포트 퍼블리시가 필요함을 확인한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 현재 web은 -p 없이 실행했으므로, 호스트에서는 접근이 어려움(예: curl 실패 가능)
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8085 || true

# 2) web을 제거하고 포트 퍼블리시로 재실행
docker rm -f web
docker run -d --name web --label lab=week1-day5 --network labnet -p 8085:80 nginx:alpine

# 3) 호스트에서 접근 확인
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8085

# 4) 포트 매핑 확인
docker ps --filter name=web --format "Ports={{.Ports}}"
docker port web
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
200
0.0.0.0:8085->80/tcp
80/tcp -> 0.0.0.0:8085
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 실제 콘텐츠 일부 확인
curl -s http://localhost:8085 | head -n 5
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `bind: address already in use` -> 8085 포트를 사용하는 프로세스가 있으면 다른 포트로 변경(예: `-p 18085:80`)
- curl이 없음 -> 브라우저로 `http://localhost:8085` 접근 또는 `wget` 사용

</details>
