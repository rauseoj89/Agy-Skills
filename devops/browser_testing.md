---
name: "Browser Testing"
description: "Automates browser-based E2E testing, visual regression checks, and accessibility audits using chrome-devtools-mcp."
category: "generic/devops"
tools_required: ["chrome-devtools-mcp"]
last_updated: 2026-06-15
---

# 🧠 Skill: Browser Testing Specialist

## 🎯 Goal
Automate user interface validation, E2E functional user flows, performance benchmarking (Lighthouse), and visual layout checks securely.

## 📊 Inputs Required
- Target website or endpoint URL.
- Test script scenario (e.g. login user credentials).
- Visual regression baseline screenshots.

## 🛠️ Step-by-Step Instructions
1. **Initialize Session & Navigation**:
   - Check active browser tabs or spin up a new page using `new_page`.
   - Direct the page using `navigate_page` to the target environment URL.
2. **Interactive UI Flow Simulation**:
   - Fill inputs and click buttons using `fill` and `click`.
   - Never hardcode user passwords or API keys in the test files. Map inputs dynamically using variables loaded from the secure vault backend.
3. **Diagnostics & Log Scans**:
   - Query `list_console_messages` to check for active JavaScript errors.
   - Query `list_network_requests` to identify broken API routes or failed asset pings.
4. **Performance & Compliance Auditing**:
   - Execute `lighthouse_audit` on the active tab. Verify that Performance, Accessibility, Best Practices, and SEO scores satisfy target standards.
5. **Visual Verification**:
   - Capture snapshots or screenshots using `take_screenshot`. Save visual reports using dynamic variables, avoiding absolute local paths.

## 🛡️ Verification & Security Checklist
1. **Zero Secret Leaks**: Verify that zero passwords, JWT tokens, or credentials appear in console logs, DOM dumps, or test screenshots.
2. **Path Compliance**: Ensure screenshots are saved in relative project locations rather than absolute user paths.
3. **Execution Auditing**: Verify that pages and scripts are handled headless in production configurations.

---
*Created by Efficiency Core*
