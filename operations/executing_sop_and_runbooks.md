---
name: executing-sop-and-runbooks
description: Parses, verifies, and executes Standard Operating Procedures (SOPs) and technical runbooks. Use when asked to follow an SOP, run a system migration, execute a deployment checklist, or automate system maintenance.
version: 1.0.0
tags: [universal, operations, runbook, sop]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Runbook & SOP Orchestrator

## 🎯 Objective

Execute technical procedures step-by-step with validation, confirmation management for destructive operations, and automated rollback support.

## 🕒 When to Use

- When executing a Standard Operating Procedure (SOP) step-by-step.
- When deploying database migrations, infrastructure updates, or staging rollouts.
- When performing routine system maintenance tasks.

## 🛡️ Universal Principles

1. **Destructive Action Gate**: Never run destructive operations (e.g. `DROP`, `rm -rf`, `docker rm`) without explicit user validation.
2. **Validation Loop**: Always follow the Test -> Execute -> Verify loop.
3. **Least Privilege**: Annotate steps with `operator` (read-only/audit) vs `admin` (write/deploy).
4. **Secrets Isolation**: No secrets in logs or terminal parameters.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
antigravity-runbook execute runbook.md --confirm-destroy
antigravity lock acquire runbook-execution
# Secrets are automatically injected from vault
```

### ▶️ If you are on Hermes Agent:

```python
# Use read_file to load the runbook
runbook = read_file(path="runbook.md", limit=500)
# Map steps to todo list
todo(todos=[{"id": "step1", "content": "...", "status": "pending"}])
# Execute with confirmation
result = terminal(command="...", timeout=300)
# If failed:
terminal(command="/rollback")
```

### ▶️ If you are on Cline / Roo Code:

```javascript
const runbook = await filesystem.readFile("runbook.md");
// Create tasks manually
await tasks.create({name: "Step 1", status: "pending"});
// Execute commands
await shell.exec("your-command");
// Fallback on failure: generate rollback script
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Ask user: "Please open the `runbook.md` file and copy and paste its contents".
2. Analyze the provided runbook.
3. Generate exact commands and detail their risk levels (Destructive Gate).
4. Ask user: "Execute each command in your terminal and paste the outcome".
5. Verify manually with user before proceeding to the next step.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Read runbook | `read_file()` | Ask user to paste content |
| Execute step | `terminal()` / `shell.exec()` | Generate command for user to execute |
| Verify success | `check_status()` | Ask user to paste output to verify |

---

## ✅ Verification

- All runbook steps completed in PASS state.
- Pre-flight checks for CPU and disk passed successfully.
- Final structured execution summary generated and saved as `report_runbook.md`.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
