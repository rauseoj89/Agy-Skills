---
name: client-onboarding
description: Structured MSP client onboarding checklist: network discovery, vault credential setup, monitoring enrollment, PSA company setup, and documentation.
version: 1.1.0
tags: [universal, operations, onboarding]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
author: JimmyR
powered_by: AntigravityAI
---

# Skill: MSP Client Onboarding Specialist

## 🎯 Objective

Execute a complete, repeatable MSP client onboarding workflow — from initial intake through network discovery, credential vaulting with `vault-bridge-mcp`, monitoring enrollment, PSA record creation (via `connectwise-mcp` or vendor portal), and handoff documentation.

## 🕒 When to Use

- When registering a new client in monitoring and support systems (PSA/RMM).
- When performing initial credential setup in the security vault.
- When documenting a client network topology and configuring backup routines.

## 🛡️ Universal Principles

1. **Credentials Vaulting**: Receive credentials only via secure channels. Store immediately using `vault_bridge.put_secret`; never store in plaintext files or notes.
2. **Secrets Gate**: Confirmed zero credentials exist in ticket notes, documentation files, or session logs.
3. **Least Privilege**: Configure monitoring agents and administration accounts with minimal required privileges.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Vault credentials securely via vault-bridge-mcp:
# vault_bridge.put_secret({ namespace: "clients", path: "client-name/domain-admin", key: "password", value: "..." })
# Record client configuration into workspace
```

### ▶️ If you are on Hermes Agent:

```python
# Vault secret via secure API or environment variable
# If ticketing MCP is configured, register onboarding ticket
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Store credentials in Vault and query client configuration via ConnectWise MCP reference
await vault_bridge.put_secret({
  namespace: "clients",
  path: "acme-corp/admin",
  key: "credential",
  value: "SecureSecretToken"
});
const config = await connectwise.cw_get_company_configuration({ company_id: "ACME" });
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide the human operator through UI steps:
# Ask: "Create the company in ConnectWise PSA and provide the resulting ID."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Ask user for client details.
2. Generate checklists and documentation templates.
3. Instruct user to create records in PSA manually.
4. Generate detailed guides for user to install RMM agents and configure backups in Veeam or Axcient.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Store client secrets | `vault_bridge.put_secret()` | Instruct user to store in password manager/vault |
| Query PSA Company | `connectwise.cw_get_company_configuration()` | Ask user for confirmation in PSA portal |
| Update/List Tickets | `connectwise.cw_list_tickets()`, `cw_update_ticket()` | Instruct user to update onboarding ticket manually |
| Save Runbook | `filesystem.write_file()` | Display Runbook markdown for user to save |

---

## ✅ Verification

- Credentials stored safely in vault (`vault_bridge.put_secret`).
- Onboarding ticket created in PSA.
- RMM agents and backups (Veeam/Axcient) verified reporting successfully.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.1.0
