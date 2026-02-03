"""Hands-on Lab 생성 에이전트"""
import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from src.vectorstore import VectorStoreManager
from .models import HandsOnLab, HandsOnStep
from .infographic import InfographicAgent


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
2. **커맨드 기반으로 1개씩 단위로 스텝을 나누세요**
   - 각 스텝은 1개의 주요 명령어 또는 작업을 수행
   - 예: "디렉토리 생성", "파일 작성", "이미지 빌드", "컨테이너 실행", "확인"
3. 스텝 개수는 유연하게 (7개 고정이 아님)
   - 간단한 실습: 5-7개 스텝
   - 복잡한 실습: 10-15개 스텝
   - 실제 작업 흐름에 맞춰 자연스럽게 나누기
4. 각 단계마다 검증 방법 포함
5. 실제 실행 가능한 명령어
6. 명령어에는 한글 주석 포함
7. **CRITICAL: Prerequisites와 Setup Instructions에 공식 문서 링크 필수 포함**
   - 각 사전 요구사항 항목마다 공식 설치/설정 가이드 링크
   - 각 환경 설정 단계마다 공식 문서 링크

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
  "prerequisites": [
    "Docker Desktop 24.0+ installed\\n  - 설치 가이드: https://docs.docker.com/desktop/install/",
    "AWS CLI configured\\n  - 설치: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html\\n  - 설정: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html",
    "기본 지식 (링크 포함)"
  ],
  "setup_instructions": [
    "설정 단계 1 (공식 문서 링크 포함)",
    "설정 단계 2 (공식 문서 링크 포함)"
  ],
  "steps": [
    {{
      "step_number": 1,
      "title": "단계 제목 (예: 프로젝트 디렉토리 생성)",
      "objective": "이 단계의 목표",
      "commands": "명령어 (bash 코드) - 1개의 주요 명령어",
      "expected_output": "예상 출력",
      "verification": "확인 명령어",
      "troubleshooting": ["문제1: 해결방법", ...]
    }},
    {{
      "step_number": 2,
      "title": "단계 제목 2 (예: package.json 파일 생성)",
      "objective": "이 단계의 목표 2",
      "commands": "명령어 (bash 코드) - 1개의 주요 명령어",
      "expected_output": "예상 출력",
      "verification": "확인 명령어",
      "troubleshooting": ["문제1: 해결방법", ...]
    }}
  ],
  "completion_summary": "실습 완료 요약",
  "next_steps": ["다음 단계1", ...]
}}

**중요**: 
1. 커맨드 기반으로 1개씩 단위로 스텝을 나누세요. 
2. **Prerequisites와 setup_instructions에 반드시 공식 문서 링크를 포함하세요**

예시:
- Step 1: 디렉토리 생성 (mkdir)
- Step 2: 파일 생성 (touch 또는 cat)
- Step 3: Dockerfile 작성 (cat > Dockerfile)
- Step 4: 이미지 빌드 (docker build)
- Step 5: 이미지 확인 (docker images)
- Step 6: 컨테이너 실행 (docker run)
- Step 7: 컨테이너 상태 확인 (docker ps)
- Step 8: 애플리케이션 테스트 (curl)
- Step 9: 로그 확인 (docker logs)
- Step 10: 정리 (docker stop, docker rm)

스텝 개수는 실습 복잡도에 따라 유연하게 조정하세요.""")
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
                
                # Minimum 5 steps, but flexible based on complexity
                if len(data["steps"]) < 5:
                    raise ValueError(f"Only {len(data['steps'])} steps generated, need at least 5")
            
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
