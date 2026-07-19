---
name: creating-agy-mcps
description: Automates the blueprinting, structural setup, and Git deployment workflow for new or modified Model Context Protocol (MCP) servers in the Agy-MCP repository. Use when the user requests to create or modify an MCP server.
version: 1.0.0
tags: [universal, operations, mcp, blueprint]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Agy-MCP Blueprint Automator

## 🎯 Objetivo

Automate the blueprinting, structure generation, and deployment of custom Model Context Protocol (MCP) servers inside the Agy-MCP repository, while strictly maintaining security, path isolation, least privilege, and input validation.

## 🕒 Cuándo usar

- Al diseñar, crear o modificar planos (blueprints) de servidores MCP.
- Al crear integraciones personalizadas conectando APIs o bases de datos externas con el workspace del agente.

## 🛡️ Principios Universales

1. **No Hardcoded Secrets**: Use placeholders like `${VAULT_SECRET_<MCP-NAME>_<KEY>}`.
2. **No Production IPs**: Use `${TARGET_HOST}` or `localhost` in configurations.
3. **No Raw Shell Exec**: Use array-based argument parsing to prevent shell injection.
4. **Least Privilege**: Minimal scopes by default. Read-only preferred.
5. **Path Isolation**: Never hardcode user absolute paths. Use placeholder variables like `${AGY_MCP_DIR}`.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Crear la estructura de carpetas en el repositorio local Agy-MCP
# Usar read_file/write_file nativos para crear BLUEPRINT.md
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar terminal o herramientas de archivos para crear carpetas
# Crear mcp-blueprints/<mcp-name>/BLUEPRINT.md
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP de filesystem para crear directorios y escribir BLUEPRINT.md y schemas/tools.json
await filesystem.createDirectory("mcp-blueprints/my-mcp");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al usuario paso a paso:
# Pide: "Crea un folder mcp-blueprints/nombre-mcp y guarda este BLUEPRINT.md"
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera el contenido de `BLUEPRINT.md` y `schemas/tools.json`.
2. Solicita al usuario que cree la estructura de carpetas manualmente.
3. Pide al usuario que guarde los contenidos en sus respectivos destinos y te confirme el resultado.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Crear Directorios | write_to_file() / create_directory() | Pedir al usuario que cree la carpeta |
| Validar Schema JSON | Librerías de validación local | Validar sintaxis mediante el motor de la IA |
| Deploy en Git | git.commit() / terminal("git push") | Proporcionar los comandos de Git para que el usuario los ejecute |

---

## ✅ Verificación

- El JSON Schema pasa la validación sin errores sintácticos.
- `BLUEPRINT.md` cubre las 6 secciones requeridas de arquitectura y seguridad.
- No hay paths absolutos del host local.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
