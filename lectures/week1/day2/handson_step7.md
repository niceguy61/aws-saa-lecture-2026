# Hands-on Lab - Step 7

## Step 7: 핵심 개념 정리 + 다음 실습 준비

**목표**: 오늘 사용한 명령을 의미와 함께 정리하고, Day 3(이미지/레이어, Dockerfile)로 연결합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker --help
docker run --help | head -n 20
docker system df
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          ...
Containers      ...
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker system df
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 출력이 너무 김 -> 스크롤로 확인하거나 파일로 저장(`docker run --help > help.txt`)
- `head`가 없음 -> Git Bash/WSL 사용 또는 스크롤로 확인

</details>

---

## 실습 완료

- Docker의 기본 루프(pull -> run -> ps/logs/exec -> stop/rm)를 수행했습니다.
- 포트 매핑으로 컨테이너 서비스를 호스트에 노출하는 방법을 확인했습니다.
- 데몬 연결/포트 충돌 같은 대표 장애 포인트를 진단하는 절차를 익혔습니다.

**다음 단계**:
- Day 3 예고: 이미지/레이어를 이해하고 Dockerfile로 직접 이미지 빌드하기
- `docker run` 옵션(환경변수, 볼륨, 리소스 제한) 실험(공식: https://docs.docker.com/reference/cli/docker/container/run/)
- `.dockerignore` 미리 보기(공식: https://docs.docker.com/build/building/context/#dockerignore-files)

