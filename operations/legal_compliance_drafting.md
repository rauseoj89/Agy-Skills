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

## 🎯 Objective

Draft, review, and customize attorney-grade legal agreements, privacy policies, data processing addenda, and healthcare compliance agreements for technology companies and MSPs using attorney-drafted, CC0-licensed templates from General Legal.

## 🕒 When to Use

- When drafting commercial client contracts: Master Services Agreements (MSAs), Statements of Work (SOWs), or Terms of Service / SaaS Terms.
- When creating non-disclosure agreements: mutual or unilateral NDAs.
- When implementing privacy disclosures: Privacy Policies (compliant with CCPA/GDPR) and Cookie Notices.
- When structuring regulatory compliance addenda: Data Processing Addenda (DPAs) or HIPAA Business Associate Agreements (BAAs).
- When preparing advisor agreements (Advisor Agreements with IP assignment) or employment offer letters.

## 🛡️ Universal Principles

1. **Structured Substitution Tags:** Meticulously replace all placeholder tags (`[Company Name]`, `[State/Country]`, `[Notice Email]`, `[Governing Law]`) leaving zero unpopulated fields.
2. **Jurisdiction & Governing Law Alignment:** Explicitly align applicable governing law, jurisdiction, and competent courts according to client domicile or operational headquarters.
3. **Regulatory Strictness:** For HIPAA BAA and GDPR DPA agreements, never dilute statutory breach notification timelines or technical and organizational security measures (TOMs).
4. **Non-Legal Advice Disclaimer:** Every generated document must include a prominent disclaimer stating that the material derives from open-source CC0 templates and must be reviewed by qualified legal counsel prior to execution.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Export structured agreement in Markdown or Word using office-mcp
# write_word_document(path="contracts/MSA_Client.docx", content=...)
```

### ▶️ If you are on Hermes Agent:

```python
# Save legal agreement to repository
with open("contracts/privacy_policy.md", "w") as f:
    f.write(contract_markdown)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Create contractual document in legal folder
await writeFile("legal/Mutual_NDA.md", ndaContent);
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide user with agreement template:
# "I have drafted the HIPAA BAA with your entity details. Review the breach notification section."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Pose key terms (Party names, jurisdiction, payment terms, liability caps).
2. Generate the full agreement text in clean, formatted Markdown directly in the chat response.
3. Attach standard legal disclaimers and signature block placeholders (e-signature ready).

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Document export | `write_word_document` / `write_pdf_document` | Generate structured Markdown in chat |
| Ingest agreements | `read_office_file` / `convert_to_markdown` | Ask user to paste agreement text |
| Tag substitution | Automated templating scripts | Direct substitution in generated text |

---

## ✅ Verification

- All placeholder tags (`[ ... ]`) were properly replaced with actual details.
- Governing law and dispute resolution clauses are included.
- For HIPAA or DPA agreements, mandatory statutory compliance timelines were enforced.
- The standard legal disclaimer is appended.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
