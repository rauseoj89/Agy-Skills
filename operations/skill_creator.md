---
name: skill-creator
description: "Authors and standardizes new local agent skills (SKILL.md directories, YAML frontmatter, scripts, and resources) in Central-Brain or local agent skill folders. Use when asked to design or create a new skill (use creating-agy-skills for Agy-Skills repo deployment)."
version: 1.0.0
tags: [universal, operations, meta, skill-authoring, standards]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Skill Creator

## 🎯 Objective

Standardize and generate modular agent skills with compliant YAML frontmatter, folder hierarchy (`SKILL.md`, `scripts/`, `examples/`, `resources/`), POSIX paths, and security-hardened templates.

## 🕒 When to Use

- When designing a new operational skill or updating an existing `SKILL.md`.
- When organizing custom agent behaviors or personas into discoverable skill directories.
- When auditing skill frontmatter, structure, and security compliance.

## 🛡️ Universal Principles

1. **Standard Folder Hierarchy:** Every skill directory `<skill-name>/` requires `SKILL.md` and may include optional `scripts/`, `examples/`, and `resources/` subdirectories.
2. **YAML Frontmatter Compliance:** Start `SKILL.md` with `name` (lowercase, numbers, hyphens only, max 64 chars) and `description` (3rd-person with clear trigger keywords, max 1024 chars).
3. **POSIX Paths & Placeholders:** Always use forward slashes (`/`) and placeholders (`${SKILLS_DIR}`, `${ENV_VAR}`)—never hardcode user home paths or OS-specific backslashes.
4. **Security Mandates:** All templates and examples must contain zero hardcoded secrets, zero production IPs, and zero raw concatenated shell execution patterns.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Scaffold a new skill directory and validate structure
mkdir -p "${SKILLS_DIR}/<skill-name>"
```

### ▶️ If you are on Claude Code:

```bash
# Create SKILL.md using standardized YAML frontmatter and inspect discovery
ls -la "${SKILLS_DIR}/<skill-name>/SKILL.md"
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Write new SKILL.md from the standard template
await write_to_file({ path: "skills/<skill-name>/SKILL.md", content: skillTemplate });
```

### ⚠️ If you do NOT have tools:

1. Ask the user for the skill's purpose, trigger keywords, and required tools/constraints.
2. Draft the complete `SKILL.md` with valid YAML frontmatter, rules, workflow checklist, Mermaid diagram, and templates.
3. Provide the `mkdir` command and target relative path for the user to save it.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Create skill folder | `mkdir -p` + `write_file()` | Output full `SKILL.md` and directory layout in chat |
| Validate frontmatter | Inspect YAML `name` and `description` | Verify character limits and kebab-case manually |
| Security review | Scan for secrets, IPs, and absolute paths | Audit template lines before presenting |

────────────────────────────────────

## ✅ Verification

- [ ] **No Hardcoded Secrets or IPs:** Confirmed zero credentials, tokens, or private IPs exist in templates or examples.
- [ ] **Frontmatter Valid:** `name` is kebab-case ($\le 64$ chars) and `description` is 3rd-person with triggers ($\le 1024$ chars).
- [ ] **Path Isolation:** Zero hardcoded local user paths; all paths use forward slashes and `${SKILLS_DIR}` placeholders.
- [ ] **Complete Structure:** Includes When to Use, Rules & Constraints, Workflow Checklist, Templates, and Resources.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
