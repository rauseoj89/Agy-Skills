---
name: executing-sop-and-runbooks
description: Parses, verifies, and executes Standard Operating Procedures (SOPs) and technical runbooks. Use when asked to follow an SOP, run a system migration, execute a deployment checklist, or automate system maintenance.
version: 1.0.0
tags: [universal, operations, runbook, sop]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Runbook & SOP Orchestrator

## 🎯 Objetivo

Ejecutar procedimientos técnicos paso a paso con validación, gestión de confirmaciones para operaciones destructivas, y rollback automatizado.

## 🕒 Cuándo usar

- Al ejecutar un Procedimiento Operativo Estándar (SOP) paso a paso.
- Al desplegar migraciones de base de datos, actualizaciones de infraestructura o despliegues.
- Al realizar tareas de mantenimiento del sistema recurrentes.

## 🛡️ Principios Universales

1. **Destructive Action Gate**: Never run destructive operations (e.g. `DROP`, `rm -rf`, `docker rm`) without explicit user validation.
2. **Validation Loop**: Always follow the Test -> Execute -> Verify loop.
3. **Least Privilege**: Annotate steps with `operator` (read-only/audit) vs `admin` (write/deploy).
4. **Secrets Isolation**: No secrets in logs or terminal parameters.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
antigravity-runbook execute runbook.md --confirm-destroy
antigravity lock acquire runbook-execution
# Secrets se inyectan automáticamente de vault
```

### ▶️ Si estás en Hermes Agent:

```python
# Usa read_file para cargar el runbook
runbook = read_file(path="runbook.md", limit=500)
# Mapear pasos a todo list
todo(todos=[{"id": "step1", "content": "...", "status": "pending"}])
# Ejecutar con confirmation
result = terminal(command="...", timeout=300)
# Si falla:
terminal(command="/rollback")
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
const runbook = await filesystem.readFile("runbook.md");
// Crear tasks manualmente
await tasks.create({name: "Step 1", status: "pending"});
// Ejecutar comandos
await shell.exec("tu-comando");
// Fallback si falla: generar script de rollback
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Pide al usuario: "Por favor, abre el archivo `runbook.md` y copia y pega su contenido".
2. Analiza el runbook proporcionado.
3. Genera los comandos exactos y detalla su nivel de riesgo (Destructive Gate).
4. Pide al usuario: "Ejecuta cada comando en tu terminal y pega el resultado".
5. Verifica manualmente con el usuario antes de proceder al siguiente paso.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Leer runbook | read_file() | Pedir al usuario que pegue el contenido |
| Ejecutar paso | terminal() / shell.exec() | Generar comando para que el usuario lo ejecute |
| Verificar éxito | check_status() | Pedir al usuario que pegue el output para verificar |

---

## ✅ Verificación

- Todos los pasos del runbook terminaron en estado PASS.
- El pre-flight check de CPU y disco pasó correctamente.
- Se ha generado un reporte final estructurado y guardado como `report_runbook.md`.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
