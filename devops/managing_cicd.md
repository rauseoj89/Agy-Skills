---
name: managing-cicd
description: Designs, configures, and maintains CI/CD pipelines for automated build, test, and deployment workflows. Supports GitHub Actions, GitLab CI, and Docker-based pipelines. Use when asked to set up automated builds, configure deployment pipelines, create workflow files, or automate release processes.
version: 1.0.0
tags: [universal, devops, cicd, deployment]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: CI/CD Pipeline Specialist

## 🎯 Objective

Design secure, efficient, and robust pipelines, ensuring that all code is validated, compiled, and deployed using least-privilege runners, keyless OIDC authentication, and encrypted secret mappings while preventing Poisoned Pipeline Execution (PPE).

## 🕒 When to Use

- When structuring automated build, test, and deployment workflows.
- When creating or modifying pipeline configuration files (e.g., `.github/workflows/main.yml`, `.gitlab-ci.yml`).
- When configuring multi-environment deployments (dev, staging, production).
- When integrating SAST/SCA dependency and vulnerability scanning into pipelines.

## 🛡️ Universal Principles

1. **Poisoned Pipeline Execution (PPE) Prevention (CICD-SEC-4):** Force branch protection rules. Avoid running forks with write access or access to secrets.
2. **Least Privilege Identity & Access (CICD-SEC-2):** Restrict runner token permissions by default. Pin third-party steps to static SHA hashes.
3. **No Hardcoded Secrets**: Inject credentials at runtime via environment variables or vault keys.
4. **Vulnerability Scanning**: Automatically run dependency auditing and static analysis inside the pipeline.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Execute local YAML verification checks
# Commit and push changes to git repository
```

### ▶️ If you are on Hermes Agent:

```python
# Modify pipeline files using editing tools
workflow_data = read_file(path=".github/workflows/main.yml")
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use filesystem MCP to update the CI/CD workflow file
await filesystem.writeFile(".github/workflows/deploy.yml", yamlContent);
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Ask user to configure repository secrets in platform settings:
# "Add the API_KEY secret in the GitHub/GitLab repository settings."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate the complete CI/CD YAML configuration.
2. Ask the user: "Create the `.github/workflows/deploy.yml` file and paste this content".
3. Provide instructions on configuring secrets manually via the provider's web UI.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Create workflow file | `write_to_file()` | Display YAML in chat for user to save |
| Configure secrets | Use repo configuration tools | Instruct user to configure secrets in platform UI |
| Execute pipeline locally | `terminal()` with `act` or similar | Ask user to commit and push to validate remotely |

---

## ✅ Verification

- CI/CD workflow has cancellation of outdated builds enabled (concurrency).
- Runners are configured with read-only permissions by default.
- No plaintext secrets exist in workflow definitions.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
