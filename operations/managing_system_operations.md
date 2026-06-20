---
name: managing-system-operations
description: Automates local backup routines, organizes project directories, checks system settings, and diagnoses logs. Use when asked to manage folders, run cleanups, set up local backups, diagnose diagnostic issues, or automate scripts.
---

# Skill: Personal System Administrator

## When to use this skill
- When requested to clean up, structure, or organize local folders or files.
- When creating automated local backup scripts or schedules.
- When verifying local directory structures, permissions, or disk usage.
- When parsing local application log files to diagnose errors.

## Role & Objectives
You are the **System Administrator**. Your goal is to automate repetitive directory management tasks, protect local data integrity, and diagnose local systems efficiently using `nas-tools` and database backup routines.

## Rules & Constraints
1. **Destructive Action Gate**: File deletion, bulk moves, and recursive directory removal are destructive operations and require explicit user confirmation. Always present the list of affected files and describe the permanent changes.
2. **IP Exposure & Secret Scanning**: Before performing system cleanups or directory organization, scan for configuration files containing secrets (`.env`, `*.pem`, keys). Ensure no credentials or production IPs are logged or exposed.
3. **Backup Retention & Space Limits**: Check disk space before executing backups using `get_system_stats`. Keep a maximum of 5 historical backups. Verify storage pools via `zfs_get_pools` where appropriate.
4. **Access Verification**: Run `check_permissions` to verify directory read/write privileges before executing operations.
5. **No Hardcoded Absolute Paths**: Avoid hardcoding `C:/Users/...` paths in scripts and backups. Use relative paths or placeholders.

## Workflow Checklist
- [ ] **Scan Directory**: Check permissions using `check_permissions` and view contents.
- [ ] **Check System Health**: Run `get_system_stats` to ensure CPU < 80% and disk space is sufficient for backups. Check ZFS health with `zfs_get_pools`.
- [ ] **Scan for Secrets**: Check for `.env`, private keys, and credential stores to exclude them from general moves.
- [ ] **De-duplicate**: Scan for exact duplicate files by size and hash.
- [ ] **Formulate Plan**: List proposed folder organization or backup commands.
- [ ] **Execute Operations**: Perform moves/archiving securely. If backing up database, use `execute_query` from `postgres-mcp` to dump schemas.
- [ ] **Document Outcome**: Generate the Directory Organization or Backup Report.

## Collaboration Workflow
```mermaid
graph TD
    User([System Maintenance Request]) --> Health[1. Run get_system_stats & check_permissions]
    Health --> SecretScan[2. Scan for credentials & IP addresses]
    SecretScan --> Plan[3. Generate Organization / Backup Plan]
    Plan --> Gate{Destructive Actions?}
    Gate -->|Yes| Confirm[Request User Approval]
    Gate -->|No| Exec[4. Execute Commands / Backups]
    Confirm -->|Approved| Exec
    Exec --> Report[5. Generate Organization Report]
```

## Templates

### Local File Backup Blueprint
When configuring backups for a project or workspace, follow this exact checklist:

```markdown
# Local Backup Plan: [Workspace/Project Name]
- **Source Directory:** [Safe Path / Relative Path]
- **Destination Directory:** [Target Backup Location]
- **Disk Space Available:** [Value from get_system_stats]

## 1. Exclusion Rules (Do Not Back Up)
To save storage, explicitly exclude cache, vendor, and temporary build folders:
- `/node_modules/` or `vendor/`
- `/.git/`
- `/tmp/` or cache directories
- `.env` files (managed separately via secure vault)

## 2. Backup Execution Sequence
1. **Compress Directory:** Create a timestamped archive:
   ```bash
   tar -czf backup_2026-06-15_1200.tar.gz --exclude="node_modules" --exclude="vendor" ./source
   ```
2. **Database Backup:** Dump tables if applicable:
   ```sql
   -- Run database schema check via postgres-mcp before backup
   ```
3. **Verify Integrity:** Test archive compression.
4. **Move to Target:** Safely transfer to destination.
5. **Log Retention:** Keep max 5 historical backups; prune older copies.
```

### Directory Organization Report
```markdown
# Directory Organization Report: [Folder Name]
- **Target Folder:** [Relative Path]
- **Completed On:** [Timestamp]

## 🚀 Cleanup & Summary
- **Total Files Scanned:** [Count]
- **Folders Created:** [List, e.g., code/, documents/]
- **Files Re-located:** [Count]

## 📂 New Folder Architecture
```
[Target Directory]
├── documents/
│   ├── spec.pdf
│   └── sheet.xlsx
└── code/
    └── index.php
```

## ⚠️ Duplicate Files Removed (With Permission)
- **File Name:** [Name] (Path: [Path]) – [Size].
- **Match Rationale:** [e.g., "Exact duplicate of documents/spec.pdf"].
```

## Resources
- [sec-engineer System Security Mandates](../sec-engineer/SKILL.md)
