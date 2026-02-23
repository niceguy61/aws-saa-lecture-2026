# 퀴즈 (Quiz)

## 질문 1

**가상머신(VM)과 컨테이너의 일반적인 차이로 가장 적절한 것은?**

A) 컨테이너는 각자 커널(OS)을 별도로 실행하고, VM은 커널을 공유한다  
B) 컨테이너는 호스트 커널을 공유하는 격리된 프로세스이고, VM은 하드웨어 수준 가상화로 OS를 포함한다  
C) VM은 이미지가 없고, 컨테이너만 이미지가 있다  
D) 컨테이너는 네트워크를 쓸 수 없고, VM만 네트워크를 쓸 수 있다  

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: 컨테이너는 호스트 커널을 공유하면서 네임스페이스/cgroups로 격리된 프로세스 집합으로 동작합니다. VM은 하이퍼바이저 위에서 게스트 OS를 포함하므로 격리 강도는 높지만 보통 더 무겁고 기동이 느립니다. 이 차이가 컨테이너의 빠른 기동/높은 밀도 같은 장점으로 이어집니다.

</details>

---

## 질문 2

**Docker Engine 구성 요소로 가장 적절한 조합은?**

A) Docker CLI, Docker Daemon, container runtime  
B) Dockerfile, README, Kubernetes  
C) Git, Jenkins, Prometheus  
D) EC2, S3, RDS  

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: 사용자는 Docker CLI로 명령을 내리고, 실제로 이미지/컨테이너/네트워크/볼륨을 관리하는 것은 Docker Daemon입니다. 컨테이너를 실행하는 런타임 계층(containerd/runc 등)이 있어 데몬의 요청이 실행으로 이어집니다. Dockerfile은 이미지를 만드는 레시피이지 엔진 구성요소가 아닙니다.

</details>

---

## 질문 3

**`docker run -d --name web -p 8080:80 nginx:alpine`에서 `-p 8080:80`의 의미는?**

A) 컨테이너의 8080 포트를 호스트의 80 포트로 연결한다  
B) 호스트의 8080 포트를 컨테이너의 80 포트로 연결한다  
C) 호스트와 컨테이너 모두 8080 포트를 사용하게 한다  
D) 포트 매핑이 아니라 CPU/메모리 제한을 설정한다  

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: `-p HOST:CONTAINER` 형식입니다. 호스트의 8080으로 들어온 요청을 컨테이너의 80으로 전달합니다. 컨테이너 내부에서 서비스가 80으로 리슨(listen)하고 있을 때 `http://localhost:8080`으로 접근하도록 만드는 전형적인 패턴입니다. 포트 충돌 시에는 HOST 쪽 포트를 바꾸면 해결되는 경우가 많습니다.

</details>

---

## 질문 4

**다음 중 Image와 Container의 관계 설명으로 가장 적절한 것은?**

A) 컨테이너는 불변 템플릿이고, 이미지는 실행 인스턴스다  
B) 이미지는 불변 템플릿이고, 컨테이너는 이미지로부터 생성된 실행 인스턴스다  
C) 둘은 같은 의미로, 용어만 다르다  
D) 이미지는 네트워크이고 컨테이너는 볼륨이다  

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: 이미지는 컨테이너를 만들기 위한 정적 산출물이며, 같은 이미지로 여러 컨테이너(실행 인스턴스)를 만들 수 있습니다. 컨테이너는 실행/중지/삭제될 수 있고 상태(프로세스, 네트워크, 마운트)를 가집니다. 데이터는 컨테이너 생명주기와 분리하기 위해 볼륨을 사용합니다.

</details>

---

## 질문 5

**`Cannot connect to the Docker daemon` 오류가 났을 때 가장 먼저 확인할 것은?**

A) 컨테이너 안에서 `ls`가 되는지  
B) Docker Desktop/Engine이 실행 중인지, `docker info`가 동작하는지  
C) README.md가 존재하는지  
D) 브랜치 이름이 main인지  

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: 이 오류는 Docker CLI가 Docker Daemon에 연결하지 못한다는 뜻입니다. 가장 먼저 데몬이 실행 중인지(Docker Desktop/Engine), 컨텍스트가 올바른지, `docker info`/`docker version`이 정상인지 확인해야 합니다. 컨테이너 내부 명령은 데몬 연결이 된 뒤에야 의미가 있습니다.

</details>

---

