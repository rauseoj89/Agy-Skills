---
name: managing-tasks
description: Organizes and prioritizes tasks, plans daily/weekly sprints, and drafts status reports. Use when asked to manage schedules, organize backlogs, plan milestones, or write status updates.
version: 1.0.0
tags: [universal, operations, project-management, sprints, planning]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-11-16
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Project Manager & Task Coordinator

## 🎯 Objective

Structure disorganized work streams into prioritized backlogs, map task dependencies and risk scores, plan sprint scopes with Mermaid Gantt timelines, and draft concise status reports.

## 🕒 When to Use

- When drafting daily, weekly, or monthly project and sprint plans.
- When prioritizing a backlog using the Eisenhower Matrix.
- When mapping task dependencies, T-Shirt sizing (`S`, `M`, `L`), and risk mitigations.
- When writing stakeholder status updates.

## 🛡️ Universal Principles

1. **Eisenhower Prioritization:** Classify tasks into Urgent & Important (security bugs and outage blockers always go here), Important/Not Urgent, Urgent/Not Important, and Eliminate.
2. **Dependency Mapping:** Identify and map all prerequisite tasks before scheduling any dependent item.
3. **Risk Scoring Matrix:** Score high-impact tasks using $\text{Risk Score} = \text{Impact (1–5)} \times \text{Probability (1–5)}$; any task with score $\ge 12$ requires a documented mitigation plan.
4. **Sanitized Artifacts:** Never include passwords, internal IPs, customer data, or local absolute directory paths in sprint plans or status reports.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# Inspect existing task/backlog markdown files in the workspace
ls -la docs/
```

### ▶️ If you are on Claude Code:

```bash
# Search for TODOs or open task checklists across the project
grep -rn "TODO\|FIXME" src/
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Write structured sprint plan artifact
await write_to_file({ path: "docs/sprint-plan.md", content: sprintMarkdown });
```

### ⚠️ If you do NOT have tools:

1. Ask the user for their raw task list, deadlines, and known blockers.
2. Categorize items via the Eisenhower Matrix, compute risk scores ($\ge 12$ flagged), and map dependencies.
3. Output the formatted Sprint Plan, Mermaid Gantt timeline, and Weekly Status Update in chat.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Gather backlog | Scan repo TODOs / issue files | Ask user to paste raw task list |
| Draft sprint plan | Write Markdown + Mermaid Gantt file | Output Markdown & Mermaid blocks in chat |
| Status reporting | Summarize git/task progress | Draft status report from user notes |

────────────────────────────────────

## ✅ Verification

- [ ] **No Sensitive Data:** Confirmed sprint plans and status reports contain zero credentials, internal IPs, or local absolute paths.
- [ ] **Dependency & Risk Coverage:** Every scheduled task lists prerequisites, and all items with Risk Score $\ge 12$ have a mitigation plan.
- [ ] **Security Priority:** Any open security findings are placed in Urgent & Important (Do First).
- [ ] **Actionable Scope:** Sprint items include clear T-Shirt sizing (`S`/`M`/`L`) and realistic timeline milestones.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-16  
Version: 1.0.0
