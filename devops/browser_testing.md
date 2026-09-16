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

## 🎯 Objetivo

Run automated browser scripts, capture frontend performance metrics, audit accessibility (WCAG), and verify frontend integrity using browser control tools.

## 🕒 Cuándo usar

- Al realizar pruebas automatizadas E2E en interfaces web.
- Al validar layouts visuales y capturar screenshots para regresión visual.
- Al ejecutar auditorías de rendimiento, accesibilidad (Lighthouse) o SEO en la web.
- Al depurar errores en la consola del navegador o payloads de red.

## 🛡️ Principios Universales

1. **Security & Redaction**: Never leak plaintext passwords/keys in screenshots, logs, or inputs. Use environment variables.
2. **No Hardcoded Absolute Paths**: Save screenshots in relative project folders (e.g. `./screenshots/`).
3. **HTTPS Enforcement**: All communications must enforce HTTPS.
4. **Navigation Stabilisation**: Always wait for elements to load to prevent race conditions.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Usar el plugin chrome-devtools nativo / herramientas integradas
# Capturar pantallazos, inspeccionar DOM y auditar
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar scripts de Python con playwright o selenium, o herramientas integradas de Hermes
# Si están disponibles, llamar a las herramientas de chrome-devtools correspondientes
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP chrome-devtools-mcp para navegar y probar
const page = await chrome_devtools.navigate_page({ url: "http://localhost:3000" });
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```bash
# Iniciar Chrome con depuración remota para conexión MCP o Playwright:
# macOS:
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev_profile"

# Linux:
google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev_profile"

# Windows PowerShell:
& "$env:ProgramFiles\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$env:TEMP\chrome_dev_profile"
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera un script de test local (Playwright, Cypress, Selenium).
2. Pide al usuario: "Guarda este script de test y ejecútalo localmente".
3. Solicita al usuario que pegue los resultados del test y las capturas generadas.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Abrir página / Navegar | `navigate_page()` o herramientas del MCP | Pedir al usuario que visite la URL en su navegador local |
| Tomar screenshot | `take_screenshot()` | Pedir al usuario que envíe una captura de pantalla |
| Correr Lighthouse | `lighthouse_audit()` | Pedir al usuario que corra Lighthouse en Chrome DevTools y reporte |

---

## ✅ Verificación

- El test reporta éxito sin excepciones JS en la consola.
- Las puntuaciones de Lighthouse superan los mínimos requeridos.
- Se verificó la encriptación HTTPS o localhost seguro.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.1.0
