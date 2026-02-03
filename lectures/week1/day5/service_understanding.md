# 서비스 이해 (Service Understanding)

## 1. 배경 정보

<details>
<summary>배경 정보 보기</summary>

Docker Networking은 컨테이너 간 통신을 관리하고 네트워크를 구성하는 기능입니다. Docker는 기본적으로 bridge 네트워크를 사용하여 컨테이너를 연결하고, host, overlay, macvlan 등의 네트워크 드라이버를 지원합니다. 컨테이너는 호스트 네트워크나 고유의 가상 네트워크를 통해 상호작용하며, 이는 마이크로서비스 아키텍처나 다중 컨테이너 애플리케이션에서 필수적인 기능입니다. Docker 네트워킹은 네트워크 격리, IP 할당, 포트 포워딩 등 다양한 기능을 제공합니다.

### 인포그래픽

```mermaid
graph TD
  A[DOCKER 네트워킹 개요] --> B[브릿지 네트워크]
  A --> C[호스트 네트워크]
  A --> D[오버레이 네트워크]
  A --> E[MACVLAN 네트워크]
  B --> F[컨테이너 간 통신]
  C --> G[호스트 네트워크 직접 접근]
  D --> H[다중 호스트 클러스터 통신]
  E --> I[MAC 주소 기반 네트워크]
  F --> J[네트워크 격리]
  F --> K[IP 할당]
  F --> L[포트 포워딩]
```

**참고 이미지**:
- [이미지 보기](https://docs.docker.com/engine/networking/images/docker-networking-diagram.png)
- [이미지 보기](https://docs.example.com/image1.png)

</details>

## 2. 핵심 개념

<details>
<summary>핵심 개념 보기</summary>

- Container Networking: 컨테이너 간 통신을 위한 네트워크 인프라
- Network Isolation: 컨테이너 간 격리 및 보안 강화
- Network Drivers: bridge, host, overlay, macvlan 등 네트워크 드라이버

### 인포그래픽

```mermaid
graph TD
  A[컨테이너 네트워킹] --> B[네트워크 격리]
  A --> C[네트워크 드라이버]
  C --> D[bridge]
  C --> E[host]
  C --> F[overlay]
  C --> G[macvlan]
  style A fill:#4CAF50,stroke:#388E3C
  style B fill:#2196F3,stroke:#1976D2
  style C fill:#FF9800,stroke:#FB8C00
  style D fill:#9C27B0,stroke:#9C27B0
  style E fill:#00BCD4,stroke:#0097A7
  style F fill:#FF5722,stroke:#E64A19
  style G fill:#795548,stroke:#6D4C41
```

**참고 이미지**:
- [이미지 보기](https://docs.example.com/image1.png)
- [이미지 보기](https://docs.example.com/image2.png)
- [이미지 보기](https://docs.example.com/image3.png)

</details>

## 3. 장단점

<details>
<summary>장단점 보기</summary>

**장점**:
- 간편한 네트워크 구성 및 컨테이너 연결
- 다양한 네트워크 드라이버로 유연한 환경 설정 가능
- 호스트 네트워크 모드로 빠른 통신이 가능

**단점**:
- 고급 네트워크 설정 시 복잡도 증가
- 잘못된 구성 시 네트워크 장애 발생 가능성

</details>

## 4. 자주 사용되는 사례

<details>
<summary>사용 사례 보기</summary>

1. 마이크로서비스 아키텍처에서 서비스 간 통신 구성
2. CI/CD 파이프라인에서 빌드 서버와 테스트 서버 연결
3. 클라우드 환경에서 컨테이너 클러스터 통신 최적화

</details>

## 5. 연관 서비스

<details>
<summary>연관 서비스 보기</summary>

- Docker Compose
- Docker Swarm
- Kubernetes

</details>

## 6. 공식 문서 링크

- [Docker Networking 공식 문서](https://docs.docker.com/network/)
- [Docker Compose 네트워크 설정 가이드](https://docs.docker.com/compose/networking/)

