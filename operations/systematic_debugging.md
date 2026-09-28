---
name: systematic-debugging
description: Root-cause-first software debugging and bug fixing harness. Enforces reproduction before modification, surgical minimal patching, and regression verification (Assess -> Fix -> Test).
version: 1.0.0
tags: [universal, engineering, operations, debugging, troubleshooting, root-cause, testing]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Systematic Debugging

## 🎯 Objective

Diagnose and repair software defects with absolute certainty, enforcing GitHub Spec-Kit's 3-phase debugging protocol (**Assess $\rightarrow$ Fix $\rightarrow$ Test**) and the "Root-Cause First" mandate. Eliminate speculative patching, unverified fixes, and accidental regressions.

## 🕒 When to Use

- When encountering any error, runtime exception, assertion failure, or stack trace.
- When a unit, integration, or E2E test fails in CI/CD pipelines or locally.
- When an API endpoint returns unexpected error codes (HTTP 500, 422, corrupted payloads).
- To surgically patch bugs without altering unrelated application behavior.

## 🛡️ Universal Principles

1. **Root-Cause First:** Never guess paths, flags, or assume root causes. Read involved source files and reliably reproduce the failure before modifying a single line of code.
2. **Reproduction Mandate:** Create a minimal reproduction script or automated test case that deterministically demonstrates the bug.
3. **Surgical Minimal Patching:** Modify strictly the minimal lines necessary to resolve the root cause. Zero unsolicited refactoring, broad reformatting, or collateral changes.
4. **Three-Attempt Backoff:** If a fix fails twice, halt, re-read the error output, and reformulate the hypothesis. If it fails a third time, pause and report the blocker with evidence to the user.
5. **Regression Defense:** Once the patch is applied, run the reproduction test (which must now pass) and the full existing test suite to ensure zero regressions.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# 1. Run reproduction test that fails
pytest tests/test_reproduce_bug.py
# 2. After applying surgical patch, verify success
pytest tests/test_reproduce_bug.py
# 3. Run full test suite
pytest
```

### ▶️ If you are on Hermes Agent:

```python
# Run test suite via terminal
result = terminal(command="npm test", timeout=120)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Run the specific reproduction test
const result = await shell.exec("npx jest -t 'handles null user token'");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide developer to isolate the defect:
# "Execute this command to reproduce the failure: 'go test -v -run TestBrokenEndpoint'."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Ask user for the complete stack trace and surrounding code lines.
2. Author a conceptual test or step-by-step procedure reproducing the failure condition.
3. Provide the surgical unified diff explaining why it resolves the root cause.
4. Ask user to run tests and confirm resolution before closing task.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Run tests | `terminal("npm test")` / MCP | Ask user to run command and paste log |
| Analyze logs | `docker_logs` / `parse_log_file` | Request last 50 lines of error log |
| Apply patches | File editing tools | Provide unified diff blocks (`diff -u`) |

---

## ✅ Verification

- Defect was reproduced with direct evidence before editing code.
- Exact root cause was identified (not merely a superficial symptom).
- Applied patch is surgical and adheres to strict scope.
- Reproduction test passes successfully.
- No regressions introduced into adjacent tests.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
