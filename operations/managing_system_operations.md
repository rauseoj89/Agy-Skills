---
name: managing-system-operations
description: Automates local backup routines, organizes project directories, checks system settings, and diagnoses logs. Use when asked to manage folders, run cleanups, set up local backups, diagnose diagnostic issues, or automate scripts.
version: 1.0.0
tags: [universal, operations, system, backup]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Personal System Administrator

## 🎯 Objetivo

Automate repetitive directory management tasks, protect local data integrity, and diagnose local systems efficiently.

## 🕒 Cuándo usar

- Al limpiar, estructurar u organizar carpetas y archivos locales.
- Al crear scripts de copia de seguridad local.
- Al verificar permisos, espacio en disco o logs de la aplicación local.

## 🛡️ Principios Universales

1. **Destructive Action Gate**: Bulk moves, deletions, and folder removals must be explicitly approved.
2. **Secrets Scan**: Scan for `.env` or credential files before performing operations. Exclude them from general moves.
3. **Backup Space Limits**: Check disk space before executing backups. Keep a max of 5 historical backups.
4. **No Hardcoded Absolute Paths**: Use relative paths or placeholders instead of hardcoded home folders.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Ejecutar comandos de copia y organización locales (tar, Move-Item, etc.)
# Usar get_system_stats para verificar salud
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar terminal para ejecutar diagnósticos o comprimir directorios
result = terminal(command="tar -czf backup.tar.gz ./src", timeout=120)
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP filesystem y terminal para comprimir y organizar archivos
const result = await shell.exec("tar -czf backup.tar.gz ./src");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Proporcionar el script de PowerShell o bash exacto para que el usuario lo ejecute:
# Pide: "Ejecuta este comando para hacer el backup: tar -czf backup.tar.gz ./src"
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera los comandos exactos de archivado o script de limpieza.
2. Pide al usuario: "Ejecuta estos comandos en tu terminal local para organizar tus carpetas".
3. Solicita confirmación visual del estado del espacio en disco resultante.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Comprimir archivos | `tar` / terminal() | Dar comando de compresión al usuario |
| Verificar espacio en disco | get_system_stats() | Pedir al usuario que corra `df -h` o mire el explorador |
| Organizar archivos | write_to_file() / terminal("mv") | Generar el script de reubicación para el usuario |

---

## ✅ Verificación

- La copia de seguridad excluye directorios pesados e innecesarios (e.g. `node_modules`).
- Se verificó que el espacio en disco restante sea saludable.
- La rotación de logs mantiene un límite estricto de hasta 5 archivos históricos.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
