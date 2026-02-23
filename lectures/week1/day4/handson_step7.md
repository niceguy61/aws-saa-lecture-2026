# Hands-on Lab - Step 7

## Step 7: 안전한 정리(클린업)와 디스크 점검

**목표**: 라벨/필터 기반으로 실습 리소스만 안전하게 제거하고, 디스크 사용량을 확인하는 습관을 만든다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 실습용 컨테이너만 제거(라벨 필터)
docker rm -f $(docker ps -aq --filter label=lab=week1-day4) 2>/dev/null || true

# 2) 볼륨 제거(실습에서 만든 named volume)
docker volume rm labdata 2>/dev/null || true

# 3) 남은 리소스 확인
docker ps -a --filter label=lab=week1-day4
docker volume ls | head -n 20

# 4) 디스크 사용량 확인
docker system df

# 5) (선택) prune는 범위가 넓으므로 주의해서 사용
# docker container prune
# docker image prune
# docker system prune
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
CONTAINER ID   ...   (없음)

TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          ...
Containers      ...
Local Volumes   ...
Build Cache     ...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 실습 라벨 컨테이너가 남아있지 않은지 확인
docker ps -a --filter label=lab=week1-day4
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `$(...)`가 동작하지 않음(Windows PowerShell) -> 라벨로 조회한 ID를 복사해서 `docker rm -f <id1> <id2>` 형태로 제거
- `volume rm` 실패 -> 해당 볼륨을 사용하는 컨테이너가 남아있는지 확인 후 먼저 컨테이너 제거

</details>

---

## 실습 완료

- 컨테이너 상태/로그/내부 확인(`ps`, `logs`, `exec`, `inspect`)의 기본 루틴을 만들었습니다.
- 종료 코드와 재시작 정책이 장애 대응에 어떤 영향을 주는지 확인했습니다.
- 리소스 제한과 볼륨으로 "운영에 필요한 기본 안전장치"를 적용했습니다.

**다음 단계**:
- (Day 5) Docker 네트워킹 기초: 브리지 네트워크, 포트 퍼블리시, DNS/서비스 디스커버리
- (이후) Compose/Kubernetes로 확장: 여러 컨테이너를 선언적으로 관리하는 방식
