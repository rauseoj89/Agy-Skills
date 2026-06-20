---
name: "Incident Response"
description: "Structured triage, containment, investigation, remediation, and documentation workflow for security and operational incidents."
category: "generic/security"
tools_required: []
last_updated: 2026-06-19
---

# Skill: Incident Response Specialist

## Goal
Execute a structured, evidence-preserving incident response workflow from initial detection through full remediation and post-incident documentation. Integrates with the PSA system for ticket creation and audit trail.

## Inputs Required
- Incident description or alert trigger (user report, RMM alert, detection tool output).
- Affected systems, users, or services.
- Approximate time of first detection or suspicious activity.

## Toolstack
- **Monitoring / Alert Source**: RMM (Remote Monitoring and Management) — primary source for endpoint and network alerts.
- **Backup / Recovery**: Veeam (VMs and servers) and BCDR/Axcient (BCDR / physical endpoints).
- **Ticketing**: PSA (Professional Services Automation) — all incident actions logged here.

## MCP vs Native Fallback

| Capability | With psa-mcp | Without MCP |
|---|---|---|
| Ticket lookup | Search tickets by keyword or ID | Ask user for ticket number |
| Time entry logging | Review time entries tool | Document in session log manually |
| Notes review | Retrieve ticket notes | User pastes prior notes |

---

## Incident Severity Classification

| Severity | Definition | Response Time |
|---|---|---|
| P1 — Critical | Active breach, ransomware, data exfiltration, full outage | Immediate — escalate within 15 min |
| P2 — High | Compromised credentials, partial outage, malware detected | Within 1 hour |
| P3 — Medium | Suspicious activity, single-system issue, policy violation | Within 4 hours |
| P4 — Low | Informational alert, minor anomaly, no active threat | Within 24 hours |

---

## Step-by-Step Instructions

### 1. Detect & Triage
- Gather all available information before taking any action:
  - What system/service is affected?
  - What is the timeline of observed events?
  - Is the activity ongoing or historical?
  - How many users or systems are impacted?
- **Check the RMM** for the affected endpoint(s):
  - RMM console → Computer view → review recent alerts, script history, and agent status.
  - Check if the issue first appeared as an RMM alert — note the exact alert time as T0.
- Assign a severity level (P1–P4) based on the classification table above.
- **Do not remediate before containing** — premature action can destroy evidence.

### 2. Create or Update PSA Ticket
- If a ticket does not exist, instruct user to create one with:
  - Summary: `[IR-P{severity}] {brief description} — {date}`
  - Service Board: Security Incidents (or equivalent)
  - Priority: mapped to P1–P4
  - Initial note: time detected, affected systems, reporter name.
- If a ticket exists, search it with `Find service tickets` and pull full details.

### 3. Contain
- **Do not skip containment** — isolate before investigating.

  | Incident Type | Containment Action |
  |---|---|
  | Compromised user account | Revoke sessions → disable account → reset password |
  | Infected endpoint | Isolate from network (VLAN or physical disconnect) |
  | Ransomware | Isolate infected segment → take VSS snapshots before cleaning |
  | Data exfiltration | Block outbound destination IP/domain at firewall |
  | Brute force in progress | Block source IP → enable account lockout policy |

- Document every containment action with exact timestamp in the PSA ticket.
- **Authorization Gate**: Stop and confirm with user/client before any containment that causes downtime or service disruption.

### 4. Investigate
- Collect and preserve evidence before making changes:
  - Export relevant logs (event logs, firewall logs, email headers) to a dated folder.
  - Note log file paths, hash values, and collection timestamps.
  - Do not modify original log files — work on copies.
- Establish timeline: first indicator → lateral movement → impact.
- Identify root cause: phishing, unpatched CVE, misconfiguration, insider, other.
- Secrets Scan: check if any credentials, API keys, or certificates may have been exposed.

### 5. Eradicate & Remediate
- Remove the threat (malware, unauthorized accounts, malicious rules):
  - Delete or quarantine malicious files.
  - Remove unauthorized email forwarding rules, inbox rules, OAuth app grants.
  - Revoke any API keys or certificates that may have been compromised.
- Patch the root cause vulnerability before restoring service.
- Reset credentials for all accounts that touched affected systems.
- **Destructive Gate**: Stop and confirm before deleting any files, accounts, or configurations that cannot be recovered.

### 6. Recover
- **Verify backup exists before restoring** — confirm last successful backup pre-dates the incident:
  - **Veeam** (VMs and servers): Veeam console → Backups → locate affected VM → confirm restore point timestamp is before incident T0.
  - **Axcient** (physical endpoints / BCDR): Axcient portal → client device → confirm last clean backup timestamp.
- **Restore procedure**:
  - **Veeam VM restore**: right-click VM → Restore → Instant VM Recovery (fastest) or Full VM Restore. Select restore point dated before T0.
  - **Axcient restore**: portal → client → Restore → select pre-incident snapshot. For full bare-metal, use Axcient appliance or cloud failover.
  - **Authorization Gate**: Confirm with client before any restore — all post-incident data will be lost.
- Bring systems back in a controlled sequence: infrastructure → services → users.
- Monitor via RMM for 24–48 hours post-recovery for recurrence.
- Confirm normal operation with the affected user or system owner.

### 7. Document & Close
- Write a complete post-incident summary in the PSA ticket:
  ```
  ## Incident Summary
  **Detection:** [timestamp] — [how detected]
  **Root Cause:** [description]
  **Scope:** [affected systems/users]
  **Containment:** [actions taken + timestamps]
  **Eradication:** [what was removed/patched]
  **Recovery:** [how restored, from what backup]
  **Lessons Learned:** [what to prevent recurrence]
  **Follow-up Actions:** [owner + due date]
  ```
- Apply security notes rule: never include plaintext passwords or keys in ticket notes — use `[REDACTED]`.
- Close ticket only after client/stakeholder sign-off.

---

## Verification & Security Checklist

1. **Containment Before Remediation**: Confirmed threat was isolated before any eradication steps.
2. **Evidence Preserved**: Log copies saved with timestamps and hash values before system changes.
3. **Authorization Obtained**: Confirmed explicit approval for any action that causes downtime or data deletion.
4. **Credentials Reset**: All accounts touching affected systems had passwords/tokens rotated.
5. **Root Cause Patched**: Confirmed the initial attack vector has been closed, not just the symptom.
6. **Ticket Closed with Summary**: Full post-incident summary in PSA with lessons learned and follow-up owners.

## Future Integrations
- `psa-mcp` *(already active)*: Ticket lookup and note review during active incidents.
- `rmm-mcp` *(agy-MCP blueprint — pending)*: Pull RMM alert history and endpoint status during triage without opening the console.
- `backup-mcp` *(agy-MCP blueprint — pending)*: Verify backup/restore point availability and initiate restores during recovery phase.
- `vault-bridge-mcp` *(agy-MCP blueprint — pending)*: Automated credential rotation during eradication phase.

---
*agy-skills — updated 2026-06-19*
