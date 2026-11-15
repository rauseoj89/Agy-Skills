---
name: security-audit
description: Autonomous coverage-led vulnerability hunting harness. Use for comprehensive security audits, code reviews, penetration tests, or vulnerability research across APIs, microservices, daemons, and client applications.
version: 1.2.0
tags: [universal, security, audit, penetration-testing, vulnerability-hunting, adversarial-verification, idor, bola]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-11-15
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Autonomous Security Audit Harness

## 🎯 Objective

Conduct systematic, coverage-led vulnerability discovery and penetration auditing across codebases, APIs, and microservices using Cloudflare's 6-phase audit harness: reconnaissance, coverage ledger mapping, isolated hunting, adversarial disproof verification, schema validation with `security-scanner-mcp`, and multi-document reporting.

## 🕒 When to Use

- When conducting full security audits or penetration tests across a repository or service.
- When evaluating AI/LLM applications against direct/indirect prompt injection or tool hijacking.
- When reviewing APIs, middlewares, and authentication layers against OWASP Top 10, SSRF, IDOR, and race conditions.
- When generating formal audit artifacts (`architecture.md`, `coverage-ledger.json`, `findings.json`, `REPORT.md`).

## 🛡️ Universal Principles

1. **Coverage-Led Hunting:** Audit every endpoint, controller, and background worker mapped in the coverage ledger (`coverage-ledger.json`). No component remains uninspected.
2. **Adversarial Disproof Verification:** For every vulnerability candidate, assume an adversarial role seeking to disprove or debunk the finding (checking for sanitizers, middlewares, or type invariants). Only findings validated with an end-to-end untrusted taint trace reaching a sink are reported.
3. **Citation & Line Verification:** Every finding must cite exact files and line numbers with reproducible code snippets.
4. **Structured Schema Validation:** Findings must conform to a structured schema (ID, CVSS severity, CWE, impact, proof-of-concept, and remediation guidance).
5. **No Blind Hallucinations:** Never claim a vulnerability without verifiable evidence in the source code.

---

## 🔄 The 6-Phase Audit Lifecycle

1. **Phase 1 — Reconnaissance & Mapping:** Identify trust boundaries, sensitive data flows, and compile `coverage-ledger.json`.
2. **Phase 2 — Coverage-Led Hunting:** Evaluate each unit against OWASP vectors, **API Object-Level Authorization (OWASP API1 - IDOR / BOLA)** (inspecting every route, download endpoint, and mutation for server-derived `owner_id`/`tenant_id` query scoping and `403`/`404` enumeration rate-limiting), injections (SQL/Command/SSRF), business logic flaws, and AI risks.
3. **Phase 3 — Adversarial Disproof:** Attempt to refute the exploitability of the candidate finding. Trace untrusted taint flow to sink.
4. **Phase 4 — Structured Schema Output:** Generate `findings.json` with severity, CWE, and attack vector metadata. Validate using `security_scanner.validate_audit_findings`.
5. **Phase 5 — Citation Verification:** Re-check that all cited lines and files exist and match current codebase state.
6. **Phase 6 — Multi-Document Reporting:** Publish executive summary `REPORT.md` with prioritized mitigation roadmap.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Execute findings schema validation via security-scanner-mcp:
# validate_audit_findings(findings_path="findings.json", ledger_path="coverage-ledger.json")
# scan_dependency_vulnerabilities(manifest_path="package.json", ecosystem="npm")
```

### ▶️ If you are on Hermes Agent:

```python
# Map repository files for coverage ledger
import os, json
routes = [f for f in os.listdir(".") if f.endswith(".go") or f.endswith(".ts")]
print(f"Coverage candidates: {len(routes)}")
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Validate findings schema and check dependency vulnerabilities
await security_scanner.validate_audit_findings({
  findings_path: "findings.json",
  ledger_path: "coverage-ledger.json"
});
await security_scanner.scan_dependency_vulnerabilities({
  manifest_path: "package.json",
  ecosystem: "npm"
});
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide audit through phased workflow:
# "Review 'src/api/auth.ts' and verify whether password reset tokens enforce expiration checks."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Request route definitions, authentication modules, and core controllers from the user.
2. Perform visual dataflow analysis and taint tracking in chat.
3. Deliver the audit report with severity ratings (Critical, High, Medium, Low) and patch-ready mitigation code.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Map attack surface | `find` / `grep` / directory listing | Ask user for file tree and primary route files |
| Schema validation | `security_scanner.validate_audit_findings()` | Manual inspection of keys in `findings.json` |
| CVE scanning | `security_scanner.scan_dependency_vulnerabilities()` | Ask user to run `npm audit` / `pip-audit` |
| Code verification | `view_file` / offset-based reading | Ask user for exact code snippet around sink |

---

## ✅ Verification

- Attack surface mapping in `coverage-ledger.json` is complete.
- Every finding in `findings.json` has a verified proof-of-concept or confirmed taint trace.
- Zero false positives survived the adversarial disproof phase.
- Published `REPORT.md` contains reproducible remediation steps.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-15  
Version: 1.2.0
