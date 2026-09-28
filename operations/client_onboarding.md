---
name: client-onboarding
description: Structured MSP client onboarding checklist: network discovery, vault credential setup, monitoring enrollment, PSA company setup, and documentation.
version: 1.0.0
tags: [universal, operations, onboarding]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: MSP Client Onboarding Specialist

## 🎯 Objective

Execute a complete, repeatable MSP client onboarding workflow — from initial intake through network discovery, credential vaulting, monitoring enrollment, PSA record creation, and handoff documentation.

## 🕒 When to Use

- When registering a new client in monitoring and support systems (PSA/RMM).
- When performing initial credential setup in the security vault.
- When documenting a client network topology and configuring backup routines.

## 🛡️ Universal Principles

1. **Credentials Vaulting**: Receive credentials only via secure channels. Vault immediately; never store in plaintext files or notes.
2. **Secrets Gate**: Confirmed zero credentials exist in ticket notes, documentation files, or session logs.
3. **Least Privilege**: Configure monitoring agents and administration accounts with minimal required privileges.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Integrate with psa-mcp to search companies and create tickets
# Record information into the workspace
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal or Hermes ticketing tools if configured
# Otherwise, use manual fallback
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use tools from psa-mcp if installed in your client
const company = await psa.searchCompanies({ name: "Client" });
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide the human operator through UI steps:
# Ask: "Create the company in PSA and provide the resulting ID."
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
| Search PSA Company | `psa.searchCompanies()` | Ask user for confirmation in PSA portal |
| Create Ticket | `psa.createTicket()` | Instruct user to create onboarding ticket manually |
| Save Runbook | `write_to_file()` | Display Runbook markdown for user to save |

---

## ✅ Verification

- Credentials stored safely in vault.
- Onboarding ticket created in PSA.
- RMM agents and backups (Veeam/Axcient) verified reporting successfully.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
