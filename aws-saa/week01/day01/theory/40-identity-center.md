# IAM Identity Center: SSO/페더레이션 관점(개요)

## 핵심 감각

- Identity Center는 “사용자/그룹을 AWS 계정에 SSO로 연결”하는 출입구다.
- 직접 IAM User를 대량으로 만들기보다, **조직 단위 SSO + 권한 세트(권한 템플릿)**로 운영을 단순하게 만드는 방향이 자주 정답이다.

## 시험에서 자주 나오는 신호

- “사내 IdP(예: AD/Okta)로 SSO” → Identity Center 후보
- “여러 계정에 동일 권한을 중앙에서 할당” → Identity Center + 권한 세트(컨셉) + Organizations 흐름

## TL;DR (한 줄 정리)

- 사용자는 **SSO로 들어오고**, 실제 권한은 **Role/정책(권한 세트 포함)**로 통제한다고 생각하면 된다.

## Back

- `../01-theory.md`
