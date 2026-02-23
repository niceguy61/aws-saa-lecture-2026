from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple


@dataclass(frozen=True)
class CurriculumEntry:
    day_number: int
    topic: str

    @property
    def week_day(self) -> Tuple[int, int]:
        # Curriculum is organized as 5 working days per week.
        week = ((self.day_number - 1) // 5) + 1
        day = ((self.day_number - 1) % 5) + 1
        return week, day


DAY_HEADING_RE = re.compile(r"^\s*####\s*Day\s+(\d+)\s*:\s*(.+?)\s*$")


def parse_curriculum_markdown(md: str) -> Dict[Tuple[int, int], CurriculumEntry]:
    """Parse `DevOps_6개월_교육과정_커리큘럼.md` into (week, day) -> entry mapping."""
    mapping: Dict[Tuple[int, int], CurriculumEntry] = {}
    for line in md.splitlines():
        m = DAY_HEADING_RE.match(line)
        if not m:
            continue
        day_num = int(m.group(1))
        topic = m.group(2).strip()
        entry = CurriculumEntry(day_number=day_num, topic=topic)
        mapping[entry.week_day] = entry
    return mapping


def load_curriculum(path: Path) -> Dict[Tuple[int, int], CurriculumEntry]:
    return parse_curriculum_markdown(path.read_text(encoding="utf-8"))


def guess_domain(topic: str) -> str:
    t = topic.lower()
    if "kubernetes" in t or "k8s" in t or "eks" in t or "helm" in t or "ingress" in t:
        return "kubernetes"
    if "aws" in t or "ec2" in t or "s3" in t or "rds" in t or "vpc" in t or "cloudfront" in t:
        return "aws"
    if "terraform" in t or "iac" in t:
        return "terraform"
    if "istio" in t or "service mesh" in t:
        return "istio"
    if "argo" in t or "gitops" in t:
        return "gitops"
    if "ci/cd" in t or "pipeline" in t or "jenkins" in t or "github actions" in t:
        return "cicd"
    if "msa" in t or "microservice" in t:
        return "msa"
    if "docker" in t or "컨테이너" in topic:
        return "docker"
    if "면접" in topic:
        return "interview"
    return "general"


def official_links_for_domain(domain: str) -> Iterable[Tuple[str, str]]:
    # Keep it small and stable. Users can extend later.
    links = {
        "docker": [
            ("Docker Docs", "https://docs.docker.com/"),
            ("Docker Get Started", "https://docs.docker.com/get-started/"),
            ("Docker Reference", "https://docs.docker.com/reference/"),
        ],
        "kubernetes": [
            ("Kubernetes Docs", "https://kubernetes.io/docs/"),
            ("Kubernetes Concepts", "https://kubernetes.io/docs/concepts/"),
            ("kubectl Reference", "https://kubernetes.io/docs/reference/kubectl/"),
        ],
        "aws": [
            ("AWS Documentation", "https://docs.aws.amazon.com/"),
            ("AWS CLI User Guide", "https://docs.aws.amazon.com/cli/latest/userguide/"),
            ("AWS Well-Architected", "https://docs.aws.amazon.com/wellarchitected/latest/framework/"),
        ],
        "terraform": [
            ("Terraform Docs", "https://developer.hashicorp.com/terraform/docs"),
            ("Terraform CLI", "https://developer.hashicorp.com/terraform/cli"),
            ("Terraform Language", "https://developer.hashicorp.com/terraform/language"),
        ],
        "istio": [
            ("Istio Docs", "https://istio.io/latest/docs/"),
            ("Istio Tasks", "https://istio.io/latest/docs/tasks/"),
            ("Istio Reference", "https://istio.io/latest/docs/reference/"),
        ],
        "gitops": [
            ("Argo CD Docs", "https://argo-cd.readthedocs.io/"),
            ("Argo Rollouts Docs", "https://argo-rollouts.readthedocs.io/"),
        ],
    }
    return links.get(domain, [])


def get_entry_for_week_day(
    mapping: Dict[Tuple[int, int], CurriculumEntry],
    week: int,
    day: int,
) -> Optional[CurriculumEntry]:
    return mapping.get((week, day))

