---
name: docum-md
description: Manages developer and agent session logs inside a hidden, git-ignored folder (CHG-Review). Use when the user requests project documentation, session tracking, daily progress reports, or immediately after executing a git push command.
version: 1.0.0
tags: [universal, operations, session, documentation]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Session Review Documenter

## 🎯 Objetivo

Manage developer and agent session logs inside a hidden, git-ignored folder (`CHG-Review`), ensuring that all changes are securely documented without leaking PII, secrets, or configurations, and restricting local directory access to the current user.

## 🕒 Cuándo usar

- Inmediatamente después de ejecutar `git push`.
- Al compilar resúmenes de progreso diarios o semanales.
- Al final de una sesión larga del agente para guardar registro de decisiones, cambios y resultados.

## 🛡️ Principios Universales

1. **CHG-Review Folder Security**: Hidden directory restricted to the current executing user (e.g. `chmod 700` or NTFS permissions).
2. **Never Push to Git**: `CHG-Review/` must always be ignored in `.gitignore`. Never track it.
3. **Secrets Sanitization**: Automatically strip keys, tokens, and raw IP addresses from log files.
4. **No Absolute Paths**: Avoid referencing the absolute home directories of the user in generated reports.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Escribir registros en CHG-Review/ y correr comandos locales para verificar git ignore
# Ocultar carpeta usando comandos del sistema de archivos local
```

### ▶️ Si estás en Hermes Agent:

```python
# Usar read_file y write_file para guardar el log del dia
content = write_file(path="CHG-Review/2026-07-18.md", content="...")
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP de filesystem para administrar logs locales
await filesystem.writeFile("CHG-Review/2026-07-18.md", sessionSummary);
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al desarrollador:
# Pide: "Crea la carpeta CHG-Review/ y agrega este resumen de sesión en un archivo de texto."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera el resumen estructurado usando la plantilla oficial.
2. Recuerda al usuario: "Guarda esto en tu archivo local git-ignorado de registro diario bajo la carpeta `CHG-Review/`".
3. Genera comandos manuales para inicializar y restringir la carpeta si es necesario.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Inicializar carpeta | `docum-helper` / terminal | Pedir al usuario que cree la carpeta y la oculte |
| Guardar log de sesión | write_to_file() | Mostrar markdown del log en chat para guardado manual |
| Ocultar carpeta | terminal / attrib +h | Dar instrucciones al usuario para ocultar la carpeta en su OS |

---

## ✅ Verificación

- La carpeta `CHG-Review` está listada en `.gitignore`.
- Los logs no contienen claves ni IPs duras.
- El log del día fue creado.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
