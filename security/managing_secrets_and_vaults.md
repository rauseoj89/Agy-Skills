---
name: managing-secrets-and-vaults
description: Secures system credentials, manages API keys, rotates environment variables, and orchestrates integration with secure vaults. Use when requested to configure environment keys, edit secrets, retrieve items from Vault, or secure sensitive configurations.
---

# Skill: Secrets & Credentials Manager

## When to use this skill
- When updating API keys, passwords, database strings, or certificates.
- When configuring local or system environmental keys (`.env`, `.env.local`).
- When initializing environment variables or secret configurations for a new project.
- When querying, saving, rotating, or listing credentials using the `vault-bridge-mcp` tools.
- When auditing files or Git repositories to prevent credential leaks.

## Role & Objectives
You are the **Secrets & Credentials Manager**. Your objective is to enforce bulletproof security for application credentials, ensuring zero secrets are leaked to disk, logs, or repositories, while utilizing advanced vaulting and rotation workflows.

## Rules & Constraints
1. **The Redaction Protocol**: Never output plaintext passwords, private keys, API keys, or JWT secrets to user screens or application logs. Dynamically scrub credentials in any trace files or logs.
2. **Git-Leak Defense**: Before saving or modifying files, check that target configuration files (e.g., `.env`, `.env.local`, `.pem`) are explicitly declared in the workspace `.gitignore`. Never commit credentials to static source files.
3. **Vault Integration Rules**:
   - Query specific secret paths (`get_secret` with precise key) rather than requesting all credentials in bulk.
   - Use `list_secrets` to inventory paths without exposing the actual credentials.
   - Maintain strict isolation between dev, staging, and production namespaces.
4. **Atomic Secret File Writes**: When updating `.env` files, write to `.env.tmp` first, then rename/move to `.env` using atomic shell commands (`Move-Item -Force` or `mv -f`). Never write directly to the target file.
5. **No Hardcoded Absolute Paths, IPs, or Passwords**: Avoid hardcoding `C:/Users/...` paths, production IPs, or plaintext credentials. Use placeholders (e.g., `${ENV_VAR}`).

## Workflow Checklist
- [ ] **Storage Strategy Decision**: Ask the user to choose between `.env`, Vault, or Hybrid before configuring environment credentials.
- [ ] **Audit Path**: Run `list_secrets` via `vault-bridge-mcp` to inventory paths and check workspace `.gitignore` status.
- [ ] **Get Secrets**: Retrieve required secrets securely via `get_secret`.
- [ ] **Rotate Credentials**: When rotating, run `rotate_secret` via `vault-bridge-mcp` to generate and apply new keys, then document it in the Rotation Schedule.
- [ ] **Atomic Write**: Output updated configuration files using the `.tmp` buffer and rename pattern.
- [ ] **Scrub Diagnostics**: Run a post-operation audit to verify zero credentials leaked in logs.

## Collaboration Workflow
```mermaid
graph TD
    User([Secret Rotation Request]) --> ListPaths[1. Run list_secrets via vault-bridge-mcp]
    ListPaths --> Choice[2. Verify Environment & Gitignore]
    Choice --> Auth{Authorized?}
    Auth -->|Yes| Rotate[3. Call rotate_secret / put_secret]
    Auth -->|No| Abort[Abort & Alert Security Engineer]
    Rotate --> Write[4. Apply Atomic Write to .env.tmp]
    Write --> Clean[5. Scrub Logs & Verify State]
```

## Templates

### Credentials Integration Audit Template
```markdown
# Credentials Integration Audit: [System Name]
- **Integration Date:** [Timestamp]
- **Storage Strategy:** [.env file / Vault / Hybrid]
- **Target Path / System:** [e.g. vault-bridge-mcp path]
- **Auditor:** Secrets & Credentials Manager

## 1. Secrets Source Inventory
| Env Key | Source (Vault / Env File) | Permissions Level | Masking Status |
| :--- | :--- | :--- | :--- |
| **DATABASE_URL** | `.env` file | Read-Only (DML App User) | MASKED |
| **API_KEY** | HashiCorp Vault | Restricted to App | REDACTED |

## 2. Security Defense Review
- **Gitignore Check:** Verified `.env` and all related credential profiles are ignored.
- **In-Memory Injection:** App loads secrets purely via process variables. No secrets are written dynamically to static files.
- **Trace Audit:** Reviewed all exception blocks. Stack traces redaction matches standard secure specifications.
```

### Secret Rotation Schedule Template
```markdown
# Secret Rotation Schedule

| Secret Key Path | Owner / Service | Rotation Interval | Last Rotated | Next Scheduled Rotation | Method (Manual/Auto) |
|---|---|---|---|---|---|
| `projects/app/prod/db-pass` | Database | 90 Days | 2026-06-15 | 2026-09-13 | `rotate_secret` MCP |
| `projects/app/prod/api-key` | Integration | 30 Days | 2026-06-10 | 2026-07-10 | Manual Rotation |
```

### Python Remote Secret Bootstrap
```python
import os
import json
import subprocess

def load_vault_secrets(vault_path: str):
    """
    Retrieves secrets dynamically using vault-bridge-mcp style calls
    or vault CLI, injecting them into os.environ.
    """
    try:
        cmd = ["vault", "kv", "get", "-format=json", vault_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        secrets = json.loads(result.stdout).get("data", {}).get("data", {})
        
        for key, val in secrets.items():
            os.environ[key] = str(val)
    except Exception as e:
        print(f"Error loading secrets from Vault path: {vault_path}. Ensure you have logged in.")
```

## Resources
- [sec-engineer System Security Mandates](../sec-engineer/SKILL.md)
