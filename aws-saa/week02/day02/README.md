# Day 02 - ELB + Auto Scaling + health checks

## Outcomes

- ALB vs NLB 선택 기준(L7 라우팅 vs L4 성능/프로토콜)을 설명한다.
- Auto Scaling으로 “수평 확장 + 자가 치유”를 구현하는 핵심 구성요소(launch template, target group, health check)를 연결한다.
- 헬스체크 실패가 어떤 복구(인스턴스 교체/타겟 제외)로 이어지는지 설명한다.

## Services In Scope

- ELB (ALB/NLB)
- EC2 Auto Scaling
- Target group health checks

## Timebox (4h)

- Theory: 2h
- Hands-on (console): 2h

## Exam-Style Design Questions

- “HTTP path 기반 라우팅” 요구가 있을 때 정답 후보는?
- “초저지연 TCP” 요구가 있을 때 ALB가 아니라 NLB가 되는 신호는?
- Auto Scaling과 ELB를 조합할 때 헬스체크는 어디서/무엇을 기준으로 하는가?

