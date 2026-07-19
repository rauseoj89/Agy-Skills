---
name: seo-auditing
description: Realiza una auditoría técnica y de optimización on-page para cualquier sitio web, generando reportes profesionales bilingües.
version: 1.0.0
tags: [universal, seo, audit, marketing, report]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
---
# Skill: SEO Auditing

## 🎯 Objetivo
Evaluar exhaustivamente el posicionamiento orgánico, accesibilidad, jerarquía de contenido e infraestructura técnica de un sitio web para generar reportes en Markdown o PDFs corporativos bajo estándares profesionales.

## 🕒 Cuándo usar
- Al evaluar las optimizaciones de motores de búsqueda de un nuevo sitio o desarrollo web.
- Al revisar cabeceras de seguridad HTTP, archivos de rastreo (`robots.txt`, `sitemap.xml`) y redirecciones.
- Al preparar informes SEO bilingües (Español/Inglés) estructurados para entrega formal.

## 🛡️ Principios Universales
1. **Verificar HTTPS:** Garantizar la navegación y cifrado SSL seguros antes de realizar la inspección técnica.
2. **Jerarquía Semántica:** El sitio web debe poseer únicamente una etiqueta `H1` principal por página para una indexación correcta.
3. **Optimización de Metadatos:** Los títulos no deben exceder 60 caracteres y las descripciones meta deben mantenerse por debajo de los 160 caracteres.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en [Antigravity]:
Utiliza el comando integrado o localiza el script:
```powershell
python C:/Users/JimmyR/.gemini/antigravity/skills/seo-audit/scripts/generate_seo_report.py data.json report.md
```

### ▶️ Si estás en [Hermes]:
Invoca el skill auditando directamente la URL meta:
```bash
# Ejecutar curls sobre headers y validar robots.txt
curl -I https://rauseojtech.com
```

### ⚠️ Si NO tienes herramientas:
1. Pide al usuario el archivo `sitemap.xml` y `robots.txt` del sitio.
2. Solicita el código fuente HTML principal o las secciones `head` y la estructura de encabezados.
3. Genera manualmente las recomendaciones SEO y el reporte Markdown.

────────────────────────────────────

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Revisar Cabeceras | `curl -I <url>` | Pedir respuesta de red del navegador |
| Estructura H1-H4 | `document.querySelectorAll("h1, h2, h3, h4")` | Pedir que extraigan el DOM del index |
| Generación de Reporte | Ejecutar script python | Escribir el reporte en markdown en el chat |

────────────────────────────────────

## ✅ Verificación
- [ ] El reporte contiene las secciones completas en el idioma seleccionado (`lang='es'` o `lang='en'`).
- [ ] No se exponen credenciales de staging en las capturas o en las cabeceras reportadas.
- [ ] La estructura de cabeceras H1-H4 no contiene saltos de nivel ilógicos (ej. H1 directamente a H3).
- [ ] Se verifica si hay imágenes sin atributo `alt`.

────────────────────────────────────
Author: JimmyR
Last Updated: 2026-07-18
Version: 1.0.0
