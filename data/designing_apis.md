---
name: "Designing APIs"
description: "Establishes RESTful/GraphQL endpoint architectures, generates OpenAPI 3.1 specifications, and designs auth models."
category: "generic/data"
tools_required: []
last_updated: 2026-06-15
---

# 🧠 Skill: API Architect & Designer

## 🎯 Goal
Design clean, secure, and self-documenting HTTP API structures, endpoint verifications, and schemas using standard OpenAPI 3.1 YAML specifications.

## 📊 Inputs Required
- System functional resource specifications.
- Required authentication and rate limiting requirements.

## 🛠️ Step-by-Step Instructions
1. **RESTful Resource Scoping**:
   - Classify entities into logical plural endpoints (e.g. `/api/v1/users`).
   - Map standard HTTP verbs (`GET`, `POST`, `PUT`, `DELETE`) to matching lifecycle events.
2. **OpenAPI 3.1 Spec Writing**:
   - Establish API specifications detailing endpoints, parameters, request body models, and HTTP response codes.
   - Enforce explicit boundaries (e.g. `maxLength`, `pattern`, `minimum`) on all parameters.
3. **Endpoint Security Architecture**:
   - Enforce Bearer Tokens (JWT) or API Keys. Never permit credentials inside URL query parameters.
   - Standardize error payloads to return generic reference messages containing unique UUID error codes.
4. **Versioning & Limits Planning**:
   - Prepend route namespaces with `/api/v1/`.
   - Document client rate-limiting rules (e.g. maximum 100 requests/minute per client).

## 🛡️ Verification & Security Checklist
1. **Validation Boundaries**: Verify that all parameters have strict length, pattern, and type limits declared.
2. **Auth Protocol**: Ensure that authorization headers are defined exclusively over HTTPS.
3. **Redacted Errors**: Verify that error models redact system tracebacks or database columns.

---
*Created by Efficiency Core*
