---
name: docker-destructive-guardrails
description: Safety guardrails and policies for destructive or irreversible Docker operations. Use before running or recommending commands that delete, prune, wipe, or reset containers, volumes, builder cache, or system images.
version: 1.0.0
tags: [universal, devops, docker, safety, risk-management, guardrails]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker Destructive Guardrails

## 🎯 Objective

Prevent accidental data loss, unexpected downtime, and destructive actions when managing Docker environments by enforcing a strict 3-tier risk classification and explicit user confirmation gates.

## 🕒 When to Use

- Before executing or recommending `docker rm`, `docker rm -f`, `docker compose down -v`, `docker volume prune`, `docker builder prune`, or `docker system prune`.
- When the user or a script requests to "clear space", "reset environment", "start from scratch", or "wipe cache".
- To identify non-destructive cleanup alternatives before resorting to volume or build cache deletion.

## 🛡️ Universal Principles

1. **Mandatory Confirmation Gate:** Never execute destructive operations automatically or by reflex. For Tier 3 operations, pause and request explicit user confirmation detailing the specific resources to be deleted.
2. **Present Non-Destructive Alternatives:** Always propose the lowest-impact alternative before executing mass deletion commands.
3. **Volume Protection:** Treat Docker volumes as production databases. Volume deletion is irreversible.
4. **Targeted Pruning:** Prefer targeted removal of specific orphaned containers or dangling `<none>` layers over broad global prunes with the `-a` flag.

---

## 🚦 3-Level Risk Classification

| Tier | Risk Level | Typical Commands | Action Policy |
| :--- | :--- | :--- | :--- |
| **Tier 1** | Low | `docker stop`, `docker rm <test-container>` | Proceed after confirming the container is ephemeral. |
| **Tier 2** | Medium | `docker compose down` (without `-v`), `docker image prune` (without `-a`), `docker network prune` | Inform which containers or networks will stop; verify no persistent state is at risk. |
| **Tier 3** | High / Critical | `docker compose down -v`, `docker volume rm`, `docker volume prune`, `docker system prune -a`, `docker builder prune -a` | **HALT:** List exact volumes, containers, and caches to be destroyed. Require explicit confirmation from the user. |

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Diagnose disk usage before proposing prunes
docker system df
# List volumes to identify specific dangling volumes
docker volume ls -qf dangling=true
```

### ▶️ If you are on Hermes Agent:

```python
# Inspect volumes before proposing destructive actions
result = terminal(command="docker volume ls", timeout=30)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Request confirmation from the user before executing shell commands with Tier 3 operations
// "The following volumes will be permanently deleted: [list]. Do you confirm to proceed?"
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Provide scoped, safe commands explaining the impact:
# "To free up disk space without deleting persistent data, run 'docker image prune' instead of 'system prune -a'."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Formulate a phased cleanup plan (identify dangling images first, then stopped containers).
2. Ask the user to run `docker system df` and report consumed disk space.
3. Generate the most restrictive command possible to mitigate data loss risks.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Inspect disk usage | `docker system df` via terminal | Ask user for `docker system df` output |
| Verify volumes | `docker volume ls` | Ask user to visually confirm existing volumes |
| Low-risk cleanup | `docker image prune` | Instruct user to execute targeted command |

---

## ✅ Verification

- Command risk was evaluated against the Tier 1, 2, or 3 matrix.
- A non-destructive alternative was presented before proceeding.
- For Tier 3 commands, exact volumes or caches to be destroyed were detailed and explicit user approval was obtained.
- The Docker host remains stable and operational post-cleanup.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
