---
name: docker-build-strategies
description: Strategies for efficient, secure, and optimized Docker image builds. Use when writing, reviewing, or optimizing Dockerfiles, handling multi-stage builds, BuildKit cache mounts, secret mounts, .dockerignore hygiene, and distroless runtimes.
version: 1.1.0
tags: [universal, devops, docker, buildkit, multi-stage, caching, security]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
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

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Use terminal or integrated shell command
const result = await shell.exec("docker buildx build -t app:latest .");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Provide optimized Dockerfile with BuildKit directives:
# "Review Dockerfile layer ordering and enforce package cache mounts."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate optimized, multi-stage `Dockerfile` and `.dockerignore`.
2. Instruct the user: "Build image using `DOCKER_BUILDKIT=1 docker build -t myapp .`".
3. Request build output logs to verify cache utilization.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Build container image | Terminal: `docker buildx build` | Provide command line for manual build |
| Inspect image history | Terminal: `docker history <image>` | Ask user to run `docker history` |
| Inspect image size | Terminal: `docker image ls` | Ask user to check image size |

---

## ✅ Verification

- First line contains `# syntax=docker/dockerfile:1`.
- Multi-stage architecture isolates build tools from runtime.
- No plaintext credentials exist in `ENV` or `ARG` declarations.
- Container executes as non-root user.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.1.0
