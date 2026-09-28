---
name: idea-assessment
description: Pre-implementation feasibility and spike framework. Use when evaluating new product ideas, technical spikes, library migrations, or architectural alternatives before committing engineering effort (Intake -> Research -> Shape -> Decide).
version: 1.0.0
tags: [universal, strategy, operations, engineering, feasibility, decision-matrix, spikes]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Idea & Feasibility Assessment

## 🎯 Objective

Evaluate whether a proposed feature, architectural pivot, or technical initiative deserves investment, delivering an evidence-backed scorecard (**Go**, **Clarify**, or **Stop**) and bounded solution shape before engineering effort is committed.

## 🕒 When to Use

- When facing strategic architectural or product questions ("Should we migrate to GraphQL?", "Is WebSockets viable here?", "Should we use library X?").
- Prior to initiating major refactoring efforts or third-party service integrations.
- To define time/effort appetite and explicitly delineate rabbit holes that must be avoided.

## 🛡️ Universal Principles

1. **Evidence-Based Evaluation:** Evaluate with objective facts and technical benchmarks rather than subjective preference. Compare maintenance overhead, latency, security impact, and learning curves.
2. **Four-Stage Process:** Every assessment strictly follows:
   - **Stage 1 — Intake & Problem Framing:** Real user problem, success metrics, and beneficiaries.
   - **Stage 2 — Technical Spikes & Research:** Architecture compatibility, ecosystem alternatives, trade-offs.
   - **Stage 3 — Solution Shaping:** Define time appetite and document out-of-scope rabbit holes.
   - **Stage 4 — Decision Scorecard:** Deliver justified verdict: 🟢 **GO**, 🟡 **CLARIFY**, or 🔴 **STOP**.
3. **No Premature Implementation:** Writing solution code is prohibited until the verdict reaches **GO** and `spec-driven-development` is initiated.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Research dependencies and licenses in the ecosystem
npm view <package> dependencies license
```

### ▶️ If you are on Hermes Agent:

```python
# Perform documentation search and benchmarks
result = web_search("benchmark postgres pgvector vs qdrant")
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Inspect current codebase compatibility
const pkg = JSON.parse(await readFile("package.json"));
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Present comparative pros/cons matrix to user:
# "Would you like to evaluate the infrastructure impact before adopting this dependency?"
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Pose appetite constraints and infrastructure boundaries to the user.
2. Compare alternatives in a multi-dimensional table (Maintenance effort, Security, Performance, Vendor lock-in risk).
3. Issue a justified final verdict (GO, CLARIFY, or STOP).

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Ecosystem research | `search_web` / MCP | Evaluation based on verified documentation and critical analysis |
| Dependency check | Manifest inspection tools | Request tech stack and key dependencies from user |
| Decision Scorecard | Structured Markdown template | Direct decision matrix in chat |

---

## ✅ Verification

- The core problem solved by the initiative is unambiguously defined.
- Risks regarding security, operational cost, and maintenance were quantified.
- Explicit non-goals (rabbit holes) were delimited.
- A definitive verdict (GO, CLARIFY, or STOP) with technical rationale was delivered.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
