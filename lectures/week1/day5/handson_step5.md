# Hands-on Lab - Step 5

## Step 5: Docker Compose 네트워크 구성

**목표**: docker-compose.yml로 네트워크 설정

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
nano docker-compose.yml # 파일 생성 및 다음 내용 추가
version: '3'
services:
  web:
    build: .
    ports:
      - "8080:80"
    networks:
      - my_custom_network
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: secret
    networks:
      - my_custom_network
networks:
  my_custom_network:
    external: true
docker-compose up -d # 서비스 실행
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
컨테이너 정상 실행 및 로그 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker-compose ps
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: YAML 문법 오류 → yamllint 명령어 사용
- 문제: 네트워크 없음 → docker network create my_custom_network 실행

</details>

