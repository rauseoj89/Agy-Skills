# Hardened Client-Side & Node.js JavaScript Security Directives

When writing, generating, or reviewing JavaScript code, the following standards are non-negotiable to maintain frontend and runtime integrity:

### 1. DOM-Based XSS & Secure Sink Handling
Directly injecting dynamic variables into structural or evaluative APIs can lead to severe DOM XSS. You must strictly control the use of JavaScript data sinks.

- **Prohibited Sinks:**
  - Never write directly to `element.innerHTML`, `element.outerHTML`, or `document.write()`.
  - Never pass raw strings to dynamic evaluation sinks: `eval()`, `new Function()`, `setTimeout(string)`, or `setInterval(string)`.
  - Never dynamically set `location.href` to unvalidated user input, as it can evaluate `javascript:` URIs.
- **Approved Safe Sinks:**
  - For plain text interpolation, use `element.textContent` or `element.innerText`. These inherently treat inputs as data, not markup.
  - For safe attribute assignment, use `element.setAttribute(attr, value)`.
  - For structural changes, use `document.createElement()` and append elements programmatically.
- **Dynamic HTML rendering:** If rendering HTML is unavoidable, the string must be sanitized immediately before insertion using a verified client-side library like **DOMPurify**:
  ```javascript
  const cleanHTML = DOMPurify.sanitize(userInput);
  element.innerHTML = cleanHTML;
  ```

### 2. Trusted Types API Enforcement
In modern browser environments, implement the **Trusted Types** standard to programmatically secure sinks:
- Establish a global security policy for dynamic scripts or HTML generation:
  ```javascript
  if (window.trustedTypes && window.trustedTypes.createPolicy) {
      const escapeHTMLPolicy = window.trustedTypes.createPolicy('myEscapePolicy', {
          createHTML: (string) => DOMPurify.sanitize(string)
      });
      // Usage
      element.innerHTML = escapeHTMLPolicy.createHTML(userInput);
  }
  ```

### 3. Prototype Pollution Mitigation
JavaScript objects inherit properties from the global `Object.prototype`. Unvalidated deep merges or key assignments can lead to property injection (Prototype Pollution).

- **Map Objects:** When using objects strictly as key-value lookups (dictionaries), always initialize them without a prototype to eliminate property inheritance risk:
  ```javascript
  const safeMap = Object.create(null);
  ```
- **Recursive Merging/Cloning:** Always sanitize object keys before performing dynamic merges or deep clones. Ensure keys like `__proto__`, `constructor`, and `prototype` are ignored or blocked:
  ```javascript
  function safeSet(obj, path, value) {
      if (path.includes('__proto__') || path.includes('constructor') || path.includes('prototype')) {
          throw new Error('Prototype Pollution attempt detected.');
      }
      // Proceed with key setting
  }
  ```

### 4. Secure Storage & Credential Handling
Client-side web storage has no access control controls against scripts running on the same origin.
- **Sensitive Secrets:** Never store sensitive details (e.g., JWT access tokens, OAuth refresh tokens, session IDs, personal user identifiers) in `localStorage` or `sessionStorage`, as they are immediately compromised in the event of an XSS vulnerability.
- **Best Practice:** Keep access tokens in memory (e.g., local closure variable) or request them from the server via secure, `HttpOnly`, `Secure`, and `SameSite` cookies.

### 5. Dependency Integrity & CDN Hardening
Loading third-party scripts introduces supply-chain risks.
- **Subresource Integrity (SRI):** Every script tag pointing to a CDN must include a secure SHA hash to guarantee the script has not been tampered with:
  ```html
  <script src="https://cdn.example.com/library-v2.js" 
          integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwGPNE" 
          crossorigin="anonymous"></script>
  ```

### 6. Code Execution Standards
- **Strict Mode:** Always declare `"use strict";` at the top of vanilla scripts, or write in ES6 Modules (which enforce strict mode automatically) to catch silent programming bugs and block unsafe language constructs (such as variable hoisting and binding `this` to global).

### 7. Node.js Destructive Operations Guard
Any Node.js script or automation performing irreversible operations must halt and require explicit user confirmation before execution. This applies to:

- **Filesystem:** `fs.rm()`, `fs.rmdir()`, recursive deletes, overwriting production config files
- **Database:** Schema drops, data truncations, bulk deletes without filters
- **Container management:** Docker teardowns, volume deletions, namespace deletions
- **Credentials:** Secret rotation, token revocation, API key deletion

**Required confirmation pattern (Node.js CLI):**
```javascript
const readline = require('readline');

async function confirmDestructiveAction(description, command) {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    return new Promise((resolve) => {
        console.log('\n⚠️  DESTRUCTIVE OPERATION DETECTED');
        console.log(`Action: ${description}`);
        console.log(`Command: ${command}`);
        console.log('This action is IRREVERSIBLE.');
        rl.question("Type 'CONFIRM' to proceed or press Enter to abort: ", (answer) => {
            rl.close();
            resolve(answer.trim() === 'CONFIRM');
        });
    });
}

// Usage
const confirmed = await confirmDestructiveAction(
    'Remove all files in the /data/uploads directory',
    'fs.rm("/data/uploads", { recursive: true, force: true })'
);
if (confirmed) {
    await fs.rm('/data/uploads', { recursive: true, force: true });
} else {
    console.log('Operation aborted.');
    process.exit(0);
}
```
*Rule:* Never use `--force` or silent flags on destructive operations in automation scripts. Always surface the risk to the operator at runtime.
