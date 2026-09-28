---
name: creating-agy-skills
description: Automates the blueprinting, creation, and Git deployment workflow for new or modified Skills inside the Agy-Skills repository. Use when the user requests to create, design, or update a Skill.
version: 1.2.0
tags: [universal, operations, skills, creation]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Agy-Skills Creator

## 🎯 Objective

Automate the creation, blueprinting, indexing, and Git deployment of custom operational skill files inside the external Agy-Skills repository while enforcing absolute security, standardized formatting, unique naming, and MCP tool reference resolution.

## 🕒 When to Use

- When creating new skills or modifying existing ones in the Agy-Skills repository.
- When organizing agent behaviors and operational rules into modular, plain text markdown documents.

## 🛡️ Universal Principles

1. **No Hardcoded Secrets**: Ensure NO passwords or credentials are hardcoded. Use vault or env vars.
2. **No Production IPs**: Use `${TARGET_HOST}` or `localhost` in examples.
3. **No Raw Shell Exec**: Use array-based argument structures for command examples.
4. **Unique Call Name**: The `name:` field in frontmatter must be a unique, concise kebab-case identifier (e.g., `docum-md`, `db-manager`).
5. **Resolvable MCP Tools**: Every MCP tool cited in Multi-Agent Execution or Fallbacks must resolve to an active blueprint in `Agy-MCP` or a documented vendor CLI fallback.
6. **Mandatory Indexing**: New skills must be indexed in the root `README.md` catalog matrix.
7. **Version & Timestamp Bump**: Every update must increment semver `version` and set `last_updated: YYYY-MM-DD` in both frontmatter and footer.
8. **Security Checklist**: Every skill must have a verification checklist with a minimum of 4 items, with the first being secrets-related.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Write the new skill directly to its path in the workspace
# Validate structure using the repository script (Windows: python / py, POSIX: python3):
python scripts/validate-skill.py
```

### ▶️ If you are on Hermes Agent:

```python
# Create and save new skill using native Hermes tools
content = write_file(path="data/new_skill.md", content="...")
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Use filesystem MCP to save markdown file
await filesystem.writeFile("data/new_skill.md", skillContent);
```

### ▶️ If you are on GitHub Copilot / Cursor:

```bash
# Guide user to save the file in the designated category path:
python scripts/validate-skill.py
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
| Validate formatting | `python scripts/validate-skill.py` | Manual validation using universal principles checklist |

---

## ✅ Verification

- Output file contains all required sections and valid YAML frontmatter.
- The `name:` field is unique and matches kebab-case convention.
- All referenced MCP tools exist in `Agy-MCP` blueprints or documented fallbacks.
- Passes validation by `python scripts/validate-skill.py` (31/31 valid).
- Contains no secrets or hardcoded production IPs.
- Indexed in root `README.md` and version incremented.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.2.0
