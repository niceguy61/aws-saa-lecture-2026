#!/usr/bin/env python3
"""CLI tool for validating generated lectures"""
import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from src.agents.validation_agent import LectureValidationAgent


def main():
    parser = argparse.ArgumentParser(
        description="Validate generated lecture content"
    )
    parser.add_argument(
        "--week", "-w",
        type=int,
        required=True,
        help="Week number (1-26)"
    )
    parser.add_argument(
        "--day", "-d",
        type=int,
        required=True,
        help="Day number (1-5)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="lectures",
        help="Lectures output directory (default: lectures)"
    )
    parser.add_argument(
        "--show-feedback",
        action="store_true",
        help="Show regeneration feedback if validation fails"
    )
    parser.add_argument(
        "--auto-fix",
        action="store_true",
        help="Automatically fix common issues (e.g., Mermaid backticks) before validation"
    )
    
    args = parser.parse_args()
    
    # Construct lecture directory path
    lecture_dir = Path(args.output_dir) / f"week{args.week}" / f"day{args.day}"
    
    if not lecture_dir.exists():
        print(f"\n❌ Error: Lecture directory not found: {lecture_dir}")
        print("   Generate the lecture first using generate_lecture.py")
        sys.exit(1)
    
    print(f"\n{'='*80}")
    print(f"Validating Lecture: Week {args.week}, Day {args.day}")
    print(f"Directory: {lecture_dir}")
    print(f"{'='*80}\n")
    
    # Create validation agent
    validator = LectureValidationAgent()
    
    # Auto-fix if requested
    if args.auto_fix:
        print(f"\n{'='*80}")
        print("🔧 Auto-fixing common issues...")
        print(f"{'='*80}\n")
        fixed_count = validator.auto_fix_mermaid_backticks(lecture_dir)
        if fixed_count > 0:
            print(f"✓ Fixed {fixed_count} file(s)\n")
    
    try:
        # Validate lecture
        result = validator.validate_lecture(args.week, args.day, lecture_dir)
        
        # Show feedback if requested and validation failed
        if args.show_feedback and not result.is_valid:
            print(f"\n{'='*80}")
            print("📝 Regeneration Feedback")
            print(f"{'='*80}\n")
            feedback = validator.generate_feedback_for_regeneration(result)
            print(feedback)
        
        # Exit with appropriate code
        sys.exit(0 if result.is_valid else 1)
        
    except Exception as e:
        print(f"\n❌ Validation failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(2)


if __name__ == "__main__":
    main()
