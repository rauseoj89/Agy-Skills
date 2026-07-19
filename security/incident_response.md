---
name: incident-response
description: Structured triage, containment, investigation, remediation, and documentation workflow for security and operational incidents.
version: 1.0.0
tags: [universal, security, incident, response]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Incident Response Specialist

## 🎯 Objetivo

Execute a structured, evidence-preserving incident response workflow from initial detection through full remediation and post-incident documentation. Integrates with the PSA system for ticket creation and audit trail.

## 🕒 Cuándo usar

- Ante la sospecha de una brecha de seguridad activa (ransomware, exfiltración, phishing).
- Para contener accesos no autorizados en cuentas o servidores.
- Al coordinar la erradicación de amenazas y la posterior recuperación desde respaldos.

## 🛡️ Principios Universales

1. **Containment Before Remediation**: Always isolate the affected systems or accounts before running cleaning steps to preserve evidence.
2. **Authorization Gate**: Always request user/client authorization before isolating production networks or restoring backups.
3. **Evidence Preservation**: Do not work on original logs or drives; make copies, compute hashes, and preserve timestamps.
4. **No Hardcoded Secrets**: Ensure credentials rotated during eradication are stored in vaults, not in ticket logs.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Consultar logs de seguridad locales para identificar el origen
# Bloquear accesos locales o coordinar el aislamiento mediante comandos de firewall
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar terminal para inspeccionar conexiones activas
result = terminal(command="netstat -ano", timeout=30)
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP de terminal o firewall para ejecutar comandos de aislamiento de red
const result = await shell.exec("powershell -Command \"Disable-NetAdapter -Name 'Ethernet'\"");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Alertar e indicar al usuario los pasos críticos para aislar el equipo:
# Pide: "Desconecta inmediatamente el equipo de la red (WiFi y cable Ethernet)."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Clasifica la severidad (P1-P4) y genera los pasos de contención inmediatos.
2. Pide al usuario: "Por favor, realiza estas acciones de aislamiento (ej. apagar el switch, deshabilitar la cuenta) de inmediato".
3. Proporciona instrucciones de recopilación de logs para que el usuario guarde las evidencias antes de limpiar.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Aislar Endpoint | terminal("Disable-NetAdapter") | Pedir al usuario que desconecte el cable de red / WiFi |
| Deshabilitar Cuenta | psa.revokeSessions() / terminal | Instruir al administrador para revocar accesos en el portal Azure/AD |
| Verificar Backups | backup.getBackupStatus() | Pedir al usuario buscar el último backup saludable en consola |

---

## ✅ Verificación

- La amenaza fue contenida y aislada.
- Se identificó el vector de ataque original y se aplicó el parche correspondiente.
- El informe de incidentes post-mortem se redactó y guardó sin revelar secretos.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
