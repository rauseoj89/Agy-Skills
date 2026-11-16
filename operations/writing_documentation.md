---
name: writing-documentation
description: Writes structured user manuals, drafts release notes, compiles FAQs, and formats technical system guides. Use when asked to write documentation, compile user guides, write release notes, or construct FAQs.
version: 1.0.0
tags: [universal, operations, documentation, technical-writing, release-notes]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Technical Documenter & Writer

## 🎯 Objective

Translate complex systems, APIs, and operational procedures into clear, scannable, version-controlled documentation—including setup guides, release notes, user manuals, and FAQs—without leaking credentials, private IPs, or local paths.

## 🕒 When to Use

- When writing setup instructions, API references, or system architecture guides.
- When compiling release notes or revision changelogs.
- When drafting step-by-step user manuals or developer wikis.
- When organizing recurring technical questions into structured FAQs.

## 🛡️ Universal Principles

1. **Smart Conciseness & Scannability:** Skip explaining generic concepts; focus on implementation specifics using bolding, tables, checklists, code blocks, and GitHub alerts (`[!NOTE]`, `[!IMPORTANT]`, `[!WARNING]`, `[!CAUTION]`).
2. **Security Documentation Mandates:** Never include plaintext passwords, API keys, or private production IPs (`192.168.x.x`, `10.x.x.x`, `172.16-31.x.x`) in guides or examples.
3. **No Absolute Local Paths:** Replace user-specific paths with `${WORKSPACE_PATH}` or relative paths.
4. **Document Versioning:** Include a version control header (Version, Last Updated in ISO 8601, Author, Reviewer, Status) and revision history on major documentation artifacts.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Scan documentation draft for accidental secrets or private IP patterns
grep -rnE "(192\.168\.|10\.[0-9]+\.|PASSWORD=|SECRET=|API_KEY=)" docs/
```

### ▶️ If you are on Claude Code:

```bash
# Verify markdown links and check for hardcoded home paths
grep -rnE "(/Users/|/home/|C:\\\\Users)" docs/
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Write versioned documentation artifact
await write_to_file({ path: "docs/GUIDE.md", content: docMarkdown });
```

### ⚠️ If you do NOT have tools:

1. Ask the user for the target audience (developer, admin, end-user) and technical source notes.
2. Draft the structured Markdown guide with version header, prerequisites, numbered steps, and security alerts.
3. Confirm all placeholders (`${WORKSPACE_PATH}`, `${ENV_VAR}`) are used in place of real paths or secrets.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Audit doc for leaks | `grep` for IPs, secrets, local paths | Manually inspect code blocks before output |
| Write guide | `write_file()` / `edit_file()` | Output complete Markdown document in chat |
| Release notes | Summarize `git log` / changelog | Draft release notes from user-supplied items |

────────────────────────────────────

## ✅ Verification

- [ ] **No Hardcoded Secrets or IPs:** Confirmed zero credentials, tokens, or private production IPs appear in prose or code examples.
- [ ] **No Local Absolute Paths:** Verified all paths are relative or use `${WORKSPACE_PATH}` placeholders.
- [ ] **Version Control Header:** Major docs include Version, ISO 8601 Last Updated date, Author, and Reviewer.
- [ ] **Technical Accuracy:** Steps, flags, and prerequisites match the verified implementation.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
