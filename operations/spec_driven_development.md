---
name: spec-driven-development
description: Enforces Specification-Driven Development (SDD). Use when building new features, modules, or services. Guides the agent through formal spec authoring (spec.md), technical planning (plan.md), task matrix generation (tasks.md), and incremental code convergence.
version: 1.1.0
tags: [universal, engineering, operations, sdd, spec-kit, planning, architecture]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-11-14
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Specification-Driven Development (SDD)

## 🎯 Objective

Eliminate agent drift, hallucinated assumptions, and unverified code generation by enforcing GitHub's Spec-Kit methodology: carrying every feature request through a formal progression of `spec.md` $\rightarrow$ `plan.md` $\rightarrow$ `tasks.md` before authoring implementation code.

## 🕒 When to Use

- When tackling non-trivial requirements (>1 file or structural/architectural changes).
- When designing or creating new components, APIs, contracts, or microservices.
- When a request is ambiguous and requires scope clarification prior to programming.
- To prevent scope-creep by explicitly defining what is "Out of Scope".

## 🛡️ Universal Principles

1. **Contracts Before Code:** Define data schemas, TypeScript interfaces, or OpenAPI 3.1 specifications before authoring business logic.
2. **Deterministic Triad Progression:** All structured development follows:
   - `spec.md`: Defines the **WHAT** (User stories, Acceptance Criteria with Gherkin, Out of Scope).
   - `plan.md`: Defines the **HOW** (Architecture, flowcharts, data models, contracts). When planning web interfaces, search Google Chrome's `modern-web-guidance` (`npx -y modern-web-guidance@latest search "<query>"`) to baseline UI patterns against native platform capabilities (`<dialog>`, `popover`, container queries, modern forms) rather than third-party dependencies.
   - `tasks.md`: Defines the **STEPS** (Ordered matrix of atomic phases with dependent checkboxes).
3. **No Code Drift:** Do not jump directly into modifying code without aligned and approved plan and contracts.
4. **Incremental Convergence:** Implement and verify phase-by-phase, checking off tasks in `tasks.md` only after verifying working functionality.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Create specifications directory and validate task structure
mkdir -p specs/feature-name
# Write spec.md, plan.md, tasks.md
```

### ▶️ If you are on Hermes Agent:

```python
# Write technical plan and task matrix
with open("plan.md", "w") as f:
    f.write("# Implementation Plan...")
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use file tools to establish the spec.md -> plan.md -> tasks.md progression
await writeFile("specs/spec.md", specContent);
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Propose plan to user before modifying production files:
# "I have drafted the specification and technical plan. Please review and approve before we begin."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Draft `spec.md` (User stories in Gherkin format + Acceptance Criteria) directly in the chat.
2. Design `plan.md` with interface contracts (TypeScript / OpenAPI / SQL DDL).
3. Present the numbered task list and request user confirmation before generating source code.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Artifact creation | `write_to_file` / filesystem MCP | Generate Markdown blocks in chat for user to save |
| Task tracking | Interactive edits to `tasks.md` | Update checklist directly in chat responses |
| Contract verification | Linters / schema validators | Manual visual verification of types and schemas |

---

## ✅ Verification

- A `spec.md` exists with clear user stories and acceptance criteria.
- Explicit non-goals (Out of Scope) are documented to avoid over-engineering.
- Contracts and interfaces (`plan.md`) were defined prior to authoring code.
- Tasks in `tasks.md` are marked complete only after verifiable evidence.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-14  
Version: 1.1.0
