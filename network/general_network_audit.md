---
name: "General Network Security Audit"
description: "Audit general networking configurations for secure protocols, unused ports, and security redacting compliance."
category: "generic/network"
tools_required: ["data-analyst-mcp", "office-mcp"]
last_updated: 2026-05-24
---

# 🧠 Skill: General Network Security Audit

## 🎯 Goal
Perform a generic, comprehensive security audit on an active networking device configuration to identify security exposures, unredacted passwords, default credentials, and ensure baseline secure management protocols.

## 📊 Inputs Required
- Raw or redacted network configuration file (e.g. `network_config.conf` or `network_config.txt`).

## 🛠️ Step-by-Step Instructions
1. **Unused Port Hardening**:
   - Audit the interface lists. Highlight any physical ports that are active but not documented, or unused ports that are not administratively disabled.
2. **Management Protocol Audit**:
   - Audit enabled services. Check if legacy protocols (Telnet, HTTP, UPnP, WPS) are enabled.
   - Flag them as immediate vulnerabilities and recommend transitioning to secure alternatives (SSH, HTTPS).
3. **Password & Secret Exposure Search**:
   - Search the file using `data-analyst-mcp` to ensure no plain-text passwords or SNMP community secrets are readable.
4. **General Compliance Mapping**:
   - Map findings against standard organizational guidelines (VLAN segmentation, documentation, labeling).

## 🛡️ Verification & Security Checklist
1. **Security Scan**: Verify that all passwords, secret hashes, and keys are redacted or masked before generating the final report.
2. **Structural Check**: Confirm that all required sections (Overview, Risk Analysis, Mitigation Steps) are generated.
3. **Data Integrity**: Verify that no placeholder text is left in the final document.
4. **File Output**: Ensure the report is saved in the `/output` subfolder and the size is greater than 0 bytes.

---
*Created by Efficiency Core*
