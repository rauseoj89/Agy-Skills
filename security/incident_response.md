---
name: incident-response
description: Structured triage, containment, investigation, remediation, and documentation workflow for security and operational incidents.
version: 1.0.0
tags: [universal, security, incident, response]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Incident Response Specialist

## 🎯 Objective

Execute a structured, evidence-preserving incident response workflow from initial detection through full remediation and post-incident documentation. Integrates with the PSA system for ticket creation and audit trail.

## 🕒 When to Use

- When suspecting an active security breach (ransomware, exfiltration, phishing).
- To contain unauthorized access to accounts or servers.
- When coordinating threat eradication and subsequent backup recovery.

## 🛡️ Universal Principles

1. **Containment Before Remediation**: Always isolate the affected systems or accounts before running cleaning steps to preserve evidence.
2. **Authorization Gate**: Always request user/client authorization before isolating production networks or restoring backups.
3. **Evidence Preservation**: Do not work on original logs or drives; make copies, compute hashes, and preserve timestamps.
4. **No Hardcoded Secrets**: Ensure credentials rotated during eradication are stored in vaults, not in ticket logs.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Query local security logs to identify origin
# Block local access or coordinate isolation using firewall rules
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal to inspect active network connections
result = terminal(command="netstat -ano", timeout=30)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use terminal or firewall MCP to execute network isolation commands
const result = await shell.exec("powershell -Command \"Disable-NetAdapter -Name 'Ethernet'\"");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Alert and guide user through critical device isolation steps:
# Ask: "Immediately disconnect the device from network (WiFi and Ethernet cable)."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Classify incident severity (P1-P4) and formulate immediate containment steps.
2. Ask user: "Please execute these isolation steps (e.g., unplug network cable, disable account) immediately".
3. Provide log acquisition instructions so user preserves evidence before remediation.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Isolate endpoint | `terminal("Disable-NetAdapter")` | Ask user to disconnect network cable / WiFi |
| Disable account | `psa.revokeSessions()` / `terminal()` | Instruct administrator to revoke access in Azure/AD portal |
| Verify backups | `backup.getBackupStatus()` | Ask user to identify latest healthy backup in console |

---

## ✅ Verification

- The threat has been contained and isolated.
- The root attack vector has been identified and patched.
- A post-incident post-mortem report was authored and saved without revealing secrets.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
