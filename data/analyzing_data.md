---
name: "Analyzing Data"
description: "Parses spreadsheets, sanitizes CSV/JSON metrics logs, and formats structured analytical dashboards."
category: "generic/data"
tools_required: ["data-analyst-mcp", "office-mcp"]
last_updated: 2026-05-24
---

# 🧠 Skill: Analyzing Data

## 🎯 Goal
Clean messy telemetry log outputs or spreadsheet records, calculate high-value metrics, and output polished markdown tables or Excel spreadsheets.

## 📊 Inputs Required
- Raw CSV, JSON, or TXT data files.
- Desired metrics calculations list.

## 🛠️ Step-by-Step Instructions
1. **Telemetry Data Hygiene**:
   - Resolve empty columns or null variables using standard replacement rules.
   - Strip duplicates and standardise date configurations (ISO 8601 formatting).
2. **Metrics Calculations**:
   - Extract records count and calculate averages, percentages, and totals.
   - Round calculations precisely to 2 decimal places.
3. **Anomalies Classification**:
   - Highlight statistical outliers (e.g. values exceeding 3 standard deviations or showing major configuration spikes).
4. **Presentation Compilation**:
   - Construct a polished markdown summary table detailing category averages and trend arrows.

## 🛡️ Verification & Security Checklist
1. **Secrets Redaction**: Audit the data inputs. Confirm no passwords or security hashes remain in the summary outputs.
2. **Tabular Alignment**: Ensure the markdown tables display cleanly with proper aligned headers.
3. **Outliers Isolation**: Verify that outlier logs are cross-referenced with exact reference codes.
4. **Excel Export**: Verify Excel exports have matching column widths and headers.

---
*Created by Efficiency Core*
