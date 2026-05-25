---
name: "Managing Docker Containers"
description: "Deploys, monitors, and audits Docker containers and Compose configuration structures."
category: "generic/devops"
tools_required: ["data-analyst-mcp", "office-mcp"]
last_updated: 2026-05-24
---

# 🧠 Skill: Managing Docker Containers

## 🎯 Goal
Inspect, configure, and monitor containerized services to ensure optimal, least-privilege, and secure operation across environments.

## 📊 Inputs Required
- Target `Dockerfile` or `docker-compose.yml` to inspect.
- Container process status and logs (via docker daemon tools).

## 🛠️ Step-by-Step Instructions
1. **Container State Vetting**:
   - Check status, mapped ports, and volume bounds for all target compose services.
2. **Dockerfile Integrity Audit**:
   - Inspect build configurations. Enforce multi-stage patterns and confirm that no root execution credentials exist (`USER` directive is active).
3. **Log Diagnostic Parsing**:
   - Review live or archived container logs to isolate errors, tracebacks, or connection crashes.
4. **Configuration Hardening**:
   - Verify environment injections are managed via variable pools rather than hardcoded scripts.

## 🛡️ Verification & Security Checklist
1. **Privilege Audit**: Verify containers operate under isolated non-root user permissions.
2. **Network Security**: Ensure databases and cache layers are locked within private subnets.
3. **Data Scrub**: Redact absolute path names and database configurations.
4. **Log Retention**: Check size bounds and verify logs are clear of private user variables.

---
*Created by Efficiency Core*
