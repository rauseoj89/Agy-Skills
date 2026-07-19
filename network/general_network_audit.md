---
name: general-network-audit
description: Performs network configuration audits, scanning for plain-text secrets, default credentials, inadequate VLAN segmentation, and outdated management protocols.
version: 1.0.0
tags: [universal, network, security, audit]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Network Audit Specialist

## 🎯 Objetivo

Perform a comprehensive network configuration audit to identify vulnerabilities, credential leaks, segmentation weaknesses, and unsecure protocol usage. Outputs a timestamped audit report with an executive summary.

## 🕒 Cuándo usar

- Al realizar auditorías de configuración de red para identificar vulnerabilidades.
- Al revisar políticas de segmentación de VLAN o reglas de firewall.
- Para buscar contraseñas por defecto, protocolos de administración inseguros (Telnet, HTTP, SNMPv1/v2).

## 🛡️ Principios Universales

1. **Immediate Secrets Redaction**: Never include raw passwords, SNMP strings, or PSKs in reports. Mask as `[REDACTED]`.
2. **Default Credentials Check**: Actively search for and flag default usernames/passwords.
3. **Protocol Audit Rules**: Enforce encryption (SSH instead of Telnet, HTTPS instead of HTTP, SNMPv3 instead of SNMPv1/v2c).
4. **Data Privacy**: Do not expose internal private IP networks in public audit summaries unless using placeholders.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Leer archivos de configuración de routers/switches/firewalls
# Usar read_file para escanear configuraciones
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar terminal para buscar o analizar archivos de configuración
config = read_file(path="switch_config.cfg")
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar MCP de filesystem para analizar los archivos de configuración de red
const config = await filesystem.readFile("firewall.conf");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Pide al usuario que proporcione la configuración:
# "Por favor, pega el contenido del archivo de configuración del router (sin secretos)."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Solicita al usuario: "Por favor, sube o pega las directivas de configuración de tus dispositivos de red".
2. Analiza manualmente en el contexto del chat.
3. Devuelve el reporte de auditoría estructurado en Markdown directamente en el chat.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Leer archivos de config | read_file() | Pedir al usuario que pegue la configuración |
| Validar IPs y subredes | Scripts automatizados de verificación | Revisión visual manual por parte de la IA |
| Exportar reporte | write_to_file() | Mostrar reporte Markdown para que el usuario lo guarde |

---

## ✅ Verificación

- No se listan contraseñas reales en los outputs.
- Se clasificaron las vulnerabilidades por niveles de criticidad (Crítico, Alto, Medio, Bajo).
- Se proponen alternativas cifradas para cada protocolo inseguro detectado.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
