---
name: "Managing System Operations"
description: "Handles directory organization, automated local backups, system settings checks, and disk health metrics."
category: "generic/operations"
tools_required: ["nas-tools"]
last_updated: 2026-06-02
---

# 🧠 Skill: Managing System Operations

## 🎯 Goal
Automate local directory structuring, execute secure database or directory backups, and diagnose system health to optimize system resources while safeguarding secrets and preventing data loss.

## 📊 Inputs Required
- Target directory to structure or back up.
- Active path for backup exports.
- Local system diagnostic metrics.

## 🛠️ Step-by-Step Instructions
1. **Secrets Scan Pass**:
   - Before moving any files or running back ups, scan the directory for credential files (e.g. `.env`, `.pem` keys, `credentials.json`, SSH keys).
   - Alert the user immediately to isolate these sensitive credentials from standard sorting routines.
2. **Directory Structuring Pass**:
   - Classify unstructured files into standard folder schemas (`documents/`, `media/`, `code/`, `archives/`, `executables/`).
   - Flag and remove exact duplicates only after verifying hashes.
3. **Destructive Action Gate**:
   - Treat file deletions, bulk folder moves, and recursive directory removals as highly destructive operations.
   - Halt execution, present the affected items to the user, and wait for explicit confirmation before proceeding.
4. **Local Backup Routines**:
   - Compress the target directory into a timestamped archive (`.zip` or `.tar.gz`).
   - Exclude large dependency folders (e.g. `node_modules/`, `vendor/`) and temporary build caches.
   - Maintain a strict rotation limit of a maximum of 5 historical archives, deleting the oldest upon successful validation of a new one.

## 🛡️ Verification & Security Checklist
1. **Data Safe**: Verify that zero user files are deleted during standard sorting runs without prior, explicit authorization.
2. **Secrets Scrub**: Confirm that no backup files contain unencrypted key databases, private certificates, or local `.env` files.
3. **Integrity Check**: Test backup archives to verify that they open and decompress without corruption.
4. **Log Retention**: Delete the oldest backup files if more than 5 historical records exist.

---
*Created by Efficiency Core*
