# Hardened HTML & Web Templating Security Directives

When writing, generating, or rendering HTML structures and web templates, the following security standards must be strictly enforced:

### 1. Context-Aware Output Encoding (XSS Mitigation)
Dynamic variables must be escaped specifically for the HTML context in which they are placed. Simple HTML body escaping is insufficient and dangerous when used inside attributes, JavaScript, or URLs.

- **HTML Body Context:**
  - *Sinks:* Between tags (e.g., `<div>$var</div>`).
  - *Standard:* Escape characters: `&` to `&amp;`, `<` to `&lt;`, `>` to `&gt;`, `"` to `&quot;`, `'` to `&#x27;`, `/` to `&#x2F;`.
- **HTML Attribute Context:**
  - *Sinks:* Inside attributes (e.g., `<input value="$var">` or `<div class="$var">`).
  - *Standard:* Always wrap attribute values in double quotes (`"`). Escape all non-alphanumeric characters using hexadecimal entities (`&#xHH;`) to prevent break-outs.
- **URL Context:**
  - *Sinks:* Inside attributes like `href` or `src` (e.g., `<a href="$var">`).
  - *Standard:* Ensure the URI begins with a safe protocol (`https://`, `mailto:`, or relative `/`). Strictly block `javascript:` or `data:` schemes. Percent-encode parameters using URL encoding rules.
- **JavaScript Context inside HTML:**
  - *Sinks:* Inside `<script>` tags or inline event handlers (e.g., `<button onclick="doSomething('$var')">`).
  - *Standard:* **Prohibited.** Never inject dynamic data directly into a JavaScript string context. Instead, use secure HTML `data-*` attributes (e.g., `<div id="data-host" data-value="[escaped-json]">`) and retrieve them using client-side JavaScript via `dataset`.

### 2. Restrictive Content Security Policy (CSP)
Ensure the application declares a strong Content Security Policy via HTTP headers or, if headers are unavailable, through a `<meta>` tag:
- **Default Policy:** `default-src 'self';` (only load resources from the origin).
- **Script Constraints:** `script-src 'self';` (block all inline scripts and `eval()`).
- **Object Constraints:** `object-src 'none';` (completely disable outdated plug-ins like Flash or Java).
- **Inline Scripts (If required):** If inline scripts are unavoidable, they must be validated using a cryptographic nonce (`nonce-t3hP4ssw0rd...`) generated per-request or a SHA-256 hash matching the script body. Never use `'unsafe-inline'` or `'unsafe-eval'`.

### 3. Clickjacking and Framing Defense
Protect the layout from being transparently overlayed in hostile domains:
- **Framing Restriction:** Enforce `frame-ancestors 'none'` or `frame-ancestors 'self'` inside the CSP header.
- **Sandbox Controls:** If rendering third-party widgets or untrusted pages via `<iframe src="...">`, always specify the `sandbox` attribute to restrict permissions:
  ```html
  <iframe src="https://example.com" sandbox="allow-scripts allow-forms" referrerpolicy="no-referrer"></iframe>
  ```
  *Rule:* Never combine `allow-scripts` and `allow-same-origin` inside a sandbox attribute, as it allows the framed document to bypass the sandboxing rules altogether.

### 4. Link & Transport Integrity
- **Reverse Tabnabbing Prevention:** Every outbound link targeting a new window must have `rel="noopener noreferrer"` defined:
  ```html
  <a href="https://external.com" target="_blank" rel="noopener noreferrer">Visit External Site</a>
  ```
- **Referrer Leakage Prevention:** Control what referrer information is sent when navigating away by adding:
  ```html
  <meta name="referrer" content="strict-origin-when-cross-origin">
  ```

### 5. Form Hardening & CSRF Protection
- **HTTPS Enforcement:** The `action` attribute of forms must point to secure `https://` URLs.
- **CSRF Token Injection:** Every state-changing form (`POST`/`PUT`/`DELETE`) must contain a cryptographically secure, random, hidden CSRF token:
  ```html
  <input type="hidden" name="csrf_token" value="c3JmX3Rva2VuX3ZhbHVlX2hlcmU=">
  ```
- **Sensitive Data Exposure:** Sensitive input elements (e.g., passwords, credit card numbers, MFA tokens) must have `autocomplete="off"` or `autocomplete="new-password"` specified to prevent credential caching.
