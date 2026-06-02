# Hardened Vanilla PHP & PostgreSQL Security Directives

When generating or reviewing code for this project, the following rules are non-negotiable to ensure a secure environment:

### 1. Zero-Trust Data Handling & Validation
- **SQLi:** Use ONLY PDO with prepared statements. Use named placeholders (e.g., `:id`).
- **Postgres Search Path:** Always specify the schema in queries (e.g., `public.users`) or set `SET search_path TO public` immediately after connecting to prevent search-path hijacking.
- **XSS:** All dynamic data rendered in HTML must be escaped via `htmlspecialchars($data, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8')`.
- **Validation:** Always cast IDs to integers `(int)$_GET['id']` and validate formatting (e.g., emails via `filter_var()`).

### 2. Infrastructure & Database Access Control
- **Non-Root Execution:** The application must run as a limited user (e.g., `www-data`).
- **Postgres Least Privilege:** Use a dedicated DB role that does NOT own the tables. Grant ONLY `SELECT`, `INSERT`, `UPDATE` on specific tables. `REVOKE ALL` on system catalogs like `pg_authid`.
- **File Permissions:** Configuration files must be 0600. The Web UI must NOT have write access to the application's source code.
- **Secrets:** Store credentials in environment variables outside the web root.

### 3. Session & Identity Integrity
- **Initialization:** `session_start()` must include `'cookie_httponly' => true`, `'cookie_secure' => true`, and `'cookie_samesite' => 'Lax'`.
- **Session Pinning:** Store `$_SERVER['REMOTE_ADDR']` and `$_SERVER['HTTP_USER_AGENT']` in the session upon login. If these change during a session, destroy it immediately.
- **Fixation:** Call `session_regenerate_id(true)` immediately after every login.

### 4. Password & MFA Handling
- **Hashing:** Use `password_hash($password, PASSWORD_ARGON2ID)` or `PASSWORD_DEFAULT`.
- **MFA Secrets:** If implementing MFA, secrets must be encrypted at rest using a key from environment variables.
- **Prohibited:** Never use MD5, SHA1, or plain text.

### 5. Content Storage & Markdown Security (Blog Posts)
- **Database Storage:** User-generated content (Blog posts, comments) must be stored in the PostgreSQL database (e.g., `TEXT` column), NEVER as files on the server disk. This eliminates Path Traversal and LFI risks.
- **Input Sanitization:** Store the RAW Markdown string in the database using PDO prepared statements. Do not sanitize on input to preserve the author's original formatting.
- **Rendering Pipeline:** When displaying content:
    1. Fetch the raw Markdown from the DB.
    2. Convert to HTML using a library (e.g., `Parsedown`) in **Safe Mode** (escapes raw HTML).
    3. **Mandatory:** Pass the resulting HTML through a second-layer sanitizer (e.g., `HTMLPurifier`) to strip dangerous tags (`<script>`, `<iframe>`) and attributes (`on*`).
- **Output Caching:** For performance, the sanitized HTML may be cached in a separate DB column or cache layer, provided the cache is invalidated whenever the post is edited.

### 6. JavaScript & Frontend Security
- **CSP:** Enforce a Content Security Policy: `Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';`.
- **SRI:** Every external JavaScript or CSS file from a CDN must include a `integrity` (Subresource Integrity) hash.
- **Headers:** Send `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, and `Referrer-Policy: strict-origin-when-cross-origin`.

### 7. File Upload & Resource Security
- **Rule:** Never trust user-provided extensions. Verify actual MIME types using `finfo_file()`.
- **Storage:** Rename files to random strings and store them in an execution-blocked directory (e.g., via `.htaccess` or Nginx config).
- **Rate Limiting:** Implement rate limiting on Login and Post Creation endpoints to prevent brute-force and resource exhaustion.

### 8. Audit Logging & Privacy
- **Errors:** `display_errors = 0` in production. Log to private files.
- **Redaction:** Redact PII (emails, passwords, session IDs) from audit logs.
- **Traceability:** Include a unique Request-ID in every log entry for end-to-end tracing.
