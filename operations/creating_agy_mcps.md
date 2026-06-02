---
name: "Creating Agy-MCPs"
description: "Automates the blueprinting, structural setup, and Git deployment workflow for new or modified Model Context Protocol (MCP) servers."
category: "generic/operations"
tools_required: ["data-analyst-mcp"]
last_updated: 2026-06-02
---

# 🧠 Skill: Agy-MCP Blueprint Automator

## 🎯 Goal
Automate the standard blueprinting, directory structuring, security auditing, and Git deployment pipeline for custom Model Context Protocol (MCP) servers.

## 📊 Inputs Required
- Target MCP server specifications (tools, APIs, and databases).
- Local `Agy-MCP` repository path (`C:\Users\JimmyR\OneDrive\Documentos\Projects\Agy-MCP`).

## 🛠️ Step-by-Step Instructions
1. **Identify Target Path & Name**:
   - Standardize target folder path in lowercase and hyphenated snake_case format: `C:\Users\JimmyR\OneDrive\Documentos\Projects\Agy-MCP\mcp-blueprints\<mcp-name>\`.
2. **Create Directory Structure**:
   - Establish `BLUEPRINT.md` (root architectural details, setup, and tool schemas).
   - Establish `schemas/` folder (JSON tool schemas) and `templates/` folder (boilerplate configuration templates).
3. **Construct BLUEPRINT.md & Schemas**:
   - Define architectural overview with Mermaid flowchart mappings.
   - Outline system requirements, package dependencies, and docker spec files.
   - Construct `.env.example` using strictly vault-aligned variable placeholders.
4. **Hardened Vanilla Compliance Check**:
   - **No Secrets:** Ensure NO live production API keys, passwords, or tokens are written into `BLUEPRINT.md` or `.env.example`. Use `${VAULT_SECRET_<MCP-NAME>_<KEY>}` structure.
   - **No IPs:** Ensure no production private IPs are hardcoded. Use `${TARGET_HOST}` or `localhost` as placeholders.
   - **No Raw Shell Exec:** Command examples must utilize array-based parameters, not raw shell strings.
5. **Git Commit & Push**:
   - Execute git staging, commit using conventional style (`feat(mcp-bp): add blueprint for <mcp-name>`), and push.

## 🛡️ Verification & Security Checklist
1. **Gitignore Verification**: Ensure `.env` and `node_modules` are excluded at the MCP repository root.
2. **Secrets Sanity**: Verify that zero plain-text production passwords or active tokens are written.
3. **Mermaid & Schema Validity**: Ensure that Mermaid diagrams render correctly and that all JSON schemas are well-formed.
4. **Clean Deployment**: Verify that git push completes successfully without conflicts.

---
*Created by Efficiency Core*
