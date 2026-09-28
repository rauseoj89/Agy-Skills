---
name: creating-agy-mcps
description: Automates the blueprinting, structural setup, and Git deployment workflow for new or modified Model Context Protocol (MCP) servers in the Agy-MCP repository. Use when the user requests to create or modify an MCP server.
version: 1.1.0
tags: [universal, operations, mcp, blueprint]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Agy-MCP Blueprint Automator

## 🎯 Objective

Automate the blueprinting, structure generation, and deployment of custom Model Context Protocol (MCP) servers inside the Agy-MCP repository, while strictly maintaining security, path isolation, least privilege, and input validation.

## 🕒 When to Use

- When designing, creating, or modifying MCP server blueprints.
- When creating custom integrations connecting external APIs or databases with the agent workspace.

## 🛡️ Universal Principles

1. **No Hardcoded Secrets**: Use placeholders like `${VAULT_SECRET_<MCP-NAME>_<KEY>}`.
2. **No Production IPs**: Use `${TARGET_HOST}` or `localhost` in configurations.
3. **No Raw Shell Exec**: Use array-based argument parsing to prevent shell injection.
4. **Least Privilege**: Minimal scopes by default. Read-only preferred.
5. **Path Isolation**: Never hardcode user absolute paths. Use placeholder variables like `${AGY_MCP_DIR}`.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Create directory structure in local Agy-MCP repository:
# mkdir -p mcp-blueprints/my-server/schemas
# Use write_to_file to create BLUEPRINT.md and schemas/tools.json
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal or filesystem tools to create directories
# Create mcp-blueprints/<mcp-name>/BLUEPRINT.md
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use filesystem MCP to create directories and write BLUEPRINT.md and schemas/tools.json
await filesystem.createDirectory("mcp-blueprints/my-mcp");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```bash
# Guide user step-by-step using standard commands:
mkdir -p mcp-blueprints/my-mcp/schemas
# Save BLUEPRINT.md and schemas/tools.json into the created directory
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate the contents of `BLUEPRINT.md` and `schemas/tools.json`.
2. Ask user to create the folder structure manually.
3. Instruct user to save the files in their respective destinations and confirm the result.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Create directories | `create_directory()` / `write_to_file()` | Ask user to create directory manually |
| Validate JSON Schema | Local schema validation libraries | Validate syntax via AI reasoning |
| Git deployment | `git commit` / `git push` | Provide git commands for user to run |

---

## ✅ Verification

- The JSON Schema passes validation without syntax errors.
- `BLUEPRINT.md` covers the 6 required architectural and security sections.
- No absolute local host paths are present.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.1.0
