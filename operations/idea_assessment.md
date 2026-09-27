---
name: idea-assessment
description: Pre-implementation feasibility and spike framework. Use when evaluating new product ideas, technical spikes, library migrations, or architectural alternatives before committing engineering effort (Intake -> Research -> Shape -> Decide).
version: 1.0.0
tags: [universal, strategy, operations, engineering, feasibility, decision-matrix, spikes]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Idea & Feasibility Assessment

## 🎯 Objetivo

Evaluate whether a proposed feature, architectural pivot, or technical initiative deserves investment, delivering an evidence-backed scorecard (**Go**, **Clarify**, or **Stop**) and bounded solution shape before engineering effort is committed.

## 🕒 Cuándo usar

- Ante preguntas estratégicas de arquitectura o producto ("¿Deberíamos migrar a GraphQL?", "¿Es viable implementar WebSockets aquí?", "¿Deberíamos usar X biblioteca?").
- Antes de comenzar tareas grandes de refactorización o integración de servicios externos.
- Para definir el apetito de tiempo/esfuerzo y delimitar las madrigueras ("Rabbit Holes") que deben evitarse deliberadamente.

## 🛡️ Principios Universales

1. **Evidence-Based Evaluation:** Evaluar con hechos y pruebas técnicas, no con preferencias subjetivas. Comparar costo de mantenimiento, latencia, seguridad y curva de aprendizaje.
2. **Four-Stage Process:** Toda evaluación sigue rigurosamente:
   - **Etapa 1 — Entrada y Planteamiento:** Problema real del usuario, métricas de éxito y beneficiarios.
   - **Etapa 2 — Investigación Técnica:** Compatibilidad con la arquitectura existente, alternativas en el ecosistema, riesgos.
   - **Etapa 3 — Modelado del Alcance (Shape):** Delimitar el apetito temporal y documentar trampas fuera de alcance.
   - **Etapa 4 — Scorecard de Decisión:** Emitir veredicto fundamentado: 🟢 **GO**, 🟡 **CLARIFY**, o 🔴 **STOP**.
3. **No Premature Implementation:** Prohibido comenzar a programar la solución hasta que el veredicto sea **GO** y se active `spec-driven-development`.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Investigar dependencias y licencias en el ecosistema
npm view <package> dependencies license
```

### ▶️ Si estás en Hermes Agent:
```python
# Realizar búsqueda o verificación de documentación
result = web_search("benchmark postgres pgvector vs qdrant")
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Inspeccionar compatibilidad de la base de código actual
const pkg = JSON.parse(await readFile("package.json"));
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Presentar la matriz comparativa de pros y contras al usuario:
# "¿Deseas evaluar el impacto en infraestructura antes de decidir adoptar esta dependencia?"
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Formula las preguntas de apetito de tiempo y restricciones de infraestructura al usuario.
2. Compara las alternativas en una tabla multidimensional (Facilidad de mantenimiento, Seguridad, Rendimiento, Riesgo de bloqueo/Vendor lock-in).
3. Emite el veredicto final justificado (GO, CLARIFY o STOP).

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Búsqueda de ecosistema | `search_web` / MCP | Evaluación basada en documentación conocida y análisis crítico |
| Verificación de dependencias | Herramientas de lectura de manifiestos | Pedir al usuario su stack y dependencias clave |
| Scorecard | Formato Markdown estructurado | Tabla de decisión directa en el chat |

---

## ✅ Verificación

- Se definió claramente el problema que resuelve la iniciativa.
- Se cuantificaron los riesgos de seguridad, costo operativo y mantenimiento.
- Se fijaron los límites de lo que NO se construirá (Rabbit Holes).
- Se emitió un veredicto definitivo (GO, CLARIFY, o STOP) con justificación técnica.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
