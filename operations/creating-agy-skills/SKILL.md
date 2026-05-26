---
name: creating-agy-skills
description: Automates the blueprinting, creation, and Git deployment workflow for new or modified Skills inside the Agy-Skills repository. Use when the user requests to create, design, or update a Skill.
---

# Skill: Agy-Skills Creator & Blueprint Automator (creating-agy-skills)

This skill automates the standard workflow for generating and deploying high-quality, structured operational skills to your local `Agy-Skills` repository.

## When to use this skill
- When the user requests to create a new Skill or modify an existing one.
- When organizing customized system agent behaviors or personas into modular skill directories.

---

## 🛠️ Blueprinting & Deployment Workflow

Whenever triggered, you must perform the following actions sequentially and without omission:

### 1. Identify Target Path & Name
- **Category**: Determine the relevant operational category (e.g., `system`, `coding`, `security`, `ops`, `qa`).
- **Skill Name**: Standardize in a lowercase, hyphen-separated gerund form (e.g., `deploying-applications`, `auditing-dependencies`).
- **Full Path**: Target `C:/Users/JimmyR/OneDrive/Documentos/Projects/Agy-Skills/<category>/<skill-name>/`

### 2. Create the Directory Structure
Create the required directory hierarchy. Ensure all forward slashes `/` are used when managing paths:
- `<skill-name>/` (Root)
  - `SKILL.md` (Main instructions and rules)
  - `scripts/` (Optional: helper scripts or CLI configurations)
  - `examples/` (Optional: reference templates or demos)

### 3. Construct the `SKILL.md`
Generate `SKILL.md` using the exact structure below:
```markdown
---
name: <gerund-name>
description: <3rd-person description including clear keywords and triggers. Max 1024 chars>
---

# Skill: <Skill Title>

## When to use this skill
- <Trigger criteria 1>
- <Trigger criteria 2>

## Mandatory Rules & Guidelines
- <Crucial guardrails, performance constraints, or operational rules>

## Automation Workflows
- <Checklists, SOPs, or validation steps>
- <Command line invocations or script executions>

## Resources
- [Link to scripts/ or resources/]
```

### 4. 🔒 Absolute Security Compliance Verification
- **No Raw Secrets**: Scan the new `SKILL.md` and any scripts. Ensure NO passwords, API keys, private keys, or active connection tokens are hardcoded. Use placeholders such as `__VAULT_SECRET_<NAME>__`.
- **Gitignore Check**: Verify that a `.gitignore` exists at the parent repository root (`C:/Users/JimmyR/OneDrive/Documentos/Projects/Agy-Skills/`) and explicitly ignores sensitive files or credentials.

### 5. Automated Git Commit & Push
Once the files are fully written, execute the following shell commands in the target repository to finalize deployment:
```powershell
# Change directory to the repository root
cd "C:/Users/JimmyR/OneDrive/Documentos/Projects/Agy-Skills"

# Stage all files
git add .

# Commit with standard conventional commit message
git commit -m "feat(skill): add blueprint for <skill-name>"

# Push to central hub
git push origin main
```

---

## Validation Checklist
Before declaring success, verify that:
- [ ] The folder is created at `C:/Users/JimmyR/OneDrive/Documentos/Projects/Agy-Skills/<category>/<skill-name>/`.
- [ ] `SKILL.md` has valid YAML frontmatter containing the matching gerund name.
- [ ] Git commit and push command completed without any branch conflicts.
