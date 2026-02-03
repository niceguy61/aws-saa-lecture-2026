# 서비스 이해 (Service Understanding)

## 1. 배경 정보

<details>
<summary>배경 정보 보기</summary>

Docker Registry는 Docker 이미지를 저장하고 분배하는 서비스로, 개발자와 운영자들이 컨테이너 이미지를 안전하게 관리하고 배포하는 데 핵심적인 역할을 합니다. 이 서비스는 Docker CLI와 통합되어 이미지의 등록, 검색, 추출 등을 지원하며, DevOps 파이프라인에서 CI/CD 자동화를 가능하게 합니다. 또한, Docker Registry는 이미지의 버전 관리, 암호화, 인증을 통해 보안성을 강화하고 있습니다.

### 인포그래픽

`mermaid
graph TD
  A[DOCKER REGISTRY] --> B[이미지 저장소]
  A --> C[CLI 통합]
  A --> D[보안 기능]
  C --> E[등록/검색/추출]
  D --> F[버전 관리]
  D --> G[암호화]
  D --> H[인증]
  subgraph DevOps
    I[CI/CD 자동화] --> J[파이프라인 통합]
  end
  style A fill:#4CAF50,stroke:#388E3C
  style B fill:#2196F3,stroke:#1976D2
  style C fill:#FFA726,stroke:#FB8C00
  style D fill:#9C27B0,stroke:#9575CD
  style F fill:#00BCD4,stroke:#0097A7
  style G fill:#FF5722,stroke:#EF6C00
  style H fill:#E91E63,stroke:#D81B60
  style I fill:#81D4FA,stroke:#4FC3F7
  style J fill:#80DEEA,stroke:#43A047
```

**참고 이미지**:
- [이미지 보기](https://docs.docker.com/registry/images/registry-architecture.png)
- [이미지 보기](https://docs.docker.com/engine/reference/commandline/cli/#docker-cli-commands)
- [이미지 보기](https://docs.docker.com/registry/recipes/auth/#using-http-basic-authentication)

</details>

## 2. 핵심 개념

<details>
<summary>핵심 개념 보기</summary>

- Docker Registry는 Docker 이미지를 저장소로 관리하는 서비스
- Docker CLI와의 통합을 통해 이미지의 등록 및 추출이 가능
- 인증 및 암호화 기능으로 보안을 강화

### 인포그래픽

`mermaid
graph TD
  A[Docker Registry] --> B[Docker CLI 통합]
  A --> C[보안 기능]
  B --> D[이미지 등록]
  B --> E[이미지 추출]
  C --> F[인증]
  C --> G[암호화]
  style A fill:#4CAF50,stroke:#388E3C
  style B fill:#2196F3,stroke:#1976D2
  style C fill:#FF9800,stroke:#FB8C00
  style D fill:#FFA726,stroke:#FB8C00
  style E fill:#FF8A65,stroke:#D50000
  style F fill:#9C27B0,stroke:#8E24AA
  style G fill:#673AB7,stroke:#4A144E
```

**참고 이미지**:
- [이미지 보기](https://docs.example.com/image1.png)

</details>

## 3. 장단점

<details>
<summary>장단점 보기</summary>

**장점**:
- 이미지의 버전 관리 및 분배를 효율화
- Docker CLI와의 원활한 통합
- 보안 강화를 위한 인증 및 암호화 지원

**단점**:
- 대규모 이미지 저장소 운영 시 복잡도 증가
- 기본적인 설정에서 보안 취약점 발생 가능성

</details>

## 4. 자주 사용되는 사례

<details>
<summary>사용 사례 보기</summary>

1. CI/CD 파이프라인에서 자동화된 이미지 배포
2. 멀티 클라우드 환경에서 이미지 공유 및 관리
3. 컨테이너 오케스트레이션 도구와의 통합

</details>

## 5. 연관 서비스

<details>
<summary>연관 서비스 보기</summary>

- Docker Engine
- Kubernetes
- Harbor
- AWS ECR

</details>

## 6. 공식 문서 링크

- [Docker Registry 공식 문서](https://docs.docker.com/registry/)

