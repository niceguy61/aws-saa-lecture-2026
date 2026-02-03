"""LangGraph workflow for lecture generation with validation"""
from typing import TypedDict, Annotated, List, Dict, Optional
from langgraph.graph import StateGraph, END
from pathlib import Path

from src.agents.lecture_agents import (
    ServiceUnderstandingAgent,
    DeepDiveAgent,
    HandsOnLabAgent,
    QuizAgent,
    DesignAgent
)
from src.agents.validation_agent import LectureValidationAgent, ValidationResult
from src.agents.evaluator_agent import EvaluatorAgent
from src.vectorstore import VectorStoreManager
from src.config import DEFAULT_PERSONA


class LectureState(TypedDict):
    """State for lecture generation workflow"""
    # Input parameters
    week: int
    day: int
    topic: str
    services: List[str]
    collections: List[str]
    output_dir: Path
    model_name: str
    max_retries: int
    persona: Optional[str]  # 페르소나 (예: "대학생", "주니어_DevOps_1년차")
    
    # RAG context
    rag_context: str
    
    # Generated content
    service_understanding: Optional[str]
    deep_dive: Optional[str]
    hands_on_steps: Optional[List[str]]
    quiz: Optional[str]
    
    # Validation
    validation_result: Optional[ValidationResult]
    feedback: Optional[str]
    attempt_count: int
    
    # Evaluation (페르소나 기반)
    evaluation_results: Optional[Dict]  # 섹션별 평가 결과
    needs_persona_improvement: bool  # 페르소나 기반 개선 필요 여부
    
    # File paths
    saved_files: Dict[str, str]
    
    # Control flow
    should_retry: bool
    is_complete: bool
    
    # Progress tracking
    total_steps: int  # 전체 단계 수
    completed_steps: int  # 완료된 단계 수
    current_phase: str  # 현재 진행 중인 단계 이름
    progress_percentage: float  # 진행률 (0-100)


class LectureGenerationWorkflow:
    """LangGraph workflow for lecture generation with validation loop"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.model_name = model_name
        self.vectorstore = VectorStoreManager()
        
        # Initialize agents
        self.su_agent = ServiceUnderstandingAgent(model_name)
        self.dd_agent = DeepDiveAgent(model_name)
        self.lab_agent = HandsOnLabAgent(model_name)
        self.quiz_agent = QuizAgent(model_name)
        self.validation_agent = LectureValidationAgent(model_name)
        self.evaluator_agent = EvaluatorAgent()
        self.design_agent = DesignAgent()
        
        # Build workflow
        self.workflow = self._build_workflow()
    
    def _calculate_total_steps(self, state: LectureState) -> int:
        """전체 단계 수 계산
        
        ServiceUnderstanding: 9 sub-steps (7 elements + 2 infographics)
        DeepDive: 2 scenarios × 2 sub-steps (scenario + infographic) = 4 sub-steps
        HandsOnLab: 동적 (최소 5개, 평균 8-10개 예상) + 1 infographic
        Quiz: 5 questions = 5 sub-steps
        Validation: 1 step
        Design: 4 files = 4 sub-steps
        Evaluation: 3 sections = 3 sub-steps (if persona set)
        Improvement: 3 sections = 3 sub-steps (if needed)
        
        Note: HandsOnLab steps are dynamic based on complexity
        """
        # Base steps: SU(9) + DD(4) + Lab(estimated 8) + Quiz(5) + Validation(1) + Design(4) = 31
        base_steps = 9 + 4 + 8 + 5 + 1 + 4  # 31 steps (Lab is estimated)
        
        if state.get("persona"):
            base_steps += 3  # evaluation
            # improvement steps added dynamically if needed
        
        return base_steps
    
    def _update_progress(self, state: LectureState, phase: str, steps_completed: int = 1) -> LectureState:
        """진행률 업데이트"""
        state["completed_steps"] = state.get("completed_steps", 0) + steps_completed
        state["current_phase"] = phase
        state["progress_percentage"] = (state["completed_steps"] / state["total_steps"]) * 100
        
        # Progress bar
        bar_length = 40
        filled = int(bar_length * state["progress_percentage"] / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        print(f"\n{'='*80}")
        print(f"📊 진행률: [{bar}] {state['progress_percentage']:.1f}%")
        print(f"🔄 현재 단계: {phase}")
        print(f"✓ 완료: {state['completed_steps']}/{state['total_steps']} 단계")
        print(f"{'='*80}\n")
        
        return state
    
    def _build_workflow(self) -> StateGraph:
        """Build the LangGraph workflow"""
        workflow = StateGraph(LectureState)
        
        # Add nodes
        workflow.add_node("collect_rag_context", self._collect_rag_context)
        workflow.add_node("generate_service_understanding", self._generate_service_understanding)
        workflow.add_node("generate_deep_dive", self._generate_deep_dive)
        workflow.add_node("generate_hands_on_lab", self._generate_hands_on_lab)
        workflow.add_node("generate_quiz", self._generate_quiz)
        workflow.add_node("validate_lecture", self._validate_lecture)
        workflow.add_node("design_lecture", self._design_lecture)
        workflow.add_node("evaluate_sections", self._evaluate_sections)
        workflow.add_node("improve_sections", self._improve_sections)
        workflow.add_node("prepare_retry", self._prepare_retry)
        workflow.add_node("finalize", self._finalize)
        
        # Set entry point
        workflow.set_entry_point("collect_rag_context")
        
        # Add edges
        workflow.add_edge("collect_rag_context", "generate_service_understanding")
        workflow.add_edge("generate_service_understanding", "generate_deep_dive")
        workflow.add_edge("generate_deep_dive", "generate_hands_on_lab")
        workflow.add_edge("generate_hands_on_lab", "generate_quiz")
        workflow.add_edge("generate_quiz", "validate_lecture")
        
        # Conditional edge from validation
        workflow.add_conditional_edges(
            "validate_lecture",
            self._should_retry_or_design,
            {
                "retry": "prepare_retry",
                "design": "design_lecture",
                "finish": "finalize",
            }
        )
        
        # After design, evaluate or finish
        workflow.add_conditional_edges(
            "design_lecture",
            self._should_evaluate_or_finish,
            {
                "evaluate": "evaluate_sections",
                "finish": "finalize",
            }
        )
        
        # Conditional edge from evaluation
        workflow.add_conditional_edges(
            "evaluate_sections",
            self._should_improve_or_finish,
            {
                "improve": "improve_sections",
                "finish": "finalize",
            }
        )
        
        # After improvement, validate again
        workflow.add_edge("improve_sections", "validate_lecture")
        
        # Retry loop
        workflow.add_edge("prepare_retry", "generate_service_understanding")
        
        # End
        workflow.add_edge("finalize", END)
        
        return workflow.compile()
    
    def _collect_rag_context(self, state: LectureState) -> LectureState:
        """Collect RAG context from ChromaDB"""
        state = self._update_progress(state, "RAG 컨텍스트 수집 중...", 0)
        print("📚 Collecting RAG context from ChromaDB...")
        
        all_docs = []
        for collection_name in state["collections"]:
            if collection_name:
                docs = self.vectorstore.search(
                    collection_name=collection_name,
                    query=state["topic"],
                    k=5
                )
                all_docs.extend(docs)
        
        rag_context = "\n\n".join(all_docs)
        print(f"✓ Collected {len(rag_context)} characters of context")
        
        state["rag_context"] = rag_context
        state["attempt_count"] = state.get("attempt_count", 0) + 1
        
        state = self._update_progress(state, "RAG 컨텍스트 수집 완료", 1)
        
        return state
    
    def _generate_service_understanding(self, state: LectureState) -> LectureState:
        """Generate Service Understanding section"""
        attempt = state["attempt_count"]
        if attempt > 1:
            print(f"\n🔄 [Attempt {attempt}] Regenerating Service Understanding with feedback...")
            if state.get("feedback"):
                print(f"📝 Feedback: {state['feedback'][:200]}...")
        else:
            print("🎓 [Service Understanding Agent] Generating...")
        
        state = self._update_progress(state, "서비스 이해 - 배경 정보 생성 중...", 0)
        
        try:
            # Create output directory
            day_dir = state["output_dir"] / f"week{state['week']}" / f"day{state['day']}"
            day_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate content (9 sub-steps tracked internally)
            # Sub-steps: background, concepts, advantages, disadvantages, use_cases, related_services, official_links, infographic1, infographic2
            su = self.su_agent.generate(state["services"][0], state["rag_context"])
            state = self._update_progress(state, "서비스 이해 - 7개 요소 생성 완료", 7)
            
            # Format and save (includes 2 infographics)
            su_md = self.su_agent.format_markdown(su, state["services"][0], state["rag_context"])
            state = self._update_progress(state, "서비스 이해 - 인포그래픽 생성 완료", 2)
            
            su_path = day_dir / "service_understanding.md"
            with open(su_path, 'w', encoding='utf-8') as f:
                f.write(su_md)
            
            state["service_understanding"] = su_md
            state["saved_files"]["service_understanding"] = str(su_path)
            
            print(f"✓ Service Understanding complete")
            print(f"💾 Saved: {su_path}")
            
        except Exception as e:
            print(f"❌ Service Understanding failed: {e}")
            state["service_understanding"] = None
        
        return state
    
    def _generate_deep_dive(self, state: LectureState) -> LectureState:
        """Generate Deep Dive section"""
        attempt = state["attempt_count"]
        if attempt > 1:
            print(f"🔄 [Attempt {attempt}] Regenerating Deep Dive...")
        else:
            print("🔍 [Deep Dive Agent] Generating...")
        
        state = self._update_progress(state, "Deep Dive - 트러블슈팅 시나리오 생성 중...", 0)
        
        try:
            day_dir = state["output_dir"] / f"week{state['week']}" / f"day{state['day']}"
            
            # Generate content (2 scenarios)
            dd = self.dd_agent.generate(state["services"][0], state["rag_context"])
            state = self._update_progress(state, "Deep Dive - 2개 시나리오 생성 완료", 2)
            
            # Format and save (includes 2 infographics)
            dd_md = self.dd_agent.format_markdown(dd, state["services"][0], state["rag_context"])
            state = self._update_progress(state, "Deep Dive - 인포그래픽 생성 완료", 2)
            
            dd_path = day_dir / "deep_dive.md"
            with open(dd_path, 'w', encoding='utf-8') as f:
                f.write(dd_md)
            
            state["deep_dive"] = dd_md
            state["saved_files"]["deep_dive"] = str(dd_path)
            
            print(f"✓ Deep Dive complete")
            print(f"💾 Saved: {dd_path}")
            
        except Exception as e:
            print(f"❌ Deep Dive failed: {e}")
            state["deep_dive"] = None
        
        return state
    
    def _generate_hands_on_lab(self, state: LectureState) -> LectureState:
        """Generate Hands-on Lab section"""
        attempt = state["attempt_count"]
        if attempt > 1:
            print(f"🔄 [Attempt {attempt}] Regenerating Hands-on Lab...")
        else:
            print("🛠️ [Hands-on Lab Agent] Generating...")
        
        state = self._update_progress(state, "Hands-on Lab - 실습 단계 생성 중...", 0)
        
        try:
            day_dir = state["output_dir"] / f"week{state['week']}" / f"day{state['day']}"
            
            # Generate content (dynamic steps based on complexity)
            lab = self.lab_agent.generate(state["services"][0], state["rag_context"])
            actual_steps = len(lab.steps)
            
            # Adjust total_steps if actual steps differ from estimated (8)
            estimated_steps = 8
            if actual_steps != estimated_steps:
                step_diff = actual_steps - estimated_steps
                state["total_steps"] = state.get("total_steps", 0) + step_diff
                print(f"  ℹ️ Adjusted total steps: {actual_steps} lab steps (estimated: {estimated_steps})")
            
            state = self._update_progress(state, f"Hands-on Lab - {actual_steps}개 단계 생성 완료", actual_steps)
            
            # Save each step (includes 1 infographic in first step)
            step_files = []
            for i, step in enumerate(lab.steps, 1):
                step_md = self.lab_agent.format_step_markdown(
                    step, i, lab, state["services"][0], state["rag_context"]
                )
                step_path = day_dir / f"handson_step{i}.md"
                with open(step_path, 'w', encoding='utf-8') as f:
                    f.write(step_md)
                
                step_files.append(step_md)
                state["saved_files"][f"handson_step{i}"] = str(step_path)
                print(f"💾 Saved: {step_path}")
            
            state = self._update_progress(state, "Hands-on Lab - 인포그래픽 생성 완료", 1)
            
            state["hands_on_steps"] = step_files
            print(f"✓ Hands-on Lab complete ({len(step_files)} steps)")
            
        except Exception as e:
            print(f"❌ Hands-on Lab failed: {e}")
            state["hands_on_steps"] = None
        
        return state
    
    def _generate_quiz(self, state: LectureState) -> LectureState:
        """Generate Quiz section"""
        attempt = state["attempt_count"]
        if attempt > 1:
            print(f"🔄 [Attempt {attempt}] Regenerating Quiz...")
        else:
            print("📝 [Quiz Agent] Generating...")
        
        state = self._update_progress(state, "Quiz - 퀴즈 문제 생성 중...", 0)
        
        try:
            day_dir = state["output_dir"] / f"week{state['week']}" / f"day{state['day']}"
            
            # Generate content (5 questions)
            quiz = self.quiz_agent.generate(state["services"][0], state["rag_context"])
            state = self._update_progress(state, f"Quiz - {len(quiz.questions)}개 문제 생성 완료", 5)
            
            # Format and save
            quiz_md = self.quiz_agent.format_markdown(quiz)
            quiz_path = day_dir / "quiz.md"
            with open(quiz_path, 'w', encoding='utf-8') as f:
                f.write(quiz_md)
            
            state["quiz"] = quiz_md
            state["saved_files"]["quiz"] = str(quiz_path)
            
            print(f"✓ Quiz complete")
            print(f"💾 Saved: {quiz_path}")
            
        except Exception as e:
            print(f"⚠️ Quiz generation failed (skipping): {e}")
            state["quiz"] = None
        
        return state
    
    def _validate_lecture(self, state: LectureState) -> LectureState:
        """Validate generated lecture"""
        state = self._update_progress(state, "검증 - 강의 내용 검증 중...", 0)
        
        print(f"{'='*80}")
        print("🔍 Starting Validation...")
        print(f"{'='*80}")
        
        day_dir = state["output_dir"] / f"week{state['week']}" / f"day{state['day']}"
        validation_result = self.validation_agent.validate_lecture(
            state["week"],
            state["day"],
            day_dir
        )
        
        state["validation_result"] = validation_result
        state["should_retry"] = not validation_result.is_valid and state["attempt_count"] < state["max_retries"]
        
        state = self._update_progress(state, "검증 완료", 1)
        
        return state
    
    def _should_retry_or_design(self, state: LectureState) -> str:
        """Decide whether to retry, apply design, or finish"""
        if state["should_retry"]:
            return "retry"
        
        # If validation passed, apply design improvements
        if state["validation_result"].is_valid:
            return "design"
        
        return "finish"
    
    def _should_evaluate_or_finish(self, state: LectureState) -> str:
        """Decide whether to evaluate or finish after design"""
        # If persona is set, evaluate
        if state.get("persona"):
            return "evaluate"
        
        return "finish"
    
    def _should_improve_or_finish(self, state: LectureState) -> str:
        """Decide whether to improve content or finish"""
        if state.get("needs_persona_improvement", False):
            return "improve"
        return "finish"
    
    def _evaluate_sections(self, state: LectureState) -> LectureState:
        """Evaluate sections based on persona"""
        persona = state.get("persona")
        if not persona:
            print("⚠️ No persona set, skipping evaluation")
            state["needs_persona_improvement"] = False
            return state
        
        state = self._update_progress(state, f"평가 - {persona} 페르소나 기반 평가 중...", 0)
        
        print(f"\n{'='*80}")
        print(f"🎯 Evaluating content for persona: {persona}")
        print(f"{'='*80}\n")
        
        evaluation_results = {}
        needs_improvement = False
        
        # Evaluate each section
        sections = {
            "service_understanding": state.get("service_understanding"),
            "deep_dive": state.get("deep_dive"),
            "quiz": state.get("quiz")
        }
        
        steps_per_section = 1
        for section_type, content in sections.items():
            if not content:
                continue
            
            print(f"📊 Evaluating {section_type}...")
            
            try:
                evaluation = self.evaluator_agent.evaluate_content(
                    content=content,
                    section_type=section_type,
                    persona_name=persona,
                    topic=state["topic"]
                )
                
                evaluation_results[section_type] = evaluation
                
                # Print evaluation summary
                print(f"  난이도: {evaluation.get('difficulty_level', 'N/A')}")
                print(f"  이해도: {evaluation.get('comprehension_level', 'N/A')}")
                print(f"  개선 필요: {'예' if evaluation.get('needs_improvement') else '아니오'}")
                
                if evaluation.get('needs_improvement'):
                    needs_improvement = True
                    print(f"  문제점: {len(evaluation.get('issues', []))}개")
                    print(f"  개선 제안: {len(evaluation.get('suggestions', []))}개")
                
                print()
                
                state = self._update_progress(state, f"평가 - {section_type} 평가 완료", steps_per_section)
                
            except Exception as e:
                print(f"  ⚠️ Evaluation failed: {e}\n")
        
        state["evaluation_results"] = evaluation_results
        state["needs_persona_improvement"] = needs_improvement
        
        if needs_improvement:
            print(f"⚠️ Content needs improvement for persona: {persona}\n")
            # Add improvement steps to total
            state["total_steps"] = state.get("total_steps", 0) + 3
        else:
            print(f"✅ Content is appropriate for persona: {persona}\n")
        
        return state
    
    def _improve_sections(self, state: LectureState) -> LectureState:
        """Improve sections based on evaluation"""
        persona = state.get("persona")
        evaluation_results = state.get("evaluation_results", {})
        
        state = self._update_progress(state, f"개선 - {persona} 페르소나 기반 개선 중...", 0)
        
        print(f"\n{'='*80}")
        print(f"🔧 Improving content for persona: {persona}")
        print(f"{'='*80}\n")
        
        day_dir = state["output_dir"] / f"week{state['week']}" / f"day{state['day']}"
        
        # Improve each section that needs it
        steps_per_section = 1
        for section_type, evaluation in evaluation_results.items():
            if not evaluation.get('needs_improvement'):
                continue
            
            print(f"🔧 Improving {section_type}...")
            
            try:
                # Get original content
                if section_type == "service_understanding":
                    original_content = state.get("service_understanding")
                elif section_type == "deep_dive":
                    original_content = state.get("deep_dive")
                elif section_type == "quiz":
                    original_content = state.get("quiz")
                else:
                    continue
                
                if not original_content:
                    continue
                
                # Improve content
                improved_content = self.evaluator_agent.improve_content(
                    content=original_content,
                    evaluation=evaluation,
                    section_type=section_type,
                    persona_name=persona,
                    topic=state["topic"]
                )
                
                # Save improved content
                file_name = f"{section_type}.md"
                file_path = day_dir / file_name
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(improved_content)
                
                # Update state
                if section_type == "service_understanding":
                    state["service_understanding"] = improved_content
                elif section_type == "deep_dive":
                    state["deep_dive"] = improved_content
                elif section_type == "quiz":
                    state["quiz"] = improved_content
                
                print(f"  ✓ Improved and saved: {file_path}")
                
                state = self._update_progress(state, f"개선 - {section_type} 개선 완료", steps_per_section)
                
            except Exception as e:
                print(f"  ⚠️ Improvement failed: {e}\n")
        
        # Reset evaluation flags for re-validation
        state["needs_persona_improvement"] = False
        state["evaluation_results"] = {}
        
        return state
    
    def _prepare_retry(self, state: LectureState) -> LectureState:
        """Prepare for retry by generating feedback"""
        print(f"\n{'='*80}")
        print(f"⚠️ Validation failed. Preparing for retry...")
        print(f"Attempt {state['attempt_count']}/{state['max_retries']}")
        print(f"{'='*80}\n")
        
        # Generate feedback
        feedback = self.validation_agent.generate_feedback_for_regeneration(
            state["validation_result"]
        )
        state["feedback"] = feedback
        
        print("📝 Feedback for regeneration:")
        print(feedback)
        print()
        
        # Delete failed files
        day_dir = state["output_dir"] / f"week{state['week']}" / f"day{state['day']}"
        critical_issues = [
            i for i in state["validation_result"].issues 
            if i.severity == "critical"
        ]
        
        for issue in critical_issues:
            if issue.location.endswith('.md'):
                file_to_delete = day_dir / issue.location
                if file_to_delete.exists():
                    file_to_delete.unlink()
                    print(f"🗑️ Deleted: {file_to_delete}")
        
        print()
        return state
    
    def _design_lecture(self, state: LectureState) -> LectureState:
        """Apply design improvements to all lecture files"""
        print(f"\n{'='*80}")
        print("🎨 [Design Agent] Improving readability and formatting...")
        print(f"{'='*80}\n")
        
        state = self._update_progress(state, "디자인 - 가독성 개선 중...", 0)
        
        day_dir = state["output_dir"] / f"week{state['week']}" / f"day{state['day']}"
        
        # Collect all lecture files
        lecture_files = {}
        
        # Service Understanding
        su_path = day_dir / "service_understanding.md"
        if su_path.exists():
            with open(su_path, 'r', encoding='utf-8') as f:
                lecture_files["service_understanding.md"] = f.read()
        
        state = self._update_progress(state, "디자인 - service_understanding.md 개선 완료", 1)
        
        # Deep Dive
        dd_path = day_dir / "deep_dive.md"
        if dd_path.exists():
            with open(dd_path, 'r', encoding='utf-8') as f:
                lecture_files["deep_dive.md"] = f.read()
        
        state = self._update_progress(state, "디자인 - deep_dive.md 개선 완료", 1)
        
        # Hands-on steps
        handson_files = sorted(day_dir.glob("handson_step*.md"))
        for handson_file in handson_files:
            with open(handson_file, 'r', encoding='utf-8') as f:
                lecture_files[handson_file.name] = f.read()
        
        # Quiz
        quiz_path = day_dir / "quiz.md"
        if quiz_path.exists():
            with open(quiz_path, 'r', encoding='utf-8') as f:
                lecture_files["quiz.md"] = f.read()
        
        state = self._update_progress(state, "디자인 - quiz.md 개선 완료", 1)
        
        # Apply design improvements
        try:
            improved_files = self.design_agent.design_lecture(
                lecture_files,
                week=state["week"],
                day=state["day"]
            )
            
            # Save improved files
            for filename, content in improved_files.items():
                file_path = day_dir / filename
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Improved: {filename}")
            
            state = self._update_progress(state, "디자인 - 모든 파일 개선 완료", 1)
            
            print(f"\n✅ Design improvements applied to {len(improved_files)} files\n")
            
        except Exception as e:
            print(f"⚠️ Design improvement failed: {e}\n")
        
        return state
    
    def _finalize(self, state: LectureState) -> LectureState:
        """Finalize the workflow"""
        state = self._update_progress(state, "완료", 0)
        
        if state["validation_result"].is_valid:
            print(f"{'='*80}")
            print(f"✅ Lecture generation complete!")
            print(f"📂 Saved {len(state['saved_files'])} files")
            print(f"{'='*80}\n")
        else:
            print(f"{'='*80}")
            print(f"❌ Maximum retries ({state['max_retries']}) reached.")
            print(f"⚠️ Lecture generated with validation issues.")
            print(f"📂 Files saved to: {state['output_dir']}/week{state['week']}/day{state['day']}")
            print(f"{'='*80}\n")
        
        state["is_complete"] = True
        return state
    
    def generate_lecture(
        self,
        week: int,
        day: int,
        topic: str,
        services: List[str],
        collections: List[str],
        output_dir: str = "lectures",
        max_retries: int = 2,
        persona: Optional[str] = None
    ) -> Dict[str, str]:
        """Generate lecture using LangGraph workflow
        
        Args:
            week: Week number
            day: Day number
            topic: Lecture topic
            services: List of services to cover
            collections: ChromaDB collections to query
            output_dir: Output directory for files
            max_retries: Maximum retry attempts
            persona: Target persona for content evaluation (optional, defaults to DEFAULT_PERSONA from .env)
        
        Returns:
            Dictionary of saved file paths
        """
        # Use DEFAULT_PERSONA from config if persona not explicitly provided
        if persona is None:
            persona = DEFAULT_PERSONA
        
        print(f"\n{'='*80}")
        print(f"🚀 LangGraph Workflow: Week {week}, Day {day} - {topic}")
        print(f"Services: {', '.join(services)}")
        print(f"Max Retries: {max_retries}")
        if persona:
            print(f"🎯 Persona: {persona} (from {'CLI argument' if persona != DEFAULT_PERSONA else '.env DEFAULT_PERSONA'})")
        else:
            print(f"🎯 Persona: None (evaluation disabled)")
        print(f"{'='*80}\n")
        
        # Initialize state
        initial_state: LectureState = {
            "week": week,
            "day": day,
            "topic": topic,
            "services": services,
            "collections": collections,
            "output_dir": Path(output_dir),
            "model_name": self.model_name,
            "max_retries": max_retries,
            "persona": persona,
            "rag_context": "",
            "service_understanding": None,
            "deep_dive": None,
            "hands_on_steps": None,
            "quiz": None,
            "validation_result": None,
            "feedback": None,
            "attempt_count": 0,
            "evaluation_results": None,
            "needs_persona_improvement": False,
            "saved_files": {},
            "should_retry": False,
            "is_complete": False,
            # Progress tracking
            "total_steps": 0,
            "completed_steps": 0,
            "current_phase": "초기화 중...",
            "progress_percentage": 0.0,
        }
        
        # Calculate total steps
        initial_state["total_steps"] = self._calculate_total_steps(initial_state)
        
        print(f"\n📊 총 예상 단계: {initial_state['total_steps']}개")
        print(f"{'='*80}\n")
        
        # Run workflow
        final_state = self.workflow.invoke(initial_state)
        
        return final_state["saved_files"]


def create_lecture_workflow(model_name: str = "qwen3:8b") -> LectureGenerationWorkflow:
    """Factory function to create lecture generation workflow"""
    return LectureGenerationWorkflow(model_name)
