"""Deep Dive 생성 에이전트"""
import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from src.vectorstore import VectorStoreManager
from .models import DeepDive
from .infographic import InfographicAgent


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
    
    def _validate_deep_dive(self, data: dict) -> DeepDive:
        """Validate and fix deep dive data structure"""
        
        # Validate scenarios field exists
        if "scenarios" not in data:
            raise ValueError("Missing required field: scenarios")
        
        # Validate and fix scenarios structure
        if isinstance(data["scenarios"], dict):
            scenarios_list = []
            for key, value in data["scenarios"].items():
                if isinstance(value, dict) and all(k in value for k in ["title", "description", "root_cause"]):
                    scenarios_list.append(value)
            data["scenarios"] = scenarios_list
        
        # Validate each scenario has required fields
        valid_scenarios = []
        required_scenario_fields = ["title", "description", "root_cause", 
                                   "diagnosis_steps", "resolution_steps", "verification_steps"]
        
        for s in data["scenarios"]:
            if isinstance(s, dict) and all(k in s for k in required_scenario_fields):
                valid_scenarios.append(s)
        
        data["scenarios"] = valid_scenarios
        
        # Validate minimum count
        if len(data["scenarios"]) < 2:
            raise ValueError(f"Only {len(data['scenarios'])} scenarios generated, need at least 2")
        
        return DeepDive(**data)
    
    def generate(self, service_name: str, rag_context: str) -> DeepDive:
        """Deep Dive 섹션 생성 with retry logic"""
        
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
        
        # Use retry logic from BaseAgent
        from src.agents.base_agent import BaseAgent
        base_agent = BaseAgent(
            name="DeepDiveAgent",
            collection_name="",
            system_prompt=""
        )
        
        return base_agent.generate_with_retry(
            chain=chain,
            input_dict={
                "service_name": service_name,
                "rag_context": rag_context[:8000]
            },
            validator_func=self._validate_deep_dive,
            error_context=f"Deep Dive for {service_name}"
        )
    
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
