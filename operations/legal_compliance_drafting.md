---
name: legal-compliance-drafting
description: Authors and audits startup and MSP legal agreements. Generates attorney-drafted contracts, terms, policies, DPAs, and HIPAA BAAs based on General Legal CC0 standards.
version: 1.0.0
tags: [universal, legal, compliance, contracts, msa, nda, hipaa, gdpr, ccpa]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Legal & Regulatory Compliance Drafting Specialist

## 🎯 Objetivo

Draft, review, and customize attorney-grade legal agreements, privacy policies, data processing addenda, and healthcare compliance agreements for technology companies and MSPs using attorney-drafted, CC0-licensed templates from General Legal.

## 🕒 Cuándo usar

- Al redactar contratos comerciales de clientes: Master Services Agreements (MSAs), Statements of Work (SOWs) o Términos de Servicio (Terms of Service / SaaS Terms).
- Al crear acuerdos de confidencialidad: NDAs mutuos o unidireccionales.
- Al implementar divulgaciones de privacidad: Políticas de Privacidad (conforme a CCPA/GDPR) y Avisos de Cookies.
- Al estructurar apéndices de cumplimiento regulatorio: Data Processing Addenda (DPAs) o Business Associate Agreements (BAAs) de HIPAA.
- Al preparar contratos de asesores (Advisor Agreements con cesión de IP) o cartas de oferta de empleo.

## 🛡️ Principios Universales

1. **Structured Substitution Tags:** Reemplazar meticulosamente todos los marcadores (`[Company Name]`, `[State/Country]`, `[Notice Email]`, `[Governing Law]`) sin dejar campos en blanco.
2. **Jurisdiction & Governing Law Alignment:** Alinear explícitamente la ley aplicable, la jurisdicción y los tribunales competentes según la sede o requerimiento del cliente.
3. **Regulatory Strictness:** Para acuerdos HIPAA BAA y GDPR DPA, no diluir los plazos de notificación de brechas de seguridad ni las medidas técnicas y organizativas de seguridad (TOMs).
4. **Non-Legal Advice Disclaimer:** Todo documento generado debe incluir el descargo de responsabilidad indicando que el material proviene de plantillas CC0 de código abierto y debe ser revisado por un abogado local calificado antes de su firma.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Exportar contrato estructurado en Markdown o Word utilizando office-mcp
# write_word_document(path="contracts/MSA_Client.docx", content=...)
```

### ▶️ Si estás en Hermes Agent:
```python
# Guardar el acuerdo legal en el repositorio
with open("contracts/privacy_policy.md", "w") as f:
    f.write(contract_markdown)
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Crear archivo contractual en el directorio legal
await writeFile("legal/Mutual_NDA.md", ndaContent);
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Guiar al usuario con la plantilla de acuerdo:
# "He generado el borrador de HIPAA BAA con tus datos. Revisa la cláusula de notificación de brechas."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Formula las preguntas clave (Nombre de las partes, jurisdicción, plazos, limitación de responsabilidad).
2. Genera el texto completo del acuerdo en Markdown limpio y formateado directamente en la respuesta.
3. Añade la advertencia legal estándar y las directivas de firma (e-signature ready).

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Exportación de documentos | `write_word_document` / `write_pdf_document` | Generar Markdown estructurado en el chat |
| Ingesta de contratos | `read_office_file` / `convert_to_markdown` | Pedir al usuario que pegue el texto del contrato |
| Sustitución de etiquetas | Scripts de templating | Reemplazo directo en el texto generado |

---

## ✅ Verificación

- Todos los marcadores de sustitución (`[ ... ]`) fueron debidamente completados.
- Se incluyó la cláusula de jurisdicción y resolución de disputas.
- Para acuerdos HIPAA o DPA, se respetaron los estándares regulatorios mandatorios.
- Se adjuntó el aviso de descargo de responsabilidad legal.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
