---
name: managing-m365
description: Administers Microsoft 365 users, licenses, MFA, Conditional Access, mailboxes, and groups using PowerShell and the Graph API.
version: 1.0.0
tags: [universal, operations, m365, office]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Microsoft 365 Administrator

## 🎯 Objetivo

Provision and deprovision M365 users, enforce MFA and Conditional Access policies, audit licenses, manage mailbox delegations, and govern group membership — securely and with full audit trails.

## 🕒 Cuándo usar

- Al crear o desactivar cuentas de usuario en Microsoft 365.
- Al verificar y auditar el estado de MFA en las cuentas administrativas y de usuario.
- Al gestionar asignación de licencias y buzones compartidos.

## 🛡️ Principios Universales

1. **No Plaintext Credentials**: Never hardcode passwords or client secret tokens in scripts or commands.
2. **Order of Deprovisioning**: Revoke sessions -> disable account -> remove groups -> convert to shared -> remove licenses.
3. **Admin MFA Protection**: Always enforce Phishing-Resistant MFA on administrative accounts.
4. **Least Privilege**: Only request scopes necessary for the operation (e.g. `User.ReadWrite.All`).

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Ejecutar comandos de PowerShell localmente usando el módulo de Microsoft Graph
# Inyectar credenciales de vault temporalmente
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar terminal para invocar scripts de PowerShell o curl para la Graph API
result = terminal(command="pwsh -File run-m365-audit.ps1", timeout=120)
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP de shell/terminal para invocar PowerShell o realizar peticiones HTTP
const result = await shell.exec("pwsh -Command \"Connect-MgGraph -Scopes ...\"");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al usuario para que ejecute los scripts locales en su terminal:
# Pide: "Ejecuta 'Connect-MgGraph' en tu PowerShell y pega la salida del estado."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera los scripts de PowerShell o las llamadas REST `curl` para la API de Graph.
2. Pide al usuario: "Por favor, abre PowerShell, inicia sesión en Microsoft Graph y ejecuta los siguientes comandos".
3. Solicita que el usuario pegue los resultados devueltos (ocultando cualquier token) para continuar con el análisis.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Conectar a Graph | terminal() / Connect-MgGraph | Dar comando para que el usuario se autentique en local |
| Consultar MFA | Graph API call | Pedir al usuario correr script de auditoría y pegar output |
| Modificar Licencia | Set-MgUserLicense | Generar script para ejecución por parte del usuario |

---

## ✅ Verificación

- Se completaron las fases de desaprovisionamiento en el orden correcto.
- Se verificó que el UPN creado tenga activada la solicitud de cambio de clave en el próximo login.
- No se han impreso contraseñas en los logs.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
