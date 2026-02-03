# Hands-on Lab - Step 6

## Step 6: AWS Secret Manager 연동

**목표**: 기밀 정보를 AWS Secret Manager에서 불러옵니다

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
aws s3 cp s3://my-bucket/secrets.json ./secrets.json && docker run -d -p 3000:3000 --mount type=bind,src=./,target=/app --env AWS_ACCESS_KEY_ID=KEY --env AWS_SECRET_ACCESS_KEY=SECRET myapp-image
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
컨테이너 실행됨
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps | grep myapp
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 권한 오류 → IAM 정책 확인: https://docs.aws.amazon.com/lambda/latest/dg/security-iam.html
- 문제: Secret 불러오기 실패 → aws s3 ls로 S3 버킷 확인

</details>

