# Hands-on Lab - Step 6

## Step 6: docker-compose watch 설정

**목표**: docker-compose.yml에서 watch 모드 적용

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
cat <<EOF > docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    command: npm start
    volumes:
      - type: bind
        source: ./web
        target: /app/web
        watch: true
      - type: bind
        source: ./proxy/nginx.conf
        target: /etc/nginx/conf.d/default.conf
        watch: sync+restart
EOF
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
docker-compose.yml 파일 생성 완료
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
cat docker-compose.yml | grep 'watch'
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: YAML 오류 → 'docker-compose config'로 유효성 검사
- 문제: 경로 오류 → 'source' 경로 재확인

</details>

