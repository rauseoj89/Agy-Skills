---
name: patch-management
description: Governs the full patch lifecycle: inventory, risk assessment, change window scheduling, staged deployment, verification, and rollback using RMM, Veeam, and Axcient.
version: 1.0.0
tags: [universal, operations, patch, sysadmin]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Patch Management Specialist

## 🎯 Objetivo

Execute a controlled, risk-aware patch lifecycle for Windows and Linux systems — from vulnerability inventory through staged deployment, post-patch validation, and rollback readiness.

## 🕒 Cuándo usar

- Al planificar ventanas de mantenimiento para aplicar parches de seguridad (OS, drivers, firmware).
- Al auditar vulnerabilidades pendientes y verificar la existencia de parches.
- Al coordinar la restauración o el rollback de sistemas caídos tras una actualización fallida.

## 🛡️ Principios Universales

1. **Pre-Patch Baseline**: Never patch a production system without a verified restore point (Veeam, Axcient, snapshot) created within the last 24 hours.
2. **Staged Deployment**: Apply patches in order: Test/Dev -> Pilot Group -> Production -> Critical Infrastructure.
3. **Change Window Gate**: No production updates are allowed outside of approved change windows.
4. **No Hardcoded Credentials**: Inject RMM, backup, or domain admin credentials dynamically using environment variables or vaults.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Integrar con rmm-mcp o backup-mcp locales para verificar copias de seguridad
# Ejecutar scripts locales de PowerShell en sistemas de prueba
```

### ▶️ Si estás en Hermes Agent:

```python
# Ejecutar scripts de terminal para comprobar si el HotFix ya está aplicado
result = terminal(command="powershell -Command \"Get-HotFix -Id KB5034441\"", timeout=60)
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar terminal/shell para ejecutar PowerShell o bash locales de validación
const status = await shell.exec("powershell -Command \"Get-HotFix\"");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al usuario para validar copias de seguridad en su consola RMM/BCDR:
# Pide: "Revisa en Veeam/Axcient que exista un backup exitoso de las últimas 24 horas."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera los scripts de validación (e.g. `Get-HotFix`, `wusa /uninstall` o comandos bash de actualización).
2. Pide al usuario: "Por favor ejecuta estos comandos para verificar parches aplicados o desinstalar la actualización problemática".
3. Solicita confirmación explícita de que se cuenta con un backup antes de proceder a la actualización de producción.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Verificar backup | backup.getBackupStatus() | Pedir al usuario verificar en portal Veeam/Axcient |
| Programar Parches | rmm.approvePatches() | Pedir al usuario programar en consola RMM |
| Desinstalar Parche | terminal("wusa /uninstall") | Generar el comando exacto para desinstalación manual |

---

## ✅ Verificación

- Existe un punto de restauración funcional de Veeam o Axcient de las últimas 24 horas.
- Todos los servicios de arranque automático están en ejecución tras el reinicio.
- Los logs del sistema no presentan errores críticos del actualizador del sistema operativo.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
