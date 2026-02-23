from __future__ import annotations

import argparse
from pathlib import Path

from .curriculum import get_entry_for_week_day, load_curriculum
from .scaffold import ScaffoldConfig, write_scaffold
from .validate import validate_day_dir


REPO_ROOT = Path(__file__).parent.parent
CURRICULUM_PATH = REPO_ROOT / "DevOps_6개월_교육과정_커리큘럼.md"
LECTURES_DIR = REPO_ROOT / "lectures"


def _day_dir(week: int, day: int) -> Path:
    return LECTURES_DIR / f"week{week}" / f"day{day}"


def cmd_generate(args: argparse.Namespace) -> int:
    mapping = load_curriculum(CURRICULUM_PATH)
    entry = get_entry_for_week_day(mapping, args.week, args.day)
    if not entry:
        print(f"ERROR: No curriculum entry for week={args.week}, day={args.day}")
        return 2

    cfg = ScaffoldConfig(lab_steps_min=args.lab_steps, quiz_questions_min=args.quiz_questions)
    out = _day_dir(args.week, args.day)
    written = write_scaffold(out, entry, cfg)
    print(f"OK: Wrote {len(written)} files under {out}")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    out = _day_dir(args.week, args.day)
    if not out.exists():
        print(f"ERROR: Day directory not found: {out}")
        return 2

    issues = validate_day_dir(out, lab_steps_min=args.lab_steps, quiz_questions_min=args.quiz_questions)
    if not issues:
        print("OK: No issues found")
        return 0

    exit_code = 0
    for it in issues:
        print(f"{it.severity.upper()}: {it.file}: {it.message}")
        if it.severity == "error":
            exit_code = 1
    return exit_code


def main() -> int:
    p = argparse.ArgumentParser(prog="lecture-cli")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("generate", help="Generate lecture scaffolds")
    g.add_argument("--week", type=int, required=True)
    g.add_argument("--day", type=int, required=True)
    g.add_argument("--lab-steps", type=int, default=7)
    g.add_argument("--quiz-questions", type=int, default=5)
    g.set_defaults(func=cmd_generate)

    v = sub.add_parser("validate", help="Validate generated lecture folder")
    v.add_argument("--week", type=int, required=True)
    v.add_argument("--day", type=int, required=True)
    v.add_argument("--lab-steps", type=int, default=7)
    v.add_argument("--quiz-questions", type=int, default=5)
    v.set_defaults(func=cmd_validate)

    args = p.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())

