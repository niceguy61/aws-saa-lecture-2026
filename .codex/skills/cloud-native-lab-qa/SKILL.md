---
name: cloud-native-lab-qa
description: QA Cloud Native DevOps hands-on labs for Docker, Kubernetes, AWS cloud native services, security, networking, and observability. Use when checking whether a lab is runnable, safe, teachable, cost-aware, and includes verification, troubleshooting, and cleanup.
---

# Cloud Native Lab QA

Use this skill to check whether a lab is ready for classroom use.

## Checks

- Prerequisites are explicit.
- Commands are ordered and copyable.
- Expected output is shown or clearly described.
- Verification commands prove the intended state.
- Failure modes and troubleshooting steps are documented.
- Cleanup returns the environment to a safe state.
- Cloud steps include cost, region, credential, and deletion warnings.
- Kubernetes steps avoid destructive shared-cluster actions unless the lab explicitly uses a disposable cluster.

## Report Format

```md
## Lab QA Result

- Status: PASS / NEEDS FIX / BLOCKED
- Environment:
- Commands checked:
- Findings:
- Required fixes:
- Residual risk:
```

