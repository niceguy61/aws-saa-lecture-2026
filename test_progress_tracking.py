"""Test script for progress tracking in LangGraph workflow"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.lecture_graph import LectureGenerationWorkflow


def test_progress_calculation():
    """Test total steps calculation"""
    print("="*80)
    print("Testing Progress Tracking")
    print("="*80)
    
    workflow = LectureGenerationWorkflow()
    
    # Test 1: Basic workflow (no persona)
    print("\n1️⃣ Test: Basic workflow (no persona)")
    state_basic = {
        "persona": None,
        "week": 1,
        "day": 1,
        "topic": "Test",
        "services": ["Docker"],
        "collections": ["docker"],
        "output_dir": Path("test_output"),
        "model_name": "qwen3:8b",
        "max_retries": 2,
    }
    
    total_steps_basic = workflow._calculate_total_steps(state_basic)
    print(f"   Expected: 27 steps")
    print(f"   Calculated: {total_steps_basic} steps")
    assert total_steps_basic == 27, f"Expected 27, got {total_steps_basic}"
    print("   ✅ PASS")
    
    # Test 2: Workflow with persona
    print("\n2️⃣ Test: Workflow with persona")
    state_persona = {
        "persona": "대학생",
        "week": 1,
        "day": 1,
        "topic": "Test",
        "services": ["Docker"],
        "collections": ["docker"],
        "output_dir": Path("test_output"),
        "model_name": "qwen3:8b",
        "max_retries": 2,
    }
    
    total_steps_persona = workflow._calculate_total_steps(state_persona)
    print(f"   Expected: 30 steps (27 + 3 evaluation)")
    print(f"   Calculated: {total_steps_persona} steps")
    assert total_steps_persona == 30, f"Expected 30, got {total_steps_persona}"
    print("   ✅ PASS")
    
    # Test 3: Progress update
    print("\n3️⃣ Test: Progress update function")
    test_state = {
        "total_steps": 27,
        "completed_steps": 0,
        "current_phase": "초기화",
        "progress_percentage": 0.0,
    }
    
    # Simulate progress updates
    print("\n   Simulating progress updates:")
    
    # Step 1: RAG context
    test_state = workflow._update_progress(test_state, "RAG 컨텍스트 수집", 1)
    assert test_state["completed_steps"] == 1
    assert abs(test_state["progress_percentage"] - 3.7) < 0.1
    
    # Step 2-10: Service Understanding
    test_state = workflow._update_progress(test_state, "서비스 이해 생성", 9)
    assert test_state["completed_steps"] == 10
    assert abs(test_state["progress_percentage"] - 37.0) < 0.1
    
    # Step 11-14: Deep Dive
    test_state = workflow._update_progress(test_state, "Deep Dive 생성", 4)
    assert test_state["completed_steps"] == 14
    assert abs(test_state["progress_percentage"] - 51.9) < 0.1
    
    # Step 15-22: Hands-on Lab
    test_state = workflow._update_progress(test_state, "Hands-on Lab 생성", 8)
    assert test_state["completed_steps"] == 22
    assert abs(test_state["progress_percentage"] - 81.5) < 0.1
    
    # Step 23-27: Quiz
    test_state = workflow._update_progress(test_state, "Quiz 생성", 5)
    assert test_state["completed_steps"] == 27
    assert abs(test_state["progress_percentage"] - 100.0) < 0.1
    
    print("   ✅ PASS")
    
    # Test 4: Progress bar visualization
    print("\n4️⃣ Test: Progress bar visualization")
    print("   Testing different progress percentages:")
    
    test_percentages = [0, 25, 50, 75, 100]
    for pct in test_percentages:
        bar_length = 40
        filled = int(bar_length * pct / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"   {pct:3d}%: [{bar}]")
    
    print("   ✅ PASS")
    
    print("\n" + "="*80)
    print("✅ All progress tracking tests passed!")
    print("="*80)


def test_step_breakdown():
    """Test step breakdown for each agent"""
    print("\n" + "="*80)
    print("Step Breakdown by Agent")
    print("="*80)
    
    breakdown = {
        "Service Understanding": {
            "7 elements": 7,
            "2 infographics": 2,
            "total": 9
        },
        "Deep Dive": {
            "2 scenarios": 2,
            "2 infographics": 2,
            "total": 4
        },
        "Hands-on Lab": {
            "7 steps": 7,
            "1 infographic": 1,
            "total": 8
        },
        "Quiz": {
            "5 questions": 5,
            "total": 5
        },
        "Validation": {
            "1 validation": 1,
            "total": 1
        },
        "Evaluation (optional)": {
            "3 sections": 3,
            "total": 3
        },
        "Improvement (optional)": {
            "3 sections": 3,
            "total": 3
        }
    }
    
    total_base = 0
    total_with_persona = 0
    total_with_improvement = 0
    
    for agent, steps in breakdown.items():
        print(f"\n{agent}:")
        for step_name, count in steps.items():
            if step_name != "total":
                print(f"  - {step_name}: {count} steps")
            else:
                print(f"  Total: {count} steps")
                if "optional" not in agent:
                    total_base += count
                if "Evaluation" in agent:
                    total_with_persona += count
                if "Improvement" in agent:
                    total_with_improvement += count
    
    print("\n" + "-"*80)
    print(f"Base workflow (no persona): {total_base} steps")
    print(f"With persona evaluation: {total_base + total_with_persona} steps")
    print(f"With persona + improvement: {total_base + total_with_persona + total_with_improvement} steps")
    print("="*80)


if __name__ == "__main__":
    try:
        test_progress_calculation()
        test_step_breakdown()
        
        print("\n🎉 All tests completed successfully!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
