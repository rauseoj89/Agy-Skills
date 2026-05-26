---
name: creating-agy-skills
description: Automates the blueprinting, creation, and Git deployment workflow for new or modified Skills inside the Agy-Skills repository. Use when the user requests to create, design, or update a Skill.
---

# Skill: Agy-Skills Creator & Blueprint Automator (creating-agy-skills)

This skill automates the standard workflow for generating and deploying high-quality, security-first operational skill files directly into your local `Agy-Skills` repository.

## When to use this skill
- When the user requests to create a new Skill or modify an existing one.
- When organizing customized system agent behaviors or personas into modular, flat skill files.

---

## 🛠️ Blueprinting & Deployment Workflow

Whenever triggered, you must perform the following actions sequentially and without omission:

### 1. Identify Target Path & Name
- **Category**: Determine the relevant operational category (e.g., `data`, `devops`, `network`, `operations`, `security`).
- **Skill Name**: Standardize in a lowercase, underscore-separated snake_case form (e.g., `deploying_applications`, `auditing_dependencies`).
- **Full Path**: Target `C:/Users/JimmyR/OneDrive/Documentos/Projects/Agy-Skills/<category>/<skill_name>.md`

### 2. Construct the flat Markdown Skill File
Generate the flat `.md` file using the exact structure below:
```markdown
---
name: <hyphen-separated-name>
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
- <Relevant references or local tools>
```

### 3. 🔒 Absolute Security Compliance Verification
- **No Raw Secrets**: Scan the new skill file. Ensure NO passwords, API keys, private keys, or active connection tokens are hardcoded. Use placeholders such as `__VAULT_SECRET_<NAME>__`.
- **Gitignore Check**: Verify that a `.gitignore` exists at the parent repository root (`C:/Users/JimmyR/OneDrive/Documentos/Projects/Agy-Skills/`) and explicitly ignores sensitive files or credentials.

### 4. Update the Index
- Open `C:/Users/JimmyR/OneDrive/Documentos/Projects/Agy-Skills/README.md`.
- Add the new skill under the Domain domain listing in the Directory tree and the **Summarized Skill Index** using the correct category path.

### 5. Automated Git Commit & Push
Once the files are fully written and updated, execute the following shell commands in the target repository to finalize deployment:
```powershell
# Change directory to the repository root
cd "C:/Users/JimmyR/OneDrive/Documentos/Projects/Agy-Skills"

# Stage all files
git add .

# Commit with standard conventional commit message
git commit -m "feat(skill): add blueprint for <skill_name>"

# Push to central hub
git push origin main
```

---

## Validation Checklist
Before declaring success, verify that:
- [ ] The file is created at `C:/Users/JimmyR/OneDrive/Documentos/Projects/Agy-Skills/<category>/<skill_name>.md`.
- [ ] The skill has valid YAML frontmatter containing the matching hyphenated name.
- [ ] The `README.md` index has been updated.
- [ ] Git commit and push command completed without any branch conflicts.
