---
name: <kebab-case-name>
description: <One clear line>
version: 1.0.0
tags: [universal, <tag1>, <tag2>]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: <YYYY-MM-DD>
author: <your-name>
powered_by: AntigravityAI
---
# Skill: <Readable Name>

## 🎯 Objective

[Agnostic description of what this skill does]

## 🕒 When to Use

- Use Case 1
- Use Case 2
- Use Case 3

## 🛡️ Universal Principles

1. **Rule 1**: Explanation (always applies)
2. **Rule 2**: Explanation (always applies)
3. **Rule 3**: Explanation (always applies)

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Example with native tools or MCP calls
agent-command --flag
```

### ▶️ If you are on Claude Code:

```bash
# Use Claude Code tools (Bash, ReadFile, EditFile)
claude-code-command --flag
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Example using MCP tools in Cline/Roo-Code
await tool.execute({ param: "value" });
```

### ⚠️ If you do NOT have tools:

1. Step 1 manual
2. Step 2 manual
3. Step 3 manual

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Read file | read_file() | Ask user to paste |
| Execute command | terminal() | Generate command for user |

────────────────────────────────────

## ✅ Verification

- [ ] Check 1
- [ ] Check 2
- [ ] Check 3
- [ ] Check 4 (Zero plaintext secrets or private IPs)

---

**Author:** <your-name>  
**Powered by:** AntigravityAI  
Last Updated: <YYYY-MM-DD>  
Version: 1.0.0
