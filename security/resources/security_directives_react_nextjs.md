# Hardened React & Next.js Security Directives

When writing, generating, or auditing React or Next.js applications, the following security standards must be strictly enforced:

### 1. XSS Prevention via DOM Insertion
React escapes variable text inside JSX by default, but escape mechanisms are easily bypassed.
- **Prohibited:** Never use `dangerouslySetInnerHTML` with unsanitized user inputs or API payloads.
- **Approved Safe Pattern:** If raw HTML rendering is absolutely required, parse it with a secure client-side or server-side library like **DOMPurify**:
  ```tsx
  import DOMPurify from 'dompurify';
  
  function SafeHTMLComponent({ rawHtml }) {
      const cleanHtml = DOMPurify.sanitize(rawHtml);
      return <div dangerouslySetInnerHTML={{ __html: cleanHtml }} />;
  }
  ```

### 2. Next.js Server Components & Data Leakage
Next.js React Server Components (RSC) run only on the server, but variables/props passed to Client Components can leak secrets to the client.
- **Rule:** Never pass database connection strings, API keys, or raw system entities containing passwords to Client Components.
- **Enforcement:** Enforce separation of server-only modules using the `server-only` package:
  ```typescript
  // database.ts (Server-only module)
  import 'server-only';
  // If a client component imports this, it triggers a build-time compile error.
  ```
- **Environmental Variable Safety:** Next.js exposes environment variables to the browser *only* if prefixed with `NEXT_PUBLIC_`. Never prefix database credentials or private API keys with `NEXT_PUBLIC_`.

### 3. Server Actions & Input Validation
Next.js Server Actions expose HTTP endpoints under the hood, making them subject to standard parameter tampering and CSRF attacks.
- **Rule:** Treat Server Actions as public API endpoints. Never trust input payloads.
- **Mandatory Validation:** Validate arguments inside Server Actions using a schema library like **Zod**:
  ```typescript
  'use server';
  import { z } from 'zod';

  const ActionSchema = z.object({
      userId: z.string().uuid(),
      amount: z.number().positive(),
  });

  export async function transferFunds(rawInput: unknown) {
      const data = ActionSchema.parse(rawInput); // Server-side schema verification
      // Perform database operations securely...
  }
  ```

### 4. Router Vulnerabilities & URL Injection
Redirects driven by dynamic URL parameters are prone to Open Redirect vulnerabilities.
- **Rule:** Only allow redirects to relative paths or verified whitelist domains.
- **Approved Safe Pattern:**
  ```typescript
  import { redirect } from 'next/navigation';

  export async function handleRedirect(targetUrl: string) {
      // Allow only relative paths (starting with '/')
      if (targetUrl.startsWith('/') && !targetUrl.startsWith('//')) {
          redirect(targetUrl);
      } else {
          redirect('/dashboard'); // Fallback path
      }
  }
  ```
