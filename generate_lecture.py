#!/usr/bin/env python3
"""CLI tool for generating daily lectures"""
import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from src.lecture_generator import LectureGenerator


# 커리큘럼 매핑 (Week, Day -> Topic, Services, Collections)
CURRICULUM_MAP = {
    # Week 1
    (1, 1): {
        "topic": "DevOps 개요 및 문화",
        "services": ["DevOps"],
        "collections": []  # 일반 지식
    },
    (1, 2): {
        "topic": "컨테이너 기술 개요 및 Docker 소개",
        "services": ["Docker"],
        "collections": ["docker_collection"]
    },
    (1, 3): {
        "topic": "Docker 이미지 기초",
        "services": ["Docker Images"],
        "collections": ["docker_collection"]
    },
    (1, 4): {
        "topic": "Docker 컨테이너 관리",
        "services": ["Docker Containers"],
        "collections": ["docker_collection"]
    },
    (1, 5): {
        "topic": "Docker 네트워킹 기초",
        "services": ["Docker Networking"],
        "collections": ["docker_collection"]
    },
    
    # Week 2
    (2, 1): {
        "topic": "Dockerfile 최적화",
        "services": ["Dockerfile"],
        "collections": ["docker_collection"]
    },
    (2, 2): {
        "topic": "Docker Registry 및 이미지 배포",
        "services": ["Docker Registry"],
        "collections": ["docker_collection"]
    },
    
    # Week 5 - AWS
    (5, 1): {
        "topic": "AWS 클라우드 개요",
        "services": ["AWS"],
        "collections": ["aws_collection"]
    },
    
    # Week 9 - Kubernetes
    (9, 1): {
        "topic": "Kubernetes 소개",
        "services": ["Kubernetes"],
        "collections": ["kubernetes_collection"]
    },
    (9, 2): {
        "topic": "Kubernetes 환경 구성",
        "services": ["Kubernetes Setup"],
        "collections": ["kubernetes_collection"]
    },
    (9, 3): {
        "topic": "Kubernetes Pods",
        "services": ["Pods"],
        "collections": ["kubernetes_collection"]
    },
    (9, 4): {
        "topic": "Deployments 및 ReplicaSets",
        "services": ["Deployments", "ReplicaSets"],
        "collections": ["kubernetes_collection"]
    },
    (9, 5): {
        "topic": "Kubernetes Services",
        "services": ["Services"],
        "collections": ["kubernetes_collection"]
    },
    
    # Week 21 - Terraform
    (21, 1): {
        "topic": "IaC 개념 및 Terraform 소개",
        "services": ["Terraform"],
        "collections": ["terraform_collection"]
    },
    (21, 2): {
        "topic": "Terraform 기본 문법",
        "services": ["Terraform HCL"],
        "collections": ["terraform_collection"]
    },
}


def main():
    parser = argparse.ArgumentParser(
        description="Generate daily lecture content using RAG and LLM"
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
        "--topic", "-t",
        type=str,
        help="Custom topic (overrides curriculum map)"
    )
    parser.add_argument(
        "--services", "-s",
        type=str,
        nargs="+",
        help="Services to cover (overrides curriculum map)"
    )
    parser.add_argument(
        "--collections", "-c",
        type=str,
        nargs="+",
        help="ChromaDB collections to query (overrides curriculum map)"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available curriculum mappings"
    )
    
    args = parser.parse_args()
    
    # List curriculum
    if args.list:
        print("\n" + "="*80)
        print("Available Curriculum Mappings")
        print("="*80 + "\n")
        
        for (week, day), info in sorted(CURRICULUM_MAP.items()):
            print(f"Week {week}, Day {day}: {info['topic']}")
            print(f"  Services: {', '.join(info['services'])}")
            print(f"  Collections: {', '.join(info['collections']) if info['collections'] else 'None'}")
            print()
        
        return
    
    # Get curriculum info
    key = (args.week, args.day)
    
    if key in CURRICULUM_MAP and not (args.topic or args.services or args.collections):
        # Use curriculum map
        curriculum = CURRICULUM_MAP[key]
        topic = curriculum["topic"]
        services = curriculum["services"]
        collections = curriculum["collections"]
        print(f"\n📚 Using curriculum map for Week {args.week}, Day {args.day}")
    else:
        # Use custom parameters
        if not args.topic or not args.services:
            print("\n❌ Error: --topic and --services are required for custom lectures")
            print("   Or use a week/day combination from the curriculum map")
            print("   Use --list to see available mappings")
            sys.exit(1)
        
        topic = args.topic
        services = args.services
        collections = args.collections or []
        curriculum = {"topic": topic, "services": services, "collections": collections}
        print(f"\n📚 Using custom parameters")
    
    print(f"   Topic: {topic}")
    print(f"   Services: {', '.join(services)}")
    print(f"   Collections: {', '.join(collections) if collections else 'None'}")
    print()
    
    # Generate lecture
    generator = LectureGenerator()
    
    try:
        # Generate lecture (now returns saved_files dict directly)
        saved_files = generator.generate_daily_lecture(
            week=args.week,
            day=args.day,
            topic=topic,
            services=services,
            collections=collections
        )
        
        print("\n" + "="*80)
        print("✅ SUCCESS!")
        print("="*80)
        print(f"\n📚 Generated lecture for Week {args.week}, Day {args.day}")
        print(f"📖 Topic: {curriculum['topic']}")
        print(f"\n📂 Files saved:")
        for file_type, file_path in saved_files.items():
            print(f"  - {file_type}: {file_path}")
        print()
        
    except Exception as e:
        print(f"\n❌ Failed to generate lecture: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
