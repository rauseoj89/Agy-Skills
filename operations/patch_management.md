---
name: "Patch Management"
description: "Governs the full patch lifecycle: inventory, risk assessment, change window scheduling, staged deployment, verification, and rollback using RMM, Veeam, and Axcient."
category: "generic/operations"
tools_required: []
last_updated: 2026-06-19
---

# Skill: Patch Management Specialist

## Goal
Execute a controlled, risk-aware patch lifecycle for Windows and Linux systems — from vulnerability inventory through staged deployment, post-patch validation, and rollback readiness.

## Inputs Required
- Target systems list (hostnames) or RMM patch group/client scope.
- Patch window date and time (change-approved window).
- Rollback method confirmed: Veeam restore point or Axcient BCDR snapshot.

## Toolstack
- **RMM / Patch Deployment**: RMM (Remote Monitoring and Management) — primary tool for patch approval, scheduling, and deployment across managed endpoints.
- **Backup / Rollback**: Veeam (VMs and servers) and Axcient (BCDR appliance + cloud) — verify successful backup before any patching.

## MCP vs Native Fallback

| Capability | With rmm-mcp *(future)* | Without MCP (current) |
|---|---|---|
| Pending patch inventory | `get_patch_status` tool | RMM console → Patch Manager |
| Approve/schedule patches | `approve_patches` tool | RMM console → Patch Approval |
| Post-patch status | `get_computer_status` tool | RMM console → Computer view |
| Manual verification | `execute_command` on target | PowerShell: `Get-HotFix` on endpoint |

---

## Patch Priority Framework

| Priority | Criteria | Deployment Window |
|---|---|---|
| Critical | CVSS ≥ 9.0, active exploit in wild, Zero-Day | Emergency — 24–48 hours |
| High | CVSS 7.0–8.9, remote code execution, privilege escalation | Next scheduled window (≤ 7 days) |
| Medium | CVSS 4.0–6.9, local exploit, no known active exploitation | Monthly patch cycle |
| Low | CVSS < 4.0, informational, hardening updates | Quarterly or next convenient window |

---

## Step-by-Step Instructions

### 1. Inventory & Vulnerability Assessment
- **Primary**: Use RMM Patch Manager to view pending patches per client/group:
  - Navigate to: Patch Manager → Approval Policies → view pending by severity.
  - Filter by `Patch Status: Missing` and `Severity: Critical` or `Important`.
  - Export the missing patch report per client for documentation.
- **Verification** (PowerShell on endpoint):
  ```powershell
  # Confirm installed patches and last update date
  Get-HotFix | Sort-Object InstalledOn -Descending | Select HotFixID, InstalledOn, Description
  ```
- Cross-reference any Critical/High patches against CVSS scores using the KB article or CVE reference. Flag immediately.

### 2. Risk Assessment & Change Window Request
- For each Critical/High patch, document:
  - CVE ID and CVSS score.
  - Affected component (OS, driver, application).
  - Reboot required? (Y/N).
  - Estimated downtime window.
- **Change Window Gate**: Do not deploy to production without an approved change window.
  - Emergency patches (Critical, active exploit): request expedited approval.
  - Standard patches: align with monthly patch cycle.
- Notify affected users/clients of expected maintenance window.

### 3. Pre-Patch Baseline
- **Verify backup is current before patching any production system**:
  - **Veeam**: Confirm last successful backup job completed within the last 24 hours in Veeam Backup & Replication console → Jobs → Last Result = Success.
  - **Axcient**: Confirm last backup status in Axcient portal → client device → last backup timestamp and status = Successful.
  - If backup is older than 24 hours or failed: resolve backup issue first — do not patch until backup is confirmed.
- Capture system state on endpoint:
  ```powershell
  # Running services snapshot
  Get-Service | Where-Object {$_.Status -eq "Running"} | Select Name, DisplayName | Export-Csv "pre_patch_services_$(Get-Date -f yyyyMMdd).csv"

  # Disk space check (require ≥ 10 GB free)
  Get-PSDrive C | Select Used, Free
  ```
- **Never patch a system with no verified Veeam or Axcient rollback point.**

### 4. Staged Deployment
- Deploy in this order — never patch all systems simultaneously:
  1. **Test/Dev** systems first — verify no application breakage.
  2. **Pilot group** (5–10% of production, non-critical users).
  3. **Production servers** — after 24-hour pilot soak period.
  4. **Critical infrastructure** (DCs, firewalls, switches) — last, with dedicated change window.

  - **RMM**: Patch Manager → Approval Policy → approve KB for target group → schedule maintenance window for reboot.
  - RMM will push and track reboot status automatically per endpoint.
  - Monitor reboot completion in RMM: Computer view → Patch Status tab.
- Monitor for reboot completion and service restoration after each stage.

### 5. Post-Patch Verification
- After reboot, confirm:
  ```powershell
  # Verify patch installed
  Get-HotFix -Id "KB5034441"

  # Confirm key services running
  Get-Service | Where-Object {$_.Status -ne "Running" -and $_.StartType -eq "Automatic"} | Select Name, Status

  # Check event log for patch-related errors
  Get-EventLog -LogName System -EntryType Error -Newest 20 | Where-Object {$_.Source -like "*Windows Update*"}
  ```
- Test application functionality (login, key workflows) with end user or automated test.
- Flag any service that failed to start automatically post-reboot.

### 6. Rollback Procedure
- If critical application failure occurs post-patch:
  1. **Uninstall specific patch** (if isolated to one KB):
     ```powershell
     wusa /uninstall /kb:5034441 /quiet /norestart
     ```
  2. **Veeam restore** (VM or server — preferred for multi-patch instability):
     - Veeam console → Backups → right-click VM → Restore → Instant VM Recovery or Full VM Restore.
     - Select the restore point dated before the patch window.
     - Confirm with client before initiating — restoring overwrites post-patch changes.
  3. **Axcient BCDR recovery** (physical machines or Axcient-protected workloads):
     - Axcient portal → client device → Restore → select pre-patch snapshot.
     - For bare-metal restore, use Axcient local appliance or cloud failover.
  4. **Authorization Gate**: Confirm with client before any restore — data created after the patch window will be lost.
- Document rollback reason and all steps taken in PSA ticket.

### 7. Documentation & Reporting
- Log all patched systems in PSA ticket with:
  - Systems patched, KB IDs applied, reboot times.
  - Any failures and resolutions.
  - Final post-patch verification status (Pass/Fail per system).
- Update asset records with last patch date.

---

## Verification & Security Checklist

1. **Rollback Verified**: Confirmed a successful Veeam or Axcient backup exists within 24 hours before patching any production system.
2. **Change Window Approved**: Confirmed maintenance window is authorized — no patches deployed without approval.
3. **Staged Deployment**: Confirmed test/pilot systems were patched before production.
4. **Post-Patch Services**: Confirmed all auto-start services are running after reboot.
5. **Critical Patch SLA**: Confirmed CVSS ≥ 9.0 patches are deployed within 48-hour emergency window.
6. **Ticket Updated**: PSA ticket updated with full patch log, failures, and verification results.

## Future Integrations
- `rmm-mcp` *(agy-MCP blueprint — pending)*: RMM REST API for patch status queries, approval, and deployment without opening the console.
- `backup-mcp` *(agy-MCP blueprint — pending)*: Veeam and Axcient API calls to verify backup status and trigger restores directly from session.

---
*agy-skills — updated 2026-06-19*
