---
name: powershell-automation
description: Authors, tests, and safely deploys PowerShell scripts for Windows automation — parameter validation, SecureString secrets, Pester testing, and execution policy.
version: 1.0.0
tags: [universal, operations, powershell, automation]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: PowerShell Automation Specialist

## 🎯 Objetivo

Write production-quality, secure PowerShell scripts for Windows automation — with proper parameter validation, secret handling via SecureString or Vault, structured error handling, Pester test coverage, and safe deployment patterns.

## 🕒 Cuándo usar

- Al crear scripts de automatización del sistema en entornos Windows (PowerShell/pwsh).
- Al configurar tareas programadas locales.
- Al escribir pruebas Pester para verificar lógica en scripts de infraestructura.

## 🛡️ Principios Universales

1. **No Hardcoded Secrets**: Load secrets from environment variables or secure vaults, never in plaintext script files.
2. **Parameter Validation**: Validate all inputs at parameter level (e.g. `[ValidateRange()]`, `[ValidatePattern()]`).
3. **SupportsShouldProcess**: Implement `-WhatIf` and `-Confirm` on any script containing destructive operations (delete, stop service, format).
4. **StrictMode & Error Handling**: Enforce strict mode (`Set-StrictMode -Version Latest`) and turn on stop error preference (`$ErrorActionPreference = 'Stop'`).

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Escribir y probar scripts de PowerShell en el entorno local
# Utilizar terminal nativa para ejecutar pwsh
```

### ▶️ Si estás en Hermes Agent:

```python
# Invocar scripts de PowerShell pasándole parámetros seguros por la terminal
result = terminal(command="pwsh -File myscript.ps1", timeout=60)
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP de terminal o shell para ejecutar Pester tests o lanzar scripts
const result = await shell.exec("pwsh -Command \"Invoke-Pester\"");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al usuario para ejecutar scripts de forma interactiva:
# Pide: "Ejecuta 'pwsh -ExecutionPolicy Bypass -File script.ps1' en tu terminal."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Escribe el script de PowerShell estructurado siguiendo la plantilla oficial.
2. Pide al usuario: "Crea el archivo `script.ps1` y pega este contenido".
3. Proporciona comandos de ejecución con `-WhatIf` para que el usuario pueda pre-evaluar los cambios.
4. Solicita que el usuario pegue la salida o cualquier error devuelto para depurar.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Correr scripts pwsh | terminal("pwsh") / shell.exec() | Generar comando pwsh para que el usuario lo ejecute |
| Crear archivo .ps1 | write_to_file() | Proporcionar código en chat para guardado manual |
| Ejecutar Pester Tests | terminal("Invoke-Pester") | Dar comando para que el usuario corra Pester en local |

---

## ✅ Verificación

- El script contiene `Set-StrictMode` y `$ErrorActionPreference = 'Stop'`.
- Los parámetros críticos están tipados y restringidos por validaciones de entrada.
- El script retorna códigos de salida adecuados (0 en éxito, 1 en error).

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
