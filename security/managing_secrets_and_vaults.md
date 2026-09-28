---
name: managing-secrets-and-vaults
description: Secures system credentials, manages API keys, rotates environment variables, and orchestrates integration with secure vaults. Use when requested to configure environment keys, edit secrets, retrieve items from Vault, or secure sensitive configurations.
version: 1.1.0
tags: [universal, security, vault, secrets]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
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
4. **Least Privilege & Namespacing**: Query specific namespaces and keys rather than reading all credentials in bulk.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Interact with vault-bridge-mcp tools:
# get_secret, put_secret, list_secrets, rotate_secret, audit_secret_access
```

### ▶️ If you are on Hermes Agent:

```python
# Load secrets dynamically using environment variables or vault bridge
import os
db_pass = os.getenv("DB_PASSWORD")
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Call vault_bridge tools with mandatory namespace parameter
const secret = await vault_bridge.get_secret({
  namespace: "production",
  path: "db",
  key: "password"
});
const catalog = await vault_bridge.list_secrets({ namespace: "production" });
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
| Retrieve secret | `vault_bridge.get_secret({namespace, path, key})` | Ask user to configure variable locally |
| List secret keys | `vault_bridge.list_secrets({namespace})` | Ask user to check vault inventory |
| Write .env file | Write via `.env.tmp` and atomic rename | Provide environment variable template to user |
| Rotate credential | `vault_bridge.rotate_secret({namespace, path, key})` | Provide step-by-step rotation guide to user |
| Audit access | `vault_bridge.audit_secret_access({namespace})` | Review audit logs in Vault console |

---

## ✅ Verification

- The `.env` file is declared in `.gitignore`.
- Zero plaintext secrets exist in console or agent logs.
- Temporary `.tmp` secret buffers were cleaned up after writing.
- Secret calls explicitly include the target namespace parameter.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.1.0
