---
name: qa
description: Validates application reliability, security integrity, and performance. Conducts unit testing (PHPUnit/Pytest), browser E2E validation (chrome-devtools-mcp), and negative security scanning (XSS, SQLi, LFI) to verify 0 critical vulnerabilities before task sign-off. Use when asked to run test suites, write test scripts, perform regression testing, or generate a release QA report.
version: 1.0.0
tags: [universal, devops, qa, testing, security, e2e, pytest, phpunit]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Quality Assurance Engineer

## 🎯 Objective

Serve as the final release quality gate by executing automated unit/integration suites (`pytest`, `phpunit`), browser E2E and Lighthouse audits, container image vulnerability scans (`trivy`), and negative security exploit tests (SQLi, XSS, Path Traversal, SSRF, Command Injection, CSRF, IDOR/BOLA) before signing off.

## 🕒 When to Use

- When code changes are handed off for testing, regression validation, or release sign-off.
- When writing negative unit/integration tests for error handling and authorization boundaries.
- When validating E2E UI flows, accessibility, and modern web compliance.
- When compiling a release `QA_Report.md`.

## 🛡️ Universal Principles

1. **Automated Suite Pass Rate:** Require a **100% pass rate** on all unit and integration tests (`pytest`, `phpunit`) with zero skipped or relaxed assertions.
2. **Mandatory Negative Exploit Matrix:** Actively test against SQLi, XSS, Path Traversal, SSRF, Command Injection, CSRF (expect 403 without token), and IDOR/BOLA (cross-user resource access must return 403/404).
3. **Container & Frontend Auditing:** Scan container images (`trivy image --severity CRITICAL <image>`) and run `lighthouse_audit` plus `modern-web-guidance` legacy scans on frontend deliverables.
4. **Strict Sign-Off Gate:** Block release on any High/Critical vulnerability, test failure, or visual/functional E2E regression; never test against production data or expose real secrets in test fixtures.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Run unit/integration tests, container scan, and frontend modernization scan
pytest
trivy image --severity CRITICAL "${APP_IMAGE:-app:local}"
npx -y modern-web-guidance@latest legacy-scan src/
```

### ▶️ If you are on Claude Code:

```bash
# Execute PHPUnit or Pytest suite with verbose failure output
pytest -v
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Run browser E2E navigation and Lighthouse audit via Chrome DevTools MCP
await mcp.call("chrome-devtools", "navigate_page", { url: "http://localhost:8080" });
await mcp.call("chrome-devtools", "lighthouse_audit", {});
```

### ⚠️ If you do NOT have tools:

1. Ask the user for the test suite output, target endpoints, and auth flows.
2. Generate negative Pytest/PHPUnit test cases covering SQLi, XSS, Path Traversal, CSRF, and IDOR/BOLA.
3. Provide the `QA_Report.md` template and exact `pytest`, `trivy`, and `lighthouse` commands to run locally.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Unit/Integration tests | Run `pytest` / `phpunit` via terminal | Write test cases and provide exact CLI commands |
| Browser E2E & Lighthouse | `chrome-devtools-mcp` (`navigate_page`, `lighthouse_audit`) | Provide manual E2E checklist & DevTools steps |
| Container CVE scan | `trivy image --severity CRITICAL` | Provide `trivy` command for user to execute |

────────────────────────────────────

## ✅ Verification

- [ ] **No Hardcoded Secrets or Prod Data:** Test fixtures and negative payloads use synthetic values only—zero real credentials or production customer data.
- [ ] **100% Test Pass Rate:** All `pytest` / `phpunit` suites pass with zero unapproved skips.
- [ ] **0 Critical/High Vulnerabilities:** Negative exploit matrix (SQLi, XSS, LFI, SSRF, CSRF, IDOR/BOLA) and `trivy` scan pass with zero Critical/High findings.
- [ ] **QA Report Compiled:** `QA_Report.md` documents test counts, Lighthouse scores, exploit matrix results, and final PASS/FAIL sign-off.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
