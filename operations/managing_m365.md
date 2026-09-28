---
name: managing-m365
description: Administers Microsoft 365 users, licenses, MFA, Conditional Access, mailboxes, and groups using PowerShell and the Graph API.
version: 1.0.0
tags: [universal, operations, m365, office]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Microsoft 365 Administrator

## 🎯 Objective

Provision and deprovision M365 users, enforce MFA and Conditional Access policies, audit licenses, manage mailbox delegations, and govern group membership — securely and with full audit trails.

## 🕒 When to Use

- When creating or deactivating user accounts in Microsoft 365.
- When verifying and auditing MFA status on administrative and user accounts.
- When managing license assignments and shared mailboxes.

## 🛡️ Universal Principles

1. **No Plaintext Credentials**: Never hardcode passwords or client secret tokens in scripts or commands.
2. **Order of Deprovisioning**: Revoke sessions -> disable account -> remove groups -> convert to shared -> remove licenses.
3. **Admin MFA Protection**: Always enforce Phishing-Resistant MFA on administrative accounts.
4. **Least Privilege**: Only request scopes necessary for the operation (e.g. `User.ReadWrite.All`).

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Execute PowerShell commands locally using Microsoft Graph PowerShell SDK
# Inject temporary credentials from vault
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal to invoke PowerShell scripts or curl against Graph API
result = terminal(command="pwsh -File run-m365-audit.ps1", timeout=120)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use shell/terminal MCP to invoke PowerShell or make HTTP requests
const result = await shell.exec("pwsh -Command \"Connect-MgGraph -Scopes ...\"");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide user to execute local scripts in their terminal:
# Ask: "Run 'Connect-MgGraph' in PowerShell and paste the connection status."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate PowerShell scripts or REST `curl` requests for the Microsoft Graph API.
2. Ask user: "Please open PowerShell, sign into Microsoft Graph, and run the following commands".
3. Request that user paste returned outputs (redacting tokens) to proceed with analysis.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Connect to Graph | `terminal()` / `Connect-MgGraph` | Provide command for user to authenticate locally |
| Query MFA status | Graph API call | Ask user to run audit script and paste output |
| Modify license | `Set-MgUserLicense` | Generate script for user execution |

---

## ✅ Verification

- Deprovisioning phases executed in exact security order.
- Verified newly created UPNs enforce password change on first login.
- Zero passwords printed in logs or terminal outputs.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
