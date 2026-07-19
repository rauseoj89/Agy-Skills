---
name: seo-auditing
description: Evaluates technical SEO and on-page alignment across websites, generating structured report indices.
version: 1.0.0
tags: [universal, seo, audit, marketing, report]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
---
# Skill: SEO Auditing

## 🎯 Goal
Thoroughly inspect search engine optimizations, accessibility indices, page-content hierarchy, and base infrastructure of a website to produce Markdown files or branded LaTeX reports.

## 🕒 When to use
- When evaluating search visibility optimizations for a target domain or new website development.
- When inspecting HTTP headers, SSL status, crawling directive files (`robots.txt`, `sitemap.xml`), and redirection flows.
- When producing bilingual (English/Spanish) structural audits.

## 🛡️ Universal Principles
1. **Verify HTTPS:** Enforce SSL checks and inspect active redirect rules for protocol security.
2. **Semantic Structure:** Verify the webpage contains exactly one primary `H1` tag to satisfy clean indexing parameters.
3. **Metadata Integrity:** Check page titles do not exceed 60 characters and description tags are kept within 160 characters.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are using [Antigravity]:
Locate and run the python helper script using environment or relative path syntax:
```powershell
python {AGENT}/skills/seo-audit/scripts/generate_seo_report.py data.json report.md
```

### ▶️ If you are using [Hermes]:
Query the remote server and parse headers:
```bash
curl -I https://example.com
```

### ⚠️ If you DO NOT have tools:
1. Ask the user to paste the `robots.txt`, `sitemap.xml`, or raw HTML snippet of the target webpage.
2. Analyze the title, description, images lacking `alt` text, and heading tags manually.
3. Write down findings and optimization lists directly inside the chat window.

────────────────────────────────────

## 🔄 Fallbacks

| Feature | With Tools | Without Tools |
| :--- | :--- | :--- |
| Header Inspection | `curl -I <url>` | Request raw response block from User |
| Heading Hierarchy | DOM query selectors | Request raw tag list from index page |
| Report Generation | Run local Python helper | Provide Markdown outline within conversational text |

────────────────────────────────────

## ✅ Verification
- [ ] The generated report supports language parameters (`lang='es'` or `lang='en'`) cleanly.
- [ ] No local configurations or staging environments are exposed in reports.
- [ ] Heading hierarchy is logical and sequential (no skips from H1 to H3).
- [ ] Accessible styling checklist is fulfilled (e.g. check for missing alt attributes).

────────────────────────────────────
Author: JimmyR
Last Updated: 2026-07-18
Version: 1.0.0
