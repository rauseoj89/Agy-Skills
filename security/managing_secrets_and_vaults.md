---
name: "Managing Secrets and Vaults"
description: "Audits, updates, and integrates credentials and environmental secrets securely using vaults."
category: "generic/security"
tools_required: ["vault-bridge-mcp"]
last_updated: 2026-06-02
---

# 🧠 Skill: Managing Secrets and Vaults

## 🎯 Goal
Audit and configure environment credential systems, ensuring zero secret leakage to version control, while executing secure, atomic integrations with secrets databases and vaults.

## 📊 Inputs Required
- System environment variables file (e.g. `.env`, `.env.local`).
- Target credential mapping records.
- Vault bridge configurations (via `vault-bridge-mcp`).

## 🛠️ Step-by-Step Instructions
1. **Env Directory Audit**:
   - Check file existence and confirm the path is explicitly listed in `.gitignore`.
2. **Plain-Text Key Check & Scans**:
   - Search source layouts for hardcoded credentials, keys, or API tokens. Flag them for immediate integration with environment variables.
3. **Vault Integration & Least Privilege**:
   - Query specific secret paths (e.g., `get_secret` with a precise key) rather than requesting all credentials in bulk.
   - Maintain strict separation between dev, staging, and production namespaces in your secrets vault.
4. **Atomic Secret Writes**:
   - When writing or rotating secrets to disk (e.g., updating `.env` files), write to a temporary file buffer (`.env.tmp`) first and rename atomically (`Move-Item -Force` or `mv -f`) to prevent corruption during process crashes.
5. **Rotation & Script Hardening**:
   - Ensure rotation scripts contain no production private IPs (use `${TARGET_HOST}` or `${VAULT_HOST}`).
   - Force all rotation scripts to use array-based subprocess invocations to prevent command injection via malformed secret values.

## 🛡️ Verification & Security Checklist
1. **Redaction Check**: Confirm all keys, passwords, and tokens are fully replaced by masking patterns (`********`) in outputs.
2. **Atomic Verification**: Confirm that environment files were updated using the temporary buffer and rename workflow.
3. **Git Check**: Verify that target secret directories are excluded in git commits.
4. **Data Protection**: Ensure no credentials are written to flat disk files outside of runtime memory spaces.

---
*Created by Efficiency Core*
