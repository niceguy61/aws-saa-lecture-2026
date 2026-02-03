# Hands-on Lab - Step 6

## Step 6: SELinux 옵션 적용

**목표**: bind mount SELinux 라벨 설정

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# Docker Compose에 SELinux 옵션 추가
    volumes:
      - type: bind
        source: ./src/web
        target: /app/web
        read_only: false
        selinux: z
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
SELinux 'z' 옵션 적용됨
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker-compose config
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: SELinux 설정 오류 시: `setenforce 0`으로 임시 비활성화
- 문제: 라벨 변경 필요 시: `chcon -Rt svirt_sandbox_file_t ./src/web` 실행

</details>

