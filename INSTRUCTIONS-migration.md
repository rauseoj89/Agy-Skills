# 🔄 Migration Instructions: Agy-Skills → Multi-Agent Universal

This file outlines the migration instructions used to convert Antigravity-specific skills to universal formats.

## 🎯 Objective

Transform all skills in the current repository (originally designed for Antigravity) into universal skills that work across any modern AI agent (Hermes, Cline, Roo Code, GitHub Copilot, Cursor, etc.).

## 📋 Required Universal Structure for Every Skill

Every updated skill MUST have this exact structure:

```markdown
---
name: <kebab-case-name>
description: <One clear line>
version: 1.0.0
tags: [universal, <tag1>, <tag2>]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: <YYYY-MM-DD>
author: <your-name>
---
# Skill: <Readable Name>
## 🎯 Objective
[Agnostic description of what it does]
## 🕒 When to Use
- Use Case 1
- Use Case 2
- Use Case 3
## 🛡️ Universal Principles
1. **Rule 1**: Explanation (always applies)
2. **Rule 2**: Explanation (always applies)
...
---
## 🤖 Multi-Agent Execution
### ▶️ If you are on [Agent A]:
...
```
