"""Quiz 생성 에이전트"""
import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from src.vectorstore import VectorStoreManager
from .models import Quiz


class QuizAgent:
    """Quiz 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
        
        # Import config values
        from src.config import MIN_QUIZ_QUESTIONS, MIN_QUIZ_QUESTIONS_MULTI_SERVICE
        self.min_questions = MIN_QUIZ_QUESTIONS
        self.min_questions_multi = MIN_QUIZ_QUESTIONS_MULTI_SERVICE
    
    def generate(self, service_name: str, rag_context: str, is_multi_service: bool = False) -> Quiz:
        """퀴즈 섹션 생성
        
        Args:
            service_name: 서비스 이름
            rag_context: RAG 컨텍스트
            is_multi_service: 멀티 서비스 여부 (True면 더 많은 질문 생성)
        """
        
        # Determine minimum questions based on service count
        min_questions = self.min_questions_multi if is_multi_service else self.min_questions
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"""당신은 DevOps 평가 전문가입니다.
주어진 서비스에 대한 퀴즈를 생성하세요.

반드시 다음 규칙을 따르세요:
1. 모든 내용은 한글로 작성
2. 최소 {min_questions}개의 질문
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

최소 """ + str(min_questions) + """개의 질문을 배열 형태로 생성하세요.""")
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
                
                # Use configured minimum
                if len(data["questions"]) < min_questions:
                    print(f"⚠️ Warning: Only {len(data['questions'])} questions generated (expected {min_questions}+)")
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
