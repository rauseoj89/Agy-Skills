# Agy-Skills ↔ CLA-Skills Sync Guide

This document tracks alignment between `rauseoj89/Agy-Skills` (universal multi-agent blueprints) and `jrauseo/CLA-Skills` (Claude Code port).

## Last Synced Reference
- **Agy-Skills Baseline Commit:** `e24f17c` (`2026-11-16`)
- **Central-Brain Baseline Commit:** `924b051` (`2026-11-16`)

## Field Mapping (Agy-Skills → CLA-Skills)

| Agy-Skills Field / Section | CLA-Skills Equivalent | Notes |
| :--- | :--- | :--- |
| `name` | `name` | Kebab-case identifier; may be a short alias (e.g., `docum-md`, `db-manager`). |
| `description` | `description` | Must be double-quoted if it contains `:`. |
| `version`, `last_updated` | `version`, `last_updated` | Semver (`X.Y.Z`) and ISO date (`YYYY-MM-DD`). |
| `## 🎯 Objective` + `## 🛡️ Universal Principles` | `## Role & Objectives` + `## Rules & Constraints` | Core persona rules remain identical. |
| `## 🤖 Multi-Agent Execution` | Claude Code execution block | Keep only Claude Code native tool instructions (`Bash`, `Read`, `Edit`). |
| `## ✅ Verification` | `## Workflow Checklist` | Security gates (no secrets, IDOR/BOLA, Attribution & Signing) must stay in sync. |

## Intentional Differences
- `Agy-Skills` includes `Multi-Agent Execution` sections for Antigravity, Hermes, Cline, Roo-Code, Copilot, Cursor, and OpenCode, plus `Fallbacks` for tool-less environments.
- `CLA-Skills` omits non-Claude agent blocks and uses `SKILL.md` per folder.
- Antigravity-native tools (`chrome-devtools`, `write_to_file`) in `Agy-Skills` are intentional.
