---
name: host-security-audit
description: Audits Linux VPS, servers, and host OS security configurations. Inspects SSH hardening, firewall status (UFW/nftables/iptables), Fail2ban/CrowdSec alignment, SUID binaries, sudo logging, open ports, and resource consumption.
version: 1.0.0
tags: [universal, security, linux, vps, hardening, ssh, firewall, fail2ban]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Linux Host Security Specialist

## 🎯 Objective

Audit, diagnose, and harden Linux Virtual Private Servers (VPS) and host operating systems, ensuring minimal attack surfaces, strict SSH policies, synchronized intrusion detection systems (Fail2ban/CrowdSec), and least-privilege configurations.

## 🕒 When to Use

- When evaluating a new or existing Linux server before promoting it to production.
- When verifying SSH daemon configuration (`/etc/ssh/sshd_config`).
- When checking firewall status (`ufw`, `nftables`, `iptables`) against listening ports and sockets (`ss -tulpn`).
- When validating that Fail2ban or CrowdSec jails match active listening ports and services.
- When auditing SUID binaries or passwordless sudo privileges.

## 🛡️ Universal Principles

1. **Read-Only Diagnostic First:** The audit phase must be strictly read-only. Do not apply destructive changes or reload firewalls without explicit user authorization.
2. **Never Lock Out SSH:** Never restart the SSH daemon or alter management ports without instructing the user to maintain an active parallel SSH session for testing.
3. **Alignment Audit:** Verify that firewall rules and Fail2ban filters correspond exactly to the ports on which services are listening (preventing silent security protection failures).
4. **Zero Listening Databases:** No database (PostgreSQL, MySQL, Redis, MongoDB) may listen on `0.0.0.0` without strict firewall restrictions.
5. **Sanitize Host Telemetry:** Mask public IP addresses, usernames, and internal hostnames in audit reports.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Non-destructive port and firewall inspection
ss -tulpn
sudo ufw status verbose
```

### ▶️ If you are on Hermes Agent:

```python
# Check sshd_config status via terminal
result = terminal(command="grep -E '^(PermitRootLogin|PasswordAuthentication|Port)' /etc/ssh/sshd_config", timeout=30)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Diagnose listening sockets and ports
const sockets = await shell.exec("ss -tulpn | grep LISTEN");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Provide audit script and commands to the user:
# "Execute 'sudo ss -tulpn' and 'sudo ufw status verbose' to compare open ports against firewall rules."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Provide user with a list of one-line diagnostic commands (`ss -tulpn`, `ufw status`, `systemctl status fail2ban`).
2. Ask user to share outputs (with IPs redacted).
3. Evaluate security posture and generate step-by-step hardening recommendations.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Inspect sockets | `ss -tulpn` via terminal | Ask user for `ss -tulpn` output |
| Firewall status | `ufw status` / `iptables -L -n -v` | Ask user for active firewall rules output |
| SSH configuration | Read `/etc/ssh/sshd_config` | Ask user for grep-filtered sshd_config lines |
| SUID binaries | `find / -perm -4000 2>/dev/null` | Provide command and ask user to review unusual binaries |

---

## ✅ Verification

- `PermitRootLogin` is set to `no` or `prohibit-password`.
- `PasswordAuthentication` is set to `no` (forcing public key authentication).
- Firewall is active and does not expose unauthenticated internal services to the internet.
- Fail2ban jails monitor the correct services and ports.
- No anomalous SUID binaries or excessive sudo privileges detected.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
