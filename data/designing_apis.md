---
name: designing-apis
description: Designs RESTful and GraphQL API architectures, generates OpenAPI 3.1 specifications, defines endpoint contracts, and establishes versioning strategies. Use when asked to design APIs, write API specs, define endpoint schemas, or plan API versioning.
version: 1.0.0
tags: [universal, api, design, rest, graphql]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: API Architect & Designer

## 🎯 Objective

Design secure, highly performant, and self-documenting API interfaces, establishing contracts, schemas, and version gates before functional code implementation, while strictly complying with OWASP API Security Top 10 (2023) mandates.

## 🕒 When to Use

- When designing API interfaces or HTTP endpoints.
- When creating OpenAPI 3.1 or Swagger specifications.
- When planning API versioning strategies (URI, headers).
- When defining authentication patterns, rate limits, and standard error structures.

## 🛡️ Universal Principles

1. **Security-First Architecture (OWASP API Security Top 10 2023)**:
   - **BOLA & BOPLA Mitigation (API1 / API3):** Server-side authorization checks on both object and property levels.
   - **Authentication (API2):** Bearer Tokens (JWT) or API Keys, never in query parameters.
   - **Resource Consumption Limits (API4):** Strict payload limit (e.g. max 10MB), limit array lengths.
   - **SSRF Protection (API7):** Validate external URL redirects; block loopback/private ranges (RFC 1918).
   - **Shadow API Mitigation (API9):** Version routes (e.g., `/api/v1/`) and deprecate explicitly.
   - **Third-Party Consumption (API10):** Validate third-party API payloads against JSON Schema.
2. **No Hardcoded Server Paths, Passwords, or IPs**: Spec templates must use dynamic parameters (e.g. `${API_BASE_URL}`).
3. **No Unbounded Collections**: Force pagination on all list-returning endpoints.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Write OpenAPI 3.1 specifications and save them in the workspace
# Use the platform's confirmation flow
```

### ▶️ If you are on Hermes Agent:

```python
# Use read_file / write_file to create the schemas
spec_content = read_file(path="openapi.yaml")
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use the filesystem MCP to read and write OpenAPI specifications
const currentSpec = await filesystem.readFile("openapi.yaml");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# If terminal and direct editing tools are unavailable:
# Ask the user to create the schema.graphql or openapi.yaml file
# and provide the full content formatted in code blocks.
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate the complete YAML/JSON content of the API contract.
2. Explain the architecture in detail.
3. Ask the user: "Please save this content into an `openapi.yaml` file".

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Create spec file | `write_to_file()` | Provide code block for user to save |
| Validate YAML/JSON | Run validator in terminal | Ask user to run validator and paste output |

---

## ✅ Verification

- The spec passes OpenAPI 3.1 validation rules without warnings.
- Pagination and limit parameters are implemented on all list endpoints.
- Stacktrace leaks are prevented in standard error schemas.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
