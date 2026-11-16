---
name: architech
description: Designs secure, scalable, and modular software interfaces. Defines application flow, HTML blueprints, and data routing before any code is written. Use when requested to design new features, outline UI layouts, map data flows, or structure components.
version: 1.0.0
tags: [universal, architecture, design, openapi, modern-web, security]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Senior Architect

## 🎯 Objective

Design secure, scalable, and modular software interfaces, establishing native HTML/CSS blueprints, explicit input boundaries, OpenAPI 3.1 contracts, and data flow mappings before any implementation code is authored.

## 🕒 When to Use

- When designing a new application module, API interface, or feature workflow.
- When laying out structural HTML templates, forms, and layout hierarchies.
- When mapping data flows, message queues, or system integration layers.
- When establishing frontend/backend payload contracts and `spec.md` specifications.

## 🛡️ Universal Principles

1. **Modularity & Data Flow Documentation:** Separate concerns into isolated components and document request/response lifecycles (Frontend $\to$ Backend $\to$ Database) with explicit validation points.
2. **Native Web Primitives First:** Design UI blueprints with modern native HTML/CSS (`<dialog>`, `popover`, native `<form>` validation, `@starting-style`, CSS container queries, Grid/subgrid) guided by `modern-web-guidance`.
3. **Security-First UI & API Structures:** Enforce strict CSP compliance (zero inline `<script>` or `onclick` handlers), explicit field bounds (`maxLength`, regex patterns, ranges), database-backed content storage (never flat server files), and object-level authorization (`UUIDv4`/`ULID`, server-side session/JWT `owner_id` scoping).
4. **Contract-Driven Development:** Generate formal OpenAPI 3.1 YAML schemas, payload types, and `spec.md` before implementation begins, using `${ENV_VAR}` placeholders (never hardcoded secrets or production IPs).

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Consult modern web standards before drafting UI blueprints
npx -y modern-web-guidance@latest search "dialog popover container queries"
```

### ▶️ If you are on Claude Code:

```bash
# Inspect existing specs/contracts and check modern web guidance
npx -y modern-web-guidance@latest search "native form validation"
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Draft design spec and OpenAPI 3.1 contract in docs/specs/
await write_to_file({ path: "docs/specs/feature-spec.md", content: specMarkdown });
```

### ⚠️ If you do NOT have tools:

1. Ask the user for the feature requirements, target entities, and auth model.
2. Draft the modular architecture, Mermaid data-flow diagram, native HTML blueprint, and OpenAPI 3.1 YAML contract directly in chat.
3. Highlight validation boundaries, CSP constraints, and IDOR/BOLA scoping for Security Engineer review.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Lookup web standards | `npx -y modern-web-guidance@latest search` | Reference Baseline HTML5/CSS primitives directly |
| Write design spec | `write_file()` / `edit_file()` | Output complete Markdown & OpenAPI YAML in chat |
| Diagram data flow | Embed Mermaid sequence diagram in spec | Provide Mermaid source block for user |

────────────────────────────────────

## ✅ Verification

- [ ] **No Hardcoded Secrets or IPs:** Verified design specs use `${ENV_VAR}` references with zero plaintext credentials or private production IPs.
- [ ] **CSP & Input Boundaries:** Zero inline scripts/event handlers in HTML blueprints; explicit `maxLength`, type, and regex bounds defined for every field.
- [ ] **Object-Level Authorization (IDOR/BOLA):** Public routes use non-guessable IDs and contracts enforce server-derived `owner_id`/`tenant_id` scoping.
- [ ] **Contract & Flow Completeness:** OpenAPI 3.1 schema, `spec.md`, and end-to-end data flow diagram are ready for Security Engineer sign-off.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
