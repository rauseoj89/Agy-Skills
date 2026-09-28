---
name: patch-management
description: Governs the full patch lifecycle: inventory, risk assessment, change window scheduling, staged deployment, verification, and rollback using RMM, Veeam, and Axcient.
version: 1.1.0
tags: [universal, operations, patch, sysadmin]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Patch Management Specialist

## 🎯 Objective

Execute a controlled, risk-aware patch lifecycle for Windows and Linux systems — from vulnerability inventory through staged deployment, post-patch validation, and rollback readiness, referencing `connectwise-mcp` and `backup-mcp`.

## 🕒 When to Use

- When planning maintenance windows to apply security patches (OS, drivers, firmware).
- When auditing pending vulnerabilities and verifying available patches.
- When coordinating restoration or rollback of impaired systems following an update failure.

## 🛡️ Universal Principles

1. **Pre-Patch Baseline**: Never patch a production system without a verified restore point (`backup-mcp` / Veeam / Axcient / snapshot) created within the last 24 hours.
2. **Staged Deployment**: Apply patches in order: Test/Dev -> Pilot Group -> Production -> Critical Infrastructure.
3. **Change Window Gate**: No production updates are allowed outside of approved change windows.
4. **No Hardcoded Credentials**: Inject RMM, backup, or domain admin credentials dynamically using environment variables or vaults.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Verify backup status via backup-mcp:
# get_backup_status(target_name="prod-app-server")
# Execute local PowerShell verification scripts:
# Get-HotFix | Select-Object -First 10
```

### ▶️ If you are on Hermes Agent:

```python
# Execute terminal commands to check if HotFix is already applied
result = terminal(command="powershell -Command \"Get-HotFix -Id KB5034441\"", timeout=60)
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Query backup status and inspect managed endpoints
const backup = await backup_tools.get_backup_status({ target_name: "db01" });
const endpoints = await connectwise.cw_list_endpoints({ company_id: "CORP" });
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide user to validate backups in their RMM/BCDR console:
# Ask: "Confirm in Veeam/Axcient that a successful backup exists from the last 24 hours."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate validation scripts (e.g. `Get-HotFix`, `wusa /uninstall`, or bash update commands).
2. Ask user: "Please run these commands to verify applied patches or uninstall the problematic update".
3. Request explicit confirmation that a backup exists before proceeding with production patching.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Verify backup freshness | `backup_mcp.get_backup_status()` | Ask user to check in Veeam/Axcient portal |
| Inspect endpoints | `connectwise.cw_list_endpoints()` | Instruct user to review RMM dashboard |
| Verify installed patches | PowerShell: `Get-HotFix` | Ask user to run Windows Update History check |
| Rollback patch | `terminal("wusa /uninstall")` | Generate exact uninstall script for human execution |

---

## ✅ Verification

- A functional restore point from Veeam or Axcient exists from within the last 24 hours.
- All automatic-startup services are running post-reboot.
- System event logs show no critical OS updater errors.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.1.0
