# Hardened Vue & Nuxt Security Directives

When writing, generating, or auditing Vue.js or Nuxt applications, the following security standards must be strictly enforced:

### 1. Vue XSS Safety and `v-html`
Like React, Vue automatically escapes text, but directives like `v-html` bypass it.
- **Rule:** Never use `v-html` with unsanitized user inputs or API dynamic text.
- **Sanitisation:** Use DOMPurify before parsing dynamically.

### 2. Nuxt SSR State and Secrets
Nuxt renders content on the server. If secrets leak into client state, they are exposed in the HTML payload.
- **Rule:** Use `runtimeConfig` and distinguish between public (client-facing) and private keys (server-only):
  ```typescript
  // nuxt.config.ts
  export default defineNuxtConfig({
    runtimeConfig: {
      apiSecret: 'secret_key', // ONLY available on server
      public: {
        apiBase: '/api' // Available on client and server
      }
    }
  })
  ```
