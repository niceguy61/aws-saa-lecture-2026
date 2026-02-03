"""Add navigation to existing lecture files"""
from pathlib import Path
from src.agents.lecture_agents.design import DesignAgent

def add_navigation_to_day(week: int, day: int):
    """Add navigation to all files in a specific day"""
    design_agent = DesignAgent()
    
    day_dir = Path(f"lectures/week{week}/day{day}")
    if not day_dir.exists():
        print(f"❌ Directory not found: {day_dir}")
        return
    
    print(f"\n{'='*80}")
    print(f"📂 Processing: Week {week} Day {day}")
    print(f"{'='*80}\n")
    
    # Collect all lecture files
    lecture_files = {}
    
    # Service Understanding
    su_path = day_dir / "service_understanding.md"
    if su_path.exists():
        with open(su_path, 'r', encoding='utf-8') as f:
            lecture_files["service_understanding.md"] = f.read()
        print(f"✓ Found: service_understanding.md")
    
    # Deep Dive
    dd_path = day_dir / "deep_dive.md"
    if dd_path.exists():
        with open(dd_path, 'r', encoding='utf-8') as f:
            lecture_files["deep_dive.md"] = f.read()
        print(f"✓ Found: deep_dive.md")
    
    # Hands-on steps
    handson_files = sorted(day_dir.glob("handson_step*.md"))
    for handson_file in handson_files:
        with open(handson_file, 'r', encoding='utf-8') as f:
            lecture_files[handson_file.name] = f.read()
        print(f"✓ Found: {handson_file.name}")
    
    # Quiz
    quiz_path = day_dir / "quiz.md"
    if quiz_path.exists():
        with open(quiz_path, 'r', encoding='utf-8') as f:
            lecture_files["quiz.md"] = f.read()
        print(f"✓ Found: quiz.md")
    
    if not lecture_files:
        print(f"⚠️ No lecture files found in {day_dir}")
        return
    
    print(f"\n📝 Total files: {len(lecture_files)}")
    print(f"\n🎨 Applying design improvements with navigation...\n")
    
    # Apply design improvements with navigation
    improved_files = design_agent.design_lecture(lecture_files, week=week, day=day)
    
    # Save improved files
    for filename, content in improved_files.items():
        file_path = day_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"💾 Saved: {filename}")
    
    print(f"\n✅ Navigation added to {len(improved_files)} files in Week {week} Day {day}\n")

if __name__ == "__main__":
    # Add navigation to Week 1 Day 1
    add_navigation_to_day(1, 1)
    
    # Add navigation to Week 1 Day 2 if exists
    add_navigation_to_day(1, 2)
    
    print(f"\n{'='*80}")
    print("✅ All done!")
    print(f"{'='*80}\n")
