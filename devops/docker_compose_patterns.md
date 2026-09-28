---
name: docker-compose-patterns
description: Patterns for robust, maintainable Docker Compose configurations. Use when wiring multi-container stacks, configuring health checks, dependencies with service readiness, network topologies, volume persistence, and development overrides.
version: 1.0.0
tags: [universal, devops, docker, compose-v2, healthchecks, networking, orchestration]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker Compose Patterns

## 🎯 Objective

Design, configure, and maintain production-grade multi-container environments using modern Compose v2 standards (`compose.yaml`), strict readiness dependency chaining (`condition: service_healthy`), isolated bridge networks, and distroless healthcheck sidecars.

## 🕒 When to Use

- When creating or refactoring multi-container architectures in Docker Compose.
- When resolving startup race conditions between applications and databases.
- When configuring native healthchecks for PostgreSQL, Redis, MySQL, or microservices.
- When implementing environment override patterns for development (`compose.override.yaml`) vs production.
- When structuring private internal networks versus publicly exposed ingress networks.

## 🛡️ Universal Principles

1. **Canonical Compose v2:** The primary compose file must always be named `compose.yaml` (not legacy `docker-compose.yml`). Do not include a root `version:` tag.
2. **Readiness Dependency Chaining:** Never use plain `depends_on: [db]` (which only waits for the container to start, not accept connections). Always specify `condition: service_healthy`.
3. **Native Healthchecks:** Every dependent service must define an explicit healthcheck:
   - PostgreSQL: `test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]`
   - Redis: `test: ["CMD", "redis-cli", "ping"]`
   - MySQL: `test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]`
4. **Sidecar Pattern for Distroless:** For containers without curl or a shell, attach a sidecar container with `network_mode: "service:<target>"` to perform HTTP health probes against localhost.
5. **Network Isolation:** Separate frontend networks (externally accessible) from backend/data networks (private, no host port bindings in production).
6. **Zero Plaintext Secrets:** Use environment variable interpolation or Compose `secrets:` directive instead of hardcoding passwords.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Validate syntax and rendered configuration
docker compose config
# Launch stack in background and await healthy state
docker compose up -d --wait
```

### ▶️ If you are on Hermes Agent:

```python
# Inspect status of orchestrated services
result = terminal(command="docker compose ps --format json", timeout=60)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Execute orchestration validation
const result = await shell.exec("docker compose config --quiet");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Ask the user to verify stack health:
# "Run 'docker compose ps' and verify that all services display '(healthy)' status."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Design the `compose.yaml` template with `condition: service_healthy` dependencies.
2. Provide a `.env.example` file with required variable definitions.
3. Generate the command `docker compose up -d` and ask the user to confirm services reach healthy status.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Validate syntax | `docker compose config` | Static linting of YAML indentation and keys |
| Monitor startup | `docker compose ps` | Ask user for `docker compose ps` output |
| View aggregated logs | `docker compose logs -f` | Ask user to filter logs per service |

---

## ✅ Verification

- File is named `compose.yaml`.
- All database and backend services define a functional `healthcheck`.
- Dependent web applications declare `depends_on` with `condition: service_healthy`.
- Internal database ports are not mapped to host interfaces in production environments.
- No plaintext credentials exist in the compose manifest.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
