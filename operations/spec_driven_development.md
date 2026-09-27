---
name: spec-driven-development
description: Enforces Specification-Driven Development (SDD). Use when building new features, modules, or services. Guides the agent through formal spec authoring (spec.md), technical planning (plan.md), task matrix generation (tasks.md), and incremental code convergence.
version: 1.0.0
tags: [universal, engineering, operations, sdd, spec-kit, planning, architecture]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Specification-Driven Development (SDD)

## 🎯 Objetivo

Eliminate agent drift, hallucinated assumptions, and unverified code generation by enforcing GitHub's Spec-Kit methodology: carrying every feature request through a formal progression of `spec.md` $\rightarrow$ `plan.md` $\rightarrow$ `tasks.md` before authoring implementation code.

## 🕒 Cuándo usar

- Al abordar requerimientos no triviales (>1 archivo o cambios estructurales/arquitectónicos).
- Al diseñar o crear nuevos componentes, APIs, contratos o microservicios.
- Cuando una solicitud es ambigua y requiere clarificación de alcance antes de programar.
- Para prevenir scope-creep delimitando explícitamente lo que está "Fuera de Alcance" (Out of Scope).

## 🛡️ Principios Universales

1. **Contracts Before Code:** Definir esquemas de datos, interfaces TypeScript o especificaciones OpenAPI 3.1 antes de escribir la lógica de negocio.
2. **Deterministic Triad Progression:** Todo desarrollo estructurado sigue:
   - `spec.md`: Define el **QUÉ** (Historias de usuario, Criterios de Aceptación con Gherkin, Fuera de Alcance).
   - `plan.md`: Define el **CÓMO** (Arquitectura, diagramas de flujo, modelos de datos, contratos).
   - `tasks.md`: Define los **PASOS** (Matriz ordenada de fases atómicas con checkboxes dependientes).
3. **No Code Drift:** No saltar directamente a modificar código sin que el plan y los contratos estén alineados y aprobados.
4. **Incremental Convergence:** Implementar y verificar fase por fase, marcando las tareas en `tasks.md` tras validar su funcionamiento real.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Crear directorio de especificaciones y validar estructura de tareas
mkdir -p specs/feature-name
# Escribir spec.md, plan.md, tasks.md
```

### ▶️ Si estás en Hermes Agent:
```python
# Escribir el plan técnico y la matriz de tareas
with open("plan.md", "w") as f:
    f.write("# Plan de Implementación...")
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Usar las herramientas de archivos para crear la progresión spec.md -> plan.md -> tasks.md
await writeFile("specs/spec.md", specContent);
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Proponer el plan al usuario antes de modificar archivos de producción:
# "He redactado la especificación y el plan técnico. Por favor revisa y aprueba para comenzar."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Redacta el `spec.md` (Historias de usuario en formato Gherkin + Criterios de Aceptación) directamente en el chat.
2. Diseña el `plan.md` con los contratos de interfaz (TypeScript / OpenAPI / SQL DDL).
3. Presenta la lista de tareas numeradas y solicita confirmación del usuario antes de emitir el código fuente.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Creación de artefactos | `write_to_file` / MCP de filesystem | Generar bloques Markdown en el chat para guardar |
| Seguimiento de tareas | Edición interactiva de `tasks.md` | Actualizar checklist en las respuestas del chat |
| Verificación de contratos | Linters / validadores de esquema | Verificación estática visual de tipos y esquemas |

---

## ✅ Verificación

- Existe un `spec.md` con historias de usuario y criterios de aceptación claros.
- Se documentó explícitamente qué queda fuera del alcance para evitar sobreingeniería.
- Los contratos e interfaces (`plan.md`) se definieron antes de iniciar la codificación.
- Las tareas en `tasks.md` se marcan como completadas únicamente tras evidencia verificable.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
