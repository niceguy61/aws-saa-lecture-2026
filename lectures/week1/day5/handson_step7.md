# Hands-on Lab - Step 7

## Step 7: 실습 리소스 정리(컨테이너/네트워크)

**목표**: 실습에 사용한 컨테이너와 네트워크를 안전하게 제거한다(라벨 기반).

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 실습용 컨테이너 제거(라벨 기반)
docker rm -f $(docker ps -aq --filter label=lab=week1-day5) 2>/dev/null || true

# 2) 실습용 네트워크 제거(컨테이너가 남아있으면 실패하므로 1) 먼저 수행)
docker network rm labnet 2>/dev/null || true
docker network rm labnet2 2>/dev/null || true

# 3) 확인
docker ps -a --filter label=lab=week1-day5
docker network ls | head -n 30
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
CONTAINER ID   ...   (없음)
labnet
labnet2
... (삭제되면 목록에 안 보임)
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# labnet/labnet2가 없어졌는지 확인
docker network ls | head -n 30
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `$(...)`가 동작하지 않음(Windows PowerShell) -> `docker ps -aq --filter label=lab=week1-day5`로 나온 ID를 복사해서 `docker rm -f <id...>`로 제거
- `network rm`이 실패 -> 아직 그 네트워크에 붙은 컨테이너가 남아있다는 의미. 먼저 컨테이너 제거 후 재시도

</details>

---

## 실습 완료

- 같은 네트워크 위에서 컨테이너 이름(DNS)으로 통신하는 방법을 익혔습니다.
- 호스트 접근은 `-p` 포트 퍼블리시가 필수라는 것을 확인했습니다.
- `localhost` 혼동을 피하는 기준(호스트 vs 컨테이너 vs 다른 컨테이너)을 정리했습니다.

**다음 단계**:
- Docker Compose로 여러 서비스를 선언적으로 묶어 네트워크/이름을 자동 구성
- (이후) Kubernetes Service/DNS/Ingress로 확장
