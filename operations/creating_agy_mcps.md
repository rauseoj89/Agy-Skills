---
name: creating-agy-mcps
description: Automates the blueprinting, structural setup, and Git deployment workflow for new or modified Model Context Protocol (MCP) servers in the Agy-MCP repository. Use when the user requests to create or modify an MCP server.
version: 1.2.0
tags: [universal, operations, mcp, blueprint]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Agy-MCP Blueprint Automator

## 🎯 Objective

Automate the blueprinting, structure generation, and deployment of custom Model Context Protocol (MCP) servers inside the Agy-MCP repository, while strictly maintaining security, path isolation, least privilege, verified package supply chains, and input validation.

## 🕒 When to Use

- When designing, creating, or modifying MCP server blueprints.
- When creating custom integrations connecting external APIs or databases with the agent workspace.

## 🛡️ Universal Principles

1. **No Hardcoded Secrets**: Use placeholders like `${VAULT_SECRET_<MCP-NAME>_<KEY>}`.
2. **No Production IPs**: Use `${TARGET_HOST}` or `localhost` in configurations.
3. **No Raw Shell Exec**: Use array-based argument parsing to prevent shell injection.
4. **Least Privilege**: Minimal scopes by default. Read-only preferred.
5. **Path Isolation**: Never hardcode user absolute paths. Use placeholder variables like `${WORKSPACE_PATH}`.
6. **Verified Packages Only**: Every package referenced in deployment snippets MUST exist on live npm or PyPI registries, must not be deprecated, and must not resolve to a security placeholder (`0.0.1-security`).
7. **Schema as Source of Truth**: All tool names, parameters, and counts in `BLUEPRINT.md` and root `README.md` must strictly match `schemas/tools.json`.

---

## 📋 The 6 Required Blueprint Sections

Every `BLUEPRINT.md` created or updated in `Agy-MCP` must contain these 6 exact numbered sections:
1. `## 1. Architectural Overview` — Mermaid diagram mapping Agent -> MCP -> Service/Resource.
2. `## 2. Setup Requirements` — Runtime engines, CLI binaries, verified packages.
3. `## 3. Environment Configuration (.env.example)` — Vault placeholders and configuration keys.
4. `## 4. Least Privilege Design` — Read-only defaults, identifier regex, max row limits, path bounds.
5. `## 5. Atomic Write Strategy` — Atomic `.tmp` buffer writes or read-only declarations.
6. `## 6. Multi-Agent Deployment & Verification Plan` — Concrete configs for Antigravity, Cline/Roo/OpenCode, fallbacks, and a concrete verification tool call.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Create directory structure in local Agy-MCP repository:
# mkdir -p mcp-blueprints/my-server/schemas
# Use write_to_file to create BLUEPRINT.md and schemas/tools.json
# Update root README.md catalog table with exact tool counts
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal or filesystem tools to create directories
# Create mcp-blueprints/<mcp-name>/BLUEPRINT.md
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

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

1. Generate the contents of `BLUEPRINT.md` adhering to the 6 required sections.
2. Generate `schemas/tools.json` with strict JSON schema bounds.
3. Ask user to save files and update root README catalog counts.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Create directories | `create_directory()` / `write_to_file()` | Ask user to create directory manually |
| Validate JSON Schema | Python: `json.load()` | Validate syntax via AI reasoning |
| Check package existence | Terminal: `npm view <pkg>` / `pip index versions <pkg>` | Instruct user to verify on npmjs.com / pypi.org |
| Git deployment | `git commit` / `git push` | Provide git commands for user to run |

---

## ✅ Verification

- The JSON Schema in `schemas/tools.json` parses as valid JSON.
- `BLUEPRINT.md` includes all 6 required sections without omission.
- External packages were verified on npm/PyPI registries.
- Root `README.md` catalog tool count matches `schemas/tools.json` length.
- Zero local absolute machine paths or plaintext secrets exist.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.2.0
