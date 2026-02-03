# Hands-on Lab - Step 5

## Step 5: 로그 확인

**목표**: 애플리케이션 실행 상태 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker logs -f <container-id>
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
nodemon 로그 출력됨
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs <container-id> | tail -n 20
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 로그 없음 → docker ps로 컨테이너 실행 상태 확인
- 문제: 권한 문제 → --user root 옵션 추가

</details>

