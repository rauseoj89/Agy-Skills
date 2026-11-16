---
name: researching-topics
description: Performs targeted web research, evaluates alternative tools, and compiles comparative audits. Use when asked to research technologies, evaluate solutions, summarize documentations, or search for best practices.
version: 1.0.0
tags: [universal, operations, research, evaluation, comparison, documentation]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Research & Competitive Analyst

## 🎯 Objective

Gather verified, Tier-1 technical documentation, evaluate competing tools or architectures objectively, detect marketing bias, and deliver structured comparison matrices and executive summaries vetted against security standards.

## 🕒 When to Use

- When researching a technology, database, framework, or cloud service.
- When evaluating and comparing alternative tools or architectures.
- When summarizing official documentation, RFCs, or technical whitepapers.
- When investigating best practices or security advisories.

## 🛡️ Universal Principles

1. **Data Credibility Hierarchy:** Prioritize **Tier 1** (official specs and first-party docs) and **Tier 2** (vetted whitepapers, CVE advisories, maintainer blogs) over **Tier 3** (community threads) and **Tier 4** (vendor marketing).
2. **Precise Query Formulation:** Use vendor-agnostic technical terms and `site:` filters against official docs, running multiple queries for limits, edge cases, and CVEs.
3. **Source Verification & Security Scrutiny:** Check publication/update dates (prefer last 2–3 years), author credentials, and crosscheck recommendations against `sec-engineer` mandates so insecure patterns are flagged.
4. **Sanitized Reports:** Never embed environment-specific secrets, private IPs, or local absolute paths in research summaries.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```text
# Use search_web with Tier-1 official domains first
search_web(query="PostgreSQL jsonb gin index performance", domain="postgresql.org")
```

### ▶️ If you are on Claude Code:

```text
# Run targeted web searches focusing on official documentation and CVE advisories
WebSearch(query="OpenAPI 3.1 specification changes site:spec.openapis.org")
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Fetch and summarize official documentation via browser/search MCP
await mcp.call("search", "query", { q: "site:developer.mozilla.org popover api" });
```

### ⚠️ If you do NOT have tools:

1. Ask the user to paste the relevant documentation excerpts or URLs they want compared.
2. Evaluate options objectively by use case, performance, security posture, operational complexity, and maintenance health.
3. Output the Product & Tool Comparison Matrix and Executive Summary with explicit `[Verify source date]` markers where live search wasn't available.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Live doc lookup | `search_web()` / web search tool | Ask user for doc excerpts; clearly mark unverified claims |
| Comparison report | Build Markdown Comparison Matrix | Output structured matrix & pros/cons in chat |
| Security vetting | Cross-check CVEs and `sec-engineer` rules | Flag potential security/ops risks for user verification |

────────────────────────────────────

## ✅ Verification

- [ ] **No Secrets, IPs, or Local Paths:** Research output contains zero credentials, private IPs, or local system paths.
- [ ] **Source Tiering & Recency:** Every key claim cites its source URL/reference and credibility tier (Tier 1–4) with publication recency checked.
- [ ] **Bias & Risk Disclosure:** Marketing claims are separated from verified benchmarks, and known limitations/deprecations are listed.
- [ ] **Security Alignment:** Recommended solutions comply with least-privilege, parameterization, and secret-isolation standards.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
