---
name: "Managing System Operations"
description: "Handles directory organization, automated local backups, system settings checks, and disk health metrics."
category: "generic/operations"
tools_required: ["data-analyst-mcp", "office-mcp"]
last_updated: 2026-05-24
---

# 🧠 Skill: Managing System Operations

## 🎯 Goal
Automate local directory structuring, execute secure database or directory backups, and diagnose system health to optimize system resources.

## 📊 Inputs Required
- Target directory to structure or back up.
- Active path for backup exports.

## 🛠️ Step-by-Step Instructions
1. **Directory Structuring pass**:
   - Classify unstructured files into standard folder schemas (`documents/`, `media/`, `code/`, `archives/`, `executables/`).
   - Flag and remove exact duplicates only after hashing.
2. **Local Backup Routines**:
   - Compress the target directory into a timestamped archive.
   - Exclude third-party dependency folders (`node_modules/`, `vendor/`) and temporary build caches.
   - Limit file logs to a max of 5 historical archives.
3. **Resource Diagnostic Check**:
   - Check disk allocation, usage metrics, and identify directories consuming excessive space.

## 🛡️ Verification & Security Checklist
1. **Data Safe**: Verify that zero user files are deleted during standard sorting runs.
2. **Secrets Scrub**: Confirm that no backup files contain unencrypted key databases or local token settings.
3. **Integrity Check**: Test backup archives to verify that they open without corruption.
4. **Log Retention**: Delete the oldest backup files if more than 5 historical records exist.

---
*Created by Efficiency Core*
