---
name: systematic-debugging
description: Root-cause-first software debugging and bug fixing harness. Enforces reproduction before modification, surgical minimal patching, and regression verification (Assess -> Fix -> Test).
version: 1.0.0
tags: [universal, engineering, operations, debugging, troubleshooting, root-cause, testing]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Systematic Debugging

## 🎯 Objetivo

Diagnose and repair software defects with absolute certainty, enforcing GitHub Spec-Kit's 3-phase debugging protocol (**Assess $\rightarrow$ Fix $\rightarrow$ Test**) and the "Root-Cause First" mandate. Eliminate speculative patching, unverified fixes, and accidental regressions.

## 🕒 Cuándo usar

- Ante cualquier error, excepción en tiempo de ejecución, fallo de assertions o stack trace.
- Cuando una prueba unitaria, de integración o E2E falle en el pipeline o en local.
- Cuando un endpoint de API devuelva códigos de error inesperados (HTTP 500, 422, datos corruptos).
- Para reparar bugs de forma quirúrgica sin alterar comportamiento no relacionado.

## 🛡️ Principios Universales

1. **Root-Cause First:** Nunca adivinar rutas, flags o suponer la causa. Leer los archivos fuente involucrados y reproducir el fallo antes de alterar una sola línea de código.
2. **Reproduction Mandate:** Crear un script de reproducción mínimo o un caso de test que falle de manera determinista demostrando el bug.
3. **Surgical Minimal Patching:** Modificar estrictamente las líneas necesarias para subsanar la causa raíz. Cero refactorizaciones no solicitadas, formateos masivos o cambios colaterales.
4. **Three-Attempt Backoff:** Si una solución falla dos veces, detenerse, releer el output del error, reformular la hipótesis. Si falla tres veces, pausar y reportar el bloqueo con evidencia al usuario.
5. **Regression Defense:** Una vez aplicado el parche, ejecutar el test de reproducción (que ahora debe pasar) y la suite completa existente para garantizar cero regresiones.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# 1. Ejecutar test de reproducción que falla
pytest tests/test_reproduce_bug.py
# 2. Tras aplicar parche quirúrgico, verificar éxito
pytest tests/test_reproduce_bug.py
# 3. Ejecutar suite completa
pytest
```

### ▶️ Si estás en Hermes Agent:
```python
# Ejecutar suite de pruebas mediante el terminal
result = terminal(command="npm test", timeout=120)
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Correr el test de reproducción específico
const result = await shell.exec("npx jest -t 'handles null user token'");
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Guiar al desarrollador en el aislamiento del bug:
# "Ejecuta este comando para reproducir el fallo: 'go test -v -run TestBrokenEndpoint'."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Pide al usuario el stack trace completo y las líneas de código circundantes.
2. Escribe una prueba conceptual o paso a paso para reproducir la condición de fallo.
3. Provee el diff quirúrgico exacto explicando por qué resuelve la causa raíz.
4. Pide al usuario que corra la prueba y confirme el resultado antes de cerrar la tarea.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Ejecutar pruebas | `terminal("npm test")` / MCP | Pedir al usuario que corra el comando y pegue el log |
| Analizar logs | `docker_logs` / `parse_log_file` | Pedir las últimas 50 líneas del log de error |
| Aplicar parches | Herramientas de edición de archivos | Proveer bloques de diff unificado (`diff -u`) |

---

## ✅ Verificación

- Se reprodujo el fallo con evidencia directa antes de editar el código.
- Se identificó la causa raíz exacta (no solo un síntoma superficial).
- El parche aplicado es quirúrgico y respeta el alcance estricto.
- La prueba de reproducción pasa exitosamente.
- No se introdujeron regresiones en los tests adyacentes.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
