# Hands-on Lab (Console): Budget 알림 만들기 + 태그 기반 비용 보기(권한 의존)

## Goal

- (권한이 있으면) AWS Budgets에서 월 예산을 만들고 이메일 알림을 설정한다.
- Cost Explorer에서 서비스/리전/태그 기준으로 비용을 보는 흐름을 익힌다.

## Prereqs

- Billing/Cost Management 콘솔 접근 권한(조직/계정 설정에 따라 학생 계정에는 없을 수 있음)
- 알림 받을 이메일 주소

## Cost Notes

- Budgets/Cost Explorer 자체는 일반적으로 큰 비용을 만들지 않지만, 계정 정책/서비스에 따라 다를 수 있다.
- 본 실습은 “설정” 중심이며 리소스를 추가로 만들지 않는다.

## Steps

### A) Console Steps

#### 1) Cost Explorer 활성화 확인(필요 시)

1. Billing and Cost Management 콘솔 진입
2. Cost Explorer 메뉴에서 활성화 상태 확인

#### 2) Budget 생성(월 비용, 알림)

1. AWS Budgets -> Create budget
2. Budget type: Cost budget
3. Period: Monthly
4. Budgeted amount: 학습용 소액(예: 5 USD 등, 조직 기준에 맞게)
5. Alerts:
  - 80% 도달 시 이메일 알림
  - 100% 도달 시 이메일 알림

#### 3) (옵션) Cost allocation tags 활성화

1. Billing -> Cost allocation tags
2. 조직 표준 태그(`CostCenter`, `Env` 등)를 활성화(권한 필요)

#### 4) Cost Explorer에서 Group by로 보기

1. Cost Explorer -> Cost and usage
2. Group by:
  - Service
  - Region
  - (가능하면) Tag

### B) Optional: If you do NOT have Billing access

- “설명 체크 과제”로 대체
  1. NAT Gateway가 비용 드라이버가 되는 이유를 2문장으로 작성
  2. 태그가 없을 때 팀별 비용을 추정하는 데 어떤 문제가 생기는지 2문장으로 작성

## Validation Checklist

- Budget이 생성되어 알림이 설정돼 있다(권한 있을 때).
- Cost Explorer에서 최소 1개 기준(Service/Region)으로 비용을 분해해 볼 수 있다(권한 있을 때).

## Cleanup

1. 학습용 Budget 삭제(원하면 유지)

