---
name: "Executing SOPs and Runbooks"
description: "Parses, verifies, and executes Standard Operating Procedures (SOPs) and technical runbooks systematically."
category: "generic/operations"
tools_required: ["data-analyst-mcp"]
last_updated: 2026-06-02
---

# 🧠 Skill: Executing SOPs and Runbooks

## 🎯 Goal
Parse markdown runbooks from secure vaults and programmatically run their instructions step-by-step while verifying system limits, enforcing permission levels, and preventing command injections.

## 📊 Inputs Required
- Target SOP markdown file (e.g., `SOP-001-db-backup.md`).
- Current system resource metrics (from `get_system_stats`).
- Target service states (from `docker_ps`).

## 🛠️ Step-by-Step Instructions
1. **Pre-Flight System Check**:
   - Check if current system resource allocations are within safety bounds: CPU must be < 80% and disk space > 15%.
   - Audit running containers (`docker_ps`) to ensure dependencies are healthy.
2. **Read and Parse Runbook with Permission Checks**:
   - Ingest target SOP file. Parse the headers, prerequisites, steps, and expected commands.
   - Categorize and label steps by required security clearance (`requiredPermission: "admin" | "operator"`).
3. **Execution Isolation Loop (Test-Execute-Confirm)**:
   - **Test:** Verify system state is prepared for execution.
   - **Execute:** Execute command using array-based subprocess spawning (`spawn`), never raw concatenated strings (`exec`), to eliminate command injection vulnerabilities.
   - **Confirm:** Perform immediate post-verification checking (e.g. check container logs, verify exit codes) before moving to the next step.
4. **Destructive Action Gate**:
   - Stop immediately if a step contains any destructive operations (e.g. `DROP`, `TRUNCATE`, `rm -rf`, `docker rm`).
   - Present the exact command and risks to the user, and wait for an explicit "CONFIRM" before proceeding.
5. **Compile Runbook Report**:
   - Write down timestamps, status checks, stats, and a structured markdown log of outcomes, redacting any private stack traces.

## 🛡️ Verification & Security Checklist
1. **Destructive Action Gate**: Verify that all destructive operations required explicit, manual user authorization.
2. **Command Injection Defense**: Ensure zero commands concatenated raw strings or unvalidated user-supplied variables.
3. **Error Isolation**: Stop execution immediately if any step returns a non-zero exit code or error trace, executing rollbacks where defined.
4. **Output Redaction**: Ensure all trace logs, credentials, and private environment variables are masked (`********`).

---
*Created by Efficiency Core*
