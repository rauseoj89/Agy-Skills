---
name: git-secret-audit
description: Runs security audits on local Git repositories to detect tracked credentials, analyze .gitignore files, and safely purge secrets from Git history.
version: 1.0.0
tags: [universal, security, git, secrets]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Git Secret Audit & Sanitization

## 🎯 Objective

Run security audits on local Git repositories to detect tracked credentials, analyze `.gitignore` files, and safely purge sensitive files (like `.env` or configurations) from Git history without affecting local instances.

## 🕒 When to Use

- When checking whether secrets were accidentally pushed to remote repositories.
- When verifying and auditing `.gitignore` rules.
- When purging commits from Git history (e.g., using `git rm --cached` or `git filter-repo`).

## 🛡️ Universal Principles

1. **Secrets Sanitization**: Immediately detect and untrack `.env`, keys, certificates, or databases.
2. **Never Force Destructive Git Purges Without Backup**: Git history rewrite commands (like `git filter-repo`) are dangerous and must be confirmed.
3. **No Plaintext Credentials**: Environment configurations must be vaulted, not stored in source code.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Run local Git commands
git ls-files | grep -E "\.env|\.key|\.pem"
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal to run git checks
result = terminal(command="git ls-files", timeout=30)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use git MCP to verify status or shell to list files
const files = await git.git_status();
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide developer in their local terminal:
# Ask: "Run 'git ls-files | grep .env' to check if the file is tracked."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Ask user to run Git commands to list tracked files or inspect status.
2. Analyze reported files.
3. Generate the exact command (`git rm --cached <filename>`) for the user to execute.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| List Git files | `git_status()` / `terminal()` | Ask user to run `git ls-files` |
| Untrack cached file | `terminal("git rm --cached")` | Provide exact command to user |
| Clean history | `terminal("git filter-repo")` | Guide user on using filter-repo or BFG |

---

## ✅ Verification

- The `.env` or sensitive file has been untracked from Git cache.
- The `.gitignore` file contains proper exclusion patterns.
- No references to secrets remain in recent commit history.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
