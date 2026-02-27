# Hands-on Lab (Console): Route 53 Weighted Routing 만들기 (개념 검증)

## Goal

- Route 53에서 Weighted routing 레코드를 구성하고 “비율 기반 분산”이 어떤 의미인지 이해한다.
- (Optional) dig로 특정 네임서버에 직접 질의해 레코드가 정상인지 검증한다.

## Prereqs

- Route 53 Hosted Zone 생성 권한
- 주의: Public hosted zone은 소액이지만 비용이 발생할 수 있다. 실습 후 삭제한다.

## Cost Notes

- Public hosted zone은 일반적으로 월 과금 항목이 있다(실습 후 즉시 삭제 권장).

## Steps

### A) Console Steps

#### 1) Public Hosted Zone 생성(학습용)

1. Route 53 콘솔 -> Hosted zones -> Create hosted zone
2. Domain name: 실제 소유 도메인이 없어도 됨(학습용) 예: `saa-lab.local` 같은 이름 사용
3. Type: Public hosted zone
4. 생성 후 NS 레코드 4개를 메모(옵션 검증에 사용)

#### 2) Weighted 레코드 2개 생성

1. Create record
2. Record name: `app`
3. Record type: A
4. Routing policy: Weighted
5. Value: `1.1.1.1` (학습용 더미 IP)
6. Weight: 80
7. 같은 이름으로 레코드를 하나 더 생성
  - Value: `8.8.8.8`
  - Weight: 20

#### 3) (설명 체크) 언제 Weighted가 정답인가

- 점진 배포/카나리/AB 테스트/트래픽 분산 요구가 있으면 Weighted가 후보.

### B) Optional: CLI Equivalents (for validation/automation)

CloudShell에서(선택) 특정 NS로 직접 질의:

```bash
dig @<ns-xxxx.awsdns-yy.net> app.saa-lab.local A +short
```

여러 번 실행하면 응답 IP가 섞여 나올 수 있다(반드시 비율 그대로는 아님, 확률/캐시 영향).

## Validation Checklist

- 동일 레코드 이름에 대해 Weighted 레코드 2개가 존재한다.
- “점진 배포/AB 테스트” 요구에서 Weighted를 선택할 수 있다.

## Common Errors

- 실제 도메인을 산 것이 아니라 “인터넷 전체”에서 해당 이름이 조회되진 않는다(Delegation 안 했기 때문).
- 캐시로 인해 질의 결과가 고정될 수 있다.

## Cleanup

1. Hosted zone 삭제(레코드가 남아있으면 삭제가 안 될 수 있으니 A 레코드부터 삭제)

