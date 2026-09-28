---
name: powershell-automation
description: Authors, tests, and safely deploys PowerShell scripts for Windows automation — parameter validation, SecureString secrets, Pester testing, and execution policy.
version: 1.0.0
tags: [universal, operations, powershell, automation]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: PowerShell Automation Specialist

## 🎯 Objective

Write production-quality, secure PowerShell scripts for Windows automation — with proper parameter validation, secret handling via SecureString or Vault, structured error handling, Pester test coverage, and safe deployment patterns.

## 🕒 When to Use

- When writing system automation scripts for Windows environments (PowerShell / pwsh).
- When configuring local scheduled tasks.
- When writing Pester tests to verify infrastructure script logic.

## 🛡️ Universal Principles

1. **No Hardcoded Secrets**: Load secrets from environment variables or secure vaults, never in plaintext script files.
2. **Parameter Validation**: Validate all inputs at parameter level (e.g. `[ValidateRange()]`, `[ValidatePattern()]`).
3. **SupportsShouldProcess**: Implement `-WhatIf` and `-Confirm` on any script containing destructive operations (delete, stop service, format).
4. **StrictMode & Error Handling**: Enforce strict mode (`Set-StrictMode -Version Latest`) and turn on stop error preference (`$ErrorActionPreference = 'Stop'`).

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Write and test PowerShell scripts in the local environment
# Use native terminal to execute pwsh
```

### ▶️ If you are on Hermes Agent:

```python
# Invoke PowerShell scripts passing secure parameters via terminal
result = terminal(command="pwsh -File myscript.ps1", timeout=60)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use terminal/shell MCP to run Pester tests or launch scripts
const result = await shell.exec("pwsh -Command \"Invoke-Pester\"");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide user to execute scripts interactively:
# Ask: "Run 'pwsh -ExecutionPolicy Bypass -File script.ps1' in your terminal."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Write the structured PowerShell script following the official template.
2. Ask user: "Create the file `script.ps1` and paste this content".
3. Provide execution commands with `-WhatIf` so the user can preview changes safely.
4. Request that user paste any errors or output for debugging.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Run pwsh scripts | `terminal("pwsh")` / `shell.exec()` | Generate pwsh command for user to run |
| Create .ps1 file | `write_to_file()` | Provide code in chat for manual save |
| Run Pester tests | `terminal("Invoke-Pester")` | Provide command for user to run Pester locally |

---

## ✅ Verification

- Script contains `Set-StrictMode` and `$ErrorActionPreference = 'Stop'`.
- Critical parameters are typed and constrained by input validation attributes.
- Script returns appropriate exit codes (0 on success, 1 on failure).

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
