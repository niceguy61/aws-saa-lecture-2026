# Hands-on Lab - Step 3

## Step 3: 시크릿 마운트 설정

**목표**: AWS 시크릿 파일을 환경 변수 및 파일로 동시에 마운트

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# docker-compose 시크릿 마운트 추가
    secrets:
      - aws-key-id
      - aws-secret-key
      - aws-session-token

secrets:
  aws-key-id:
    file: ./aws-key-id
    env: AWS_ACCESS_KEY_ID
  aws-secret-key:
    file: ./aws-secret-key
    env: AWS_SECRET_ACCESS_KEY
  aws-session-token:
    file: ./aws-session-token
    env: AWS_SESSION_TOKEN
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
시크릿 설정이 docker-compose.yml에 추가됨
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
grep 'secrets' docker-compose.yml
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 파일 경로 오류 시: `./aws-key-id` 파일 존재 여부 확인
- 문제: 권한 문제 시: `chmod 600 ./aws-key-id` 실행

</details>

