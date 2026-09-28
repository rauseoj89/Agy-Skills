---
name: managing-system-operations
description: Automates local backup routines, organizes project directories, checks system settings, and diagnoses logs. Use when asked to manage folders, run cleanups, set up local backups, diagnose diagnostic issues, or automate scripts.
version: 1.1.0
tags: [universal, operations, system, backup]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Personal System Administrator

## 🎯 Objective

Automate repetitive directory management tasks, protect local data integrity, and diagnose local systems efficiently without depending on external NAS orchestration tools.

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
# Verify disk space using native PowerShell or df:
# Windows PowerShell: Get-PSDrive -PSProvider FileSystem
# Linux: df -h
# Use filesystem-mcp tools: move_file, get_file_info, list_directory
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal to run diagnostics or compress directories
result = terminal(command="tar -czf backup.tar.gz ./src", timeout=120)
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Use filesystem MCP to check file info and move files safely
const fileInfo = await filesystem.get_file_info({ path: "large_log.log" });
await filesystem.move_file({ source: "old_path.txt", destination: "archive/old_path.txt" });
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Provide exact PowerShell or bash script for user execution:
# Windows: Compress-Archive -Path ./src -DestinationPath backup.zip
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate exact archive commands or cleanup scripts.
2. Ask user: "Run these commands in your local terminal to organize your folders".
3. Request visual confirmation of resulting disk space.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Compress files | `tar` / `Compress-Archive` | Provide compression command to user |
| Check disk space | PowerShell: `Get-PSDrive` / POSIX: `df -h` | Ask user to check file explorer or run `df -h` |
| Organize files | `filesystem.move_file()`, `filesystem.get_file_info()` | Generate file relocation script for user |

---

## ✅ Verification

- Backups exclude heavy, unneeded directories (e.g. `node_modules`).
- Verified remaining disk space is healthy.
- Log rotation maintains a strict limit of up to 5 historical archive files.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.1.0
