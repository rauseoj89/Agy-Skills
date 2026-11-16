---
name: managing-dependencies
description: Audits, pins, and secures project dependencies across npm, pip, and Composer. Detects vulnerabilities, enforces version pinning, and validates supply chain integrity. Use when asked to audit dependencies, update packages, check for vulnerabilities, or set up lockfile enforcement.
version: 1.0.0
tags: [universal, devops, dependencies, supply-chain, sri, cve]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Dependency & Supply Chain Manager

## 🎯 Objective

Audit external dependencies across npm, pip, and Composer, block packages with Critical or High CVEs, enforce exact version pinning and lockfile integrity, and validate Subresource Integrity (SRI) hashes for CDN assets.

## 🕒 When to Use

- When introducing new third-party libraries or packages to a project.
- When auditing existing codebases for known CVEs or outdated dependencies.
- When configuring lockfiles (`package-lock.json`, `poetry.lock`, `composer.lock`) for reproducible builds.
- When generating SRI hashes for external stylesheets or scripts.

## 🛡️ Universal Principles

1. **Block Vulnerable Packages:** Reject any dependency with **CRITICAL** or **HIGH** severity CVEs using `npm audit`, `pip-audit` (or `safety check`), and `composer audit`.
2. **Strict Version Pinning & Lockfiles:** Pin production dependencies to exact versions (no `^`, `~`, or `*` ranges) and commit lockfiles to prevent build drift.
3. **Subresource Integrity (SRI):** All external CDN `<script>` and `<link>` tags must include a verified `integrity` SHA-384 hash and `crossorigin="anonymous"`.
4. **No Secrets in Registry Configs:** Never store plaintext auth tokens in `.npmrc`, `pip.conf`, or `auth.json`; reference `${ENV_VAR}` placeholders only.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Run dependency audits and generate SHA-384 SRI hash
npm audit --audit-level=high
openssl dgst -sha384 -binary script.js | openssl base64 -A
```

### ▶️ If you are on Claude Code:

```bash
# Audit Python and PHP dependencies
pip-audit
composer audit
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Run package audit via terminal tool
await shell.exec("npm audit --audit-level=high");
```

### ⚠️ If you do NOT have tools:

1. Ask the user to share `package.json`, `requirements.txt`, or `composer.json` and recent audit output.
2. Identify unpinned version ranges (`^`, `~`, `*`) and flag any missing lockfiles or CDN SRI attributes.
3. Provide the exact `npm audit`, `pip-audit`, `composer audit`, and `openssl dgst` commands for the user to run.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Vulnerability scan | `npm audit` / `pip-audit` / `composer audit` | Provide audit commands and review pasted output |
| Version pinning | Inspect and edit manifest files directly | List exact pinned versions for user to apply |
| SRI generation | `openssl dgst -sha384 -binary` | Provide `openssl` / PowerShell hash command |

────────────────────────────────────

## ✅ Verification

- [ ] **No Hardcoded Secrets:** Confirmed `.npmrc`, `pip.conf`, and manifests contain zero plaintext registry tokens or credentials.
- [ ] **Zero Critical/High CVEs:** Verified `npm audit`, `pip-audit`, or `composer audit` reports zero Critical/High vulnerabilities.
- [ ] **Exact Pinning & Lockfile:** Production dependencies use exact versions and matching lockfiles are committed.
- [ ] **SRI Enforcement:** External CDN assets include verified `integrity="sha384-..."` and `crossorigin="anonymous"` attributes.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
