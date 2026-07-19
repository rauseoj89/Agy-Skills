---
name: client-onboarding
description: Structured MSP client onboarding checklist: network discovery, vault credential setup, monitoring enrollment, PSA company setup, and documentation.
version: 1.0.0
tags: [universal, operations, onboarding]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: MSP Client Onboarding Specialist

## 🎯 Objetivo

Execute a complete, repeatable MSP client onboarding workflow — from initial intake through network discovery, credential vaulting, monitoring enrollment, PSA record creation, and handoff documentation.

## 🕒 Cuándo usar

- Al dar de alta a un nuevo cliente en los sistemas de monitoreo y soporte (PSA/RMM).
- Al realizar el setup inicial de credenciales en la bóveda de seguridad.
- Al documentar la red de un cliente y configurar backups.

## 🛡️ Principios Universales

1. **Credentials Vaulting**: Receive credentials only via secure channel. Vault immediately; never store in plaintext files or notes.
2. **Secrets Gate**: Confirmed zero credentials exist in ticket notes, documentation files, or session logs.
3. **Least Privilege**: Configure monitoring agents and administration accounts with minimal required privileges.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Integrar con psa-mcp para buscar compañías y crear tickets
# Registrar información en el workspace
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar terminal o herramientas de ticketing de Hermes si están configuradas
# De lo contrario, usar fallback manual
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar herramientas del MCP psa-mcp si está instalado en tu cliente
const company = await psa.searchCompanies({ name: "Cliente" });
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al operador humano en los pasos de la UI:
# Pide: "Crea la compañía en el PSA y escribe el ID resultante."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Solicita al usuario los datos del cliente.
2. Genera los checklists y plantillas de documentación.
3. Pide al usuario que cree los registros en el PSA de forma manual.
4. Genera las guías detalladas para que el usuario instale los agentes RMM y configure los respaldos en Veeam o Axcient.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Buscar Compañía PSA | psa.searchCompanies() | Pedir al usuario confirmación en el portal PSA |
| Crear Ticket | psa.createTicket() | Solicitar al usuario crear ticket de onboarding manualmente |
| Guardar Runbook | write_to_file() | Mostrar markdown del Runbook al usuario para guardar |

---

## ✅ Verificación

- Las credenciales están en la bóveda.
- El ticket de onboarding está creado en el PSA.
- Se verificó que el RMM y los backups (Veeam/Axcient) estén reportando de forma correcta.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
