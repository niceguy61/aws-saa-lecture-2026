"""Lecture Generator - 독립적인 에이전트 사용"""
import sys
from pathlib import Path
from typing import List, Dict

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.vectorstore import VectorStoreManager
from src.agents.lecture_agents import (
    ServiceUnderstandingAgent,
    DeepDiveAgent,
    HandsOnLabAgent,
    QuizAgent
)


class LectureGenerator:
    """강의 생성 메인 클래스 - 각 에이전트 조율"""
    
    def __init__(self, model_name: str = "qwen3:8b", output_dir: str = "lectures"):
        self.vectorstore = VectorStoreManager()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # 독립적인 에이전트들 초기화
        self.service_understanding_agent = ServiceUnderstandingAgent(model_name)
        self.deep_dive_agent = DeepDiveAgent(model_name)
        self.hands_on_lab_agent = HandsOnLabAgent(model_name)
        self.quiz_agent = QuizAgent(model_name)
    
    def get_rag_context(self, query: str, collections: List[str]) -> str:
        """ChromaDB에서 관련 문서 검색"""
        all_docs = []
        
        for collection_name in collections:
            if collection_name:
                docs = self.vectorstore.search(
                    collection_name=collection_name,
                    query=query,
                    k=5
                )
                all_docs.extend(docs)
        
        return "\n\n".join(all_docs)
    
    def generate_daily_lecture(
        self,
        week: int,
        day: int,
        topic: str,
        services: List[str],
        collections: List[str]
    ) -> Dict[str, str]:
        """일별 강의 생성 - 점진적 저장"""
        
        print(f"\n{'='*80}")
        print(f"Generating Lecture: Week {week}, Day {day} - {topic}")
        print(f"Services: {', '.join(services)}")
        print(f"{'='*80}\n")
        
        # 1. 디렉토리 먼저 생성
        day_dir = self.output_dir / f"week{week}" / f"day{day}"
        day_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created directory: {day_dir}\n")
        
        saved_files = {}
        
        # RAG 컨텍스트 수집
        print("📚 Collecting RAG context from ChromaDB...")
        rag_context = self.get_rag_context(topic, collections)
        print(f"✓ Collected {len(rag_context)} characters of context\n")
        
        # 2. Service Understanding Agent
        try:
            print("🎓 [Service Understanding Agent] Generating...")
            su = self.service_understanding_agent.generate(services[0], rag_context)
            print("✓ Service Understanding complete")
            
            # 즉시 저장 (with infographics)
            su_md = self.service_understanding_agent.format_markdown(su, services[0], rag_context)
            su_path = day_dir / "service_understanding.md"
            with open(su_path, 'w', encoding='utf-8') as f:
                f.write(su_md)
            saved_files["service_understanding"] = str(su_path)
            print(f"💾 Saved: {su_path}\n")
        except Exception as e:
            print(f"❌ Service Understanding failed: {e}\n")
        
        # 3. Deep Dive Agent
        try:
            print("🔍 [Deep Dive Agent] Generating...")
            dd = self.deep_dive_agent.generate(services[0], rag_context)
            print("✓ Deep Dive complete")
            
            # 즉시 저장 (with infographics)
            dd_md = self.deep_dive_agent.format_markdown(dd, services[0], rag_context)
            dd_path = day_dir / "deep_dive.md"
            with open(dd_path, 'w', encoding='utf-8') as f:
                f.write(dd_md)
            saved_files["deep_dive"] = str(dd_path)
            print(f"💾 Saved: {dd_path}\n")
        except Exception as e:
            print(f"❌ Deep Dive failed: {e}\n")
        
        # 4. Hands-on Lab Agent
        try:
            print("🛠️ [Hands-on Lab Agent] Generating...")
            lab = self.hands_on_lab_agent.generate(services[0], rag_context)
            print("✓ Hands-on Lab complete")
            
            # 각 스텝 즉시 저장 (with infographics on step 1)
            for i, step in enumerate(lab.steps, 1):
                step_md = self.hands_on_lab_agent.format_step_markdown(
                    step, i, lab, services[0], rag_context
                )
                step_path = day_dir / f"handson_step{i}.md"
                with open(step_path, 'w', encoding='utf-8') as f:
                    f.write(step_md)
                saved_files[f"handson_step{i}"] = str(step_path)
                print(f"💾 Saved: {step_path}")
            print()
        except Exception as e:
            print(f"❌ Hands-on Lab failed: {e}\n")
        
        # 5. Quiz Agent (선택사항)
        try:
            print("📝 [Quiz Agent] Generating (optional)...")
            quiz = self.quiz_agent.generate(services[0], rag_context)
            print("✓ Quiz complete")
            
            # 즉시 저장
            quiz_md = self.quiz_agent.format_markdown(quiz)
            quiz_path = day_dir / "quiz.md"
            with open(quiz_path, 'w', encoding='utf-8') as f:
                f.write(quiz_md)
            saved_files["quiz"] = str(quiz_path)
            print(f"💾 Saved: {quiz_path}\n")
        except Exception as e:
            print(f"⚠️ Quiz generation failed (skipping): {e}\n")
        
        print(f"{'='*80}")
        print(f"✅ Lecture generation complete!")
        print(f"📂 Saved {len(saved_files)} files to: {day_dir}")
        print(f"{'='*80}\n")
        
        return saved_files
