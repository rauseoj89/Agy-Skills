---
name: docum-md
description: Manages developer and agent session logs inside a hidden, git-ignored folder (CHG-Review). Enforces Global Agent Rule 6 reporting, atomic writes, MCP data sanitization, and SDD/debugging alignment upon session completion or git push.
version: 1.2.0
tags: [universal, operations, session, documentation, audit, rule-6]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Session Review Documenter

## 🎯 Objective

Manage developer and agent session logs inside a hidden, git-ignored folder (`CHG-Review`), ensuring that all changes, decisions, and verifications are securely documented according to **Global Agent Rule 6**, without leaking PII, secrets, database dumps, or infrastructure configurations.

## 🕒 When to Use

- Immediately after executing `git push`.
- When compiling daily or weekly progress summaries.
- At the end of an extended development session to record architectural decisions and test evidence.
- When documenting phase completion under Specification-Driven Development (SDD) or bug resolutions under Systematic Debugging.

## 🛡️ Universal Principles

1. **CHG-Review Folder Security**:
   - POSIX: `chmod 700 CHG-Review`
   - Windows: `attrib +h CHG-Review` and `icacls CHG-Review /inheritance:r /grant:r "%USERNAME%:F"`
2. **Never Push to Git**:
   - `CHG-Review/` must always be declared in `.gitignore`. Use `git-mcp` or `git status --ignored` to verify it is ignored. Never run `git add` on this directory.
3. **Global Agent Rule 6 Alignment**: Every log entry must include the 4 standard sections:
   - **Changed:** Exact files modified or created.
   - **Verified:** Executed commands and observed terminal outcomes.
   - **Not Verified / Assumptions:** Omitted tests, dependency assumptions, or unverified paths.
   - **Risks & Rollback:** Exact rollback steps and commands (`git revert <sha>` / migration rollback).
4. **Data & MCP Sanitization**: Automatically strip keys, tokens, private IP addresses, and database dumps from MCP tools (`postgres-mcp`) or Vault paths (`vault-bridge-mcp`).
5. **Atomic Buffering**: Write entries via an intermediate buffer (`.tmp`) before appending to log files to prevent truncation on process interruptions.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Initialize restricted directory if missing (POSIX)
mkdir -p CHG-Review && chmod 700 CHG-Review

# On Windows PowerShell:
if (-not (Test-Path "CHG-Review")) { New-Item -ItemType Directory -Path "CHG-Review" }
attrib +h CHG-Review
icacls CHG-Review /inheritance:r /grant:r "${env:USERNAME}:(OI)(CI)F"

# Write entry via write_to_file
```

### ▶️ If you are on Hermes Agent:

```python
# Use write_file with structured Rule 6 template
content = write_file(path="CHG-Review/2026-09-28.md", content="### 🚀 Session Entry...\n#### 📂 Changed: ...")
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Use filesystem MCP to draft and persist session logs
await filesystem.writeFile("CHG-Review/" + new Date().toISOString().slice(0,10) + ".md", sessionSummary);
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide developer:
# "I have drafted the session review under Rule 6. Please save it in your local CHG-Review/ folder."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate structured review in chat using the official Rule 6 template.
2. Remind user: "Save this entry to your local git-ignored daily log under the `CHG-Review/` directory".
3. Provide the command to secure directory permissions (`chmod 700 CHG-Review` or Windows `icacls`).

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Initialize directory | `mkdir -p CHG-Review && chmod 700` / `icacls` | Instruct user to create directory with restricted permissions |
| Verify .gitignore | `git-mcp.git_status` / `filesystem-mcp.read_file` | Instruct user to check `.gitignore` manually |
| Save session log | `filesystem-mcp.write_file` with atomic buffer | Output formatted Markdown for user to copy/paste |
| Data sanitization | Automated regex scrubbing | Visual static inspection on generated text |

---

## ✅ Verification

- The `CHG-Review/` directory is declared in the project's `.gitignore` file.
- Folder permissions prevent access by other users (`chmod 700` on Linux or `icacls` on Windows).
- The log entry contains all 4 mandatory Rule 6 sections (Changed, Verified, Not Verified, Risks & Rollback).
- No passwords, database dumps, or internal IP addresses were leaked.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.2.0
