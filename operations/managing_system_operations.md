---
name: managing-system-operations
description: Automates local backup routines, organizes project directories, checks system settings, and diagnoses logs. Use when asked to manage folders, run cleanups, set up local backups, diagnose diagnostic issues, or automate scripts.
version: 1.0.0
tags: [universal, operations, system, backup]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Personal System Administrator

## 🎯 Objective

Automate repetitive directory management tasks, protect local data integrity, and diagnose local systems efficiently.

## 🕒 When to Use

- When cleaning, structuring, or organizing local files and directories.
- When creating local backup scripts and routines.
- When inspecting file permissions, available disk space, or local application logs.

## 🛡️ Universal Principles

1. **Destructive Action Gate**: Bulk moves, deletions, and directory removals must be explicitly approved by the user.
2. **Secrets Scan**: Scan for `.env` or credential files before performing operations. Exclude them from general moves or archives.
3. **Backup Space Limits**: Check disk space before executing backups. Keep a maximum of 5 historical backups.
4. **No Hardcoded Absolute Paths**: Use relative paths or environment variables instead of hardcoded home folders.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Execute local copy and organize commands (tar, Move-Item, etc.)
# Use get_system_stats to verify system health
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal to run diagnostics or compress directories
result = terminal(command="tar -czf backup.tar.gz ./src", timeout=120)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use filesystem MCP and terminal to compress and organize files
const result = await shell.exec("tar -czf backup.tar.gz ./src");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Provide exact PowerShell or bash script for user execution:
# Ask: "Run this command to create the backup: tar -czf backup.tar.gz ./src"
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate exact archive commands or cleanup scripts.
2. Ask user: "Run these commands in your local terminal to organize your folders".
3. Request visual confirmation of resulting disk space.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Compress files | `tar` / `terminal()` | Provide compression command to user |
| Check disk space | `get_system_stats()` | Ask user to run `df -h` or check file explorer |
| Organize files | `write_to_file()` / `terminal("mv")` | Generate file relocation script for user |

---

## ✅ Verification

- Backups exclude heavy, unneeded directories (e.g. `node_modules`).
- Verified remaining disk space is healthy.
- Log rotation maintains a strict limit of up to 5 historical archive files.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
