---
name: managing-git-workflows
description: Enforces Git best practices including interactive semantic commits, logical commit splitting, branching strategies, conventional commits, pull request workflows, merge conflict resolution, and code review processes. Use when asked to commit changes, set up git workflows, resolve merge conflicts, create branch strategies, or standardize commit messages.
version: 1.1.0
tags: [universal, devops, git, conventional-commits, branching, code-review]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode, Claude-Code]
last_updated: 2026-10-17
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Git Workflow Specialist

## 🎯 Objective

Ensure repository structure cleanliness, enforce atomic Conventional Commits through interactive pre-commit confirmation and logical group splitting, prevent credential leakage, and govern branch and pull request review gates.

## 🕒 When to Use

- When asked to commit current changes (`/commit`, "commit my changes") by splitting them into logical groups with Conventional Commits.
- When configuring branch protection rules or choosing a branching strategy (GitFlow, Trunk-Based).
- When writing standardized commit messages or Pull Request (PR) templates.
- When resolving merge conflicts or conducting code reviews and pre-commit security audits.

## 🛡️ Universal Principles

1. **No Hardcoded Secrets (Pre-Commit Gate):** Before staging, committing, or pushing, verify that zero `.env*` files, passwords, private keys, `CHG-Review/` logs, or production private IPs leak in the diff.
2. **Interactive Commit Confirmation:** Inspect `git branch --show-current`, `git status --short`, and `git diff HEAD` first, then present 3 options in this exact order:
   - `1. Commit + push (Recommended)` — commit on the current branch, then push it.
   - `2. Commit only` — commit on the current branch, no push.
   - `3. Commit on a new branch` — create a branch named after the changes (`git switch -c <type/short-summary>`), commit there, then push it.
3. **Logical Group Splitting & Scoped Staging:** Split working-tree changes into independent logical groups (one atomic commit per group). Run `git add <file1> <file2>` only for each group's files; never run unbounded `git add .` or `git add -A`.
4. **Conventional Commits & Zero AI Attribution:** Format as `type(scope): summary` (`feat`, `fix`, `docs`, `refactor`, `style`, `test`, `build`, `chore`) in English, imperative mood, under 72 characters. Never add `Co-Authored-By`, `"Generated with ..."`, or AI session links/trailers.
5. **Clean Merges & Hook Integrity:** Never use `git push --force` on `main` or `release` branches, and never bypass security hooks (`--no-verify`).

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity / OpenCode:

```bash
# 1. Inspect current state before prompting the user (via ask_question)
git branch --show-current
git status --short
git diff HEAD

# 2. Stage explicitly per logical group and create a Conventional Commit with zero AI attribution
git add src/module.ts tests/module.test.ts
git commit -m "feat(module): add input validation boundary"
```

### ▶️ If you are on Claude Code:

```bash
# Inspect state and stage specific files per logical commit group
git status --short && git diff HEAD
git add src/module.ts tests/module.test.ts
git commit -m "feat(module): add input validation boundary"
```

### ▶️ If you are on Cline / Roo-Code:

```javascript
// Run pre-commit inspection and prompt user with ask_followup_question
const status = await shell.exec("git branch --show-current && git status --short");
await shell.exec('git add src/module.ts && git commit -m "feat(module): add validation"');
```

### ⚠️ If you do NOT have tools:

1. Request the output of `git branch --show-current`, `git status --short`, and `git diff HEAD` from the user.
2. Ask which of the 3 commit options they prefer (*Commit + push*, *Commit only*, or *Commit on a new branch*).
3. Provide the exact command blocks separated by logical group using `git add <files>` and `git commit -m "type(scope): summary"`.

────────────────────────────────────

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Inspect Git state | `git status --short` / `git diff HEAD` via terminal | Ask user to paste `git status` and `git diff` output |
| Prompt commit action | Interactive question tool (`ask_question`) | Present the 3 numbered options in chat |
| Commit logical groups | `git add <files>` + `git commit` per logical group | Generate exact command sequence for the user to run |

────────────────────────────────────

## ✅ Verification

- [ ] **No Hardcoded Secrets:** Confirmed zero credentials, `.env*` files, private keys, or `CHG-Review/` directories are staged.
- [ ] Each commit stages only related files via explicit `git add <files>` (never `git add .` or `git add -A`).
- [ ] All commit messages follow Conventional Commits (`<72` chars, imperative mood, English) with zero AI attribution or trailers.
- [ ] **Destructive Gate:** Confirmed no `git push --force`, `git reset --hard`, or `--no-verify` flags are used.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-10-17  
Version: 1.1.0
