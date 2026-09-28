---
name: managing-secrets-and-vaults
description: Secures system credentials, manages API keys, rotates environment variables, and orchestrates integration with secure vaults. Use when requested to configure environment keys, edit secrets, retrieve items from Vault, or secure sensitive configurations.
version: 1.0.0
tags: [universal, security, vault, secrets]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Secrets & Credentials Manager

## 🎯 Objective

Enforce bulletproof security for application credentials, ensuring zero secrets are leaked to disk, logs, or repositories, while utilizing advanced vaulting and rotation workflows.

## 🕒 When to Use

- When updating passwords, API keys, connection strings, or certificates.
- When configuring or modifying environment variable files (`.env`, `.env.local`).
- When inventorying or rotating secrets using external vaults.
- To audit and prevent secret leaks in Git history.

## 🛡️ Universal Principles

1. **The Redaction Protocol**: Strip or replace plaintext passwords/keys with `[REDACTED]` or `********` in all logs, screenshots, and terminal outputs.
2. **Git-Leak Defense**: Force target config files (like `.env`) to be explicitly in `.gitignore` before writing secrets to them.
3. **Atomic Secret File Writes**: Never edit environment files directly. Write updates to `.env.tmp` first, then replace.
4. **Least Privilege**: Query specific paths rather than reading all credentials in bulk.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Interact with vault-bridge-mcp to read or rotate secrets
# Use local system variables securely
```

### ▶️ If you are on Hermes Agent:

```python
# Load secrets dynamically using hermes_secrets or environment variables
import os
db_pass = os.getenv("DB_PASSWORD") or hermes_secrets.get("db_password")
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Call vault MCP or vault-bridge-mcp to retrieve secrets
const secret = await vault.getSecret({ path: "production/db", key: "password" });
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide user to store keys in local environment variables:
# Ask: "Configure the 'DB_PASSWORD' environment variable on your local machine."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Ask user to set environment variables manually in their operating system.
2. Generate empty `.env.example` templates with clear placeholders (e.g., `DB_PASSWORD=YOUR_PASSWORD_HERE`).
3. Warn user never to commit these files to Git and verify they are listed in `.gitignore`.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Retrieve secret | `get_secret()` / `vault.getSecret()` | Ask user to configure variable locally |
| Write .env file | Write via `.env.tmp` and atomic rename | Provide environment variable template to user |
| Rotate credential | `rotate_secret()` | Provide step-by-step rotation guide to user |

---

## ✅ Verification

- The `.env` file is declared in `.gitignore`.
- Zero plaintext secrets exist in console or agent logs.
- Temporary `.tmp` secret buffers were cleaned up after writing.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
