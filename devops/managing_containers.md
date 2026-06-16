---
name: "Managing Docker Containers"
description: "Deploys, monitors, and audits Docker containers and Compose configuration structures."
category: "generic/devops"
tools_required: ["nas-tools"]
last_updated: 2026-06-02
---

# 🧠 Skill: Managing Docker Containers

## 🎯 Goal
Inspect, configure, deploy, and monitor containerized services to ensure optimal, least-privilege, and secure operation across environments, in alignment with container security directives.

## 📊 Inputs Required
- Target `Dockerfile` or `docker-compose.yml` to inspect.
- Container process status and logs (via docker daemon tools).
- Environment security configurations.

## 🛠️ Step-by-Step Instructions
1. **Container State & Privilege Vetting**:
   - Check status, mapped ports, and volume bounds for all target compose services.
   - Enforce non-root execution rules (`USER` directive is active in `Dockerfile` and `securityContext.runAsNonRoot: true` in Kubernetes specs).
2. **Secrets & Mount Hardening**:
   - Never inject credentials or private keys as container environment variables.
   - Force secrets injection exclusively through read-only volume mounts (`readOnly: true`).
3. **Image Vulnerability Scan**:
   - Scan container images using scanners like Trivy or Grype before deployment.
   - Block deployments if any **CRITICAL** severity CVEs are found.
4. **Log Diagnostic Parsing & Troubleshooting**:
   - Review live or archived container logs to isolate errors, tracebacks, or connection crashes.
5. **Destructive Container Gate**:
   - Halt execution and request explicit user confirmation before executing any destructive operations (e.g., `docker rm`, `docker-compose down -v`, volume deletion, namespace deletions).

## 🛡️ Verification & Security Checklist
1. **Privilege Audit**: Verify containers operate under isolated non-root user permissions and read-only root filesystems where applicable.
2. **Secrets Exposure**: Ensure no plaintext secrets are visible in `docker inspect` or pod environment definitions.
3. **Network Isolation**: Ensure databases and cache layers are locked within private networks with default-deny policies.
4. **Vulnerability Pass**: Verify image scanning has been completed and verified clean of blocking CVEs.

---
*Created by Efficiency Core*
