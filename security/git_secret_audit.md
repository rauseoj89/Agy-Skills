# Git Secret Audit & Sanitization Skill 🛡️

This skill instructs the AI agent on how to run security audits on local Git repositories to detect tracked credentials, analyze `.gitignore` files, and safely purge sensitive files (like `.env` or configurations) from Git history without affecting local instances.

---

## 🛠️ WORKFLOW DIRECTIVES

### 1. Audit Phase (Detection)
* **Check `.gitignore` completeness:** Ensure `.env`, `config.php`, `id_rsa`, `*.key`, and `dist/` are defined.
* **Scan for tracked secrets:**
  ```powershell
  # List all tracked files matching secret naming patterns
  git ls-files | Where-Object { $_ -match "\.env|\.key|\.pem|id_rsa|\.db|\.sqlite|config\.php$" }
  ```

### 2. Sanitization Phase (Untracking Files)
If a secret file (like `.env`) is tracked despite being in `.gitignore`:
* **Untrack without deleting local files:**
  ```bash
  git rm --cached <filename>
  ```
* **Commit the changes:**
  ```bash
  git commit -m "security: untrack sensitive files and keep local"
  git push origin main
  ```

### 3. History Purging (Severe Exposures)
If a secret was committed and has public history, changing the password is the safest action. To completely wipe the file from the git history locally before pushing:
* **Using Git Filter-Repo:**
  ```bash
  git filter-repo --path <filename> --invert-paths
  ```
