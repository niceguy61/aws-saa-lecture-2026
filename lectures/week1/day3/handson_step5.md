# Hands-on Lab - Step 5

## Step 5: docker-compose watch 모드 설정

**목표**: 파일 변경 시 실시간 동기화 구현

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker-compose.yml 파일에 다음 추가:

services:
  web:
    build:
      context: .
    volumes:
      - type: bind
        source: ./src
        target: /app/src
        watch: true
      - type: bind
        source: ./nginx.conf
        target: /etc/nginx/conf.d/default.conf
        watch: true
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
docker-compose.yml 파일 업데이트
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
cat docker-compose.yml | grep watch
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 구성 파일 오류 → 해결: docker-compose config 명령어로 유효성 검사
- 문제: 동기화 실패 → 해결: docker-compose down && docker-compose up 명령어로 재시작

</details>

