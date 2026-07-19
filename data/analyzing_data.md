---
name: analyzing-data
description: Parses CSV/JSON datasets, cleans data values, calculates key business metrics, and formats tabular summaries. Use when asked to parse datasets, clean data logs, calculate averages, or generate formatted data tables.
version: 1.0.0
tags: [universal, data, analysis]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Data Analyst

## 🎯 Objetivo

Convert raw data records into structured, high-value metrics, exposing patterns and anomalies while ensuring data classification compliance, secret redaction, and PII protection.

## 🕒 Cuándo usar

- Cuando se solicita analizar registros de datos raw en CSV, JSON o texto.
- Al limpiar registros o tablas desordenadas (inconsistencias de formato, valores en blanco).
- Al calcular métricas de negocio clave (totales, promedios, porcentajes, tendencias).
- Al formatear datos numéricos en tablas Markdown altamente estructuradas.

## 🛡️ Principios Universales

1. **PII and PHI Detection**: Scan all records for sensitive data (SSNs, emails, phone numbers). Mask or redact sensitive information.
2. **Secrets Scan Pass (Security Gate)**: Ingested data must be scanned for API keys, passwords, and connection strings. Redact with `[REDACTED]`.
3. **Float Artifact Prevention**: All numeric outputs must pass through rounding mechanisms (e.g., `Math.round()` or `.toFixed(2)`).
4. **File Size Cap**: Enforce a 50 MB limit on ingested files.
5. **Least Privilege**: Always request minimum required permissions to read or write database datasets.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Leer datasets locales usando las herramientas nativas
# Usar read_file para leer datasets y procesarlos
```

### ▶️ Si estás en Hermes Agent:

```python
# Usar herramientas nativas de Hermes para cargar y procesar
content = read_file(path="dataset.csv", limit=5000)
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar MCP filesystem para leer datos
const content = await filesystem.readFile("dataset.csv");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guíar al usuario si no hay herramientas de terminal o archivo:
# Pide: "Por favor, copie y pegue las primeras 100 líneas del archivo dataset.csv"
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Solicita al usuario: "Por favor, copia y pega el contenido del dataset o las primeras líneas aquí".
2. Procesa la información mediante razonamiento en el contexto del chat.
3. Genera la tabla Markdown resumida para el usuario.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Leer dataset | read_file() / filesystem.readFile() | Pedir al usuario que copie y pegue el contenido |
| Escribir reporte | write_to_file() | Mostrar el reporte en el chat para que el usuario lo guarde |
| Consultar base de datos | postgres.query() | Generar SQL exacto para que el usuario lo ejecute y pegue el resultado |

---

## ✅ Verificación

- El archivo de salida contiene la clasificación de datos correcta.
- No hay floats sin redondear.
- Toda la información PII y secretos ha sido detectada y redactada.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
