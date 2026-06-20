---
name: creating-agy-skills
description: Automates the blueprinting, creation, and Git deployment workflow for new or modified Skills inside the Agy-Skills repository. Use when the user requests to create, design, or update a Skill.
category: "generic/operations"
tools_required: []
last_updated: 2026-06-19
---

# Skill: Agy-Skills Creator

## Goal
Automate the creation, blueprinting, indexing, and Git deployment of custom operational skill files inside the external `Agy-Skills` repository while enforcing absolute security, standardized formatting, and local synchronization.

## MCP vs Native Fallback

| Capability | With filesystem/git MCPs | Without MCP (Native) |
|---|---|---|
| Read/Write files | Use MCP file write tools | Use native Read/Write file tools |
| Git operations | Use git MCP tools | PowerShell: run git commands directly |

---

## When to use this skill
- When the user requests to create a new Skill or modify an existing one in the external Agy-Skills repository.
- When organizing customized system agent behaviors or personas into modular, flat skill files in the central skills repository.

## Rules & Constraints
1. **Absolute Security Compliance (Hardened Vanilla)**:
   - **No Hardcoded Secrets**: Ensure NO passwords, API keys, private keys, SNMP strings, or active connection tokens are hardcoded. Use environment variables: `${VAULT_SECRET_<NAME>}` or Vault Bridge references.
   - **No Production IPs**: Ensure no `192.168.x.x`, `10.x.x.x`, or `172.16-31.x.x` subnets appear in examples. Use `${TARGET_HOST}` or `localhost`.
   - **No Raw Shell Exec**: Ensure all command examples use array-based argument patterns, not raw string concatenation.
2. **Security Checklist Standards**:
   - Every skill must have a verification checklist with a minimum of 4 items.
   - The first checklist item must be secrets-related (e.g., verifying zero credentials exist in the codebase, logs, or outputs).
   - Any skill that contains destructive operations (deleting resources, formatting, dropping tables/databases, or stopping critical services) must have a dedicated "Destructive Gate" checklist item.
3. **Standardized Fallbacks**:
   - Any skill that specifies a non-empty `tools_required` parameter must contain a dedicated `MCP vs Native Fallback` section outlining how the capability is fulfilled if the MCP is absent.
4. **Path Isolation**: Never hardcode absolute path strings (like `C:/Users/...`). Use placeholders such as `${AGY_SKILLS_DIR}` or relative paths.
5. **Gitignore Check**: Verify that a `.gitignore` exists at the parent repository root and explicitly ignores sensitive files, `.env` files, and credentials.

## Workflow Checklist
- [ ] **Identify Target Path & Name**: Determine the relevant operational category (e.g., `data`, `devops`, `operations`). Standardize the skill name in lowercase, snake_case (e.g., `deploying_applications`). Set the target path to `${AGY_SKILLS_DIR}/<category>/<skill-name>.md`.
- [ ] **Construct Flat Markdown Skill**: Generate the `.md` file using the exact structure below.
- [ ] **Audit Security & Checklist Standards**: Verify that zero credentials, IPs, or absolute paths leak in the code or examples. Confirm that checklist requirements (secrets check, minimum 4 items, destructive gates) are met.
- [ ] **Update Index**: Open `${AGY_SKILLS_DIR}/README.md` and add the new skill under the correct category domain listing and the Summarized Skill Index.
- [ ] **Local Sync**: Immediately copy the new skill to the local agent execution directory at `~/.gemini/antigravity/skills/<name>/SKILL.md` (or the equivalent local active skills folder) to ensure the current session is immediately updated.
- [ ] **Git Deploy**: Stage, commit, and push the changes to the central repository.

## Collaboration Workflow
```mermaid
graph TD
    User([User Request]) --> AB[Identify Target Path & Category]
    AB --> CS[Construct Flat Skill MD]
    CS --> SEC[Security & Fallback Audit]
    SEC --> LS[Local Sync to Agent Folder]
    LS --> UI[Update README.md Index]
    UI --> Git[Commit & Push to ${AGY_SKILLS_DIR}]
```

## Templates

### Flat Markdown Skill Template
```markdown
---
name: <hyphen-separated-name>
description: <3rd-person description including clear keywords and triggers. Max 1024 chars>
category: "generic/<domain>"
tools_required: [<required-mcps-if-any>]
last_updated: <YYYY-MM-DD>
---

# Skill: <Skill Title>

## Goal
<Brief description of what the skill accomplishes.>

## MCP vs Native Fallback
<Only required if tools_required is not empty. Outline tools used vs manual/native fallbacks.>

---

## When to use this skill
- <Trigger criteria 1>
- <Trigger criteria 2>

## Rules & Constraints
- <Crucial guardrails, performance constraints, or operational rules>

## Workflow Checklist
- [ ] <Checklists, SOPs, or validation steps>
- [ ] <Command line invocations or script executions>

## Verification & Security Checklist
1. **No Hardcoded Secrets**: Confirmed zero credentials, keys, or connection strings are present.
2. <Checklist item 2>
3. <Checklist item 3>
4. <Checklist item 4 (e.g. Destructive Gate if applicable)>

## Resources
- <Relevant references or local tools>
```

### Git Deployment Commands
```powershell
# Change directory to the repository root
cd "${AGY_SKILLS_DIR}"

# Stage all files
git add .

# Commit with standard conventional commit message
git commit -m "feat(skill): add blueprint for <skill_name>"

# Push to central hub
git push origin main
```

## Resources
- [sec-engineer System Security Mandates](../sec-engineer/SKILL.md)
