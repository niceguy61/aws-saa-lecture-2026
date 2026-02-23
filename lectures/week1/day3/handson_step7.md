# Hands-on Lab - Step 7

## Step 7: 이미지 `save/load`와 정리(클린업)

**목표**: 네트워크 없이 이미지를 옮겨야 하는 상황을 가정하고, 이미지 파일로 내보내기(`save`)와 가져오기(`load`)를 수행한 뒤 실습 리소스를 정리한다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) 실행 중인 컨테이너 정리
docker rm -f img-web 2>/dev/null || true
docker rm -f img-go 2>/dev/null || true

# 2) 이미지 내보내기(save)
docker save -o img-lab-web.tar img-lab:web-v1 img-lab:web-latest
docker save -o img-lab-go.tar img-lab:go-ms

# 3) 이미지 삭제 후(load로 복구해보기)
docker image rm -f img-lab:web-latest img-lab:web-v1 img-lab:go-ms

# 4) 이미지 가져오기(load)
docker load -i img-lab-web.tar
docker load -i img-lab-go.tar

# 5) 복구 확인
docker image ls | head -n 30
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Loaded image: img-lab:web-v1
Loaded image: img-lab:web-latest
Loaded image: img-lab:go-ms
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
# 웹 이미지 재실행으로 정상 동작 확인(선택)
docker run --rm -d --name img-web -p 8080:80 img-lab:web-v1
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
docker rm -f img-web

# 디스크 사용량 확인(선택)
docker system df
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `no such image` -> save 대상 태그가 존재하는지 먼저 `docker image ls`로 확인
- tar 파일이 매우 큼 -> 여러 이미지를 한 번에 save했는지 확인, 필요 없는 태그/이미지를 정리 후 다시 생성
- 정리 중 실수로 다른 이미지를 지움 -> `docker image rm`은 정확한 태그만 지정해서 삭제(와일드카드/광범위 prune는 주의)

</details>

---

## 실습 완료

- Dockerfile로 이미지를 빌드하고 실행하는 전체 흐름을 경험했습니다.
- 레이어/캐시/컨텍스트(.dockerignore)가 빌드 시간과 이미지 크기에 직접 영향을 준다는 것을 확인했습니다.
- 멀티스테이지 빌드로 최종 이미지를 슬림하게 만드는 이유를 이해했습니다.
- `save/load`로 이미지 아티팩트를 파일로도 운반할 수 있음을 확인했습니다.

**다음 단계**:
- (Day 4) 컨테이너 관리: 로그/리소스/재시작 정책, 볼륨/바인드 마운트, 정리 전략
- 레지스트리 활용: `docker login/push/pull`, 사설 레지스트리/권한 관리
- 이미지 보안: 최소 베이스 이미지, 취약점 스캔, 서명/검증, 시크릿 유출 방지
