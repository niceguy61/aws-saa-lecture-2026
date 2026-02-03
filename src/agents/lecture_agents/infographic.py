"""인포그래픽 생성 에이전트"""
import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from src.vectorstore import VectorStoreManager
from .models import Infographic


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

**CRITICAL - Mermaid 예약어 금지**:
- 노드 ID로 'start', 'end', 'default', 'class', 'style' 등 예약어 사용 금지
- 대신 'Start', 'End', 'Begin', 'Finish', 'Step1', 'Step2' 등 사용
- 예: start(X) → Start(O), end(X) → End(O)

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
  "content": "```mermaid\\ngraph TD\\n  Start[시작] --> Step1[단계1]\\n  Step1 --> End[완료]\\n```",
  "image_references": ["https://docs.example.com/image1.png", ...]
}}

**CRITICAL**: 노드 ID는 반드시 대문자로 시작하거나 숫자를 포함하세요 (Start, End, Step1, Step2 등)

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
            
            # Fix Mermaid reserved keywords
            if data.get("type") == "mermaid" and "content" in data:
                data["content"] = self._fix_mermaid_reserved_keywords(data["content"])
            
            return Infographic(**data)
        except Exception as e:
            print(f"❌ Infographic generation error: {e}")
            print(f"Response content: {response.content[:500]}")
            # Return default infographic on error
            return Infographic(
                type="mermaid",
                content="```mermaid\ngraph LR\n  Start[시작] --> Progress[진행중]\n  Progress --> End[완료]\n```",
                image_references=None
            )
    
    def _fix_mermaid_reserved_keywords(self, content: str) -> str:
        """Fix Mermaid reserved keywords in diagram content"""
        import re
        
        # Mermaid reserved keywords that cannot be used as node IDs
        reserved_keywords = {
            r'\bstart\b': 'Start',
            r'\bend\b': 'End',
            r'\bdefault\b': 'Default',
            r'\bclass\b': 'Class',
            r'\bstyle\b': 'Style',
            r'\bgraph\b(?!\s+(TD|LR|TB|BT|RL))': 'Graph',  # Don't replace graph direction
            r'\bsubgraph\b(?!\s+\w)': 'Subgraph',  # Don't replace subgraph declaration
        }
        
        # Fix node IDs (case-insensitive for node IDs only)
        for pattern, replacement in reserved_keywords.items():
            # Fix in node definitions: start[label] -> Start[label]
            content = re.sub(
                pattern + r'(\[|\(|\{)',
                replacement + r'\1',
                content,
                flags=re.IGNORECASE
            )
            
            # Fix in connections: A --> start -> A --> Start
            content = re.sub(
                r'-->\s*' + pattern + r'\b',
                r'--> ' + replacement,
                content,
                flags=re.IGNORECASE
            )
            
            # Fix in style/class assignments: start:class -> Start:class
            content = re.sub(
                pattern + r':',
                replacement + ':',
                content,
                flags=re.IGNORECASE
            )
        
        # Remove invalid style declarations that use reserved keywords
        # style start fill:... -> (remove this line)
        content = re.sub(
            r'^\s*style\s+(start|end|default|class)\s+.*$',
            '',
            content,
            flags=re.MULTILINE | re.IGNORECASE
        )
        
        # Remove invalid classDef with reserved keywords
        content = re.sub(
            r'^\s*classDef\s+(start|end|default|class|style)\s+.*$',
            '',
            content,
            flags=re.MULTILINE | re.IGNORECASE
        )
        
        # Clean up multiple blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        return content
    
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
