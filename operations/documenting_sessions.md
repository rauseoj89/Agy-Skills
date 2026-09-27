---
name: docum-md
description: Manages developer and agent session logs inside a hidden, git-ignored folder (CHG-Review). Enforces Global Agent Rule 6 reporting, atomic writes, MCP data sanitization, and SDD/debugging alignment upon session completion or git push.
version: 1.1.0
tags: [universal, operations, session, documentation, audit, rule-6]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Session Review Documenter

## 🎯 Objetivo

Manage developer and agent session logs inside a hidden, git-ignored folder (`CHG-Review`), ensuring that all changes, decisions, and verifications are securely documented according to **Global Agent Rule 6**, without leaking PII, secrets, database dumps, or infrastructure configurations.

## 🕒 Cuándo usar

- Inmediatamente después de ejecutar `git push`.
- Al compilar resúmenes de progreso diarios o semanales.
- Al final de una sesión larga de desarrollo para registrar decisiones arquitectónicas y evidencias de pruebas.
- Al documentar el cierre de fases bajo Specification-Driven Development (SDD) o resolución de bugs bajo Systematic Debugging.

## 🛡️ Principios Universales

1. **CHG-Review Folder Security**: Carpeta oculta restringida al usuario en ejecución (`chmod 700` en POSIX / permisos NTFS en Windows).
2. **Never Push to Git**: `CHG-Review/` siempre debe estar declarado en `.gitignore`. Nunca ejecutar `git add` sobre esta carpeta.
3. **Global Agent Rule 6 Alignment**: Todo registro debe contener obligatoriamente las 4 secciones estándar:
   - **Changed:** Archivos exactos modificados o creados.
   - **Verified:** Comandos ejecutados y resultados observados en terminal.
   - **Not Verified / Assumptions:** Pruebas omitidas, supuestos de dependencias o rutas no verificadas.
   - **Risks & Rollback:** Pasos y comandos de reversión exactos (`git revert <sha>` / rollback de migración).
4. **Data & MCP Sanitization**: Limpiar automáticamente claves, tokens, direcciones IP privadas y volcados de datos de bases de datos (`postgres-mcp`) o rutas de Vault (`vault-bridge-mcp`).
5. **Atomic Buffering**: Escribir entradas mediante un archivo intermedio (`.tmp`) antes de anexar al archivo de log para evitar corrupción por interrupciones.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Inicializar carpeta restringida si no existe y registrar sesión
mkdir -p CHG-Review && chmod 700 CHG-Review
# Escribir en CHG-Review/$(date +%Y-%m-%d).md
```

### ▶️ Si estás en Hermes Agent:
```python
# Usar write_file con plantilla estructurada de Regla 6
content = write_file(path="CHG-Review/2026-09-26.md", content="### 🚀 Session Entry...\n#### 📂 Changed: ...")
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Usar el MCP de filesystem para redactar y guardar el log de sesión
await filesystem.writeFile("CHG-Review/" + new Date().toISOString().slice(0,10) + ".md", sessionSummary);
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Guiar al desarrollador:
# "He estructurado el resumen de la sesión bajo la Regla 6. Por favor guárdalo en tu carpeta local CHG-Review/."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Genera el resumen estructurado en el chat aplicando la plantilla oficial de la Regla 6.
2. Recuerda al usuario: "Guarda esto en tu archivo local git-ignorado de registro diario bajo la carpeta `CHG-Review/`".
3. Provee el comando para asegurar los permisos de la carpeta (`chmod 700 CHG-Review`).

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Inicializar carpeta | `mkdir -p CHG-Review && chmod 700` | Instruir al usuario a crear la carpeta y permisos |
| Guardar log de sesión | `write_to_file` con atomic buffer | Mostrar markdown formateado para copiar y pegar |
| Sanitización de datos | Scrubbing automático de regex | Verificación estática visual en el texto generado |

---

## ✅ Verificación

- La carpeta `CHG-Review/` está declarada en el archivo `.gitignore` del proyecto.
- Los permisos de la carpeta impiden el acceso a otros usuarios (`chmod 700`).
- La entrada contiene las 4 secciones obligatorias de la Regla 6 (Changed, Verified, Not Verified, Risks & Rollback).
- No se filtraron contraseñas, volcados de registros de bases de datos ni IPs internas.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.1.0
