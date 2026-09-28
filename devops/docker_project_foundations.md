---
name: docker-project-foundations
description: Guidance for initializing, structuring, and containerizing a project from scratch. Use when creating initial .dockerignore, Dockerfile, and compose.yaml assets for local development without polluting the host toolchain.
version: 1.0.0
tags: [universal, devops, docker, scaffolding, foundations, compose-v2]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker Project Foundations

## 🎯 Objective

Scaffold complete, production-aligned containerization for any project from zero, delivering the foundational triad (`.dockerignore`, `Dockerfile`, `compose.yaml`) with zero host toolchain pollution and strict credential isolation.

## 🕒 When to Use

- When Dockerizing or initializing container infrastructure for a new or existing project.
- When a repository lacks Docker assets or uses obsolete `docker-compose.yml` v1 configurations.
- When adding local services (Postgres, Redis, RabbitMQ) for development without installing binaries on the host system.

## 🛡️ Universal Principles

1. **The Foundational Triad:** Every containerization workflow must provide the three essential artifacts:
   - `.dockerignore`: Prevents polluting the build context with local dependencies, binaries, or secrets.
   - `Dockerfile`: Multi-stage build, BuildKit optimization, non-root user.
   - `compose.yaml`: Service orchestration with readiness healthchecks and dedicated networks.
2. **Zero Host Toolchain Pollution:** Design workflows so compilation, migrations, and execution occur inside containers, without requiring global host installations (`npm -g`, `pip install`, `brew`).
3. **Strict Credential Isolation:** Ensure `.env` and certificates are never indexed by build contexts or tracked in git. Always provide a sanitized `.env.example`.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Validate build context and launch initial orchestration
docker compose up -d --build
```

### ▶️ If you are on Hermes Agent:

```python
# Initialize configuration files and verify startup
result = terminal(command="docker compose up -d", timeout=120)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Write the 3 triad files and verify syntax with shell
await shell.exec("docker compose config");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Generate files and request the developer to run:
# "Execute 'docker compose up -d --build' to initialize your development environment."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Detect primary tech stack (Node.js, Go, Python, PHP, Rust) by inspecting manifest files.
2. Draft the complete triad (`.dockerignore`, `Dockerfile`, `compose.yaml`) and the `.env.example` file.
3. Provide the user with step-by-step initialization and verification instructions.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Create triad | File writing tools | Generate Markdown code blocks to copy/paste |
| Validate stack | `docker compose up -d` / `docker compose ps` | Ask user for startup log confirmation |
| Verify ignore rules | `docker build` (monitor transferred bytes) | Manual review of `.dockerignore` patterns |

---

## ✅ Verification

- All 3 files generated: `.dockerignore`, `Dockerfile`, `compose.yaml`.
- `.dockerignore` explicitly excludes `.git`, `.env*`, dependency directories, and build artifacts.
- `compose.yaml` defines dependencies ordered by health checks (`condition: service_healthy`).
- The stack starts cleanly without requiring software installed directly on the developer host.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
