# Hardened CI/CD Pipeline Security Directives

When creating, updating, or auditing CI/CD configurations, the following security standards must be strictly enforced:

### 1. Pinned Actions and Workflows
Dynamic tag references (e.g., `uses: actions/checkout@v4`) can be mutated by upstream compromises.
- **Rule:** Pin third-party actions to an exact git SHA. Do not rely solely on tag names:
  ```yaml
  # CORRECT:
  uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
  ```

### 2. Secret Masking and Access Control
Exposing passwords or keys to runner output logs is prohibited.
- **Rule:** Never echo credentials to the console.
- **Environment Context:** Pass secrets via environment configurations linked to runners, and use OpenID Connect (OIDC) to federate credentials with Cloud Providers instead of saving long-lived credentials in variables.
