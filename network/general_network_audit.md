---
name: "general-network-audit"
description: "Performs network configuration audits, scanning for plain-text secrets, default credentials, inadequate VLAN segmentation, and outdated management protocols."
category: "generic/network"
tools_required: []
last_updated: 2026-06-19
---

# Skill: Network Audit Specialist

## Goal
Perform a comprehensive network configuration audit to identify vulnerabilities, credential leaks, segmentation weaknesses, and unsecure protocol usage. Outputs a timestamped audit report with an executive summary.

## Inputs Required
- Network ranges (CIDR) or network configuration files to analyze.
- Known VLAN mappings and site information.

## MCP vs Native Fallback

| Capability | With filesystem/markitdown MCPs | Without MCP |
|---|---|---|
| Read configuration files | Use MCP file read tools | Native file read tools |
| Parse complex network docs | Use markitdown tool for PDF/Word | User manually extracts/pastes config text |

---

## Step-by-Step Instructions

### 1. Immediate Secret Scan
- **Mandatory Step 1:** Before performing any other analysis, run a regex scan on configuration files for potential secrets:
  - Search patterns: `password =`, SNMP community strings (e.g., `public`, `private`), and IPSec pre-shared keys.
  - **Redaction Gate:** Immediately redact all identified secrets in memory or temporary files. Replace them with `[REDACTED]` in all output logs and reports before saving.

### 2. Default Credential Check
- Analyze configuration files or device accesses for default accounts.
- Flag as **CRITICAL** any occurrences of known default usernames (such as `admin`, `cisco`, `enable`, `root`, `ubnt`) paired with default or blank passwords.

### 3. VLAN & Segmentation Review
- Review configuration files (routing, switchport settings, firewall rules) to verify network segmentation:
  - Check that database and application servers are on isolated VLANs.
  - Verify that database/server VLANs are not directly routable from general user or Guest Wi-Fi VLANs.
  - Inspect trunk ports and flag any undocumented trunk ports or VLAN leakage.

### 4. Management Protocol Audit
- Review active management protocols against the standard security baseline:

  | Insecure Protocol | Secure Alternative | Action Required |
  |---|---|---|
  | Telnet (port 23) | SSH (port 22) | Disable Telnet, enforce SSH v2 only. |
  | HTTP (port 80) | HTTPS (port 443) | Disable HTTP management, redirect to HTTPS. |
  | SNMP v1 / v2c | SNMP v3 | Migrate to SNMP v3 (encrypted credentials). |
  | FTP (port 21) | SFTP / SCP | Enforce SFTP/SCP for configuration backups. |
  | WPS / UPnP | Disabled | Disable WPS and UPnP on all routers/firewalls. |

### 5. Report Generation
- Compile audit findings into a report file named `network_audit_YYYYMMDD.md`.
- The report must begin with an **Executive Summary** detailing:
  - Total Critical, High, Medium, and Low severity findings counts.
  - Key recommendations and security posture rating.
  - Timestamped log of the audit run.

---

## Verification & Security Checklist

1. **Immediate Secrets Redaction**: Verified that no plain-text passwords or community strings are stored in the final report.
2. **Default Credentials Check**: Confirmed that all systems were scanned for default usernames and blank passwords.
3. **Segmentation Verified**: Flagged any VLAN bridging or undocumented trunk ports.
4. **Protocols Validated**: Confirmed all Telnet, HTTP, SNMP v1/v2c, and FTP instances are flagged for remediation.
5. **Severity Counts Validation**: Cross-validated that the sum of findings in the detailed section matches the counts listed in the Executive Summary.

---
*agy-skills — updated 2026-06-19*
