# Deep Dive - 트러블슈팅

## 시나리오 1: 컨테이너 간 네트워크 연결 실패

### 트러블슈팅 흐름도

```mermaid
graph TD
  A[컨테이너 통신 실패: Connection refused] --> B[1. 동일 네트워크 확인]
  B --> C[네트워크 구성 확인]
  C --> D[컨테이너 네트워크 설정 오류]
  D --> E[고정 네트워크 생성]
  C --> F[포트 매핑 확인]
  F --> G[포트 매핑 누락]
  G --> H[포트 매핑 추가]
  F --> I[포트 충돌]
  I --> J[포트 재할당]
  J --> K[서비스 재시작]
  K --> L[문제 해결 완료]
  A --> M[2. 방화벽/보안 그룹 확인]
  M --> N[방화벽 규칙 조정]
  N --> L
  A --> O[3. Docker 상태 점검]
  O --> P[Docker 재시작]
  P --> L
```

**참고 이미지**:
- [이미지 보기](https://docs.docker.com/network/images/network-bridge.png)
- [이미지 보기](https://docs.docker.com/network/images/network-host.png)
- [이미지 보기](https://docs.docker.com/network/images/network-overlay.png)
- [이미지 보기](https://docs.docker.com/engine/reference/run/images/run-ports.png)
- [이미지 보기](https://docs.docker.com/storage/images/bind-mounts.png)
- [이미지 보기](https://docs.docker.com/network/images/network-custom.png)


### 시나리오 설명

<details>
<summary>문제 상황 보기</summary>

두 컨테이너가 서로 통신할 수 없고, 'Connection refused' 오류 발생

</details>

### 원인 분석

<details>
<summary>원인 분석 보기</summary>

Docker 네트워크 설정 오류 또는 서비스가 동일 네트워크에 정의되지 않음

</details>

### 원인 확인 방법

<details>
<summary>진단 단계 보기</summary>

docker network ls 명령어로 현재 네트워크 목록 확인

docker network inspect <network-name> 명령어로 네트워크 구성 검사

docker exec -it <container-id> sh 명령어로 컨테이너 내부에서 ping 명령어로 연결 테스트

curl http://<other-container-ip> 명령어로 외부 컨테이너 접근 시도

docker logs <container-id> 명령어로 로그 확인

</details>

### 수정 방법

<details>
<summary>해결 단계 보기</summary>

docker network create --driver bridge my-network 명령어로 커스텀 네트워크 생성

docker rm -f <container-id> && docker run -d --network my-network --name <container-name> <image> 명령어로 컨테이너 재부팅

docker network inspect my-network 명령어로 네트워크 구성 재확인

docker service create --network my-network <service-name> <image> 명령어로 서비스 재등록

docker network prune 명령어로 불필요한 네트워크 정리

</details>

### 정상 확인 방법

<details>
<summary>검증 단계 보기</summary>

docker network inspect my-network 명령어로 네트워크 상태 확인

curl http://<other-container-ip> 명령어로 연결 성공 여부 검증

docker exec -it <container-id> ping <other-container-ip> 명령어로 ICMP 테스트

docker stats <container-id> 명령어로 네트워크 통계 확인

docker network ls 명령어로 최종 네트워크 상태 확인

</details>

---

## 시나리오 2: 포트 매핑 오류로 외부 접근 실패

### 트러블슈팅 흐름도

```mermaid
graph TD
  A[호스트에서 컨테이너 포트 접근 시 오류 발생] --> B[1. 포트 충돌 확인]
  B --> C[2. Dockerfile에 EXPOSE 지시어 존재 여부 확인]
  C --> D[3. --publish 옵션 올바르게 설정되었는지 확인]
  D --> E[4. 컨테이너 재시작]
  E --> F[문제 해결 완료]
  A --> G[1. 포트 사용 중인 프로세스 확인]
  G --> H[2. 충돌 프로세스 종료]
  H --> F
```


### 시나리오 설명

<details>
<summary>문제 상황 보기</summary>

호스트에서 컨테이너 포트 접근 시 'Address already in use' 또는 'Connection refused' 오류 발생

</details>

### 원인 분석

<details>
<summary>원인 분석 보기</summary>

Dockerfile에 EXPOSE 지시어 누락 또는 --publish 옵션 설정 오류

</details>

### 원인 확인 방법

<details>
<summary>진단 단계 보기</summary>

docker ps --format 'table {{.PORTS}}' 명령어로 포트 매핑 확인

docker inspect <container-id> | grep -i port 명령어로 포트 정보 추출

netstat -tuln | grep <port-number> 명령어로 호스트 포트 확인

curl http://localhost:<host-port> 명령어로 접근 테스트

docker logs <container-id> 명령어로 컨테이너 로그 확인

</details>

### 수정 방법

<details>
<summary>해결 단계 보기</summary>

Dockerfile에 EXPOSE <container-port> 추가 후 rebuild 수행

docker stop <container-id> && docker rm <container-id> 명령어로 컨테이너 제거

docker run -d -p <host-port>:<container-port> --name <container-name> <image> 명령어로 재시작

docker network inspect <network-name> 명령어로 네트워크 구성 확인

docker system prune -a 명령어로 이전 컨테이너 정리

</details>

### 정상 확인 방법

<details>
<summary>검증 단계 보기</summary>

docker ps --format 'table {{.PORTS}}' 명령어로 포트 매핑 재확인

curl http://localhost:<host-port> 명령어로 접근 성공 여부 검증

netstat -tuln | grep <host-port> 명령어로 호스트 포트 확인

docker inspect <container-id> | grep -i port 명령어로 포트 정보 재검사

docker stats <container-id> 명령어로 네트워크 상태 확인

</details>

---

