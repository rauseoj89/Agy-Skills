---
name: incident-response
description: Structured triage, containment, investigation, remediation, and documentation workflow for security and operational incidents.
version: 1.1.0
tags: [universal, security, incident, response]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Incident Response Specialist

## 🎯 Objective

Execute a structured, evidence-preserving incident response workflow from initial detection through containment, forensic investigation with log parsing, remediation, secret rotation, and post-incident documentation.

## 🕒 When to Use

- When suspecting an active security breach (ransomware, exfiltration, phishing).
- To contain unauthorized access to accounts, endpoints, or cloud tenants.
- When coordinating threat eradication, credential rotation, and subsequent system recovery.

## 🛡️ Universal Principles

1. **Containment Before Remediation**: Always isolate affected systems or revoke sessions before running remediation to preserve volatile evidence.
2. **Authorization Gate**: Always request authorization before isolating production networks or restoring backups.
3. **Evidence Preservation**: Do not work on original logs; make copies, compute hashes, and preserve timestamps.
4. **No Hardcoded Secrets**: Ensure all credentials rotated during eradication are stored in vaults using `vault-bridge-mcp`.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Triage logs using data-analyst-mcp:
# parse_log_file(file_path="auth.log")
# Inspect listening sockets via security-scanner-mcp:
# audit_listening_ports(protocol="all")
# Rotate compromised credentials via vault-bridge-mcp:
# rotate_secret(namespace="production", path="service-accounts", key="api-token")
```

### ▶️ If you are on Hermes Agent:

```python
# Revoke active user sessions via Microsoft Graph or AD PowerShell
result = terminal(command="powershell -Command \"Revoke-MgUserSignInSession -UserId 'compromised@domain.com'\"", timeout=60)
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Rotate secrets in Vault and record incident notes
await vault_bridge.rotate_secret({
  namespace: "production",
  path: "db",
  key: "password"
});
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
| Isolate endpoint | Terminal: `Disable-NetAdapter` / `ip link set down` | Ask user to disconnect network cable / WiFi |
| Revoke sign-in / disable | PowerShell: `Revoke-MgUserSignInSession` / `Disable-ADAccount` | Instruct admin to revoke sessions in Entra ID / AD |
| Parse security logs | `data_analyst.parse_log_file()` | Ask user to grep relevant log lines |
| Inspect active sockets | `security_scanner.audit_listening_ports()` | Terminal: `netstat -ano` / `ss -tulpn` |
| Rotate credentials | `vault_bridge.rotate_secret()` | Provide manual credential rotation steps |
| Incident ticket logging | `connectwise.cw_update_ticket()` | Instruct user to update PSA incident ticket |

---

## ✅ Verification

- The threat has been contained and isolated.
- The root attack vector has been identified and patched.
- Compromised accounts have sessions revoked and credentials rotated.
- A post-incident post-mortem report was authored and saved without revealing secrets.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.1.0
