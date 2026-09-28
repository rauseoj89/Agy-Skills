---
name: creating-agy-skills
description: Automates the blueprinting, creation, and Git deployment workflow for new or modified Skills inside the Agy-Skills repository. Use when the user requests to create, design, or update a Skill.
version: 1.1.0
tags: [universal, operations, skills, creation]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Agy-Skills Creator

## 🎯 Objective

Automate the creation, blueprinting, indexing, and Git deployment of custom operational skill files inside the external Agy-Skills repository while enforcing absolute security, standardized formatting, and local synchronization.

## 🕒 When to Use

- When creating new skills or modifying existing ones in the Agy-Skills repository.
- When organizing agent behaviors and operational rules into modular, plain text markdown documents.

## 🛡️ Universal Principles

1. **No Hardcoded Secrets**: Ensure NO passwords or credentials are hardcoded. Use vault or env vars.
2. **No Production IPs**: Use `${TARGET_HOST}` or `localhost` in examples.
3. **No Raw Shell Exec**: Use array-based argument structures for command examples.
4. **Security Checklist**: Every skill must have a verification checklist with a minimum of 4 items, with the first being secrets-related.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Write the new skill directly to its path in the workspace
# Validate structure using the repository script:
python3 scripts/validate-skill.py
```

### ▶️ If you are on Hermes Agent:

```python
# Create and save new skill using native Hermes tools
content = write_file(path="data/new_skill.md", content="...")
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use filesystem MCP to save markdown file
await filesystem.writeFile("data/new_skill.md", skillContent);
```

### ▶️ If you are on GitHub Copilot / Cursor:

```bash
# If terminal or filesystem tools are unavailable:
# Guide user to save the file in the designated category path.
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate the complete markdown content of the new skill.
2. Ask the user: "Please create the file in the appropriate category folder (e.g. `operations/`) and paste this content".
3. Provide the Git command to commit and push changes.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Create skill file | `write_to_file()` | Provide markdown in chat for manual save |
| Update README | `edit_file()` | Ask user to append entry to README index |
| Validate formatting | `python3 scripts/validate-skill.py` | Manual validation using universal principles checklist |

---

## ✅ Verification

- Output file contains all required sections.
- Passes validation by `scripts/validate-skill.py`.
- Contains no secrets or hardcoded production IPs.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.1.0
