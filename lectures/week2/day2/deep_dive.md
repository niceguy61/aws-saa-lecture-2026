# Deep Dive - 트러블슈팅

## 시나리오 1: Docker Registry 포트 매핑 실패

### 트러블슈팅 흐름도

`mermaid
graph TD
  A[도커 레지스터리 컨테이너 접근 오류] --> B[포트 매핑 확인]
  B --> C[네트워크 정책 검사]
  C --> D[외부 포트 노출 확인]
  D --> E[방화벽/ACL 규칙 점검]
  E --> F[서비스 연결 테스트]
  F --> G[문제 해결 완료]
  G --> H[로그 확인: docker logs <container-id>]
  H --> I[포트 매핑 재설정]
  I --> J[네트워크 정책 조정]
  J --> K[연결 성공]
  K --> L[서비스 재시작]
```

**참고 이미지**:
- [이미지 보기](https://docs.example.com/image1.png)


### 시나리오 설명

<details>
<summary>문제 상황 보기</summary>

Docker Registry 컨테이너가 정상적으로 작동하지만 외부에서 접근할 수 없는 문제가 발생했습니다.

</details>

### 원인 분석

<details>
<summary>원인 분석 보기</summary>

포트 매핑 설정 오류 또는 네트워크 정책 제약으로 인해 외부 접근이 차단됨

</details>

### 원인 확인 방법

<details>
<summary>진단 단계 보기</summary>

docker ps -a --format 'table {STATUS}' | grep -i 'exited'

docker inspect <container-id> | grep -i 'PortBindings'

curl -v http://localhost:5000/v2/_catalog

</details>

### 수정 방법

<details>
<summary>해결 단계 보기</summary>

docker run -d -p 5000:5000 --name registry registry:2

docker network inspect bridge | grep -i '5000'

docker exec -it registry registryctl -u http://registry:5000

</details>

### 정상 확인 방법

<details>
<summary>검증 단계 보기</summary>

curl -v http://localhost:5000/v2/_catalog

docker logs registry

docker stats registry

</details>

---

## 시나리오 2: Docker Registry 파일 동기화 실패

### 트러블슈팅 흐름도

`mermaid
graph TD
  A[소스 코드 변경] --> B[경로 매핑 확인]
  B --> C{경로 오류?
  C -->|아니요| D[파일 권한 점검]
  D -->|성공| E[동기화 완료]
  C -->|예| F[bind mount 설정 재확인]
  F --> G[--mount type=bind 추가]
  G --> H[권한 설정: useradd/chown]
  H --> I[서비스 재시작]
  A --> J[동기화 실패 시]
  J --> K[로그 확인: docker logs]
  K --> L[오류 해결 후]
  L --> M[서비스 재구동]
```

**참고 이미지**:
- [이미지 보기](https://docs.docker.com/compose/reference/options/#security-opt)
- [이미지 보기](https://docs.docker.com/engine/reference/commandline/logs/)
- [이미지 보기](https://docs.docker.com/compose/compose-file/#build)
- [이미지 보기](https://docs.docker.com/engine/reference/run/#mount-points)


### 시나리오 설명

<details>
<summary>문제 상황 보기</summary>

Docker Compose watch 모드에서 소스 코드 변경이 컨테이너에 반영되지 않는 문제가 발생했습니다.

</details>

### 원인 분석

<details>
<summary>원인 분석 보기</summary>

watch 설정의 경로 매핑 오류 또는 파일 권한 문제로 인한 동기화 실패

</details>

### 원인 확인 방법

<details>
<summary>진단 단계 보기</summary>

docker-compose config | grep -i 'watch'

docker inspect <container-id> | grep -i 'Mounts'

docker logs <container-id> | grep -i 'sync'

</details>

### 수정 방법

<details>
<summary>해결 단계 보기</summary>

docker-compose up --build -d

docker exec <container-id> chown -R app:app /app/web

docker-compose restart <service-name>

</details>

### 정상 확인 방법

<details>
<summary>검증 단계 보기</summary>

echo 'test' >> ./web/testfile.txt

docker logs <container-id> | grep -i 'testfile'

docker-compose down && docker-compose up -d

</details>

---

