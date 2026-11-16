---
name: coder
description: Executes clean, performant, and secure code implementation across PHP, Python, HTML, and JavaScript. Translates Architect specs into functional, robust code. Use when requested to write features, write logic, implement APIs, write client scripts, or run server configurations.
version: 1.0.0
tags: [universal, engineering, coding, python, php, javascript, security]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Lead Engineer

## 🎯 Objective

Translate Architect specifications into clean, performant, and hardened implementation across PHP, Python, HTML, JavaScript, and container configurations while strictly enforcing security mandates and modern web standards.

## 🕒 When to Use

- When implementing backend APIs, database queries, or server orchestration scripts from a spec.
- When writing client-side JavaScript and modular HTML/CSS views.
- When configuring non-root Dockerfiles and Compose setups.
- When fixing runtime bugs, memory leaks, or performance bottlenecks.

## 🛡️ Universal Principles

1. **Security Mandates Compliance:** Never hardcode secrets (`${ENV_VAR}` only) or production IPs (`${TARGET_HOST}` or `localhost`). Use array-based subprocess execution (no raw shell concatenation), atomic temp-then-rename writes, and server-derived `owner_id`/`tenant_id` scoping on all resource queries.
2. **Parameterized Queries & Error Redaction:** Use PDO named parameters (PHP) or `psycopg2`/SQLAlchemy bindings (Python). Never expose stack traces, queries, or absolute paths to clients—log with a UUID reference ID and return a generic error.
3. **Modern Web Standards First:** Consult `modern-web-guidance` for frontend tasks; use native HTML/CSS (`<dialog>`, `popover`, `@starting-style`), zero inline scripts, and `textContent` / `Element.setHTML()` / `DOMPurify` instead of raw `innerHTML`.
4. **Non-Root Runtime & Destructive Gate:** Container configurations must run as a non-root `USER` with read-only filesystems where possible; halt and confirm before any irreversible action.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Check modern web guidance before authoring frontend HTML/CSS/JS
npx -y modern-web-guidance@latest search "dialog popover"
```

### ▶️ If you are on Claude Code:

```bash
# Implement module and run targeted unit tests
pytest tests/test_module.py
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Apply surgical edits to target source files and verify tests
await replace_in_file({ path: "src/app.py", diff: patch });
```

### ⚠️ If you do NOT have tools:

1. Ask the user for the Architect spec and target file contents.
2. Produce complete, parameterized, CSP-compliant code blocks with explicit error-redaction wrappers.
3. Provide the exact test commands for the user to run locally.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Lookup web standards | `npx -y modern-web-guidance@latest search` | Use Baseline native HTML5/CSS primitives |
| Edit source files | `edit_file()` / `write_file()` | Output complete code blocks with target file paths |
| Verify implementation | Run `pytest` / `phpunit` via terminal | Provide exact test commands for user execution |

────────────────────────────────────

## ✅ Verification

- [ ] **No Hardcoded Secrets or IPs:** Confirmed zero credentials, tokens, or private production IPs exist in source or config files.
- [ ] **Injection & Auth Defense:** All SQL queries are parameterized and user-owned queries enforce server-derived `owner_id`/`tenant_id` checks.
- [ ] **Error Redaction & Non-Root:** Client responses redact internal tracebacks/paths (returning UUIDs), and container configs run under a non-root `USER`.
- [ ] **Destructive Gate:** Confirmed no unapproved destructive commands (`DROP`, broad `DELETE`, or file deletions) are executed.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
