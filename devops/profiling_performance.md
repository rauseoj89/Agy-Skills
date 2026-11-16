---
name: profiling-performance
description: Conducts performance profiling, load testing, and bottleneck analysis for web applications, APIs, and databases. Use when asked to profile application performance, run load tests, optimize response times, or identify bottlenecks.
version: 1.0.0
tags: [universal, devops, performance, profiling, explain-analyze, cwv]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Performance & Profiling Specialist

## 🎯 Objective

Identify latency bottlenecks across databases, APIs, and frontend rendering using `EXPLAIN (ANALYZE, BUFFERS)`, browser performance traces, and Core Web Vitals optimization, verifying measurable improvements against baseline benchmarks.

## 🕒 When to Use

- When optimizing slow SQL queries or eliminating sequential scans.
- When tracing frontend rendering times, memory leaks, or Core Web Vitals (LCP, INP, CLS).
- When benchmarking API response latencies and establishing baselines.
- When auditing server resource metrics during load tests.

## 🛡️ Universal Principles

1. **Right Tool Per Layer:** Use `EXPLAIN (ANALYZE, BUFFERS)` for SQL queries, Chrome DevTools traces (`performance_start_trace` / `performance_stop_trace` / `lighthouse_audit`) for frontend rendering, and native OS counters (`top`, `vmstat`, `Get-Counter`) for host metrics.
2. **Benchmark Baselines:** Target $< 100\text{ ms}$ for DB queries ($< 10\text{ ms}$ for transactional SELECTs), $< 200\text{ ms}$ for API endpoints, and FCP $< 1.8\text{ s}$.
3. **Modern Web CWV Optimization:** Consult `modern-web-guidance` for LCP, INP, and CLS, preferring native browser primitives (`content-visibility: auto`, `fetchpriority="high"`, native lazy loading) over heavy JS wrappers.
4. **No Hardcoded Targets or Secrets:** Load benchmark URLs and DB connection strings from environment variables (`${TARGET_URL}`, `${DATABASE_URL}`).

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Check Core Web Vitals guidance before frontend optimization
npx -y modern-web-guidance@latest search "CWV LCP INP CLS"
```

### ▶️ If you are on Claude Code:

```bash
# Run EXPLAIN ANALYZE on a slow query (read-only SELECT)
psql "${DATABASE_URL}" -c "EXPLAIN (ANALYZE, BUFFERS) SELECT id, title FROM public.posts ORDER BY created_at DESC LIMIT 20;"
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Capture browser performance trace via Chrome DevTools MCP
await mcp.call("chrome-devtools", "performance_start_trace", { reload: true });
```

### ⚠️ If you do NOT have tools:

1. Ask the user for the slow SQL query, API endpoint latency, or Lighthouse/DevTools trace summary.
2. Provide the exact `EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS)` query and index recommendations.
3. Outline frontend CWV optimizations and a before/after Performance Optimization Log template.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| SQL profiling | `postgres-mcp` `execute_query` with `EXPLAIN` | Provide `EXPLAIN (ANALYZE, BUFFERS)` SQL for user |
| Frontend tracing | `chrome-devtools-mcp` trace & `lighthouse_audit` | Guide user to capture DevTools Performance trace |
| CWV best practices | `npx -y modern-web-guidance@latest search` | Recommend native `fetchpriority`, `content-visibility` |

────────────────────────────────────

## ✅ Verification

- [ ] **No Hardcoded Secrets or IPs:** Confirmed benchmark scripts and queries load targets/credentials from `${ENV_VAR}` placeholders.
- [ ] **Baseline & Post-Fix Comparison:** Recorded before/after metrics (DB query ms, API latency ms, Lighthouse/CWV scores).
- [ ] **Index & Query Safety:** Verified `EXPLAIN ANALYZE` on mutating statements is wrapped in a rolled-back transaction (`BEGIN; EXPLAIN ANALYZE ...; ROLLBACK;`) or run on `SELECT` only.
- [ ] **Modern Web Alignment:** Frontend optimizations use native browser primitives before adding JS dependencies.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
