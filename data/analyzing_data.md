---
name: analyzing-data
description: Parses CSV/JSON datasets, cleans data values, calculates key business metrics, and formats tabular summaries. Use when asked to parse datasets, clean data logs, calculate averages, or generate formatted data tables.
version: 1.1.0
tags: [universal, data, analysis]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Data Analyst

## 🎯 Objetivo

Convert raw data records and documents into structured, high-value metrics, exposing patterns and anomalies while ensuring data classification compliance, secret redaction, and PII protection.

## 🕒 Cuándo usar

- Cuando se solicita analizar registros de datos raw en CSV, JSON, Excel, PDF o texto plano.
- Al limpiar registros o tablas desordenadas (inconsistencias de formato, valores en blanco, espacios).
- Al calcular métricas de negocio clave (totales, promedios, medianas, porcentajes, tendencias).
- Al formatear datos numéricos en tablas Markdown altamente estructuradas o exportar a hojas de cálculo (.xlsx).

## 🛡️ Principios Universales

1. **PII and PHI Detection**: Scan all records for sensitive data (SSNs, emails, phone numbers). Mask or redact sensitive information.
2. **Secrets Scan Pass (Security Gate)**: Ingested data must be scanned for API keys, passwords, and connection strings. Redact with `[REDACTED]`.
3. **Float Artifact Prevention**: All numeric outputs must pass through rounding mechanisms (e.g., `Math.round()` or `.toFixed(2)`).
4. **File Size Cap**: Enforce memory limits (max 50 MB / 100,000 rows) on ingested files.
5. **Least Privilege**: Always request minimum required permissions to read or write database datasets.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Ingestión con data-analyst-mcp:
# parse_csv(path="dataset.csv", max_rows=50000)
# parse_excel(path="report.xlsx", sheet_name="Sheet1")
# extract_pdf_data(path="document.pdf")
# read_word_document(path="notes.docx")

# Limpieza y métricas:
# clean_tabular_data(records=data, null_strategy="drop", trim_strings=true)
# calculate_metrics(records=cleaned_data, numeric_columns=["revenue", "cost"])

# Generación de Excel con office-mcp:
# write_excel_sheet(filePath="summary.xlsx", data=excel_payload)
```

### ▶️ Si estás en Hermes Agent:

```python
# Usar herramientas nativas de Hermes o scripts Python para cargar y procesar
content = read_file(path="dataset.csv", limit=5000)
# Procesar con pandas / in-memory analytics
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar MCP data-analyst o filesystem para leer y transformar datos
const dataset = await data_analyst.parse_csv({ path: "dataset.csv" });
const metrics = await data_analyst.calculate_metrics({ records: dataset.rows, numeric_columns: ["amount"] });
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al usuario si no hay herramientas de terminal o archivo:
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
| Ingestar CSV / Excel | `parse_csv()` / `parse_excel()` | Pedir al usuario que copie y pegue el contenido |
| Ingestar PDF / Word | `extract_pdf_data()` / `read_word_document()` | Pedir al usuario texto extraído |
| Limpiar datos | `clean_tabular_data()` | Limpieza mediante razonamiento en contexto |
| Calcular métricas | `calculate_metrics()` | Calcular métricas en chat |
| Escribir reporte Excel | `write_excel_sheet()` / `write_to_file()` | Mostrar tabla Markdown en chat |
| Consultar base de datos | `postgres.execute_query()` | Generar SQL exacto para que el usuario lo ejecute |

---

## ✅ Verificación

- El archivo de salida contiene la clasificación de datos correcta.
- No hay floats sin redondear.
- Toda la información PII y secretos ha sido detectada y redactada.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.1.0
