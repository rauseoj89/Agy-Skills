---
name: docker-build-strategies
description: Strategies for efficient, secure, and optimized Docker image builds. Use when writing, reviewing, or optimizing Dockerfiles, handling multi-stage builds, BuildKit cache mounts, secret mounts, .dockerignore hygiene, and distroless runtimes.
version: 1.0.0
tags: [universal, devops, docker, buildkit, multi-stage, caching, security]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker Build Strategies

## 🎯 Objective

Architect, optimize, and secure container image builds using modern BuildKit capabilities: multi-stage architectures, package manager cache mounts, build-time secret injection, `COPY --link` optimizations, and minimal non-root runtime environments.

## 🕒 When to Use

- When creating or refactoring `Dockerfile` files for any technology (Node, Python, Go, Java, Rust).
- When optimizing build speed, image size, or resolving cache invalidation bottlenecks.
- When needing to inject private credentials (npm tokens, SSH keys) securely without persisting them in layers.
- When debugging bloated layers or writing strict `.dockerignore` files.

## 🛡️ Universal Principles

1. **BuildKit First:** Always declare `# syntax=docker/dockerfile:1` as the very first line.
2. **Secrets Hygiene:** Never use `ARG` or `ENV` for passwords, tokens, or SSH keys (these leak into layer history and metadata). Use `--mount=type=secret,id=...` or `--mount=type=ssh`.
3. **Multi-Stage & Minimal Runtime:** Separate the build stage (`FROM ... AS build`) from the runtime stage (`FROM ... AS runtime`). Use distroless (`gcr.io/distroless/static-debian12:nonroot`) or Alpine/Slim base images.
4. **Cache Optimization:** Order instructions from least to most frequently changing. Use cache mounts (`--mount=type=cache,target=...`) for package managers (Go, npm, pip, maven).
5. **Decoupled Layers:** Use `COPY --link` to decouple independent file layers and maximize cache reuse.
6. **Non-Root Execution:** Always enforce `USER nonroot` or an unprivileged UID before `ENTRYPOINT`/`CMD`.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Execute build with BuildKit enabled
DOCKER_BUILDKIT=1 docker build --secret id=npmrc,src=.npmrc -t myapp:latest .
```

### ▶️ If you are on Hermes Agent:

```python
# Execute build via terminal
result = terminal(command="DOCKER_BUILDKIT=1 docker buildx build --tag myapp:latest .", timeout=300)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use terminal or integrated shell command
const result = await shell.exec("docker buildx build -t app:latest .");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Ask the user to run the build with BuildKit:
# "Execute 'DOCKER_BUILDKIT=1 docker build -t my-app .' to validate syntax and caching."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Design the optimized `Dockerfile` following multi-stage patterns and cache mounts.
2. Design an exhaustive `.dockerignore` file blocking `.git`, `.env*`, `node_modules`, `tests/`.
3. Provide the exact build instructions to the user with BuildKit flags.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Image build | `docker buildx build` via terminal/MCP | Generate command with flags and ask user to run |
| Inspect layers | `docker history` / `docker_inspect()` | Ask for `docker history <image>` output |
| Size diagnostics | `docker images --format` | Request image size report from user |

---

## ✅ Verification

- The first line is `# syntax=docker/dockerfile:1`.
- A `.dockerignore` file exists and prevents leakage of secrets and development files.
- The final user in the production image is explicitly non-root.
- No secrets or tokens are stored in `ARG` or `ENV` variables.
- Subsequent builds successfully leverage cache mounts.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
