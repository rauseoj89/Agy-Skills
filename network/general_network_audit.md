---
name: general-network-audit
description: Performs network configuration audits, scanning for plain-text secrets, default credentials, inadequate VLAN segmentation, open listening sockets, and outdated management protocols.
version: 1.1.0
tags: [universal, network, security, audit]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor, OpenCode]
last_updated: 2026-09-28
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Network Audit Specialist

## 🎯 Objective

Perform a comprehensive network configuration and listening port audit to identify vulnerabilities, credential leaks, segmentation weaknesses, open listening sockets, and unsecure protocol usage. Outputs a timestamped audit report with an executive summary.

## 🕒 When to Use

- When conducting network configuration audits to identify vulnerabilities.
- When reviewing VLAN segmentation policies or firewall rules.
- When correlating open listening network sockets with active firewall policies.
- When scanning for default passwords or insecure management protocols (Telnet, HTTP, SNMPv1/v2).

## 🛡️ Universal Principles

1. **Immediate Secrets Redaction**: Never include raw passwords, SNMP strings, or PSKs in reports. Mask as `[REDACTED]`.
2. **Default Credentials Check**: Actively search for and flag default usernames/passwords.
3. **Protocol Audit Rules**: Enforce encryption (SSH instead of Telnet, HTTPS instead of HTTP, SNMPv3 instead of SNMPv1/v2c).
4. **Data Privacy**: Do not expose internal private IP networks in public audit summaries unless using placeholders.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Read router, switch, or firewall configuration files
# Audit listening network sockets via security-scanner-mcp:
# audit_listening_ports(protocol="all")
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal to search or analyze configuration files
config = read_file(path="switch_config.cfg")
```

### ▶️ If you are on Cline / Roo Code / OpenCode:

```javascript
// Scan listening ports and analyze network configurations
const ports = await security_scanner.audit_listening_ports({ target_host: "localhost", protocol: "all" });
const config = await filesystem.readFile("firewall.conf");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Ask user to provide configuration text:
# "Please paste the contents of your router configuration file (redacting any active secrets)."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Ask user: "Please upload or paste your network device configuration directives".
2. Analyze configurations manually in chat context.
3. Return the structured audit report in Markdown directly in chat.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Inspect listening sockets | `security_scanner.audit_listening_ports()` | Terminal: `netstat -ano` (Windows) / `ss -tulpn` (Linux) |
| Read configuration files | `filesystem-mcp.read_file()` | Ask user to paste configuration |
| Validate IPs and subnets | Automated verification scripts | Manual visual review by AI |
| Export audit report | `filesystem-mcp.write_file()` | Output Markdown report for user to save |

---

## ✅ Verification

- No actual passwords are listed in outputs.
- Vulnerabilities are categorized by severity levels (Critical, High, Medium, Low).
- Encrypted alternatives are proposed for every unsecure protocol detected.
- Active listening ports have corresponding verified firewall rules.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-28  
Version: 1.1.0
