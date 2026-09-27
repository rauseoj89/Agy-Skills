---
name: security-audit
description: Autonomous coverage-led vulnerability hunting harness. Use for comprehensive security audits, code reviews, penetration tests, or vulnerability research across APIs, microservices, daemons, and client applications.
version: 1.0.0
tags: [universal, security, audit, penetration-testing, vulnerability-hunting, adversarial-verification]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Autonomous Security Audit Harness

## 🎯 Objetivo

Conduct systematic, coverage-led vulnerability discovery and penetration auditing across codebases, APIs, and microservices using Cloudflare's 6-phase audit harness: reconnaissance, coverage ledger mapping, isolated hunting, adversarial disproof verification, schema validation, and multi-document reporting.

## 🕒 Cuándo usar

- Al realizar auditorías de seguridad completas o pentests sobre un repositorio o servicio.
- Al evaluar aplicaciones con IA/LLM contra inyecciones de prompts directas/indirectas o secuestro de herramientas.
- Al revisar APIs, middlewares y capas de autenticación contra OWASP Top 10, SSRF, IDOR y race conditions.
- Al generar artefactos de auditoría formales (`architecture.md`, `coverage-ledger.json`, `findings.json`, `REPORT.md`).

## 🛡️ Principios Universales

1. **Coverage-Led Hunting:** Auditar cada endpoint, controlador y worker mapeado en un libro de cobertura (`coverage-ledger.json`). Ningún componente queda sin inspeccionar.
2. **Adversarial Disproof Verification:** Para cada candidato a vulnerabilidad, adoptar un rol adversarial que busque activamente refutar o desacreditar el hallazgo (buscar sanitizaciones, middlewares, o invariantes de tipo). Solo los hallazgos validados con taint trace se reportan.
3. **Citation & Line Verification:** Cada hallazgo debe citar archivos y líneas exactas con fragmentos de código reproducibles.
4. **Structured Schema Validation:** Los hallazgos deben conformar un esquema estructurado (ID, severidad CVSS, CWE, impacto, prueba de concepto y remediación precisa).
5. **No Blind Hallucinations:** Nunca declarar una vulnerabilidad sin evidencia verificable en el código fuente.

---

## 🔄 El Ciclo de Auditoría en 6 Fases

1. **Fase 1 — Reconocimiento y Mapeo:** Identificar límites de confianza, flujos de datos sensibles y compilar `coverage-ledger.json`.
2. **Fase 2 — Caza Dirigida por Cobertura:** Evaluar cada unidad contra vectores OWASP, inyecciones (SQL/Command/SSRF), fallos lógicos y riesgos de IA.
3. **Fase 3 — Validación Adversarial:** Intentar refutar la explotabilidad del hallazgo. Trazar la entrada no confiable hasta el sumidero (sink).
4. **Fase 4 — Salida Estructurada:** Generar `findings.json` con metadatos de severidad, CWE y vector de ataque.
5. **Fase 5 — Verificación de Citaciones:** Re-comprobar que todas las líneas y archivos citados existan y no hayan sido modificados.
6. **Fase 6 — Reporte Multi-Documento:** Publicar el resumen ejecutivo `REPORT.md` con recomendaciones y plan de mitigación.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Ejecutar validación de esquema de hallazgos
node -e 'const f = require("./findings.json"); console.log(`Total Findings: ${f.findings?.length || 0}`);'
```

### ▶️ Si estás en Hermes Agent:
```python
# Mapear archivos del repositorio para el coverage ledger
import os, json
routes = [f for f in os.listdir(".") if f.endswith(".go") or f.endswith(".ts")]
print(f"Coverage candidates: {len(routes)}")
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Leer estructura de rutas y controladores para construir coverage-ledger.json
const files = await listFiles("src/controllers");
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Guiar la auditoría por fases:
# "Revisa 'src/api/auth.ts' y verifica si los tokens de reseteo tienen verificación de expiración."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Solicita al usuario los archivos de rutas, autenticación y controladores principales.
2. Aplica el análisis de flujo de datos y taint tracking visualmente.
3. Emite el reporte de auditoría con severidades (Crítica, Alta, Media, Baja) y código de mitigación listo para aplicar.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Mapear superficie | `find` / `grep` / lectura de directorios | Pedir al usuario el árbol de archivos y rutas principales |
| Validación de esquema | Script de validación JSON / linter | Verificación manual de claves en `findings.json` |
| Verificación de código | `view_file` / lectura con offset | Pedir al usuario el bloque exacto alrededor del sink |

---

## ✅ Verificación

- Se completó el mapeo en `coverage-ledger.json`.
- Cada hallazgo en `findings.json` tiene prueba de concepto o traza taint confirmada.
- Ningún falso positivo resistió la fase de validación adversarial.
- Se emitió el reporte `REPORT.md` con pasos de mitigación reproducibles.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
