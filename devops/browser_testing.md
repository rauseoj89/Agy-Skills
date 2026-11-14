---
name: browser-testing
description: Automates browser-based E2E testing, visual regression, Lighthouse audits, and interactive UI validation using browser-tools-mcp. Use when asked to test web pages, run accessibility audits, capture screenshots, validate UI flows, or perform visual regression testing.
version: 1.3.0
tags: [universal, devops, browser, testing]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-11-14
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Browser Testing Specialist

## 🎯 Objective

Run automated browser scripts, capture frontend performance metrics, audit accessibility (WCAG), and verify frontend integrity using `browser-tools-mcp` tools.

## 🕒 When to Use

- When executing automated E2E tests on web interfaces.
- When validating visual layouts and capturing screenshots for visual regression.
- When running performance, accessibility (Lighthouse), or SEO audits on web applications.
- When debugging browser console errors or network payloads.

## 🛡️ Universal Principles

1. **Security & Redaction**: Never leak plaintext passwords/keys in screenshots, logs, or inputs. Use environment variables.
2. **No Hardcoded Absolute Paths**: Save screenshots in relative project folders (e.g. `./screenshots/`).
3. **HTTPS Enforcement**: All external communications must enforce HTTPS.
4. **Navigation Stabilisation**: Always wait for elements to load to prevent race conditions.
5. **Modern Web Standards Alignment**: Align accessibility, interactive flow, and UI audits with Google Chrome's `modern-web-guidance` standards (testing native `<dialog>`, `popover`, top-layer backdrops, and modern keyboard navigation). For legacy codebases, execute `npx -y modern-web-guidance@latest legacy-scan <path>` to flag obsolete web patterns.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Use browser-tools-mcp tools / native browser integration:
# new_page, navigate_page, take_snapshot, lighthouse_audit
```

### ▶️ If you are on Hermes Agent:

```python
# Use Python scripts with playwright or browser-tools-mcp
# Call new_page and take_snapshot for visual verification
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Use browser-tools-mcp to navigate, snapshot, and inspect
await browser_tools.new_page();
await browser_tools.navigate_page({ url: "http://localhost:3000" });
const snapshot = await browser_tools.take_snapshot();
const audit = await browser_tools.lighthouse_audit({ url: "http://localhost:3000" });
```

### ▶️ If you are on GitHub Copilot / Cursor:

```bash
# Launch Chrome with remote debugging for MCP connection:
# Windows PowerShell:
& "$env:ProgramFiles\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$env:TEMP\chrome_dev_profile"
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate a local test script (Playwright, Cypress, Puppeteer).
2. Ask user: "Please save this test script and execute it locally".
3. Request that user paste the test results and captured screenshots.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Open page / Navigate | `new_page()`, `navigate_page()` | Ask user to visit URL in browser |
| Inspect DOM / Layout | `take_snapshot()`, `take_screenshot()` | Ask user to inspect elements |
| Run Lighthouse | `lighthouse_audit()` | Ask user to run Lighthouse in DevTools |
| Console / Network log | `list_console_messages()`, `list_network_requests()` | Ask user to check Console/Network tab |

---

## ✅ Verification

- The test reports success without JS console exceptions.
- Lighthouse scores exceed required minimum thresholds.
- Secure HTTPS or localhost encryption verified.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-11-14  
Version: 1.3.0
