# Hands-on Lab - Step 4

## Step 4: 컨테이너 상태/로그 확인

**목표**: 실행 중인 컨테이너를 관찰하는 기본 명령을 익힙니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker ps
docker logs --tail 20 web
docker inspect web --format "{{json .State}}"
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
{"Status":"running","Running":true,"Pid":...}
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
curl -I http://localhost:8080
docker logs web | tail -n 5
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `No such container: web` -> 컨테이너 이름 확인(`docker ps -a`)
- 로그가 거의 없음 -> 요청이 없으면 로그가 적을 수 있음. curl 호출 후 재확인

</details>

