# Hardened Python Security Directives

When writing, generating, or auditing Python code, the following security standards must be strictly enforced:

### 1. Zero-Trust SQL Parameterization & ORM Usage
Concatenating strings into SQL queries introduces critical SQL injection risks.
- **Raw Queries (DB-API 2.0):** Use parameter placeholders provided by the connector. Never construct SQL via `format()`, f-strings, or `%` operators:
  ```python
  # CORRECT:
  cursor.execute("SELECT id, email FROM users WHERE id = %s", (user_id,))
  ```
- **ORM Auditing (SQLAlchemy / Django):** Use ORM-provided query methods (e.g., `session.query(User).filter_by(id=user_id)`) which parameterize by default.
  - If using raw SQL constructs (e.g., `text()` in SQLAlchemy), always bind parameters using `:name`:
    ```python
    # CORRECT:
    session.execute(text("SELECT id FROM users WHERE status = :status"), {"status": active_status})
    ```

### 2. XSS Prevention & Safe Templating
- **Jinja2 Auto-escaping:** Ensure auto-escaping is explicitly configured for templating systems:
  ```python
  from jinja2 import Environment, select_autoescape
  env = Environment(autoescape=select_autoescape(['html', 'xml']))
  ```
- **Markdown & Rich Content Sanitization:** If the application renders user-supplied Markdown (e.g., blog posts), use a safe rendering pipeline:
  1. Convert Markdown to HTML using a robust library (e.g., `markdown` or `mistune`).
  2. Parse the output HTML through a second-layer sanitizer like **Bleach** to whitelist safe tags (`p`, `strong`, `em`, `a`, `ul`, `li`) and strip unsafe tags (`script`, `iframe`, `onload` attributes):
     ```python
     import bleach
     allowed_tags = ['p', 'a', 'strong', 'em', 'ul', 'li', 'h1', 'h2', 'pre', 'code']
     allowed_attrs = {'a': ['href', 'title', 'rel']}
     clean_html = bleach.clean(raw_html, tags=allowed_tags, attributes=allowed_attrs, strip=True)
     ```

### 3. Password Hashing & Secret Generation
- **Hashing Algorithm:** Use **Argon2id** via the `argon2-cffi` library for all password hashing:
  ```python
  from argon2 import PasswordHasher
  ph = PasswordHasher()
  hash_val = ph.hash("user_password")
  # Verification
  ph.verify(hash_val, "user_password")
  ```
  *Rule:* Never use legacy hashes (MD5, SHA1, plain SHA256) for password storage.
- **Cryptographic Randomness:** For security keys, CSRF tokens, session IDs, and reset tokens, use the `secrets` module:
  ```python
  import secrets
  token = secrets.token_urlsafe(32)
  ```
  *Rule:* Never use the `random` module for generating security credentials.

### 4. Session & Identity Hardening
- **Secure Cookie Flags:** Configure application session cookies securely:
  ```python
  # Flask example
  app.config.update(
      SESSION_COOKIE_HTTPONLY=True,
      SESSION_COOKIE_SECURE=True,
      SESSION_COOKIE_SAMESITE='Lax'
  )
  ```
- **Session Pinning & Regeneration:**
  - Regenerate session keys upon login to prevent Session Fixation.
  - Pin the user's agent and IP subnet at login; destroy the session if a sudden discrepancy is detected.

### 5. Secure File Uploads
- **MIME Verification:** Never trust the extension provided by the client. Always verify the actual file headers using a library like `python-magic`:
  ```python
  import magic
  mime_type = magic.from_buffer(uploaded_file.read(1024), mime=True)
  if mime_type not in ['image/jpeg', 'image/png']:
      raise ValueError("Invalid file format")
  ```
- **Storage and Naming:** Rename uploaded files to random UUID strings (e.g., `uuid.uuid4().hex`) and save them outside of the application's executable root in an execution-disabled directory (e.g., S3 or blocked filesystem).

### 6. Audit Logging & Debug Configurations
- **Production Settings:** Ensure `debug` mode is set to `False` in production (e.g., `DEBUG = False` in Django/Flask). Live tracebacks reveal environment variables and database table names.
- **PII Redaction:** Implement filters in your logging configuration to prevent logging of sensitive parameters (passwords, social security numbers, bank details).
- **Request Traceability:** Inject a unique UUID in log outputs using a ContextVar or logging filter to correlate actions originating from the same HTTP request:
  ```python
  import contextvars
  request_id = contextvars.ContextVar('request_id', default='')
  ```

### 7. Destructive Operations Guard
Any Python script or automation that performs irreversible operations must include an explicit user confirmation step before execution. This applies to:

- **Database operations:** `DROP TABLE`, `TRUNCATE`, `DELETE FROM` without a `WHERE` clause
- **Filesystem operations:** `shutil.rmtree()`, `os.remove()` on critical paths, bulk file deletion
- **Credential operations:** Password rotation, API key deletion, certificate revocation
- **Service operations:** Stopping production services, flushing caches

**Required confirmation pattern:**
```python
import sys

def confirm_destructive_action(description: str, command: str) -> bool:
    """Prompt user before executing any destructive operation."""
    print(f"\n⚠️  DESTRUCTIVE OPERATION DETECTED")
    print(f"Action: {description}")
    print(f"Command: {command}")
    print(f"This action is IRREVERSIBLE.")
    response = input("Type 'CONFIRM' to proceed or press Enter to abort: ").strip()
    return response == 'CONFIRM'

# Usage example
if confirm_destructive_action(
    description="Delete all records from the sessions table",
    command="DELETE FROM public.sessions"
):
    cursor.execute("DELETE FROM public.sessions")
else:
    print("Operation aborted by user.")
    sys.exit(0)
```
*Rule:* Automated scripts (e.g., cron jobs or CI pipelines) that perform destructive operations must require a `--force-destructive` flag passed explicitly at runtime — never execute silently by default.
