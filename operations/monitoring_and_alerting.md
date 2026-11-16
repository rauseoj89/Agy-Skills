---
name: monitoring-and-alerting
description: Configures system monitoring, health checks, uptime tracking, and alert thresholds. Supports Docker container monitoring, database health checks, and resource utilization dashboards. Use when asked to set up monitoring, configure alerts, check system health proactively, or create health check scripts.
version: 1.0.0
tags: [universal, operations, monitoring, alerting, healthchecks, observability]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Systems Observer & Alert Configurator

## 🎯 Objective

Design and configure proactive observability, health check scripts, container/database monitors, and alert thresholds so resource exhaustion or service degradation triggers immediate notifications.

## 🕒 When to Use

- When configuring health check scripts, cron monitors, or uptime webhook alerts.
- When setting thresholds for CPU, memory, disk usage, or storage pool health.
- When auditing database connection pool utilization or API endpoint latency.
- When checking Docker container runtime health and logs.

## 🛡️ Universal Principles

1. **Native Tooling First:** Use POSIX (`top`, `df -h`) or PowerShell (`Get-Process`, `Get-PSDrive`) for host stats, Docker CLI (`docker ps`, `docker stats`, `docker logs`) for containers, and `postgres-mcp` (`execute_query`) for database connection pool metrics.
2. **Standard Alert Thresholds:** Trigger high-priority alerts when CPU $\ge 80\%$ (>5 min), Memory $\ge 90\%$, free disk $\le 15\%$ (critical $\le 10\%$), or storage pool status is not `ONLINE`.
3. **No Hardcoded Targets or Secrets:** Load endpoint URLs, webhook URLs, and credentials exclusively from environment variables (`${HEALTH_CHECK_TARGET}`, `${ALERT_WEBHOOK_URL}`).
4. **Non-Destructive Diagnostics:** Monitoring checks must be read-only and time-bounded (`--max-time 5`) so probes never exhaust connections or alter state.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Check host disk/containers and run parameterized health probe
df -h
docker ps --format "table {{.Names}}\t{{.Status}}"
curl -o /dev/null -s -w "%{http_code}\n" --max-time 5 "${HEALTH_CHECK_TARGET:-http://localhost:8080/health}"
```

### ▶️ If you are on Claude Code:

```bash
# Inspect container resource utilization without streaming
docker stats --no-stream
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Run read-only container and disk checks
await shell.exec("df -h && docker stats --no-stream");
```

### ⚠️ If you do NOT have tools:

1. Ask the user for their target service stack (host OS, Docker, PostgreSQL, HTTP endpoints).
2. Generate parameterized Bash/PowerShell health check scripts and `pg_stat_activity` queries using `${ENV_VAR}` placeholders.
3. Specify exact cron/scheduler intervals and alert threshold rules.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Host & container stats | `df -h`, `docker ps`, `docker stats --no-stream` | Provide read-only diagnostic commands for user |
| DB pool monitoring | `postgres-mcp` `execute_query` | Provide `pg_stat_activity` SQL query |
| Health check script | Write script with `${ENV_VAR}` targets | Output parameterized script in chat |

────────────────────────────────────

## ✅ Verification

- [ ] **No Hardcoded Secrets or IPs:** Confirmed webhook URLs, tokens, and target hosts use `${ENV_VAR}` placeholders with zero plaintext credentials.
- [ ] **Read-Only & Bounded Probes:** Health checks use timeouts (`--max-time 5`) and read-only queries.
- [ ] **Threshold Coverage:** CPU ($\ge 80\%$), Memory ($\ge 90\%$), Disk ($\le 15\%$), and pool/endpoint health thresholds are explicitly defined.
- [ ] **Alert Delivery Tested:** Verified alert trigger logic handles non-200 responses and threshold breaches cleanly.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
