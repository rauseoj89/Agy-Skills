---
name: "Managing Microsoft 365"
description: "Administers Microsoft 365 users, licenses, MFA, Conditional Access, mailboxes, and groups using PowerShell and the Graph API."
category: "generic/operations"
tools_required: []
last_updated: 2026-06-19
---

# Skill: Microsoft 365 Administrator

## Goal
Provision and deprovision M365 users, enforce MFA and Conditional Access policies, audit licenses, manage mailbox delegations, and govern group membership — securely and with full audit trails.

## Inputs Required
- Target tenant domain or tenant ID.
- User UPN(s), group name(s), or license SKU to act on.
- Admin credentials injected via environment variables — never hardcoded.

## MCP vs Native Fallback

| Capability | With graph-api-mcp *(future)* | Without MCP (current) |
|---|---|---|
| User management | Graph API tool calls | PowerShell: `Microsoft.Graph` module |
| License assignment | Graph API tool calls | PowerShell: `Set-MgUserLicense` |
| MFA status check | Graph API tool calls | PowerShell: `Get-MgUserAuthMethod` |
| Mailbox management | Graph API tool calls | PowerShell: `ExchangeOnlineManagement` module |

> Until `graph-api-mcp` is deployed, all operations use PowerShell with the `Microsoft.Graph` and `ExchangeOnlineManagement` modules. Connect once per session; never store credentials in scripts.

---

## Step-by-Step Instructions

### 1. Secure Connection
- Connect using certificate-based or interactive auth — never username/password in scripts:
  ```powershell
  Connect-MgGraph -Scopes "User.ReadWrite.All","Group.ReadWrite.All","Directory.ReadWrite.All"
  Connect-ExchangeOnline -UserPrincipalName admin@domain.com
  ```
- Confirm connected tenant before any write operation:
  ```powershell
  Get-MgOrganization | Select DisplayName, Id
  ```

### 2. User Provisioning
- Create user with required fields only — never set a plaintext password in script:
  ```powershell
  $params = @{
    DisplayName       = "Jane Doe"
    UserPrincipalName = "jdoe@domain.com"
    MailNickname      = "jdoe"
    AccountEnabled    = $true
    PasswordProfile   = @{ ForceChangePasswordNextSignIn = $true; Password = $env:TEMP_USER_PASSWORD }
  }
  New-MgUser @params
  ```
- Assign license immediately after creation:
  ```powershell
  Set-MgUserLicense -UserId "jdoe@domain.com" -AddLicenses @{SkuId = "<SKU-GUID>"} -RemoveLicenses @()
  ```

### 3. User Deprovisioning
- Follow this sequence in order — never skip steps:
  1. Revoke all active sessions: `Revoke-MgUserSignInSession -UserId $upn`
  2. Disable account: `Update-MgUser -UserId $upn -AccountEnabled $false`
  3. Remove from all groups and distribution lists.
  4. Convert mailbox to shared (retain 30 days): `Set-Mailbox $upn -Type Shared`
  5. Remove licenses (stop billing): `Set-MgUserLicense -UserId $upn -RemoveLicenses @("<SKU-GUID>") -AddLicenses @()`
  6. Log action with timestamp in PSA ticket or session log.

### 4. MFA Enforcement Audit
- List users without MFA registered:
  ```powershell
  Get-MgUser -All | ForEach-Object {
    $methods = Get-MgUserAuthenticationMethod -UserId $_.Id
    if ($methods.Count -le 1) { $_.UserPrincipalName }
  }
  ```
- Flag any admin accounts without Phishing-Resistant MFA (FIDO2 or Certificate) as CRITICAL.
- Never disable MFA for any account — escalate to client if requested.

### 5. Conditional Access Review
- List all CA policies and their enabled/disabled state:
  ```powershell
  Get-MgIdentityConditionalAccessPolicy | Select DisplayName, State, CreatedDateTime
  ```
- Verify these policies exist and are **Enabled**:
  - Require MFA for all users.
  - Block legacy authentication protocols.
  - Require compliant device for admin roles.
- Flag any policy in `reportOnly` state as needing promotion to `enabled`.

### 6. License Audit
- List all SKUs and consumed units:
  ```powershell
  Get-MgSubscribedSku | Select SkuPartNumber, ConsumedUnits, @{N="Available";E={$_.PrepaidUnits.Enabled - $_.ConsumedUnits}}
  ```
- Flag SKUs where `Available < 5` (low license headroom warning).
- Flag users with duplicate/redundant license assignments for cost optimization.

### 7. Mailbox Delegation & Shared Mailboxes
- Grant mailbox access (Full Access):
  ```powershell
  Add-MailboxPermission -Identity "shared@domain.com" -User "jdoe@domain.com" -AccessRights FullAccess -InheritanceType All
  ```
- Audit existing delegations:
  ```powershell
  Get-MailboxPermission -Identity "shared@domain.com" | Where-Object { $_.User -notlike "NT AUTHORITY*" }
  ```
- Never grant SendAs to distribution groups without explicit client approval.

---

## Verification & Security Checklist

1. **No Plaintext Credentials**: Confirm zero passwords or tokens appear in any script, log, or session output.
2. **MFA Enabled**: Confirm all users — especially admins — have MFA registered before session ends.
3. **Deprovisioning Order**: Confirm session revoke → disable → license remove sequence was followed in full.
4. **CA Policy State**: Confirm no critical CA policies are in `reportOnly` or `disabled` state.
5. **License Headroom**: Confirm no SKU is at 100% consumption (would block new user provisioning).
6. **Audit Trail**: Confirm all changes are logged in PSA ticket or session documentation.

## Future Integrations
- `graph-api-mcp` *(agy-MCP blueprint — pending)*: Direct Graph API calls for user, group, and mailbox management without PowerShell session overhead.

---
*agy-skills — updated 2026-06-19*
