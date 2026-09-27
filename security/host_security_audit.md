---
name: host-security-audit
description: Audits Linux VPS, servers, and host OS security configurations. Inspects SSH hardening, firewall status (UFW/nftables/iptables), Fail2ban/CrowdSec alignment, SUID binaries, sudo logging, open ports, and resource consumption.
version: 1.0.0
tags: [universal, security, linux, vps, hardening, ssh, firewall, fail2ban]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Linux Host Security Specialist

## 🎯 Objetivo

Audit, diagnose, and harden Linux Virtual Private Servers (VPS) and host operating systems, ensuring minimal attack surfaces, strict SSH policies, synchronized intrusion detection systems (Fail2ban/CrowdSec), and least-privilege configurations.

## 🕒 Cuándo usar

- Al evaluar un servidor Linux nuevo o existente antes de pasarlo a producción.
- Al verificar la configuración del demonio SSH (`/etc/ssh/sshd_config`).
- Al revisar el estado del cortafuegos (`ufw`, `nftables`, `iptables`) frente a puertos y sockets en escucha (`ss -tulpn`).
- Al validar que las cárceles de Fail2ban o CrowdSec coincidan con los puertos reales de los servicios.
- Al auditar binarios con permisos SUID o privilegios de sudo sin contraseña.

## 🛡️ Principios Universales

1. **Read-Only Diagnostic First:** La fase de auditoría debe ser estrictamente de solo lectura. No aplicar cambios destructivos ni recargar cortafuegos sin autorización explícita.
2. **Never Lock Out SSH:** Nunca reiniciar el servicio SSH ni bloquear el puerto de gestión sin requerir al usuario que mantenga una sesión abierta paralela para pruebas.
3. **Alignment Audit:** Verificar que las reglas del cortafuegos y los filtros de Fail2ban correspondan exactamente a los puertos en los que los servicios están escuchando (prevenir fallos silenciosos de protección).
4. **Zero Listening Databases:** Ninguna base de datos (PostgreSQL, MySQL, Redis, MongoDB) debe escuchar en `0.0.0.0` sin restricción de cortafuegos.
5. **Sanitize Host Telemetry:** Enmascarar direcciones IP públicas, nombres de usuario y dominios en los reportes de auditoría.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Inspección no destructiva de puertos y firewall
ss -tulpn
sudo ufw status verbose
```

### ▶️ Si estás en Hermes Agent:
```python
# Comprobar estado de sshd_config mediante el terminal
result = terminal(command="grep -E '^(PermitRootLogin|PasswordAuthentication|Port)' /etc/ssh/sshd_config", timeout=30)
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Diagnosticar sockets abiertos y puertos
const sockets = await shell.exec("ss -tulpn | grep LISTEN");
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Proporcionar el script de auditoría y comandos al usuario:
# "Ejecuta 'sudo ss -tulpn' y 'sudo ufw status verbose' para comparar puertos abiertos vs firewall."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Provee al usuario una lista de comandos de diagnóstico de una sola línea (`ss -tulpn`, `ufw status`, `systemctl status fail2ban`).
2. Pide que comparta las salidas (con IPs enmascaradas).
3. Evalúa la postura de seguridad y genera recomendaciones de endurecimiento paso a paso.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Revisar sockets | `ss -tulpn` vía terminal | Pedir salida de `ss -tulpn` |
| Estado de firewall | `ufw status` / `iptables -L -n -v` | Pedir salida de reglas activas del firewall |
| Configuración SSH | Lectura de `/etc/ssh/sshd_config` | Pedir al usuario contenido filtrado con grep |
| Binarios SUID | `find / -perm -4000 2>/dev/null` | Proveer comando y pedir revisar binarios inusuales |

---

## ✅ Verificación

- `PermitRootLogin` está en `no` o `prohibit-password`.
- `PasswordAuthentication` está en `no` (forzando autenticación por llaves públicas).
- El cortafuegos está activo y no expone servicios internos no autenticados a Internet.
- Las cárceles de Fail2ban monitorean los puertos y servicios correctos.
- No se detectaron binarios SUID anómalos ni privilegios sudo desmedidos.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
