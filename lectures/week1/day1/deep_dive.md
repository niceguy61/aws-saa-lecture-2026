# Deep Dive - 트러블슈팅

## 시나리오 1: GitLab CI/CD 파이프라인 실행 실패

### 시나리오 설명

GitLab CI/CD 파이프라인이 예상대로 실행되지 않고 오류 발생

### 원인 분석

파이프라인 트리거 조건이 잘못 설정되거나, .gitlab-ci.yml 파일에서 문법 오류 발생

### 원인 확인 방법

git log --oneline 확인하여 최신 커밋 히스토리 확인

curl -H 'Private-Token: <TOKEN>' 'https://gitlab.com/api/v4/projects/<PROJECT_ID>/pipeline' 명령어로 파이프라인 상태 확인

git diff .gitlab-ci.yml 파일의 최신 변경 사항 검토

aws logs get-log-events --log-group-name /aws/lambda/<FUNCTION_NAME> --log-stream-name <STREAM_NAME> 명령어로 Lambda 로그 확인

gitlab-runner diagnostics 명령어로 러너 상태 점검

### 수정 방법

yq eval '.' .gitlab-ci.yml 파일의 YAML 문법 검증

git push --set-upstream origin <BRANCH_NAME> 명령어로 변경 사항 반영

gitlab-ci.yml 파일에서 'only' 또는 'except' 키워드 재검토

aws ec2 describe-security-groups --group-ids <GROUP_ID> 명령어로 VPC 보안 그룹 설정 확인

gitlab-runner stop && gitlab-runner start 명령어로 러너 재시작

### 정상 확인 방법

curl -I https://gitlab.com/api/v4/projects/<PROJECT_ID>/pipelines/latest 명령어로 파이프라인 상태 확인

git status 명령어로 로컬 저장소 상태 검증

aws logs get-log-events --log-group-name /aws/lambda/<FUNCTION_NAME> --log-stream-name <STREAM_NAME> 로그 검토

gitlab-ci.yml 파일에서 'script' 섹션 실행 여부 확인

aws ec2 describe-instances --instance-ids <INSTANCE_ID> 명령어로 인스턴스 상태 점검

---

## 시나리오 2: Kubernetes 배포 실패

### 시나리오 설명

Kubernetes 클러스터에 배포 시 '500 Internal Server Error' 발생

### 원인 분석

Deployment YAML 파일에서 리소스 제한 설정 누락 또는 ConfigMap/Secrets 접근 권한 문제

### 원인 확인 방법

kubectl get deployments --all-namespaces 명령어로 배포 상태 확인

kubectl describe deployment <DEPLOYMENT_NAME> --namespace <NAMESPACE> 명령어로 상세 정보 검토

kubectl get configmap <CONFIGMAP_NAME> --namespace <NAMESPACE> 명령어로 ConfigMap 상태 점검

kubectl describe secret <SECRET_NAME> --namespace <NAMESPACE> 명령어로 Secret 정보 확인

kubectl logs <POD_NAME> --namespace <NAMESPACE> 명령어로 Pod 로그 분석

### 수정 방법

kubectl edit deployment <DEPLOYMENT_NAME> --namespace <NAMESPACE> 명령어로 리소스 제한 추가

kubectl apply -f <CONFIGMAP_YAML_FILE> 명령어로 ConfigMap 재등록

kubectl apply -f <SECRET_YAML_FILE> 명령어로 Secret 재등록

kubectl set env deployment/<DEPLOYMENT_NAME> <ENV_VAR_NAME>=<VALUE> 명령어로 환경 변수 설정

kubectl rollout restart deployment/<DEPLOYMENT_NAME> --namespace <NAMESPACE> 명령어로 재배포

### 정상 확인 방법

kubectl get pods --namespace <NAMESPACE> 명령어로 Pod 상태 확인

kubectl get services --namespace <NAMESPACE> 명령어로 서비스 엔드포인트 검토

curl -I <SERVICE_ENDPOINT> 명령어로 서비스 접근성 점검

kubectl logs <POD_NAME> --namespace <NAMESPACE> 로그 재확인

kubectl get events --namespace <NAMESPACE> 명령어로 이벤트 로그 분석

---

