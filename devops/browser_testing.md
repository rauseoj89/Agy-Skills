---
name: browser-testing
description: Automates browser-based E2E testing, visual regression, Lighthouse audits, and interactive UI validation using chrome-devtools. Use when asked to test web pages, run accessibility audits, capture screenshots, validate UI flows, or perform visual regression testing.
version: 1.1.0
tags: [universal, devops, browser, testing]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Browser Testing Specialist

## 🎯 Objective

Run automated browser scripts, capture frontend performance metrics, audit accessibility (WCAG), and verify frontend integrity using browser control tools.

## 🕒 When to Use

- When executing automated E2E tests on web interfaces.
- When validating visual layouts and capturing screenshots for visual regression.
- When running performance, accessibility (Lighthouse), or SEO audits on web applications.
- When debugging browser console errors or network payloads.

## 🛡️ Universal Principles

1. **Security & Redaction**: Never leak plaintext passwords/keys in screenshots, logs, or inputs. Use environment variables.
2. **No Hardcoded Absolute Paths**: Save screenshots in relative project folders (e.g. `./screenshots/`).
3. **HTTPS Enforcement**: All communications must enforce HTTPS.
4. **Navigation Stabilisation**: Always wait for elements to load to prevent race conditions.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Use native chrome-devtools plugin / integrated tools
# Capture screenshots, inspect DOM, and perform audits
```

### ▶️ If you are on Hermes Agent:

```python
# Use Python scripts with playwright or selenium, or integrated Hermes tools
# If available, call the corresponding chrome-devtools tools
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use the chrome-devtools-mcp MCP to navigate and test
const page = await chrome_devtools.navigate_page({ url: "http://localhost:3000" });
```

### ▶️ If you are on GitHub Copilot / Cursor:

```bash
# Launch Chrome with remote debugging for MCP connection or Playwright:
# macOS:
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev_profile"

# Linux:
google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev_profile"

# Windows PowerShell:
& "$env:ProgramFiles\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$env:TEMP\chrome_dev_profile"
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Generate a local test script (Playwright, Cypress, Selenium).
2. Ask the user: "Please save this test script and execute it locally".
3. Request that the user paste the test results and any captured screenshots.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Open page / Navigate | `navigate_page()` or MCP tools | Ask user to visit the URL in their local browser |
| Capture screenshot | `take_screenshot()` | Ask user to provide a screenshot |
| Run Lighthouse | `lighthouse_audit()` | Ask user to run Lighthouse in Chrome DevTools and report |

---

## ✅ Verification

- The test reports success without JS console exceptions.
- Lighthouse scores exceed required minimum thresholds.
- Secure HTTPS or localhost encryption verified.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.1.0
