---
name: "Creating Agy-Skills"
description: "Automates the blueprinting, creation, and Git deployment workflow for new or modified Skills inside the Agy-Skills repository."
category: "generic/operations"
tools_required: ["data-analyst-mcp"]
last_updated: 2026-06-02
---

# 🧠 Skill: Agy-Skills Creator & Blueprint Automator

## 🎯 Goal
Automate the standard blueprinting, formatting, security scanning, and deployment of modular operational skill files directly into the local `Agy-Skills` repository.

## 📊 Inputs Required
- Target skill specifications (name, category, triggers, and checklists).
- Local `Agy-Skills` repository path (`${AGY_SKILLS_DIR}`).

## 🛠️ Step-by-Step Instructions
1. **Identify Target Path & Name**:
   - Determine the category (e.g., `data`, `devops`, `network`, `operations`, `security`).
   - Standardize in snake_case: `${AGY_SKILLS_DIR}/<category>/<skill_name>.md`.
2. **Structure flat Blueprint File**:
   - Generate standard YAML frontmatter (`name`, `description`, `category`, `tools_required`, `last_updated`).
   - Standardize sections: Goal, Inputs Required, Step-by-Step Instructions, Verification & Security Checklist.
3. **Hardened Vanilla Compliance Check**:
   - **No Secrets:** Prevent any plaintext credentials. Use placeholders such as `${VAULT_SECRET_<NAME>}`.
   - **No IPs:** Scan and remove any private production IP subnets. Use `${TARGET_HOST}` or `localhost`.
   - **No Raw Shell Exec:** Format all command blocks to use array-based parameter definitions, never raw concatenated shell executions.
4. **Update Index**:
   - Append the new skill to both the Directory Tree and the Summarized Skill Index in `${AGY_SKILLS_DIR}/README.md`.
5. **Git Commit & Push**:
   - Run git staging, commit using conventional style (`feat(skill): add blueprint for <skill_name>`), and push to the central hub.

## 🛡️ Verification & Security Checklist
1. **Gitignore Status**: Verify all `.env` files and system-specific files are ignored.
2. **Secrets Scan**: Ensure absolutely zero plain-text secrets or production private IPs appear in the blueprint.
3. **Index Updated**: Confirm the README matches the newly added skill.
4. **Clean Commits**: Ensure Git push resolves without conflicts.

---
*Created by Efficiency Core*
