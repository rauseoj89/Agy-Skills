---
name: "Executing SOPs and Runbooks"
description: "Parses, verifies, and executes Standard Operating Procedures (SOPs) and technical runbooks systematically."
category: "generic/operations"
tools_required: ["data-analyst-mcp", "office-mcp"]
last_updated: 2026-05-24
---

# 🧠 Skill: Executing SOPs and Runbooks

## 🎯 Goal
Parse markdown runbooks from the OneDrive Vault and programmatically run their instructions step-by-step while verifying system limits and container logs.

## 📊 Inputs Required
- Target SOP markdown file (e.g., `SOP-001-db-backup.md`).
- Current system resource metrics (from `get_system_stats`).
- Target service states (from `docker_ps`).

## 🛠️ Step-by-Step Instructions
1. **Pre-Flight System Check**:
   - Check if current system resource allocations are within safety bounds. CPU must be < 80% and disk space > 15%.
2. **Read and Parse Runbook**:
   - Ingest target SOP file. Parse the headers, prerequisites, steps, and expected commands.
3. **Execution Isolation Loop**:
   - For each action step:
     - Verify prerequisites.
     - Formulate the exact command.
     - Run the command using the target shell executor.
     - Inspect console outputs, database checks, or container logs to confirm success.
4. **Compile Runbook Report**:
   - Write down timestamps, status checks, stats, and a structured markdown log of outcomes.

## 🛡️ Verification & Security Checklist
1. **Security Scan**: Verify that all credentials, database strings, private keys, or SNMP names are masked in reports.
2. **Error Isolation**: Stop immediately if any step returns a non-zero exit code or error trace.
3. **Data Integrity**: Ensure no system-specific private identifiers are printed in plain text.
4. **File Output**: Write execution report to the `output/` folder and check for valid size.

---
*Created by Efficiency Core*
