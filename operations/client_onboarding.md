---
name: "Client Onboarding"
description: "Structured MSP client onboarding checklist: network discovery, vault credential setup, monitoring enrollment, PSA company setup, and documentation."
category: "generic/operations"
tools_required: ["psa-mcp"]
last_updated: 2026-06-19
---

# Skill: MSP Client Onboarding Specialist

## Goal
Execute a complete, repeatable MSP client onboarding workflow — from initial intake through network discovery, credential vaulting, monitoring enrollment, PSA record creation, and handoff documentation.

## Inputs Required
- Client company name, primary contact, and domain name.
- Network ranges (CIDR) and known site locations.
- PSA company ID (if already created) or instruction to create.
- Access credentials for client systems (provided by client — vault immediately on receipt).

## MCP vs Native Fallback

| Capability | With psa-mcp | Without MCP |
|---|---|---|
| Verify company exists | `Search for companies` tool | Ask user to confirm in PSA portal |
| Pull company details | `Retrieve complete company details` tool | User provides company info manually |
| Review existing tickets | `Find service tickets` tool | Manual ticket search in PSA |

---

## Onboarding Phases Overview

```
1. Intake & Kick-Off
2. PSA Company Setup
3. Network Discovery
4. Credential Vaulting
5. Monitoring Enrollment
6. Security Baseline
7. Handoff Documentation
```

---

## Step-by-Step Instructions

### 1. Intake & Kick-Off
- Collect from client:
  - Legal company name, doing-business-as, primary domain.
  - Primary technical contact (name, email, phone).
  - Billing contact.
  - Number of users and locations.
  - List of in-scope systems and services (servers, workstations, cloud tenants).
  - Existing vendors (ISP, backup, telephony, LOB application vendors).
- Confirm scope of services (managed, co-managed, or project-only).
- Set onboarding kick-off date and assign internal technician owner.

### 2. PSA Company Setup
- Search for existing company record:
  - Use `Search for companies` with client name to check for duplicates.
- If company exists, pull details with `Retrieve complete company details` and verify:
  - Status is Active.
  - Territory, SLA, and billing configuration are correct.
  - Primary and billing contacts are populated.
- If company does not exist, instruct user to create it in PSA with:
  - Company Name, Identifier (short code), Status: Active.
  - Correct Service Board and SLA assignment.
  - Territory matching client location.
- Create onboarding ticket: `[ONBOARDING] {Company Name} — {date}`.
- Log all onboarding actions as notes in this ticket.

### 3. Network Discovery
- Perform initial network discovery from the network assessment runbook:
  - Run `general-network-audit` skill against client network ranges.
  - Document: IP scheme, subnet layout, gateway, DNS servers, DHCP server.
  - Identify all managed devices: firewalls, switches, APs, servers, printers.
- Verify VLAN segmentation:
  - Servers on isolated VLAN.
  - Guest Wi-Fi isolated from internal.
  - Management VLAN (if applicable) restricted to IT.
- Flag any critical missing segmentation as a remediation item (P2 ticket).
- Export network map to client documentation folder.

### 4. Credential Vaulting
- Receive all client credentials via secure channel only (never email, never chat in plaintext).
- Vault immediately on receipt — never store in notes, spreadsheets, or plaintext files:
  - All credentials go into the designated vault system under the client's namespace.
  - Naming convention: `{client-code}/{system-type}/{identifier}` (e.g., `acme/firewall/asa-01`).
- Rotate any credentials that were transmitted via insecure channel before storing.
- Verify vault entry for each critical system:
  - Firewall admin.
  - Switch admin.
  - Domain Admin / local admin.
  - M365 Global Admin.
  - Backup system.
- **Secrets Gate**: Confirm zero credentials appear in PSA ticket notes, documentation files, or this session output.

### 5. Monitoring Enrollment — RMM
- **Install RMM agent on all managed Windows endpoints**:
  - Download the client-specific agent installer from the RMM.
  - Deploy via Group Policy, manual install, or the RMM's built-in deployment tool.
  - Confirm agent checks in: RMM console → client group → computers → status = Online.
- **Add network devices to RMM network monitoring** (SNMP v3 only — never v1/v2c):
  - RMM → Network Devices → Add → enter device IP, SNMP credentials from vault.
- **Apply the client's monitoring template** (create one if it doesn't exist):
  - Configure alert thresholds on the template:
    - CPU: alert at > 90% sustained for > 5 minutes.
    - Memory: alert at > 85%.
    - Disk: alert at > 80% used on any drive.
    - Service: alert on any critical service (SQL, IIS, etc.) stopping unexpectedly.
  - Verify heartbeat/ping monitoring for firewalls, switches, and servers.
- **Configure RMM → PSA ticket integration**:
  - Alerts must auto-create tickets on the correct service board.
  - Assign priority mapping: RMM critical alert → PSA P1, warning → PSA P3.
- Test end-to-end: trigger a test alert in RMM → confirm PSA ticket created → resolve and confirm ticket closes.

### 5b. Backup Enrollment — Veeam / Axcient
- **Veeam** (for VMs and servers):
  - Add client's VMs or physical servers to Veeam Backup & Replication.
  - Create a backup job: Daily at off-hours, retention ≥ 14 restore points.
  - Verify first backup completes successfully before onboarding sign-off.
- **Axcient** (for BCDR / physical endpoints or additional cloud protection):
  - Deploy Axcient agent on in-scope endpoints.
  - Configure backup schedule and cloud replication in Axcient portal.
  - Verify first backup status = Successful in portal.
- Document backup job names, schedules, and retention policies in the client runbook.

### 6. Security Baseline
- Run `sec-engineer` skill or manual baseline check:
  - Antivirus/EDR installed and reporting on all endpoints (visible in RMM).
  - Windows Defender ATP or equivalent enabled and reporting.
  - M365 MFA enforced for all users (use `managing-m365` skill).
  - Veeam backup job running successfully with ≥ 14 restore points.
  - Axcient agent deployed and last backup status = Successful.
  - Domain password policy: minimum 12 characters, complexity enabled.
  - Local admin accounts: unique passwords per system (no shared local admin).
- Document any gaps as remediation items with priority and owner.

### 7. Handoff Documentation
- Create client runbook document containing:
  - Network diagram (topology, VLANs, IP scheme).
  - Device inventory (hostname, IP, role, OS, warranty date).
  - Vendor list (ISP, backup, telephony — contact + account numbers).
  - Escalation path (Tier 1 → Tier 2 → vendor contacts).
  - Known issues and workarounds at time of onboarding.
  - Monitoring coverage summary (what is monitored, alert thresholds).
- Save to client documentation folder following naming convention: `{ClientCode}_Runbook_v1.0_{YYYYMMDD}.md`.
- Link documentation in PSA company record.
- Close onboarding ticket with final checklist confirmation note.

---

## Verification & Security Checklist

1. **Credentials Vaulted**: Confirm zero client credentials appear in tickets, chat, session logs, or documentation files.
2. **PSA Record Complete**: Confirm company record has Active status, correct SLA, territory, and billing contact.
3. **Monitoring Verified**: Confirm RMM agent online for all endpoints and at least one alert tested end-to-end (trigger → PSA ticket).
4. **Backup Verified**: Confirm Veeam and/or Axcient first backup completed successfully before handoff.
5. **Documentation Delivered**: Confirm network diagram, device inventory, and vendor list are in client runbook.
6. **Onboarding Ticket Closed**: Confirm all checklist items logged in PSA ticket and ticket closed with client sign-off.

## Future Integrations
- `psa-mcp` *(already active)*: Company lookup and ticket management during onboarding.
- `rmm-mcp` *(agy-MCP blueprint — pending)*: Agent status verification and monitoring template application via API.
- `backup-mcp` *(agy-MCP blueprint — pending)*: Veeam and Axcient backup job verification and first-backup confirmation.
- `graph-api-mcp` *(agy-MCP blueprint — pending)*: Automated M365 user and MFA status verification during security baseline step.
- `vault-bridge-mcp` *(agy-MCP blueprint — pending)*: Direct credential storage during vaulting step without manual portal entry.

---
*agy-skills — updated 2026-06-19*
