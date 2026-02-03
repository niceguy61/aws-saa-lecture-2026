"""독립적인 강의 생성 에이전트들"""
import json
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from src.vectorstore import VectorStoreManager


# Pydantic Models
class Infographic(BaseModel):
    """인포그래픽"""
    type: str = Field(description="mermaid 또는 svg")
    content: str = Field(description="다이어그램 코드 또는 SVG 코드")
    image_references: Optional[List[str]] = Field(description="참고 이미지 링크", default=None)


class ServiceUnderstanding(BaseModel):
    """서비스 이해 섹션"""
    background: str = Field(description="배경 정보")
    concepts: List[str] = Field(description="핵심 개념 리스트")
    advantages: List[str] = Field(description="장점 (최소 3개)")
    disadvantages: List[str] = Field(description="단점 (최소 2개)")
    use_cases: List[str] = Field(description="자주 사용되는 사례 (최소 3개)")
    related_services: List[str] = Field(description="연관 서비스")
    official_links: List[Dict[str, str]] = Field(description="공식 문서 링크")


class TroubleshootingScenario(BaseModel):
    """트러블슈팅 시나리오"""
    title: str
    description: str
    root_cause: str
    diagnosis_steps: List[str]
    resolution_steps: List[str]
    verification_steps: List[str]


class DeepDive(BaseModel):
    """Deep Dive 섹션"""
    scenarios: List[TroubleshootingScenario] = Field(description="최소 2개의 시나리오")


class HandsOnStep(BaseModel):
    """실습 단계"""
    step_number: int
    title: str
    objective: str
    commands: Optional[str] = None
    expected_output: Optional[str] = None
    verification: Optional[str] = None
    troubleshooting: Optional[List[str]] = None


class HandsOnLab(BaseModel):
    """실습 섹션"""
    title: str
    purpose: str
    learning_objectives: List[str]
    estimated_time: str
    difficulty: str
    prerequisites: List[str]
    setup_instructions: List[str]
    steps: List[HandsOnStep] = Field(description="최소 7개의 단계")
    completion_summary: str
    next_steps: Optional[List[str]] = None


class QuizQuestion(BaseModel):
    """퀴즈 질문"""
    question: str
    choices: List[str] = Field(description="4개의 선택지")
    answer: str
    explanation: str


class Quiz(BaseModel):
    """퀴즈 섹션"""
    questions: List[QuizQuestion] = Field(description="최소 5개의 질문")


class InfographicAgent:
    """인포그래픽 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
    
    def generate(
        self, 
        service_name: str, 
        context: str, 
        section_type: str,
        rag_context: str
    ) -> Infographic:
        """인포그래픽 생성
        
        Args:
            service_name: 서비스 이름
            context: 섹션 내용 (배경정보, 핵심개념 등)
            section_type: 섹션 타입 (background, concepts, troubleshooting, hands_on)
            rag_context: ChromaDB에서 가져온 문서 (이미지 링크 포함)
        """
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 기술 문서 시각화 전문가입니다.
주어진 내용을 시각적으로 표현하는 다이어그램을 생성하세요.

반드시 다음 규칙을 따르세요:
1. Mermaid 다이어그램 사용 (graph, sequence, flowchart 등)
2. 명확하고 이해하기 쉬운 구조
3. 한글 레이블 사용
4. 색상과 스타일로 가독성 향상
5. RAG 컨텍스트에서 이미지 링크 추출

JSON 형식으로 응답하세요."""),
            ("user", """서비스: {service_name}
섹션 타입: {section_type}

섹션 내용:
{context}

RAG 컨텍스트 (이미지 링크 포함):
{rag_context}

다음 JSON 스키마로 응답하세요:
{{
  "type": "mermaid",
  "content": "```mermaid\\ngraph TD\\n  A[시작] --> B[단계1]\\n  B --> C[완료]\\n```",
  "image_references": ["https://docs.example.com/image1.png", ...]
}}

섹션 타입별 다이어그램 가이드:
- background: 역사적 흐름이나 발전 과정 (timeline, flowchart)
- concepts: 개념 간 관계 (graph, mindmap)
- troubleshooting: 문제 해결 흐름 (flowchart, sequence)
- hands_on: 실습 단계 흐름 (flowchart, sequence)

RAG 컨텍스트에서 관련 이미지 URL을 찾아 image_references에 포함하세요.""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "service_name": service_name,
            "section_type": section_type,
            "context": context[:2000],
            "rag_context": rag_context[:4000]
        })
        
        try:
            data = json.loads(response.content)
            return Infographic(**data)
        except Exception as e:
            print(f"❌ Infographic generation error: {e}")
            print(f"Response content: {response.content[:500]}")
            # Return default infographic on error
            return Infographic(
                type="mermaid",
                content="```mermaid\ngraph LR\n  A[시작] --> B[진행중]\n  B --> C[완료]\n```",
                image_references=None
            )
    
    def format_markdown(self, infographic: Infographic) -> str:
        """Format infographic as markdown"""
        md = ""
        
        # Add diagram
        if infographic.type == "mermaid":
            md += f"{infographic.content}\n\n"
        elif infographic.type == "svg":
            md += f"{infographic.content}\n\n"
        
        # Add image references if available
        if infographic.image_references:
            md += "**참고 이미지**:\n"
            for img_url in infographic.image_references:
                md += f"- [이미지 보기]({img_url})\n"
            md += "\n"
        
        return md


class ServiceUnderstandingAgent:
    """서비스 이해 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
        self.infographic_agent = InfographicAgent(model_name)
    
    def generate(self, service_name: str, rag_context: str) -> ServiceUnderstanding:
        """서비스 이해 섹션 생성"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 DevOps 교육 전문가입니다.
주어진 서비스에 대한 서비스 이해 섹션을 생성하세요.

반드시 다음 규칙을 따르세요:
1. 모든 내용은 한글로 작성
2. 기술 용어는 한글(English) 형식으로 첫 사용 시 표기
3. 장점 최소 3개, 단점 최소 2개
4. 사용 사례 최소 3개
5. Mermaid 다이어그램 포함
6. 공식 문서 링크 포함

JSON 형식으로 응답하세요."""),
            ("user", """서비스: {service_name}

RAG 컨텍스트:
{rag_context}

다음 JSON 스키마로 응답하세요:
{{
  "background": "배경 정보 (한글)",
  "concepts": ["개념1", "개념2", ...],
  "advantages": ["장점1", "장점2", "장점3", ...],
  "disadvantages": ["단점1", "단점2", ...],
  "use_cases": ["사례1", "사례2", "사례3", ...],
  "related_services": ["서비스1", "서비스2", ...],
  "official_links": [
    {{"name": "링크명", "url": "https://..."}}
  ]
}}""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "service_name": service_name,
            "rag_context": rag_context[:8000]
        })
        
        try:
            data = json.loads(response.content)
            
            # Validate and fix official_links structure
            if "official_links" in data:
                if isinstance(data["official_links"], dict):
                    # Convert dict to list of dicts
                    links_list = []
                    for key, value in data["official_links"].items():
                        if isinstance(value, dict) and "url" in value:
                            if "name" not in value:
                                value["name"] = key
                            links_list.append(value)
                        elif isinstance(value, str):
                            # If value is just a URL string
                            links_list.append({"name": key, "url": value})
                    data["official_links"] = links_list
                
                # Ensure all links have name and url
                valid_links = []
                for link in data["official_links"]:
                    if isinstance(link, dict):
                        if "name" not in link:
                            link["name"] = "공식 문서"
                        if "url" not in link:
                            link["url"] = "#"
                        valid_links.append(link)
                data["official_links"] = valid_links
            
            return ServiceUnderstanding(**data)
        except Exception as e:
            print(f"❌ Service Understanding generation error: {e}")
            print(f"Response content: {response.content[:500]}")
            raise
    
    def format_markdown(self, su: ServiceUnderstanding, service_name: str, rag_context: str) -> str:
        """Format as markdown with <details> tags and infographics"""
        try:
            md = "# 서비스 이해 (Service Understanding)\n\n"
            
            # 1. 배경 정보 + 인포그래픽
            md += "## 1. 배경 정보\n\n"
            md += "<details>\n"
            md += "<summary>배경 정보 보기</summary>\n\n"
            md += f"{su.background}\n\n"
            
            # Generate infographic for background
            print("  📊 Generating infographic for background...")
            bg_infographic = self.infographic_agent.generate(
                service_name=service_name,
                context=su.background,
                section_type="background",
                rag_context=rag_context
            )
            md += "### 인포그래픽\n\n"
            md += self.infographic_agent.format_markdown(bg_infographic)
            
            md += "</details>\n\n"
            
            # 2. 핵심 개념 + 인포그래픽
            md += "## 2. 핵심 개념\n\n"
            md += "<details>\n"
            md += "<summary>핵심 개념 보기</summary>\n\n"
            for concept in su.concepts:
                md += f"- {concept}\n"
            md += "\n"
            
            # Generate infographic for concepts
            print("  📊 Generating infographic for concepts...")
            concepts_text = "\n".join(su.concepts)
            concepts_infographic = self.infographic_agent.generate(
                service_name=service_name,
                context=concepts_text,
                section_type="concepts",
                rag_context=rag_context
            )
            md += "### 인포그래픽\n\n"
            md += self.infographic_agent.format_markdown(concepts_infographic)
            
            md += "</details>\n\n"
            
            # 3. 장단점
            md += "## 3. 장단점\n\n"
            md += "<details>\n"
            md += "<summary>장단점 보기</summary>\n\n"
            md += "**장점**:\n"
            for adv in su.advantages:
                md += f"- {adv}\n"
            md += "\n**단점**:\n"
            for dis in su.disadvantages:
                md += f"- {dis}\n"
            md += "\n</details>\n\n"
            
            # 4. 자주 사용되는 사례
            md += "## 4. 자주 사용되는 사례\n\n"
            md += "<details>\n"
            md += "<summary>사용 사례 보기</summary>\n\n"
            for i, uc in enumerate(su.use_cases, 1):
                md += f"{i}. {uc}\n"
            md += "\n</details>\n\n"
            
            # 5. 연관 서비스
            md += "## 5. 연관 서비스\n\n"
            md += "<details>\n"
            md += "<summary>연관 서비스 보기</summary>\n\n"
            for rs in su.related_services:
                md += f"- {rs}\n"
            md += "\n</details>\n\n"
            
            # 6. 공식 문서 링크
            md += "## 6. 공식 문서 링크\n\n"
            print(f"  🔗 Processing {len(su.official_links)} official links...")
            for i, link in enumerate(su.official_links):
                print(f"    Link {i+1} type: {type(link)}, value: {link}")
                # Handle both dict and object access
                if isinstance(link, dict):
                    link_name = link.get('name', '링크')
                    link_url = link.get('url', '#')
                else:
                    link_name = getattr(link, 'name', '링크')
                    link_url = getattr(link, 'url', '#')
                md += f"- [{link_name}]({link_url})\n"
            md += "\n"
            
            return md
            
        except Exception as e:
            print(f"❌ Error in format_markdown: {e}")
            import traceback
            traceback.print_exc()
            raise


class DeepDiveAgent:
    """Deep Dive 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
        self.infographic_agent = InfographicAgent(model_name)
    
    def generate(self, service_name: str, rag_context: str) -> DeepDive:
        """Deep Dive 섹션 생성"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 DevOps 트러블슈팅 전문가입니다.
주어진 서비스의 트러블슈팅 시나리오를 생성하세요.

반드시 다음 규칙을 따르세요:
1. 모든 내용은 한글로 작성
2. 최소 2개의 시나리오
3. 각 시나리오는 5단계 구조
4. 실제 명령어 포함
5. 공식 문서 기반

CRITICAL: scenarios는 반드시 배열(array)이어야 합니다. 객체가 아닙니다!

JSON 형식으로 응답하세요."""),
            ("user", """서비스: {service_name}

RAG 컨텍스트:
{rag_context}

다음 JSON 스키마로 정확히 응답하세요. scenarios는 배열입니다:
{{
  "scenarios": [
    {{
      "title": "시나리오 제목",
      "description": "문제 상황 설명",
      "root_cause": "원인 분석",
      "diagnosis_steps": ["확인 단계1", "확인 단계2", ...],
      "resolution_steps": ["해결 단계1", "해결 단계2", ...],
      "verification_steps": ["검증 단계1", "검증 단계2", ...]
    }},
    {{
      "title": "시나리오 제목 2",
      "description": "문제 상황 설명 2",
      "root_cause": "원인 분석 2",
      "diagnosis_steps": ["확인 단계1", "확인 단계2", ...],
      "resolution_steps": ["해결 단계1", "해결 단계2", ...],
      "verification_steps": ["검증 단계1", "검증 단계2", ...]
    }}
  ]
}}

최소 2개의 시나리오를 배열 형태로 생성하세요.""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "service_name": service_name,
            "rag_context": rag_context[:8000]
        })
        
        try:
            data = json.loads(response.content)
            
            # Validate and fix scenarios structure
            if "scenarios" in data:
                if isinstance(data["scenarios"], dict):
                    scenarios_list = []
                    for key, value in data["scenarios"].items():
                        if isinstance(value, dict) and all(k in value for k in ["title", "description", "root_cause"]):
                            scenarios_list.append(value)
                    data["scenarios"] = scenarios_list
                
                valid_scenarios = []
                for s in data["scenarios"]:
                    if isinstance(s, dict) and all(k in s for k in ["title", "description", "root_cause", "diagnosis_steps", "resolution_steps", "verification_steps"]):
                        valid_scenarios.append(s)
                
                data["scenarios"] = valid_scenarios
                
                if len(data["scenarios"]) < 2:
                    raise ValueError(f"Only {len(data['scenarios'])} scenarios generated, need at least 2")
            
            return DeepDive(**data)
            
        except json.JSONDecodeError as e:
            print(f"❌ JSON parsing error: {e}")
            print(f"Response content: {response.content[:500]}")
            raise
        except Exception as e:
            print(f"❌ Deep Dive validation error: {e}")
            print(f"Data structure: {data}")
            raise
    
    def format_markdown(self, dd: DeepDive, service_name: str, rag_context: str) -> str:
        """Format as markdown with <details> tags and infographics"""
        md = "# Deep Dive - 트러블슈팅\n\n"
        
        for i, scenario in enumerate(dd.scenarios, 1):
            md += f"## 시나리오 {i}: {scenario.title}\n\n"
            
            # Generate infographic for troubleshooting flow
            print(f"  📊 Generating infographic for scenario {i}...")
            scenario_context = f"{scenario.description}\n{scenario.root_cause}"
            scenario_infographic = self.infographic_agent.generate(
                service_name=service_name,
                context=scenario_context,
                section_type="troubleshooting",
                rag_context=rag_context
            )
            md += "### 트러블슈팅 흐름도\n\n"
            md += self.infographic_agent.format_markdown(scenario_infographic)
            md += "\n"
            
            # 시나리오 설명
            md += "### 시나리오 설명\n\n"
            md += "<details>\n"
            md += "<summary>문제 상황 보기</summary>\n\n"
            md += f"{scenario.description}\n\n"
            md += "</details>\n\n"
            
            # 원인 분석
            md += "### 원인 분석\n\n"
            md += "<details>\n"
            md += "<summary>원인 분석 보기</summary>\n\n"
            md += f"{scenario.root_cause}\n\n"
            md += "</details>\n\n"
            
            # 원인 확인 방법
            md += "### 원인 확인 방법\n\n"
            md += "<details>\n"
            md += "<summary>진단 단계 보기</summary>\n\n"
            for step in scenario.diagnosis_steps:
                md += f"{step}\n\n"
            md += "</details>\n\n"
            
            # 수정 방법
            md += "### 수정 방법\n\n"
            md += "<details>\n"
            md += "<summary>해결 단계 보기</summary>\n\n"
            for step in scenario.resolution_steps:
                md += f"{step}\n\n"
            md += "</details>\n\n"
            
            # 정상 확인 방법
            md += "### 정상 확인 방법\n\n"
            md += "<details>\n"
            md += "<summary>검증 단계 보기</summary>\n\n"
            for step in scenario.verification_steps:
                md += f"{step}\n\n"
            md += "</details>\n\n"
            
            md += "---\n\n"
        
        return md


class HandsOnLabAgent:
    """Hands-on Lab 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
        self.infographic_agent = InfographicAgent(model_name)
    
    def generate(self, service_name: str, rag_context: str) -> HandsOnLab:
        """실습 섹션 생성"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 DevOps 실습 교육 전문가입니다.
주어진 서비스의 실습 과정을 생성하세요.

반드시 다음 규칙을 따르세요:
1. 모든 내용은 한글로 작성
2. 최소 7개의 단계
3. 각 단계는 3-4개 이하의 작업
4. 각 단계마다 검증 방법 포함
5. 실제 실행 가능한 명령어
6. 명령어에는 한글 주석 포함

CRITICAL: steps는 반드시 배열(array)이어야 합니다. 객체가 아닙니다!

JSON 형식으로 응답하세요."""),
            ("user", """서비스: {service_name}

RAG 컨텍스트:
{rag_context}

다음 JSON 스키마로 정확히 응답하세요. steps는 배열입니다:
{{
  "title": "실습 제목",
  "purpose": "실습 목적",
  "learning_objectives": ["목표1", "목표2", ...],
  "estimated_time": "45분",
  "difficulty": "Beginner",
  "prerequisites": ["요구사항1", "요구사항2", ...],
  "setup_instructions": ["설정1", "설정2", ...],
  "steps": [
    {{
      "step_number": 1,
      "title": "단계 제목",
      "objective": "이 단계의 목표",
      "commands": "명령어 (bash 코드)",
      "expected_output": "예상 출력",
      "verification": "확인 명령어",
      "troubleshooting": ["문제1: 해결방법", ...]
    }},
    {{
      "step_number": 2,
      "title": "단계 제목 2",
      "objective": "이 단계의 목표 2",
      "commands": "명령어 (bash 코드)",
      "expected_output": "예상 출력",
      "verification": "확인 명령어",
      "troubleshooting": ["문제1: 해결방법", ...]
    }}
  ],
  "completion_summary": "실습 완료 요약",
  "next_steps": ["다음 단계1", ...]
}}

최소 7개의 단계를 배열 형태로 생성하세요.""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "service_name": service_name,
            "rag_context": rag_context[:8000]
        })
        
        try:
            data = json.loads(response.content)
            
            # Validate and fix steps structure
            if "steps" in data:
                if isinstance(data["steps"], dict):
                    steps_list = []
                    for key, value in sorted(data["steps"].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0):
                        if isinstance(value, dict):
                            if "step_number" not in value:
                                value["step_number"] = int(key) if key.isdigit() else len(steps_list) + 1
                            steps_list.append(value)
                    data["steps"] = steps_list
                
                valid_steps = []
                for i, s in enumerate(data["steps"], 1):
                    if isinstance(s, dict):
                        if "step_number" not in s or s["step_number"] != i:
                            s["step_number"] = i
                        
                        # Fix commands field if it's a list
                        if "commands" in s and isinstance(s["commands"], list):
                            s["commands"] = "\n".join(s["commands"])
                        
                        # Fix expected_output field if it's a list
                        if "expected_output" in s and isinstance(s["expected_output"], list):
                            s["expected_output"] = "\n".join(s["expected_output"])
                        
                        # Fix verification field if it's a list
                        if "verification" in s and isinstance(s["verification"], list):
                            s["verification"] = "\n".join(s["verification"])
                        
                        if all(k in s for k in ["step_number", "title", "objective"]):
                            valid_steps.append(s)
                
                data["steps"] = valid_steps
                
                if len(data["steps"]) < 7:
                    raise ValueError(f"Only {len(data['steps'])} steps generated, need at least 7")
            
            return HandsOnLab(**data)
            
        except json.JSONDecodeError as e:
            print(f"❌ JSON parsing error: {e}")
            print(f"Response content: {response.content[:500]}")
            raise
        except Exception as e:
            print(f"❌ Hands-on Lab validation error: {e}")
            print(f"Data structure: {data}")
            raise
    
    def format_step_markdown(
        self, 
        step: HandsOnStep, 
        step_num: int, 
        lab: HandsOnLab,
        service_name: str,
        rag_context: str
    ) -> str:
        """Format a single step as markdown with <details> tags and infographics"""
        md = f"# Hands-on Lab - Step {step_num}\n\n"
        
        # Add lab context on first step
        if step_num == 1:
            md += "## 실습 개요\n\n"
            md += f"**제목**: {lab.title}\n\n"
            md += f"**목적**: {lab.purpose}\n\n"
            md += "**학습 목표**:\n"
            for obj in lab.learning_objectives:
                md += f"- {obj}\n"
            md += f"\n**예상 소요 시간**: {lab.estimated_time}\n\n"
            md += f"**난이도**: {lab.difficulty}\n\n"
            
            # Generate infographic for hands-on flow
            print("  📊 Generating infographic for hands-on lab flow...")
            lab_context = f"{lab.title}\n{lab.purpose}\n" + "\n".join([f"Step {i}: {s.title}" for i, s in enumerate(lab.steps, 1)])
            lab_infographic = self.infographic_agent.generate(
                service_name=service_name,
                context=lab_context,
                section_type="hands_on",
                rag_context=rag_context
            )
            md += "### 실습 흐름도\n\n"
            md += self.infographic_agent.format_markdown(lab_infographic)
            md += "\n"
            
            md += "## 사전 요구사항\n\n"
            md += "<details>\n"
            md += "<summary>사전 요구사항 보기</summary>\n\n"
            for req in lab.prerequisites:
                md += f"- {req}\n"
            md += "\n</details>\n\n"
            
            md += "## 환경 설정\n\n"
            md += "<details>\n"
            md += "<summary>환경 설정 보기</summary>\n\n"
            for setup in lab.setup_instructions:
                md += f"{setup}\n\n"
            md += "</details>\n\n"
            
            md += "---\n\n"
        
        md += f"## Step {step_num}: {step.title}\n\n"
        
        md += f"**목표**: {step.objective}\n\n"
        
        if step.commands:
            md += "**명령어**:\n"
            md += "<details>\n"
            md += "<summary>명령어 보기</summary>\n\n"
            md += "```bash\n"
            md += f"{step.commands}\n"
            md += "```\n\n"
            md += "</details>\n\n"
        
        if step.expected_output:
            md += "**예상 출력**:\n"
            md += "<details>\n"
            md += "<summary>예상 출력 보기</summary>\n\n"
            md += "```\n"
            md += f"{step.expected_output}\n"
            md += "```\n\n"
            md += "</details>\n\n"
        
        if step.verification:
            md += "**확인 방법**:\n"
            md += "<details>\n"
            md += "<summary>확인 방법 보기</summary>\n\n"
            md += "```bash\n"
            md += f"{step.verification}\n"
            md += "```\n\n"
            md += "</details>\n\n"
        
        if step.troubleshooting:
            md += "**문제 해결**:\n"
            md += "<details>\n"
            md += "<summary>문제 해결 보기</summary>\n\n"
            for ts in step.troubleshooting:
                md += f"- {ts}\n"
            md += "\n</details>\n\n"
        
        # Add completion info on last step
        if step_num == len(lab.steps):
            md += "---\n\n"
            md += "## 실습 완료\n\n"
            md += f"{lab.completion_summary}\n\n"
            
            if lab.next_steps:
                md += "**다음 단계**:\n"
                for ns in lab.next_steps:
                    md += f"- {ns}\n"
                md += "\n"
        
        return md


class QuizAgent:
    """Quiz 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
    
    def generate(self, service_name: str, rag_context: str) -> Quiz:
        """퀴즈 섹션 생성"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 DevOps 평가 전문가입니다.
주어진 서비스에 대한 퀴즈를 생성하세요.

반드시 다음 규칙을 따르세요:
1. 모든 내용은 한글로 작성
2. 최소 5개의 질문
3. 각 질문은 4개의 선택지
4. 모든 질문에 상세한 설명 포함
5. 다양한 유형 (지식, 시나리오, 명령어, 비교)

CRITICAL: questions는 반드시 배열(array)이어야 합니다. 객체가 아닙니다!

JSON 형식으로 응답하세요."""),
            ("user", """서비스: {service_name}

RAG 컨텍스트:
{rag_context}

다음 JSON 스키마로 정확히 응답하세요. questions는 배열입니다:
{{
  "questions": [
    {{
      "question": "질문 내용 (한글)",
      "choices": ["A) 선택지1", "B) 선택지2", "C) 선택지3", "D) 선택지4"],
      "answer": "A",
      "explanation": "상세한 설명 (한글)"
    }},
    {{
      "question": "질문 내용 2 (한글)",
      "choices": ["A) 선택지1", "B) 선택지2", "C) 선택지3", "D) 선택지4"],
      "answer": "B",
      "explanation": "상세한 설명 (한글)"
    }}
  ]
}}

최소 5개의 질문을 배열 형태로 생성하세요.""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "service_name": service_name,
            "rag_context": rag_context[:8000]
        })
        
        try:
            data = json.loads(response.content)
            
            # Validate and fix questions structure
            if "questions" in data:
                if isinstance(data["questions"], dict):
                    questions_list = []
                    for key, value in data["questions"].items():
                        if isinstance(value, dict) and "question" in value:
                            questions_list.append(value)
                        elif isinstance(value, str):
                            continue
                    data["questions"] = questions_list
                
                valid_questions = []
                for q in data["questions"]:
                    if isinstance(q, dict) and all(k in q for k in ["question", "choices", "answer", "explanation"]):
                        valid_questions.append(q)
                
                data["questions"] = valid_questions
                
                if len(data["questions"]) < 5:
                    print(f"⚠️ Warning: Only {len(data['questions'])} questions generated (expected 5+)")
                    if len(data["questions"]) == 0:
                        raise ValueError(f"No valid questions generated")
            
            return Quiz(**data)
            
        except json.JSONDecodeError as e:
            print(f"❌ JSON parsing error: {e}")
            print(f"Response content: {response.content[:500]}")
            raise
        except Exception as e:
            print(f"❌ Quiz validation error: {e}")
            print(f"Data structure: {data}")
            raise
    
    def format_markdown(self, quiz: Quiz) -> str:
        """Format as markdown with <details> tags"""
        md = "# 퀴즈 (Quiz)\n\n"
        
        for i, q in enumerate(quiz.questions, 1):
            md += f"## 질문 {i}\n\n"
            md += f"**{q.question}**\n\n"
            
            for choice in q.choices:
                md += f"{choice}\n"
            md += "\n"
            
            md += "<details>\n"
            md += "<summary>정답 및 해설 보기</summary>\n\n"
            md += f"**답**: {q.answer}\n\n"
            md += f"**설명**: {q.explanation}\n\n"
            md += "</details>\n\n"
            md += "---\n\n"
        
        return md
