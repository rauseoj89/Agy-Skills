---
name: creating-agy-skills
description: Automates the blueprinting, creation, and Git deployment workflow for new or modified Skills inside the Agy-Skills repository. Use when the user requests to create, design, or update a Skill.
version: 1.0.0
tags: [universal, operations, skills, creation]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Agy-Skills Creator

## 🎯 Objetivo

Automate the creation, blueprinting, indexing, and Git deployment of custom operational skill files inside the external Agy-Skills repository while enforcing absolute security, standardized formatting, and local synchronization.

## 🕒 Cuándo usar

- Al crear nuevos skills o modificar los existentes en el repositorio de Agy-Skills.
- Al organizar comportamientos de agentes y reglas operativas en archivos planos y modulares.

## 🛡️ Principios Universales

1. **No Hardcoded Secrets**: Ensure NO passwords or credentials are hardcoded. Use vault or env vars.
2. **No Production IPs**: Use `${TARGET_HOST}` or `localhost` in examples.
3. **No Raw Shell Exec**: Use array-based argument structures for command examples.
4. **Security Checklist**: Every skill must have a verification checklist with a minimum of 4 items, with the first being secrets-related.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Escribir el nuevo skill directamente a su ruta en el workspace
# Copiar al directorio local de skills en ~/.gemini/antigravity/skills/
```

### ▶️ Si estás en Hermes Agent:

```python
# Crear y guardar el nuevo skill usando herramientas nativas de Hermes
content = write_file(path="skills/data/new_skill.md", content="...")
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP filesystem para guardar el archivo markdown
await filesystem.writeFile("skills/data/new_skill.md", skillContent);
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Si no hay terminal ni filesystem tools:
# Guiar al usuario para que guarde el archivo en la ruta correspondiente.
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera el contenido markdown completo del nuevo skill.
2. Pide al usuario: "Por favor, crea el archivo en la carpeta `operations/` o la categoría que corresponda y pega este contenido".
3. Proporciona el comando de Git para subir los cambios.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Crear archivo de skill | write_to_file() | Proporcionar markdown en chat para guardar manualmente |
| Actualizar el README | edit_file() | Pedir al usuario que añada la línea al README |
| Sync Local de Skills | Copiar a carpeta de agentes local | Pedir al usuario que reinicie la sesión o cargue las reglas |

---

## ✅ Verificación

- El archivo de salida contiene las secciones requeridas.
- Pasa la validación de `scripts/validate-skill.py`.
- No contiene secretos ni IPs duras.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
