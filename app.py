#!/usr/bin/env python3
"""Gradio UI for DevOps Lecture Generation Pipeline"""
import gradio as gr
import sys
from pathlib import Path
from datetime import datetime
import json

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from src.lecture_graph import create_lecture_workflow
from src.lecture_generator import LectureGenerator
from src.config import DEFAULT_PERSONA, AVAILABLE_PERSONAS


# 커리큘럼 매핑 (130일 전체)
CURRICULUM_MAP = {
    # Week 1: DevOps 기본 이론 및 환경 구성
    (1, 1): {"topic": "DevOps 개요 및 문화", "services": ["DevOps"], "collections": []},
    (1, 2): {"topic": "컨테이너 기술 개요 및 Docker 소개", "services": ["Docker"], "collections": ["docker_collection"]},
    (1, 3): {"topic": "Docker 이미지 기초", "services": ["Docker Images"], "collections": ["docker_collection"]},
    (1, 4): {"topic": "Docker 컨테이너 관리", "services": ["Docker Containers"], "collections": ["docker_collection"]},
    (1, 5): {"topic": "Docker 네트워킹 기초", "services": ["Docker Networking"], "collections": ["docker_collection"]},
    
    # Week 2: Docker 심화
    (2, 1): {"topic": "Dockerfile 최적화", "services": ["Dockerfile"], "collections": ["docker_collection"]},
    (2, 2): {"topic": "Docker Registry 및 이미지 배포", "services": ["Docker Registry"], "collections": ["docker_collection"]},
    (2, 3): {"topic": "Docker Compose 기초", "services": ["Docker Compose"], "collections": ["docker_collection"]},
    (2, 4): {"topic": "Docker Compose 심화", "services": ["Docker Compose"], "collections": ["docker_collection"]},
    (2, 5): {"topic": "Docker Swarm 소개", "services": ["Docker Swarm"], "collections": ["docker_collection"]},
    
    # Week 3: Docker 실전 프로젝트 및 MSA 기초
    (3, 1): {"topic": "Docker 보안", "services": ["Docker Security"], "collections": ["docker_collection"]},
    (3, 2): {"topic": "MSA 개요", "services": ["Microservices"], "collections": []},
    (3, 3): {"topic": "MSA 통신 패턴", "services": ["Microservices Communication"], "collections": []},
    (3, 4): {"topic": "Docker 기반 MSA 구현", "services": ["Docker", "Microservices"], "collections": ["docker_collection"]},
    (3, 5): {"topic": "1개월차 종합 프로젝트", "services": ["Docker", "Microservices"], "collections": ["docker_collection"]},
    
    # Week 4: Docker 고급 주제 및 실전 운영
    (4, 1): {"topic": "Docker 모니터링 및 로깅", "services": ["Docker Monitoring"], "collections": ["docker_collection"]},
    (4, 2): {"topic": "Docker 성능 최적화", "services": ["Docker Performance"], "collections": ["docker_collection"]},
    (4, 3): {"topic": "Docker 트러블슈팅", "services": ["Docker Troubleshooting"], "collections": ["docker_collection"]},
    (4, 4): {"topic": "Docker 실전 운영 사례", "services": ["Docker Operations"], "collections": ["docker_collection"]},
    (4, 5): {"topic": "1개월차 최종 평가", "services": ["Docker"], "collections": ["docker_collection"]},
    
    # Week 5: AWS 기본 이해 및 핵심 서비스
    (5, 1): {"topic": "AWS 클라우드 개요", "services": ["AWS"], "collections": ["aws_collection"]},
    (5, 2): {"topic": "EC2", "services": ["EC2"], "collections": ["aws_collection"]},
    (5, 3): {"topic": "AWS 스토리지 (S3, EBS)", "services": ["S3", "EBS"], "collections": ["aws_collection"]},
    (5, 4): {"topic": "AWS 데이터베이스 (RDS)", "services": ["RDS"], "collections": ["aws_collection"]},
    (5, 5): {"topic": "VPC", "services": ["VPC"], "collections": ["aws_collection"]},
    
    # Week 6: AWS 네트워킹 및 로드 밸런싱
    (6, 1): {"topic": "AWS 로드 밸런싱 (ELB, ALB, NLB)", "services": ["ELB", "ALB", "NLB"], "collections": ["aws_collection"]},
    (6, 2): {"topic": "Auto Scaling", "services": ["Auto Scaling"], "collections": ["aws_collection"]},
    (6, 3): {"topic": "Route 53 및 CloudFront", "services": ["Route 53", "CloudFront"], "collections": ["aws_collection"]},
    (6, 4): {"topic": "AWS 보안 (IAM, KMS)", "services": ["IAM", "KMS"], "collections": ["aws_collection"]},
    (6, 5): {"topic": "모니터링 및 로깅 (CloudWatch)", "services": ["CloudWatch"], "collections": ["aws_collection"]},
    
    # Week 7: AWS 컨테이너 서비스
    (7, 1): {"topic": "AWS 컨테이너 서비스 개요", "services": ["ECS", "EKS", "Fargate"], "collections": ["aws_collection"]},
    (7, 2): {"topic": "ECS 기초", "services": ["ECS"], "collections": ["aws_collection"]},
    (7, 3): {"topic": "Fargate", "services": ["Fargate"], "collections": ["aws_collection"]},
    (7, 4): {"topic": "EKS 소개", "services": ["EKS"], "collections": ["aws_collection"]},
    (7, 5): {"topic": "AWS 컨테이너 실습", "services": ["ECS", "EKS"], "collections": ["aws_collection"]},
    
    # Week 8: AWS 고급 서비스
    (8, 1): {"topic": "Lambda 및 서버리스", "services": ["Lambda"], "collections": ["aws_collection"]},
    (8, 2): {"topic": "메시징 서비스 (SQS, SNS)", "services": ["SQS", "SNS"], "collections": ["aws_collection"]},
    (8, 3): {"topic": "인프라 자동화 기초 (CloudFormation)", "services": ["CloudFormation"], "collections": ["aws_collection"]},
    (8, 4): {"topic": "비용 관리", "services": ["Cost Explorer"], "collections": ["aws_collection"]},
    (8, 5): {"topic": "2개월차 종합 프로젝트", "services": ["AWS"], "collections": ["aws_collection"]},
    
    # Week 9: Kubernetes 기본 개념
    (9, 1): {"topic": "Kubernetes 소개", "services": ["Kubernetes"], "collections": ["kubernetes_collection"]},
    (9, 2): {"topic": "환경 구성 (Minikube, kubectl)", "services": ["Kubernetes Setup"], "collections": ["kubernetes_collection"]},
    (9, 3): {"topic": "Pods", "services": ["Pods"], "collections": ["kubernetes_collection"]},
    (9, 4): {"topic": "ReplicaSets 및 Deployments", "services": ["Deployments", "ReplicaSets"], "collections": ["kubernetes_collection"]},
    (9, 5): {"topic": "Services", "services": ["Services"], "collections": ["kubernetes_collection"]},
    
    # Week 10: Kubernetes 핵심 리소스
    (10, 1): {"topic": "ConfigMaps 및 Secrets", "services": ["ConfigMaps", "Secrets"], "collections": ["kubernetes_collection"]},
    (10, 2): {"topic": "Volumes 및 Persistent Storage", "services": ["Volumes", "PV", "PVC"], "collections": ["kubernetes_collection"]},
    (10, 3): {"topic": "Namespaces 및 리소스 관리", "services": ["Namespaces"], "collections": ["kubernetes_collection"]},
    (10, 4): {"topic": "Labels, Selectors, Annotations", "services": ["Labels"], "collections": ["kubernetes_collection"]},
    (10, 5): {"topic": "네트워킹 심화 (Ingress)", "services": ["Ingress"], "collections": ["kubernetes_collection"]},
    
    # Week 11: Kubernetes 고급 리소스
    (11, 1): {"topic": "DaemonSets 및 Jobs", "services": ["DaemonSets", "Jobs"], "collections": ["kubernetes_collection"]},
    (11, 2): {"topic": "StatefulSets", "services": ["StatefulSets"], "collections": ["kubernetes_collection"]},
    (11, 3): {"topic": "RBAC", "services": ["RBAC"], "collections": ["kubernetes_collection"]},
    (11, 4): {"topic": "Resource Limits 및 QoS", "services": ["Resource Limits"], "collections": ["kubernetes_collection"]},
    (11, 5): {"topic": "모니터링 및 로깅", "services": ["Prometheus", "Grafana"], "collections": ["kubernetes_collection"]},
    
    # Week 12: Kubernetes 공식 문서 Deep Dive
    (12, 1): {"topic": "Workloads Deep Dive", "services": ["Workloads"], "collections": ["kubernetes_collection"]},
    (12, 2): {"topic": "Services & Networking Deep Dive", "services": ["Services", "Networking"], "collections": ["kubernetes_collection"]},
    (12, 3): {"topic": "Storage & Configuration Deep Dive", "services": ["Storage"], "collections": ["kubernetes_collection"]},
    (12, 4): {"topic": "Security & Policies Deep Dive", "services": ["Security"], "collections": ["kubernetes_collection"]},
    (12, 5): {"topic": "3개월차 종합 프로젝트", "services": ["Kubernetes"], "collections": ["kubernetes_collection"]},
    
    # Week 13: 클라우드 네이티브 Kubernetes
    (13, 1): {"topic": "EKS 심화", "services": ["EKS"], "collections": ["aws_collection", "kubernetes_collection"]},
    (13, 2): {"topic": "EKS 네트워킹 및 보안", "services": ["EKS Networking"], "collections": ["aws_collection", "kubernetes_collection"]},
    (13, 3): {"topic": "GKE", "services": ["GKE"], "collections": ["kubernetes_collection"]},
    (13, 4): {"topic": "AKS", "services": ["AKS"], "collections": ["kubernetes_collection"]},
    (13, 5): {"topic": "K8s 배포 시 AWS 고려사항", "services": ["EKS"], "collections": ["aws_collection", "kubernetes_collection"]},
    
    # Week 14: Kubernetes 고급 운영
    (14, 1): {"topic": "Helm", "services": ["Helm"], "collections": ["kubernetes_collection"]},
    (14, 2): {"topic": "Operators", "services": ["Operators"], "collections": ["kubernetes_collection"]},
    (14, 3): {"topic": "고급 스케줄링", "services": ["Scheduling"], "collections": ["kubernetes_collection"]},
    (14, 4): {"topic": "트러블슈팅", "services": ["Troubleshooting"], "collections": ["kubernetes_collection"]},
    (14, 5): {"topic": "업그레이드 및 유지보수", "services": ["Upgrade"], "collections": ["kubernetes_collection"]},
    
    # Week 15: Istio Service Mesh
    (15, 1): {"topic": "Service Mesh 및 Istio 소개", "services": ["Istio"], "collections": ["istio_collection"]},
    (15, 2): {"topic": "Istio 트래픽 관리", "services": ["Istio Traffic"], "collections": ["istio_collection"]},
    (15, 3): {"topic": "Istio 보안", "services": ["Istio Security"], "collections": ["istio_collection"]},
    (15, 4): {"topic": "Istio 관찰성", "services": ["Istio Observability"], "collections": ["istio_collection"]},
    (15, 5): {"topic": "Istio 고급 기능", "services": ["Istio Advanced"], "collections": ["istio_collection"]},
    
    # Week 16: Kubernetes 실전 프로젝트
    (16, 1): {"topic": "프로젝트 계획", "services": ["Project Planning"], "collections": []},
    (16, 2): {"topic": "인프라 구현", "services": ["EKS", "Istio"], "collections": ["aws_collection", "kubernetes_collection", "istio_collection"]},
    (16, 3): {"topic": "애플리케이션 구현", "services": ["Microservices"], "collections": ["kubernetes_collection"]},
    (16, 4): {"topic": "최적화 및 테스트", "services": ["Performance"], "collections": []},
    (16, 5): {"topic": "프로젝트 발표", "services": ["Project"], "collections": []},
    
    # Week 17: CI/CD 기초
    (17, 1): {"topic": "CI/CD 개념", "services": ["CI/CD"], "collections": []},
    (17, 2): {"topic": "CI - 빌드 및 테스트", "services": ["CI Build"], "collections": []},
    (17, 3): {"topic": "CI - 보안 및 품질", "services": ["CI Security"], "collections": []},
    (17, 4): {"topic": "CD - 배포 전략", "services": ["CD Deployment"], "collections": []},
    (17, 5): {"topic": "CD - 환경 관리", "services": ["CD Environment"], "collections": []},
    
    # Week 18: CI/CD 도구 실습
    (18, 1): {"topic": "GitHub Actions 기초", "services": ["GitHub Actions"], "collections": []},
    (18, 2): {"topic": "GitHub Actions 심화", "services": ["GitHub Actions"], "collections": []},
    (18, 3): {"topic": "Jenkins 기초", "services": ["Jenkins"], "collections": []},
    (18, 4): {"topic": "Jenkins 심화", "services": ["Jenkins"], "collections": []},
    (18, 5): {"topic": "기타 CI/CD 도구", "services": ["CircleCI", "GitLab CI"], "collections": []},
    
    # Week 19: CI/CD 최적화
    (19, 1): {"topic": "파이프라인 최적화", "services": ["Pipeline Optimization"], "collections": []},
    (19, 2): {"topic": "CI/CD 보안", "services": ["Pipeline Security"], "collections": []},
    (19, 3): {"topic": "모니터링 및 관찰성", "services": ["Pipeline Monitoring"], "collections": []},
    (19, 4): {"topic": "주의사항 및 트러블슈팅", "services": ["Pipeline Troubleshooting"], "collections": []},
    (19, 5): {"topic": "Docker Image Registry 심화", "services": ["Registry"], "collections": ["docker_collection"]},
    
    # Week 20: GitOps 및 ArgoCD
    (20, 1): {"topic": "GitOps 개념", "services": ["GitOps"], "collections": ["argocd_collection"]},
    (20, 2): {"topic": "ArgoCD 기초", "services": ["ArgoCD"], "collections": ["argocd_collection"]},
    (20, 3): {"topic": "ArgoCD 심화", "services": ["ArgoCD"], "collections": ["argocd_collection"]},
    (20, 4): {"topic": "ArgoCD 고급", "services": ["ArgoCD", "Argo Rollouts"], "collections": ["argocd_collection"]},
    (20, 5): {"topic": "5개월차 종합 프로젝트", "services": ["CI/CD", "GitOps"], "collections": []},
    
    # Week 21: Terraform 기초
    (21, 1): {"topic": "IaC 개념 및 Terraform 소개", "services": ["Terraform"], "collections": ["terraform_collection"]},
    (21, 2): {"topic": "Terraform 기본 문법", "services": ["Terraform HCL"], "collections": ["terraform_collection"]},
    (21, 3): {"topic": "State 관리", "services": ["Terraform State"], "collections": ["terraform_collection"]},
    (21, 4): {"topic": "모듈", "services": ["Terraform Modules"], "collections": ["terraform_collection"]},
    (21, 5): {"topic": "Workspace 및 환경 관리", "services": ["Terraform Workspace"], "collections": ["terraform_collection"]},
    
    # Week 22: Terraform 심화
    (22, 1): {"topic": "고급 기능", "services": ["Terraform Advanced"], "collections": ["terraform_collection"]},
    (22, 2): {"topic": "AWS 통합", "services": ["Terraform AWS"], "collections": ["terraform_collection", "aws_collection"]},
    (22, 3): {"topic": "모범 사례", "services": ["Terraform Best Practices"], "collections": ["terraform_collection"]},
    (22, 4): {"topic": "테스팅", "services": ["Terraform Testing"], "collections": ["terraform_collection"]},
    (22, 5): {"topic": "장단점 및 사용 케이스", "services": ["Terraform"], "collections": ["terraform_collection"]},
    
    # Week 23: Terraform 실전
    (23, 1): {"topic": "VPC 및 네트워킹", "services": ["Terraform VPC"], "collections": ["terraform_collection", "aws_collection"]},
    (23, 2): {"topic": "컴퓨팅 및 스토리지", "services": ["Terraform EC2"], "collections": ["terraform_collection", "aws_collection"]},
    (23, 3): {"topic": "데이터베이스 및 캐싱", "services": ["Terraform RDS"], "collections": ["terraform_collection", "aws_collection"]},
    (23, 4): {"topic": "컨테이너 및 서버리스", "services": ["Terraform EKS"], "collections": ["terraform_collection", "aws_collection"]},
    (23, 5): {"topic": "모듈화 프로젝트", "services": ["Terraform Modules"], "collections": ["terraform_collection"]},
    
    # Week 24: Terraform Import 및 FinOps
    (24, 1): {"topic": "Terraform Import 기초", "services": ["Terraform Import"], "collections": ["terraform_collection"]},
    (24, 2): {"topic": "Import 고급", "services": ["Terraform Import"], "collections": ["terraform_collection"]},
    (24, 3): {"topic": "FinOps 개념", "services": ["FinOps"], "collections": []},
    (24, 4): {"topic": "AWS 비용 최적화", "services": ["Cost Optimization"], "collections": ["aws_collection"]},
    (24, 5): {"topic": "FinOps 도구 및 자동화", "services": ["FinOps Tools"], "collections": []},
    
    # Week 25: 최종 프로젝트
    (25, 1): {"topic": "프로젝트 기획", "services": ["Final Project"], "collections": []},
    (25, 2): {"topic": "인프라 구축", "services": ["Terraform", "EKS"], "collections": ["terraform_collection", "aws_collection", "kubernetes_collection"]},
    (25, 3): {"topic": "애플리케이션 배포", "services": ["CI/CD", "ArgoCD"], "collections": ["argocd_collection"]},
    (25, 4): {"topic": "운영 및 최적화", "services": ["Operations"], "collections": []},
    (25, 5): {"topic": "프로젝트 발표", "services": ["Final Project"], "collections": []},
    
    # Week 26: 취업 준비
    (26, 1): {"topic": "DevOps 취업 준비", "services": ["Career"], "collections": []},
    (26, 2): {"topic": "면접 대비 - Docker & Kubernetes", "services": ["Interview"], "collections": ["docker_collection", "kubernetes_collection"]},
    (26, 3): {"topic": "면접 대비 - AWS & Terraform", "services": ["Interview"], "collections": ["aws_collection", "terraform_collection"]},
    (26, 4): {"topic": "면접 대비 - CI/CD & DevOps", "services": ["Interview"], "collections": []},
    (26, 5): {"topic": "과정 수료", "services": ["Graduation"], "collections": []},
}


def get_curriculum_options():
    """커리큘럼 옵션 리스트 생성"""
    options = []
    for (week, day), info in sorted(CURRICULUM_MAP.items()):
        label = f"Week {week}, Day {day}: {info['topic']}"
        value = f"{week},{day}"
        options.append((label, value))
    return options


def parse_curriculum_selection(selection):
    """선택된 커리큘럼 파싱"""
    if not selection:
        return None, None, None
    
    week, day = map(int, selection.split(','))
    curriculum = CURRICULUM_MAP.get((week, day))
    
    if curriculum:
        return week, day, curriculum
    return None, None, None


class PipelineLogger:
    """파이프라인 로그를 수집하는 클래스"""
    def __init__(self):
        self.logs = []
        self.current_step = ""
        self.progress = 0
        
    def log(self, message, step="", progress=None):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.logs.append(log_entry)
        
        if step:
            self.current_step = step
        if progress is not None:
            self.progress = progress
            
        return "\n".join(self.logs)
    
    def clear(self):
        self.logs = []
        self.current_step = ""
        self.progress = 0


# 전역 로거
logger = PipelineLogger()


def generate_lecture_langgraph(
    curriculum_selection,
    max_retries,
    persona_selection,
    progress=gr.Progress()
):
    """LangGraph 워크플로우로 강의 생성"""
    logger.clear()
    
    try:
        # 커리큘럼 파싱
        week, day, curriculum = parse_curriculum_selection(curriculum_selection)
        
        if not curriculum:
            error_msg = "❌ 커리큘럼을 선택해주세요"
            logger.log(error_msg)
            return logger.log(""), "", "실패", {}
        
        topic = curriculum["topic"]
        services = curriculum["services"]
        collections = curriculum["collections"]
        
        # 페르소나 처리
        persona = None if persona_selection == "없음" else persona_selection
        
        # 시작 로그
        logger.log("="*80)
        logger.log(f"🚀 강의 생성 시작", step="초기화")
        logger.log(f"📚 Week {week}, Day {day}: {topic}")
        logger.log(f"🔧 Services: {', '.join(services)}")
        logger.log(f"📦 Collections: {', '.join(collections) if collections else 'None'}")
        logger.log(f"🔄 Max Retries: {max_retries}")
        if persona:
            logger.log(f"🎯 Persona: {persona}")
        logger.log("="*80)
        
        progress(0.1, desc="워크플로우 초기화 중...")
        
        # 워크플로우 생성
        workflow = create_lecture_workflow()
        logger.log("✓ LangGraph 워크플로우 생성 완료", step="워크플로우 생성")
        
        progress(0.2, desc="강의 생성 중...")
        logger.log("\n📚 강의 생성 시작...", step="강의 생성")
        
        # 강의 생성 (generate_lecture 메서드 사용)
        try:
            # generate_lecture 메서드를 사용하여 워크플로우 실행
            # 이 메서드는 내부적으로 워크플로우를 실행하고 검증까지 수행합니다
            saved_files = workflow.generate_lecture(
                week=week,
                day=day,
                topic=topic,
                services=services,
                collections=collections,
                output_dir="lectures",
                max_retries=max_retries,
                persona=persona
            )
            
            progress(0.8, desc="검증 중...")
            logger.log("\n🔍 강의 검증 완료", step="검증")
            
            # 검증 결과는 워크플로우 내부에서 이미 처리됨
            validation_result = None
            status = "성공"
            
            progress(1.0, desc="완료!")
            
            # 결과 요약
            logger.log("\n" + "="*80)
            logger.log("✅ 강의 생성 완료!", step="완료")
            logger.log(f"📂 생성된 파일: {len(saved_files)}개")
            logger.log("="*80)
            
            # 파일 목록
            file_list = "\n".join([f"- {name}: {path}" for name, path in saved_files.items()])
            
            # 검증 결과 JSON (워크플로우 내부에서 처리되므로 간단히 표시)
            validation_json = {
                "status": "completed",
                "files_generated": len(saved_files)
            }
            
            return (
                logger.log(""),
                file_list,
                status,
                validation_json
            )
            
        except Exception as e:
            logger.log(f"\n❌ 오류 발생: {str(e)}", step="오류")
            import traceback
            logger.log(f"\n{traceback.format_exc()}")
            return logger.log(""), "", "실패", {}
    
    except Exception as e:
        logger.log(f"❌ 초기화 오류: {str(e)}")
        return logger.log(""), "", "실패", {}


def generate_lecture_traditional(
    curriculum_selection,
    max_retries,
    progress=gr.Progress()
):
    """전통적인 재시도 루프로 강의 생성"""
    logger.clear()
    
    try:
        # 커리큘럼 파싱
        week, day, curriculum = parse_curriculum_selection(curriculum_selection)
        
        if not curriculum:
            error_msg = "❌ 커리큘럼을 선택해주세요"
            logger.log(error_msg)
            return logger.log(""), "", "실패", {}
        
        topic = curriculum["topic"]
        services = curriculum["services"]
        collections = curriculum["collections"]
        
        # 시작 로그
        logger.log("="*80)
        logger.log(f"📝 강의 생성 시작 (전통적 방식)", step="초기화")
        logger.log(f"📚 Week {week}, Day {day}: {topic}")
        logger.log(f"🔧 Services: {', '.join(services)}")
        logger.log(f"📦 Collections: {', '.join(collections) if collections else 'None'}")
        logger.log(f"🔄 Max Retries: {max_retries}")
        logger.log("="*80)
        
        progress(0.1, desc="생성기 초기화 중...")
        
        # 생성기 생성
        generator = LectureGenerator()
        logger.log("✓ 강의 생성기 초기화 완료", step="생성기 초기화")
        
        progress(0.3, desc="강의 생성 중...")
        logger.log("\n📚 강의 콘텐츠 생성 중...", step="콘텐츠 생성")
        
        # 강의 생성
        saved_files = generator.generate_daily_lecture(
            week=week,
            day=day,
            topic=topic,
            services=services,
            collections=collections,
            max_retries=max_retries
        )
        
        progress(1.0, desc="완료!")
        
        # 결과 요약
        logger.log("\n" + "="*80)
        logger.log("✅ 강의 생성 완료!", step="완료")
        logger.log(f"📂 생성된 파일: {len(saved_files)}개")
        logger.log("="*80)
        
        # 파일 목록
        file_list = "\n".join([f"- {name}: {path}" for name, path in saved_files.items()])
        
        return (
            logger.log(""),
            file_list,
            "성공",
            {}
        )
        
    except Exception as e:
        logger.log(f"\n❌ 오류 발생: {str(e)}", step="오류")
        import traceback
        logger.log(f"\n{traceback.format_exc()}")
        return logger.log(""), "", "실패", {}


def load_lecture_files(curriculum_selection):
    """생성된 강의 파일 로드"""
    if not curriculum_selection:
        return {}, "커리큘럼을 선택하세요"
    
    week, day, curriculum = parse_curriculum_selection(curriculum_selection)
    if not curriculum:
        return {}, "유효하지 않은 커리큘럼입니다"
    
    # 파일 경로
    lecture_dir = Path("lectures") / f"week{week}" / f"day{day}"
    
    if not lecture_dir.exists():
        return {}, f"강의 파일이 없습니다: {lecture_dir}"
    
    # 파일 읽기
    files = {}
    file_list = []
    
    for file_path in lecture_dir.glob("*.md"):
        try:
            content = file_path.read_text(encoding='utf-8')
            files[file_path.name] = content
            file_list.append(f"✓ {file_path.name} ({len(content)} chars)")
        except Exception as e:
            file_list.append(f"✗ {file_path.name} (오류: {e})")
    
    if not files:
        return {}, "강의 파일을 찾을 수 없습니다"
    
    summary = f"📂 {lecture_dir}\n\n" + "\n".join(file_list)
    return files, summary


def regenerate_section(
    curriculum_selection,
    section_name,
    custom_prompt,
    progress=gr.Progress()
):
    """특정 섹션 재생성"""
    logger.clear()
    
    try:
        # 커리큘럼 파싱
        week, day, curriculum = parse_curriculum_selection(curriculum_selection)
        
        if not curriculum:
            error_msg = "❌ 커리큘럼을 선택해주세요"
            logger.log(error_msg)
            return logger.log(""), "", "실패"
        
        topic = curriculum["topic"]
        services = curriculum["services"]
        collections = curriculum["collections"]
        
        # 시작 로그
        logger.log("="*80)
        logger.log(f"🔄 섹션 재생성 시작", step="초기화")
        logger.log(f"📚 Week {week}, Day {day}: {topic}")
        logger.log(f"📝 섹션: {section_name}")
        logger.log(f"💬 커스텀 프롬프트: {custom_prompt if custom_prompt else '없음'}")
        logger.log("="*80)
        
        progress(0.2, desc="생성기 초기화 중...")
        
        # 생성기 생성
        generator = LectureGenerator()
        logger.log("✓ 강의 생성기 초기화 완료", step="생성기 초기화")
        
        progress(0.4, desc=f"{section_name} 재생성 중...")
        logger.log(f"\n📝 {section_name} 재생성 중...", step="섹션 생성")
        
        # 섹션별 에이전트 매핑
        section_map = {
            "서비스 이해 (Service Understanding)": "service_understanding",
            "Deep Dive": "deep_dive",
            "실습 가이드 (Hands-on Lab)": "hands_on_lab",
            "퀴즈 (Quiz)": "quiz"
        }
        
        section_key = section_map.get(section_name)
        if not section_key:
            logger.log(f"❌ 알 수 없는 섹션: {section_name}")
            return logger.log(""), "", "실패"
        
        # RAG 컨텍스트 수집
        progress(0.5, desc="RAG 컨텍스트 수집 중...")
        logger.log("\n📚 RAG 컨텍스트 수집 중...", step="RAG")
        
        rag_context = ""
        if collections:
            for collection_name in collections:
                try:
                    results = generator.vectorstore.search(
                        query=f"{topic} {' '.join(services)}",
                        collection_name=collection_name,
                        n_results=5
                    )
                    if results:
                        rag_context += f"\n\n### {collection_name}\n"
                        for doc in results:
                            rag_context += f"\n{doc}\n"
                except Exception as e:
                    logger.log(f"⚠️ {collection_name} 검색 실패: {e}")
        
        # 커스텀 프롬프트 추가
        additional_instructions = ""
        if custom_prompt:
            additional_instructions = f"\n\n### 추가 요구사항\n{custom_prompt}"
        
        # 섹션 생성
        progress(0.7, desc=f"{section_name} 생성 중...")
        
        content = ""
        if section_key == "service_understanding":
            content = generator.service_understanding_agent.generate(
                topic=topic,
                services=services,
                rag_context=rag_context + additional_instructions
            )
        elif section_key == "deep_dive":
            content = generator.deep_dive_agent.generate(
                topic=topic,
                services=services,
                rag_context=rag_context + additional_instructions
            )
        elif section_key == "hands_on_lab":
            content = generator.hands_on_lab_agent.generate(
                topic=topic,
                services=services,
                rag_context=rag_context + additional_instructions
            )
        elif section_key == "quiz":
            content = generator.quiz_agent.generate(
                topic=topic,
                services=services,
                rag_context=rag_context + additional_instructions
            )
        
        # 파일 저장
        progress(0.9, desc="파일 저장 중...")
        logger.log(f"\n💾 파일 저장 중...", step="저장")
        
        output_dir = Path("lectures") / f"week{week}" / f"day{day}"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        file_name = f"{section_key}.md"
        file_path = output_dir / file_name
        file_path.write_text(content, encoding='utf-8')
        
        logger.log(f"✓ 저장 완료: {file_path}")
        
        progress(1.0, desc="완료!")
        
        # 결과 요약
        logger.log("\n" + "="*80)
        logger.log(f"✅ {section_name} 재생성 완료!", step="완료")
        logger.log(f"📂 파일: {file_path}")
        logger.log(f"📏 크기: {len(content)} characters")
        logger.log("="*80)
        
        return (
            logger.log(""),
            content,
            "성공"
        )
        
    except Exception as e:
        logger.log(f"\n❌ 오류 발생: {str(e)}", step="오류")
        import traceback
        logger.log(f"\n{traceback.format_exc()}")
        return logger.log(""), "", "실패"


def create_ui():
    """Gradio UI 생성"""
    
    with gr.Blocks(
        title="DevOps 강의 생성 파이프라인",
        theme=gr.themes.Soft()
    ) as demo:
        
        gr.Markdown("""
        # 🎓 DevOps 강의 생성 파이프라인
        
        LangGraph 기반 자동 강의 생성 시스템입니다.
        커리큘럼을 선택하고 생성 방식을 선택하여 강의를 생성하세요.
        """)
        
        # 탭 구성
        with gr.Tabs() as tabs:
            # 탭 1: 강의 생성
            with gr.Tab("🎓 강의 생성", id=0):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### ⚙️ 설정")
                        
                        # 커리큘럼 선택
                        curriculum_dropdown = gr.Dropdown(
                            choices=get_curriculum_options(),
                            label="📚 커리큘럼 선택",
                            info="생성할 강의를 선택하세요",
                            value=None
                        )
                        
                        # 선택된 커리큘럼 정보 표시
                        with gr.Group():
                            gr.Markdown("#### 📋 선택된 강의 정보")
                            curriculum_info = gr.Markdown("커리큘럼을 선택하세요")
                        
                        # 재시도 횟수
                        max_retries = gr.Slider(
                            minimum=0,
                            maximum=5,
                            value=2,
                            step=1,
                            label="🔄 최대 재시도 횟수",
                            info="검증 실패 시 재생성 횟수"
                        )
                        
                        # 페르소나 선택
                        default_persona_display = DEFAULT_PERSONA if DEFAULT_PERSONA else "없음"
                        persona_dropdown = gr.Dropdown(
                            choices=["없음"] + AVAILABLE_PERSONAS,
                            label=f"🎯 대상 페르소나 (기본값: {default_persona_display})",
                            info=f"강의 난이도를 평가할 대상 페르소나. .env 파일의 DEFAULT_PERSONA로 기본값 설정 가능",
                            value=default_persona_display
                        )
                        
                        gr.Markdown(f"""
                        **페르소나 평가**:
                        - 선택한 페르소나 수준에 맞게 내용 평가
                        - 너무 어렵거나 설명이 부족하면 자동 개선
                        - 개념 설명, 예시, 배경 지식 추가
                        - 현재 기본값: **{default_persona_display}** (.env 파일에서 변경 가능)
                        """)
                        
                        # 생성 방식 선택
                        gr.Markdown("#### 🚀 생성 방식")
                        
                        with gr.Row():
                            langgraph_btn = gr.Button(
                                "🔷 LangGraph 워크플로우",
                                variant="primary",
                                size="lg"
                            )
                            traditional_btn = gr.Button(
                                "📝 전통적 방식",
                                variant="secondary",
                                size="lg"
                            )
                        
                        gr.Markdown("""
                        **LangGraph 워크플로우** (권장):
                        - 상태 기반 워크플로우
                        - 자동 피드백 및 재생성
                        - 단계별 추적 가능
                        
                        **전통적 방식**:
                        - 단순 재시도 루프
                        - 빠른 실행
                        """)
                    
                    with gr.Column(scale=2):
                        gr.Markdown("### 📊 파이프라인 실행 로그")
                        
                        # 로그 출력
                        log_output = gr.Textbox(
                            label="실행 로그",
                            lines=20,
                            max_lines=30,
                            interactive=False
                        )
                        
                        # 상태 표시
                        with gr.Row():
                            status_output = gr.Textbox(
                                label="상태",
                                value="대기 중",
                                interactive=False,
                                scale=1
                            )
                            
                        # 검증 결과
                        with gr.Accordion("🔍 검증 결과", open=False):
                            validation_output = gr.JSON(
                                label="검증 상세 정보"
                            )
                        
                        # 생성된 파일 목록
                        with gr.Accordion("📂 생성된 파일", open=True):
                            files_output = gr.Textbox(
                                label="파일 목록",
                                lines=10,
                                interactive=False
                            )
            
            # 탭 2: 강의 파일 보기 및 재생성
            with gr.Tab("📖 강의 보기 & 재생성", id=1):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### 📚 강의 선택")
                        
                        # 커리큘럼 선택 (재사용)
                        curriculum_dropdown_view = gr.Dropdown(
                            choices=get_curriculum_options(),
                            label="📚 커리큘럼 선택",
                            info="보거나 재생성할 강의를 선택하세요",
                            value=None
                        )
                        
                        # 파일 로드 버튼
                        load_btn = gr.Button(
                            "📂 강의 파일 로드",
                            variant="primary",
                            size="lg"
                        )
                        
                        # 파일 목록
                        with gr.Group():
                            gr.Markdown("#### 📄 로드된 파일")
                            loaded_files_info = gr.Markdown("강의를 선택하고 로드 버튼을 클릭하세요")
                        
                        gr.Markdown("---")
                        
                        # 섹션 재생성
                        gr.Markdown("### 🔄 섹션 재생성")
                        
                        section_dropdown = gr.Dropdown(
                            choices=[
                                "서비스 이해 (Service Understanding)",
                                "Deep Dive",
                                "실습 가이드 (Hands-on Lab)",
                                "퀴즈 (Quiz)"
                            ],
                            label="📝 재생성할 섹션",
                            info="재생성할 섹션을 선택하세요",
                            value=None
                        )
                        
                        custom_prompt = gr.Textbox(
                            label="💬 추가 요구사항 (선택사항)",
                            placeholder="예: 더 자세한 설명 추가, 실습 단계를 10개로 늘려줘, 퀴즈를 더 어렵게 만들어줘",
                            lines=3,
                            info="섹션 재생성 시 추가로 반영할 내용을 입력하세요"
                        )
                        
                        regenerate_btn = gr.Button(
                            "🔄 섹션 재생성",
                            variant="secondary",
                            size="lg"
                        )
                    
                    with gr.Column(scale=2):
                        gr.Markdown("### 📄 강의 내용")
                        
                        # 파일 선택 탭
                        with gr.Tabs() as file_tabs:
                            file_content_service = gr.Textbox(
                                label="서비스 이해 (service_understanding.md)",
                                lines=25,
                                max_lines=40,
                                interactive=False
                            )
                            
                            file_content_deepdive = gr.Textbox(
                                label="Deep Dive (deep_dive.md)",
                                lines=25,
                                max_lines=40,
                                interactive=False
                            )
                            
                            file_content_handson = gr.Textbox(
                                label="실습 가이드 (handson_step*.md)",
                                lines=25,
                                max_lines=40,
                                interactive=False
                            )
                            
                            file_content_quiz = gr.Textbox(
                                label="퀴즈 (quiz.md)",
                                lines=25,
                                max_lines=40,
                                interactive=False
                            )
                        
                        # 재생성 로그
                        with gr.Accordion("🔄 재생성 로그", open=False):
                            regen_log_output = gr.Textbox(
                                label="재생성 로그",
                                lines=15,
                                interactive=False
                            )
                        
                        # 재생성 상태
                        with gr.Row():
                            regen_status_output = gr.Textbox(
                                label="재생성 상태",
                                value="대기 중",
                                interactive=False,
                                scale=1
                            )
        
        # 탭 1 이벤트 핸들러
        # 커리큘럼 선택 시 정보 업데이트
        def update_curriculum_info(selection):
            if not selection:
                return "커리큘럼을 선택하세요"
            
            week, day, curriculum = parse_curriculum_selection(selection)
            if curriculum:
                info = f"""
**Week {week}, Day {day}**

**주제**: {curriculum['topic']}

**서비스**: {', '.join(curriculum['services'])}

**컬렉션**: {', '.join(curriculum['collections']) if curriculum['collections'] else 'None'}
                """
                return info
            return "커리큘럼 정보를 불러올 수 없습니다"
        
        curriculum_dropdown.change(
            fn=update_curriculum_info,
            inputs=[curriculum_dropdown],
            outputs=[curriculum_info]
        )
        
        # LangGraph 버튼 클릭
        langgraph_btn.click(
            fn=generate_lecture_langgraph,
            inputs=[curriculum_dropdown, max_retries, persona_dropdown],
            outputs=[log_output, files_output, status_output, validation_output]
        )
        
        # 전통적 방식 버튼 클릭
        traditional_btn.click(
            fn=generate_lecture_traditional,
            inputs=[curriculum_dropdown, max_retries],
            outputs=[log_output, files_output, status_output, validation_output]
        )
        
        # 예제
        gr.Markdown("""
        ---
        ### 💡 사용 방법
        
        1. **커리큘럼 선택**: 드롭다운에서 생성할 강의를 선택합니다
        2. **재시도 횟수 설정**: 검증 실패 시 재생성할 횟수를 설정합니다 (권장: 2)
        3. **생성 방식 선택**: LangGraph 워크플로우 또는 전통적 방식을 선택합니다
        4. **실행**: 버튼을 클릭하여 강의 생성을 시작합니다
        5. **결과 확인**: 로그와 생성된 파일 목록을 확인합니다
        
        ### 📚 문서
        
        - [README.md](./README.md) - 프로젝트 개요
        - [LANGGRAPH_IMPLEMENTATION.md](./LANGGRAPH_IMPLEMENTATION.md) - LangGraph 구현 상세
        - [VALIDATION_IMPROVEMENTS.md](./VALIDATION_IMPROVEMENTS.md) - 검증 개선 사항
        """)
    
    return demo


if __name__ == "__main__":
    demo = create_ui()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )
