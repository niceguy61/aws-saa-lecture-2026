#!/usr/bin/env python3
"""Quick verification script for Evaluator Agent integration"""
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

def verify_imports():
    """Verify all imports work"""
    print("✓ Verifying imports...")
    try:
        from src.agents.evaluator_agent import EvaluatorAgent
        from src.lecture_graph import create_lecture_workflow
        from src.config import DEFAULT_PERSONA, AVAILABLE_PERSONAS
        print("  ✓ All imports successful")
        return True
    except Exception as e:
        print(f"  ✗ Import failed: {e}")
        return False

def verify_evaluator_agent():
    """Verify EvaluatorAgent initialization"""
    print("✓ Verifying EvaluatorAgent...")
    try:
        from src.agents.evaluator_agent import EvaluatorAgent
        agent = EvaluatorAgent()
        
        # Check personas
        personas = agent.list_personas()
        assert len(personas) == 8, f"Expected 8 personas, got {len(personas)}"
        
        # Check persona info
        for persona in personas:
            info = agent.get_persona_info(persona)
            assert info is not None, f"Persona info missing for {persona}"
            assert 'level' in info
            assert 'description' in info
            assert 'knowledge' in info
            assert 'expectations' in info
        
        print(f"  ✓ EvaluatorAgent initialized with {len(personas)} personas")
        return True
    except Exception as e:
        print(f"  ✗ EvaluatorAgent verification failed: {e}")
        return False

def verify_workflow_integration():
    """Verify workflow has evaluator agent"""
    print("✓ Verifying workflow integration...")
    try:
        from src.lecture_graph import create_lecture_workflow
        workflow = create_lecture_workflow()
        
        assert hasattr(workflow, 'evaluator_agent'), "Workflow missing evaluator_agent"
        assert workflow.evaluator_agent is not None, "Evaluator agent not initialized"
        
        print("  ✓ Workflow has evaluator_agent")
        return True
    except Exception as e:
        print(f"  ✗ Workflow integration failed: {e}")
        return False

def verify_config():
    """Verify configuration"""
    print("✓ Verifying configuration...")
    try:
        from src.config import AVAILABLE_PERSONAS
        
        expected_personas = [
            "초등학생", "중학생", "고등학생", "대학생",
            "주니어_DevOps_1년차", "주니어_DevOps_2년차",
            "시니어_DevOps", "IT_비전공자"
        ]
        
        for persona in expected_personas:
            assert persona in AVAILABLE_PERSONAS, f"Missing persona in config: {persona}"
        
        print(f"  ✓ Configuration has {len(AVAILABLE_PERSONAS)} personas")
        return True
    except Exception as e:
        print(f"  ✗ Configuration verification failed: {e}")
        return False

def verify_files():
    """Verify documentation files exist"""
    print("✓ Verifying documentation files...")
    try:
        files = [
            "EVALUATOR_AGENT_GUIDE.md",
            "EVALUATOR_INTEGRATION_SUMMARY.md",
            "test_evaluator.py",
            "src/agents/evaluator_agent.py"
        ]
        
        for file in files:
            path = Path(file)
            assert path.exists(), f"Missing file: {file}"
        
        print(f"  ✓ All {len(files)} documentation files exist")
        return True
    except Exception as e:
        print(f"  ✗ File verification failed: {e}")
        return False

def main():
    """Run all verifications"""
    print("\n" + "="*80)
    print("🔍 EVALUATOR AGENT INTEGRATION VERIFICATION")
    print("="*80 + "\n")
    
    results = []
    
    results.append(("Imports", verify_imports()))
    results.append(("EvaluatorAgent", verify_evaluator_agent()))
    results.append(("Workflow Integration", verify_workflow_integration()))
    results.append(("Configuration", verify_config()))
    results.append(("Documentation Files", verify_files()))
    
    print("\n" + "="*80)
    print("📊 VERIFICATION SUMMARY")
    print("="*80 + "\n")
    
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {name}")
    
    all_passed = all(result[1] for result in results)
    
    if all_passed:
        print("\n" + "="*80)
        print("✅ ALL VERIFICATIONS PASSED!")
        print("="*80 + "\n")
        print("🎉 Evaluator Agent is fully integrated and ready to use!")
        print()
        print("📝 Quick Start:")
        print("  1. CLI: python generate_lecture.py --week 1 --day 3 --use-langgraph --persona \"대학생\"")
        print("  2. UI: python app.py (select persona from dropdown)")
        print("  3. Docs: See EVALUATOR_AGENT_GUIDE.md for details")
        print()
        return 0
    else:
        print("\n" + "="*80)
        print("❌ SOME VERIFICATIONS FAILED")
        print("="*80 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
