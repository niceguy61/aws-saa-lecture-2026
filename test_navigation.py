"""Test navigation generation"""
from src.agents.lecture_agents.design import DesignAgent

# Create design agent
design_agent = DesignAgent()

# Test files
test_files = {
    "service_understanding.md": "# Test Service Understanding\n\nSome content here.",
    "deep_dive.md": "# Test Deep Dive\n\nSome content here.",
    "handson_step1.md": "# Test Hands-on Step 1\n\nSome content here.",
    "handson_step2.md": "# Test Hands-on Step 2\n\nSome content here.",
    "quiz.md": "# Test Quiz\n\nSome content here."
}

# Apply design with navigation
improved_files = design_agent.design_lecture(test_files, week=1, day=1)

# Check if navigation was added
for filename, content in improved_files.items():
    print(f"\n{'='*80}")
    print(f"File: {filename}")
    print(f"{'='*80}")
    
    # Check for navigation markers
    has_top_nav = "Week 1 - Day 1" in content
    has_bottom_nav = "학습 완료" in content
    has_prev_next = "이전" in content and "다음" in content
    
    print(f"Has top navigation: {has_top_nav}")
    print(f"Has bottom navigation: {has_bottom_nav}")
    print(f"Has prev/next buttons: {has_prev_next}")
    
    # Show first 500 chars
    print(f"\nFirst 500 chars:")
    print(content[:500])
    
    # Show last 500 chars
    print(f"\nLast 500 chars:")
    print(content[-500:])

print(f"\n{'='*80}")
print("Test complete!")
