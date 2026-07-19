---
name: seo-audit
description: Comprehensive technical and on-page SEO evaluation of websites with PDF/Markdown report generation.
version: 1.1.0
tags: [universal, seo, audit, marketing, technical-seo, on-page-seo, pdf-report]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-19
author: JimmyR
---
# Skill: SEO Audit

## 🎯 Objetivo

Inspect webpage SEO structures, HTTP connectivity, index crawlability files, and semantic content layout, generating structured bilingual (English/Spanish) reports in PDF or Markdown format.

## 🕒 Cuándo usar

- When evaluating search visibility optimizations for a target domain or new website development.
- When inspecting HTTP headers, SSL status, crawling directive files (`robots.txt`, `sitemap.xml`), and redirection flows.
- When producing bilingual (English/Spanish) structural audits.

## 🛡️ Principios Universales

1. **Verify HTTPS:** Enforce SSL checks and inspect active redirect rules for protocol security.
2. **Semantic Structure:** Verify the webpage contains exactly one primary `H1` tag to satisfy clean indexing parameters.
3. **Metadata Integrity:** Check page titles do not exceed 60 characters and description tags are kept within 160 characters.

---

## 🤖 Ejecución Multi-Agente / Multi-Agent Execution

### ▶️ Si estás en [Antigravity] o [Hermes]:
Locate and run the python helper script inside the skill references:
```bash
# Para informe PDF:
python generate_seo_pdf.py data.json logo.png reports/output-report.pdf es

# Para informe Markdown:
python generate_seo_markdown.py data.json reports/output-report.md en
```

### ▶️ Si estás en [Cline] o [Roo-Code]:
Use `filesystem-mcp` to write report data or execute commands via terminal.

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Pide al usuario que proporcione las cabeceras HTTP, el contenido de `robots.txt` y `sitemap.xml`, y la estructura de HTML del sitio.
2. Realice el análisis manualmente.
3. Genere la estructura de informe en Markdown directamente en el chat.

────────────────────────────────────

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Inspección de Cabeceras | `curl -I <url>` | Solicitar respuesta HTTP raw al usuario |
| Estructura de Encabezados | Selectores de DOM | Solicitar lista de tags HTML al usuario |
| Generación de Reportes | Ejecutar scripts locales de python | Generar Markdown directamente en la conversación |

────────────────────────────────────

## ✅ Verificación
- [ ] ¿El sitio utiliza HTTPS?
- [ ] ¿Tiene un archivo `robots.txt` válido?
- [ ] ¿Hay exactamente un encabezado `H1` por página?
- [ ] ¿Todas las imágenes tienen etiqueta `alt`?
- [ ] ¿La meta descripción está presente y tiene menos de 160 caracteres?
- [ ] (PDF) ¿El logotipo se inserta y formatea correctamente?
- [ ] (PDF/MD) ¿El reporte está en el idioma solicitado (ES/EN)?

────────────────────────────────────

## 🌐 Soporte Bilingüe y Valores por Defecto
- **Default language**: **English** (`lang='en'`) — All reports are generated in English by default unless explicitly requested in Spanish.
- **Spanish** (`lang='es'`): Set explicitly ONLY when the user requests Spanish output.
- **CRITICAL: NO HARDCODED TEXT** — All text elements (section titles, table headers, labels, footer, messages) MUST use bilingual dictionaries indexed by `lang`:
  ```python
  SECTIONS = {
      'es': {'summary': "1. Resumen Ejecutivo", 'technical': "2. Auditoría Técnica", ...},
      'en': {'summary': "1. Executive Summary", 'technical': "2. Technical Audit", ...}
  }
  LABELS_HEADER = {
      'es': {'site_label': "Sitio Web:", 'date_label': "Fecha de análisis:", ...},
      'en': {'site_label': "Website:", 'date_label': "Analysis Date:", ...}
  }
  ```
- **Data requirements**: Both `*_en` and `*_es` keys must be present in `seo_data` for summaries and recommendations, but only the active language's content is used.
- **Pitfall — Hardcoded Spanish in English reports**: If reports show Spanish text when English was requested, check for:
  - Hard-coded section titles (e.g., `"1. Resumen Ejecutivo"` instead of `SECTIONS[lang]['summary']`)
  - Hard-coded labels in headers (e.g., `"Sitio Web:"` instead of `LABELS_HEADER[lang]['site_label']`)
  - Hard-coded footer/pagination text (e.g., `"Página X"` instead of `page_label_en`)
  - Hard-coded status messages (e.g., accessibility messages)
- **Pitfall — Missing bilingual support in Markdown**: The `generate_seo_markdown.py` script must also use bilingual dictionaries for table headers and section titles, not just the PDF script.

## ⚠️ Pitfalls & Lessons Learned

- **SPA Content Blindness:** `browser_console` or `web_extract` may return empty results if the page renders content dynamically. Use `browser_snapshot` or `browser_vision` to verify content exists.
- **Missing Metadata:** A `null` result for meta descriptions is a critical finding—report as high-priority "Quick Win".
- **PDF Library:** Ensure `reportlab` and `pillow` are installed in a venv before generating PDFs.
- **Bilingual Data:** Always provide both `*_es` and `*_en` strings in `seo_data` to avoid KeyError when switching languages.
- **Markdown Fallback:** If PDF generation fails, the Markdown report offers a portable, universally readable alternative.
- **Spanish Typo Check:** Verify all Spanish labels are correct before final generation. Critical checks:
  - "Contenido **Actual**" (NOT "Actuel")
  - "Fecha de análisis" (NOT "Fecha de Análisis" con mayúscula incorrecta)
  - "Servidor" (NOT "Server" en la versión ES)
- **Bilingual Table Headers in Markdown (CRITICAL FIX):** All table headers in `generate_seo_markdown.py` MUST use bilingual constants (e.g., `TABLE_TECH_HEADER[lang]`) instead of hardcoded strings. Hardcoded Spanish headers will appear in English reports. Pattern: define `TABLE_* = {'es': "...", 'en': "..."}` and always access with `[lang]`.
- **CRITICAL: No Hard-Coded Text in PDF Scripts:** ALL text elements (section titles, table headers, labels, footer messages, pagination) must use bilingual dictionaries (`SECTIONS[lang]`, `LABELS_HEADER[lang]`). Hard-coded strings like `"1. Resumen Ejecutivo"` or `"Sitio Web:"` will appear in reports even when English is requested. This is a common bug that requires careful review of the entire script.

### 🎨 PDF Design & Layout (DEFINITIVE — LaTeX Style)

**CRITICAL**: The PDF report follows a **strict LaTeX-inspired design** with corporate branding (Brand Blue #1A365D, Tech Gray #4A5568). All geometry, colors, and layout MUST match exactly.

#### 1. Page Geometry & Packages (Mandatory)
- **Margins**: **2.5cm** on all sides (Top, Bottom, Left, Right) — standard paper geometry
- Use `SimpleDocTemplate` with `rightMargin=2.5*cm`, `leftMargin=2.5*cm`, `topMargin=2.5*cm`, `bottomMargin=2.5*cm`

#### 2. Corporate Color Palette
Define and use consistently:
- `COLOR_BRAND_BLUE = HexColor('#1A365D')` — Azul Oscuro Ejecutivo (headers, divider line)
- `COLOR_TECH_GRAY = HexColor('#4A5568')` — Gris Técnico (labels, meta text)
- `COLOR_SUCCESS = HexColor('#38a169')` — Verde para estados OK
- `COLOR_WARNING = HexColor('#e53e3e')` — Rojo para fallos/missing

#### 3. Header Layout (Page 1 — Exact Structure)
Structure the header exactly as **2 minipages** (simulated via Table with 2 columns):

**Left Minipage (45% width)**:
- Logo image: `width=4.5cm`, height auto
- Vertically aligned bottom `[b]`

**Right Minipage (50% width)**:
- Text aligned **right** (`\raggedleft` → `TA_RIGHT`)
- 3 lines (MUST use bilingual dictionaries):
  1. `"<b>{LABELS_HEADER[lang]['site_label']}</b> <blue>{domain}</blue>"` (size 9, Tech Gray label + Brand Blue value)
  2. `"<b>{LABELS_HEADER[lang]['date_label']}</b> <date>"` (size 9, Tech Gray)
  3. `"<b>{LABELS_HEADER[lang]['doc_label']}</b>"` (size 9, Tech Gray)

**Important**: Never hard-code "Sitio Web:", "Fecha de análisis:", or other labels. Always use `LABELS_HEADER[lang]['site_label']`, etc.

**Divider Line**: 
- Horizontal rule: `{color: brandblue}, height: 1.5pt, width: \textwidth`
- Spacing: `\vspace{0.3cm}` before, `\vspace{0.6cm}` after

#### 4. Table Column Widths (Consistent Across All Tables)
All tables (Technical, On-Page) use **identical column widths** to ensure visual consistency:
- **Column 1** (Aspect/Element): `25%` of available width
- **Column 2** (Status): `15%` of available width  
- **Column 3** (Detail/Content): `60%` of available width
- **Heading Table**: Column 1 `15%`, Column 2 `85%`

#### 5. Text Wrap (Required for Column 3)
**ReportLab does NOT auto-wrap**. Implement manual wrap function that inserts `<br/>` every **55 characters**:

```python
def wrap_text(text, max_len=55):
    if not text or len(text) <= max_len: return text
    words = text.split()
    wrapped, line = "", ""
    for w in words:
        if len(line) + len(w) > max_len:
            wrapped += line + "<br/>"
            line = w + " "
        else:
            line += w + " "
    return wrapped + line if line else wrapped
```

Apply wrap **BEFORE** creating the Table, then use `Paragraph(wrap_text(...), cell_style)`.

#### 6. Table Styles (Corporate Branding)
**Header row background**: `COLOR_BRAND_BLUE` (#1A365D)
**Header text**: `colors.whitesmoke`, `Helvetica-Bold`, size 9
**Body rows**: Alternating backgrounds `[white, #f7fafc]`
**Grid**: `0.5pt`, color `#cbd5e0`
**Padding**: 4pt all sides
**Font size**: 9pt (header), 8.5pt (body)

#### 7. Footer & Pagination (fancyhdr equivalent)
Implement using `onFirstPage` and `onLaterPages` callbacks:
- **Footer text** (centered, size 8, gray #718096): Use bilingual dictionaries:
  - ES: `"Informe generado por Hermes Agent | {site_url}"`
  - EN: `"Report generated by Hermes Agent | {site_url}"`
- **Page number** (centered, below footer): 
  - ES: `"Página {page_num}"`
  - EN: `"Page {page_num}"`
- **Implementation**: Define `footer_text_es`, `footer_text_en`, `page_label_es`, `page_label_en`, then select based on `lang`
- Positions: Footer at **25pt** from bottom, Page number at **15pt** from bottom

#### Section Headings (MUST use bilingual dictionaries)
- **English examples**: `SECTIONS[lang]['summary']` → "1. Executive Summary", `SECTIONS[lang]['technical']` → "2. Technical Audit"
- **Spanish examples**: `SECTIONS[lang]['summary']` → "1. Resumen Ejecutivo", `SECTIONS[lang]['technical']` → "2. Auditoría Técnica"
- Color: `COLOR_BRAND_BLUE`
- Font: `Helvetica-Bold`, size 13, leading 15
- Spacing: `spaceBefore=12`, `spaceAfter=8`

DO NOT hard-code section titles like `"1. Resumen Ejecutivo"` or `"2. Auditoría Técnica"`. Always use `SECTIONS[lang]['summary']`, `SECTIONS[lang]['technical']`, etc.

#### Body Text
- Font: `Helvetica`, size 10, leading 13
- Alignment: `TA_JUSTIFY` (justified)
- Color: Black, optional use of `<b>` and `<code>` inline tags

────────────────────────────────────

Author: JimmyR
Last Updated: 2026-07-19
Version: 1.1.0
