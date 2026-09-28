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

## 🎯 Objective

Convert raw data records and documents into structured, high-value metrics, exposing patterns and anomalies while ensuring data classification compliance, secret redaction, and PII protection.

## 🕒 When to Use

- When asked to analyze raw data records in CSV, JSON, Excel, PDF, or plain text formats.
- When cleaning messy records or tables (formatting inconsistencies, blank values, whitespace padding).
- When calculating key business metrics (totals, averages, medians, percentages, trends).
- When formatting numerical data into highly structured Markdown tables or exporting to spreadsheets (`.xlsx`).

## 🛡️ Universal Principles

1. **PII and PHI Detection**: Scan all records for sensitive data (SSNs, emails, phone numbers). Mask or redact sensitive information.
2. **Secrets Scan Pass (Security Gate)**: Ingested data must be scanned for API keys, passwords, and connection strings. Redact with `[REDACTED]`.
3. **Float Artifact Prevention**: All numeric outputs must pass through rounding mechanisms (e.g., `Math.round()` or `.toFixed(2)`).
4. **File Size Cap**: Enforce memory limits (max 50 MB / 100,000 rows) on ingested files.
5. **Least Privilege**: Always request minimum required permissions to read or write database datasets.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Ingestion with data-analyst-mcp:
# parse_csv(path="dataset.csv", max_rows=50000)
# parse_excel(path="report.xlsx", sheet_name="Sheet1")
# extract_pdf_data(path="document.pdf")
# read_word_document(path="notes.docx")

# Cleaning and metrics:
# clean_tabular_data(records=data, null_strategy="drop", trim_strings=true)
# calculate_metrics(records=cleaned_data, numeric_columns=["revenue", "cost"])

# Excel generation with office-mcp:
# write_excel_sheet(filePath="summary.xlsx", data=excel_payload)
```

### ▶️ If you are on Hermes Agent:

```python
# Use native Hermes tools or Python scripts to load and process
content = read_file(path="dataset.csv", limit=5000)
# Process with pandas / in-memory analytics
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use data-analyst MCP or filesystem to read and transform data
const dataset = await data_analyst.parse_csv({ path: "dataset.csv" });
const metrics = await data_analyst.calculate_metrics({ records: dataset.rows, numeric_columns: ["amount"] });
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide the user if terminal or file tools are unavailable:
# Ask: "Please copy and paste the first 100 lines of the dataset.csv file"
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Ask the user: "Please copy and paste the dataset content or the first few lines here."
2. Process the information using in-context reasoning in the chat.
3. Generate the summarized Markdown table for the user.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Ingest CSV / Excel | `parse_csv()` / `parse_excel()` | Ask user to copy and paste the content |
| Ingest PDF / Word | `extract_pdf_data()` / `read_word_document()` | Ask user for extracted text |
| Clean data | `clean_tabular_data()` | Data cleaning via in-context reasoning |
| Calculate metrics | `calculate_metrics()` | Calculate metrics in chat |
| Write Excel report | `write_excel_sheet()` / `write_to_file()` | Display Markdown table in chat |
| Query database | `postgres.execute_query()` | Generate exact SQL for user to execute |

---

## ✅ Verification

- Output file contains correct data classification.
- No unrounded floating-point artifacts.
- All PII and secret data has been detected and redacted.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.1.0
