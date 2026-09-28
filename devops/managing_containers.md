---
name: managing-containers
description: Audits, deploys, and maintains Docker containers, Compose architectures, and image environments. Use when asked to configure Dockerfiles, compose services, parse container logs, verify port configurations, or manage local development virtualization.
version: 1.2.0
tags: [universal, devops, docker, kubernetes, containers, buildkit, compose-v2]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker & Kubernetes Container Specialist

## 🎯 Objective

Design, deploy, and maintain robust, high-performance containerized and orchestrated infrastructures, strictly adhering to modern Docker standards (BuildKit, Compose v2) and CIS Docker and Kubernetes Security Benchmarks.

## 🕒 When to Use

- When configuring or optimizing `Dockerfile` or `compose.yaml` files.
- When configuring Kubernetes manifests (Deployments, Services, NetworkPolicies).
- When inspecting active Docker/K8s processes, networks, or volumes.
- When analyzing container logs to diagnose crashes or startup errors.
- When validating resource limits, non-root policies, or destructive operation guardrails.

## 🛡️ Universal Principles

1. **Canonical Compose v2:** Always use `compose.yaml` (never legacy `docker-compose.yml`).
2. **BuildKit Standards:** Always declare `# syntax=docker/dockerfile:1`. Use package cache mounts (`--mount=type=cache`), secret mounts (`--mount=type=secret`), and `COPY --link`.
3. **Non-Root Runtime:** Force execution context using non-root users (`USER 10001` or `USER nonroot:nonroot` / `runAsNonRoot: true`).
4. **Readiness Dependencies:** Always pair `depends_on` with `condition: service_healthy` for databases and backend services.
5. **Distroless Sidecar Healthchecks:** For images without curl/shell, attach a sidecar container using `network_mode: "service:<target>"`.
6. **3-Tier Destructive Gate:** Never delete volumes or run `system prune` without explicit user confirmation and presenting scoped alternatives.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Inspect processes and logs with native docker CLI:
docker compose -f compose.yaml ps
docker logs --tail 100 <container-name>
```

### ▶️ If you are on Hermes Agent:

```python
# Use integrated terminal to inspect containers
result = terminal(command="docker compose ps", timeout=60)
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Use terminal to run docker commands
const result = await shell.exec("docker compose ps");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Ask user to run local diagnostic commands if terminal is unavailable:
# "Please run 'docker compose ps' and 'docker logs <container-name>'."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate valid `Dockerfile` and `compose.yaml` files.
2. Ask the user: "Save these files and run 'docker compose up -d'".
3. Request that the user run verification commands and report the logs back.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| View container status | Terminal: `docker compose ps` | Ask user to run `docker compose ps` |
| View container logs | Terminal: `docker logs <container>` | Ask user to run and paste `docker logs` |
| Container control | Terminal: `docker compose start/stop` | Generate appropriate command for user |
| Delete resources (Tier 3) | Request confirmation + `docker rm` | Warn about data loss and generate exact command |

---

## ✅ Verification

- Orchestration file is named `compose.yaml`.
- Container runs under an unprivileged user (`USER nonroot`).
- Root filesystem is read-only.
- Container logs show no critical exceptions and status is `healthy`.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.2.0
