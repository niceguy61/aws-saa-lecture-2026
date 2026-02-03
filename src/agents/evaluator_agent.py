"""
Evaluator Agent - 페르소나 기반 강의 난이도 평가 및 개선
"""
from typing import Dict, List, Optional
from .base_agent import BaseAgent


class EvaluatorAgent(BaseAgent):
    """페르소나 기반으로 강의 내용을 평가하고 개선하는 에이전트"""
    
    # 페르소나 정의
    PERSONAS = {
        "초등학생": {
            "level": "elementary",
            "description": "초등학교 고학년 (5-6학년) 학생",
            "knowledge": "컴퓨터 기본 사용, 간단한 프로그래밍 경험 없음",
            "expectations": "매우 쉬운 설명, 많은 비유, 단계별 상세 설명"
        },
        "중학생": {
            "level": "middle_school",
            "description": "중학생 (1-3학년)",
            "knowledge": "컴퓨터 활용 가능, 기본 프로그래밍 개념 이해",
            "expectations": "쉬운 설명, 실생활 비유, 개념 중심 설명"
        },
        "고등학생": {
            "level": "high_school",
            "description": "고등학생 또는 IT 입문자",
            "knowledge": "프로그래밍 기초, 컴퓨터 구조 기본 이해",
            "expectations": "명확한 설명, 기술 용어 설명 포함, 실습 중심"
        },
        "대학생": {
            "level": "university",
            "description": "컴퓨터공학 전공 대학생",
            "knowledge": "프로그래밍, 운영체제, 네트워크 기초 지식",
            "expectations": "기술적 설명, 이론과 실습 균형, 심화 내용 포함"
        },
        "주니어_DevOps_1년차": {
            "level": "junior_1year",
            "description": "DevOps 실무 경험 1년차",
            "knowledge": "기본 인프라 운영, 배포 경험, 기본 도구 사용",
            "expectations": "실무 중심, 트러블슈팅, 베스트 프랙티스"
        },
        "주니어_DevOps_2년차": {
            "level": "junior_2year",
            "description": "DevOps 실무 경험 2년차",
            "knowledge": "인프라 자동화, CI/CD 구축, 모니터링 경험",
            "expectations": "고급 패턴, 아키텍처 설계, 성능 최적화"
        },
        "시니어_DevOps": {
            "level": "senior",
            "description": "DevOps 실무 경험 3년 이상",
            "knowledge": "전체 인프라 설계, 대규모 시스템 운영",
            "expectations": "아키텍처 패턴, 엔터프라이즈 솔루션, 고급 최적화"
        },
        "IT_비전공자": {
            "level": "non_major",
            "description": "IT 비전공 전환 희망자",
            "knowledge": "컴퓨터 기본 사용, 기술 용어 생소",
            "expectations": "매우 상세한 설명, 용어 정의, 단계별 가이드"
        }
    }
    
    def __init__(self):
        # Initialize BaseAgent with evaluator-specific parameters
        super().__init__(
            name="Evaluator Agent",
            collection_name="",  # Evaluator doesn't use a specific collection
            system_prompt="당신은 교육 콘텐츠 평가 및 개선 전문가입니다."
        )
        self.agent_name = "Evaluator Agent"
    
    def get_persona_info(self, persona_name: str) -> Optional[Dict]:
        """페르소나 정보 조회"""
        return self.PERSONAS.get(persona_name)
    
    def list_personas(self) -> List[str]:
        """사용 가능한 페르소나 목록"""
        return list(self.PERSONAS.keys())
    
    def evaluate_content(
        self,
        content: str,
        section_type: str,
        persona_name: str,
        topic: str
    ) -> Dict:
        """
        페르소나 기반으로 강의 내용 평가
        
        Args:
            content: 평가할 강의 내용
            section_type: 섹션 타입 (service_understanding, deep_dive, hands_on_lab, quiz)
            persona_name: 페르소나 이름
            topic: 강의 주제
            
        Returns:
            평가 결과 딕셔너리
        """
        persona = self.get_persona_info(persona_name)
        if not persona:
            return {
                "status": "error",
                "message": f"알 수 없는 페르소나: {persona_name}"
            }
        
        # 평가 프롬프트 생성
        evaluation_prompt = self._create_evaluation_prompt(
            content, section_type, persona, topic
        )
        
        # LLM으로 평가 수행
        evaluation_result = self.llm.invoke(evaluation_prompt)
        evaluation_text = evaluation_result.content if hasattr(evaluation_result, 'content') else str(evaluation_result)
        
        # 평가 결과 파싱
        return self._parse_evaluation_result(evaluation_text, persona_name)
    
    def improve_content(
        self,
        content: str,
        evaluation: Dict,
        section_type: str,
        persona_name: str,
        topic: str
    ) -> str:
        """
        평가 결과를 바탕으로 강의 내용 개선
        
        Args:
            content: 원본 강의 내용
            evaluation: 평가 결과
            section_type: 섹션 타입
            persona_name: 페르소나 이름
            topic: 강의 주제
            
        Returns:
            개선된 강의 내용
        """
        persona = self.get_persona_info(persona_name)
        
        # 개선이 필요하지 않은 경우
        if evaluation.get("difficulty_level") == "적절함" and \
           evaluation.get("comprehension_level") == "우수":
            return content
        
        # 개선 프롬프트 생성
        improvement_prompt = self._create_improvement_prompt(
            content, evaluation, section_type, persona, topic
        )
        
        # LLM으로 개선된 내용 생성
        improved_result = self.llm.invoke(improvement_prompt)
        improved_content = improved_result.content if hasattr(improved_result, 'content') else str(improved_result)
        
        return improved_content
    
    def _create_evaluation_prompt(
        self,
        content: str,
        section_type: str,
        persona: Dict,
        topic: str
    ) -> str:
        """평가 프롬프트 생성"""
        
        section_names = {
            "service_understanding": "서비스 이해",
            "deep_dive": "Deep Dive",
            "hands_on_lab": "실습 가이드",
            "quiz": "퀴즈"
        }
        
        section_name = section_names.get(section_type, section_type)
        
        prompt = f"""당신은 교육 콘텐츠 평가 전문가입니다.

# 평가 대상 페르소나
- **이름**: {persona['description']}
- **지식 수준**: {persona['knowledge']}
- **기대 수준**: {persona['expectations']}

# 평가할 강의 내용
**주제**: {topic}
**섹션**: {section_name}

**내용**:
{content}

---

# 평가 기준

다음 기준으로 평가하고, 각 항목에 대해 상세히 분석하세요:

## 1. 난이도 평가 (Difficulty Level)
- **너무 어려움**: 페르소나의 지식 수준을 크게 초과, 이해 불가능
- **약간 어려움**: 페르소나가 이해하기 어려운 부분이 일부 존재
- **적절함**: 페르소나의 수준에 딱 맞음
- **약간 쉬움**: 페르소나에게 너무 쉬운 내용
- **너무 쉬움**: 페르소나의 수준보다 훨씬 낮음

## 2. 이해도 평가 (Comprehension Level)
- **우수**: 개념이 명확하고, 예시가 적절하며, 단계별 설명이 잘 되어 있음
- **양호**: 대부분 이해 가능하나 일부 개선 필요
- **보통**: 이해 가능하나 추가 설명이 필요한 부분이 많음
- **미흡**: 개념 설명이 부족하고, 예시가 부족함
- **불량**: 페르소나가 이해하기 매우 어려움

## 3. 구체적 문제점
다음 항목을 체크하세요:
- 전문 용어가 설명 없이 사용되었는가?
- 개념 설명이 충분한가?
- 예시나 비유가 적절한가?
- 단계별 설명이 상세한가?
- 사전 지식 요구사항이 명시되었는가?
- 실습 단계가 페르소나 수준에 맞는가?

## 4. 개선 제안
페르소나가 더 잘 이해할 수 있도록 구체적인 개선 방안을 제시하세요:
- 추가해야 할 설명
- 보완해야 할 예시
- 단순화해야 할 부분
- 추가해야 할 배경 지식

---

# 출력 형식

반드시 다음 형식으로 출력하세요:

## 난이도 평가
[너무 어려움/약간 어려움/적절함/약간 쉬움/너무 쉬움]

## 이해도 평가
[우수/양호/보통/미흡/불량]

## 문제점
1. [구체적 문제점 1]
2. [구체적 문제점 2]
3. [구체적 문제점 3]
...

## 개선 제안
1. [구체적 개선 방안 1]
2. [구체적 개선 방안 2]
3. [구체적 개선 방안 3]
...

## 종합 의견
[전체적인 평가 및 권장사항]
"""
        return prompt
    
    def _create_improvement_prompt(
        self,
        content: str,
        evaluation: Dict,
        section_type: str,
        persona: Dict,
        topic: str
    ) -> str:
        """개선 프롬프트 생성"""
        
        section_names = {
            "service_understanding": "서비스 이해",
            "deep_dive": "Deep Dive",
            "hands_on_lab": "실습 가이드",
            "quiz": "퀴즈"
        }
        
        section_name = section_names.get(section_type, section_type)
        
        # 평가 결과 요약
        issues = "\n".join([f"- {issue}" for issue in evaluation.get("issues", [])])
        suggestions = "\n".join([f"- {suggestion}" for suggestion in evaluation.get("suggestions", [])])
        
        prompt = f"""당신은 교육 콘텐츠 개선 전문가입니다.

# 대상 페르소나
- **이름**: {persona['description']}
- **지식 수준**: {persona['knowledge']}
- **기대 수준**: {persona['expectations']}

# 개선할 강의 내용
**주제**: {topic}
**섹션**: {section_name}

**원본 내용**:
{content}

---

# 평가 결과

**난이도**: {evaluation.get('difficulty_level', 'N/A')}
**이해도**: {evaluation.get('comprehension_level', 'N/A')}

**문제점**:
{issues}

**개선 제안**:
{suggestions}

---

# 개선 지침

다음 원칙에 따라 내용을 개선하세요:

## 1. 페르소나 맞춤 설명
- 페르소나의 지식 수준에 맞는 용어 사용
- 필요한 경우 전문 용어에 쉬운 설명 추가
- 페르소나가 이해할 수 있는 비유와 예시 사용

## 2. 개념 설명 강화
- 핵심 개념을 단계별로 설명
- "왜 필요한가?"에 대한 배경 설명 추가
- 실생활 또는 실무 예시 추가

## 3. 구조 개선
- 복잡한 내용은 단계별로 분해
- 시각적 요소 (다이어그램, 표) 활용
- 요약 및 핵심 포인트 강조

## 4. 실습 가이드 개선 (해당 시)
- 각 단계를 더 상세하게 설명
- 예상 결과 및 검증 방법 명시
- 자주 발생하는 문제 및 해결 방법 추가

## 5. 퀴즈 개선 (해당 시)
- 난이도를 페르소나 수준에 맞게 조정
- 설명을 더 상세하게 작성
- 오답 이유도 명확히 설명

---

# 중요 규칙

1. **원본 구조 유지**: 섹션 구조와 형식은 최대한 유지
2. **한글 작성**: 모든 설명은 한글로 작성 (코드/명령어 제외)
3. **완전한 내용**: 개선된 전체 내용을 출력 (일부만 출력 금지)
4. **Mermaid 다이어그램**: 필요시 추가하되 ```mermaid 형식 사용
5. **실용성**: 이론과 실습의 균형 유지

---

# 출력

개선된 전체 내용을 출력하세요. 설명이나 주석 없이 개선된 마크다운 내용만 출력하세요.
"""
        return prompt
    
    def _parse_evaluation_result(self, evaluation_text: str, persona_name: str) -> Dict:
        """평가 결과 파싱"""
        
        result = {
            "persona": persona_name,
            "difficulty_level": "알 수 없음",
            "comprehension_level": "알 수 없음",
            "issues": [],
            "suggestions": [],
            "summary": "",
            "needs_improvement": False
        }
        
        lines = evaluation_text.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if not line:
                continue
            
            # 섹션 헤더 감지
            if '난이도 평가' in line or '## 난이도' in line:
                current_section = 'difficulty'
                continue
            elif '이해도 평가' in line or '## 이해도' in line:
                current_section = 'comprehension'
                continue
            elif '문제점' in line or '## 문제점' in line:
                current_section = 'issues'
                continue
            elif '개선 제안' in line or '## 개선' in line:
                current_section = 'suggestions'
                continue
            elif '종합 의견' in line or '## 종합' in line:
                current_section = 'summary'
                continue
            
            # 내용 파싱
            if current_section == 'difficulty':
                if any(keyword in line for keyword in ['너무 어려움', '약간 어려움', '적절함', '약간 쉬움', '너무 쉬움']):
                    result['difficulty_level'] = line.strip('[]')
            
            elif current_section == 'comprehension':
                if any(keyword in line for keyword in ['우수', '양호', '보통', '미흡', '불량']):
                    result['comprehension_level'] = line.strip('[]')
            
            elif current_section == 'issues':
                if line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '-', '*')):
                    issue = line.lstrip('0123456789.-* ').strip()
                    if issue:
                        result['issues'].append(issue)
            
            elif current_section == 'suggestions':
                if line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '-', '*')):
                    suggestion = line.lstrip('0123456789.-* ').strip()
                    if suggestion:
                        result['suggestions'].append(suggestion)
            
            elif current_section == 'summary':
                result['summary'] += line + ' '
        
        # 개선 필요 여부 판단
        result['needs_improvement'] = (
            result['difficulty_level'] in ['너무 어려움', '약간 어려움', '너무 쉬움'] or
            result['comprehension_level'] in ['미흡', '불량', '보통']
        )
        
        result['summary'] = result['summary'].strip()
        
        return result
