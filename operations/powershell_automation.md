---
name: "PowerShell Automation"
description: "Authors, tests, and safely deploys PowerShell scripts for Windows automation — parameter validation, SecureString secrets, Pester testing, and execution policy."
category: "generic/operations"
tools_required: []
last_updated: 2026-06-19
---

# Skill: PowerShell Automation Specialist

## Goal
Write production-quality, secure PowerShell scripts for Windows automation — with proper parameter validation, secret handling via SecureString or Vault, structured error handling, Pester test coverage, and safe deployment patterns.

## Inputs Required
- Automation goal description (what the script should do).
- Target environment: local, remote PSSession, or scheduled task.
- Secrets required (loaded from environment variables or vault — never hardcoded).

## MCP vs Native Fallback

| Capability | With terminal-mcp *(future)* | Without MCP (current) |
|---|---|---|
| Run script on remote host | `execute_command` tool | `Invoke-Command` / PSSession |
| Check execution policy | `execute_command` tool | Direct PowerShell Bash tool call |
| Read script output | `execute_command` tool | Native Bash/PowerShell tool |

---

## Script Structure Standard

Every script must follow this layout:

```powershell
#Requires -Version 5.1
<#
.SYNOPSIS
  One-line description.
.DESCRIPTION
  What the script does and what it requires.
.PARAMETER ParamName
  Description of parameter.
.EXAMPLE
  .\ScriptName.ps1 -ParamName "value"
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory, HelpMessage = "Description")]
    [ValidateNotNullOrEmpty()]
    [string]$ParamName,

    [Parameter()]
    [ValidateRange(1, 100)]
    [int]$Count = 10
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# --- Functions ---

function Invoke-SomeAction {
    [CmdletBinding(SupportsShouldProcess)]
    param([string]$Target)

    if ($PSCmdlet.ShouldProcess($Target, "Action description")) {
        # do work
    }
}

# --- Main ---
try {
    Invoke-SomeAction -Target $ParamName
}
catch {
    Write-Error "Script failed: $_"
    exit 1
}
```

---

## Step-by-Step Instructions

### 1. Parameter Design
- Use `[CmdletBinding()]` on every script — enables `-Verbose`, `-WhatIf`, `-Confirm`.
- Validate all inputs at the parameter level — never inside function bodies:
  ```powershell
  [ValidateNotNullOrEmpty()]  # no empty strings
  [ValidateSet("dev","staging","production")]  # enum constraint
  [ValidatePattern("^[a-zA-Z0-9._-]+$")]  # regex constraint
  [ValidateRange(1, 65535)]  # numeric bounds
  ```
- Never accept credentials as plain `[string]` — use `[System.Management.Automation.PSCredential]` or load from environment:
  ```powershell
  $password = ConvertTo-SecureString $env:SERVICE_PASSWORD -AsPlainText -Force
  $cred = New-Object PSCredential("serviceaccount@domain.com", $password)
  ```

### 2. Secret Handling
- **Never hardcode** passwords, API keys, or connection strings in scripts.
- Load secrets exclusively from environment variables or vault:
  ```powershell
  # From environment variable
  $apiKey = $env:MY_API_KEY

  # From Windows Credential Manager (SecretManagement module)
  $secret = Get-Secret -Name "MyApiKey" -AsPlainText
  ```
- Use `ConvertTo-SecureString` for any secret that must be held in memory.
- Use `[System.Runtime.InteropServices.Marshal]::ZeroFreeGlobalAllocUnicode()` to wipe SecureString from memory after use in long-running scripts.

### 3. Error Handling
- Set `$ErrorActionPreference = 'Stop'` at script top — converts non-terminating errors to terminating.
- Wrap all external calls in `try/catch/finally`:
  ```powershell
  try {
      $result = Invoke-RestMethod -Uri $uri -Headers $headers
  }
  catch [System.Net.WebException] {
      Write-Error "Network error: $($_.Exception.Message)"
      exit 1
  }
  catch {
      Write-Error "Unexpected error: $_"
      exit 1
  }
  finally {
      # Cleanup: close connections, remove temp files
      if ($tempFile -and (Test-Path $tempFile)) { Remove-Item $tempFile -Force }
  }
  ```
- Always return meaningful exit codes: `exit 0` (success), `exit 1` (failure).

### 4. Destructive Operation Gate
- Any script with `Remove-Item`, `Format-`, `Clear-`, `Reset-`, or `Stop-Service` must implement `-WhatIf` and `-Confirm` support via `SupportsShouldProcess`.
- Test with `-WhatIf` first — confirm output before live run:
  ```powershell
  .\CleanupScript.ps1 -WhatIf  # dry run first
  .\CleanupScript.ps1 -Confirm  # prompt per item
  ```
- Never use `-Force` and `-Recurse` together on `Remove-Item` without explicit user confirmation.

### 5. Pester Testing
- Write Pester tests for every function that has logic:
  ```powershell
  # ScriptName.Tests.ps1
  BeforeAll {
      . "$PSScriptRoot\ScriptName.ps1"  # dot-source to import functions
  }

  Describe "Invoke-SomeAction" {
      It "Should process valid input" {
          $result = Invoke-SomeAction -Target "testhost"
          $result | Should -Not -BeNullOrEmpty
      }

      It "Should reject empty target" {
          { Invoke-SomeAction -Target "" } | Should -Throw
      }
  }
  ```
- Run tests before deploying:
  ```powershell
  Invoke-Pester -Path .\ScriptName.Tests.ps1 -Output Detailed
  ```
- Minimum: one happy-path test and one invalid-input test per function.

### 6. Execution Policy & Deployment
- Never set `Unrestricted` on production systems.
- Use `RemoteSigned` for scripts you control, `AllSigned` for maximum security:
  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope LocalMachine
  ```
- For scheduled tasks, run as a service account (not `SYSTEM` or a personal account):
  ```powershell
  $action = New-ScheduledTaskAction -Execute "pwsh.exe" -Argument "-NonInteractive -File C:\Scripts\MyScript.ps1"
  $trigger = New-ScheduledTaskTrigger -Daily -At "02:00"
  Register-ScheduledTask -TaskName "MyTask" -Action $action -Trigger $trigger -RunLevel Highest
  ```
- Log output to a file with timestamps for scheduled tasks:
  ```powershell
  Start-Transcript -Path "C:\Logs\MyScript_$(Get-Date -f yyyyMMdd_HHmmss).log" -Append
  ```

### 7. Use Approved Verbs
- Always use PowerShell approved verbs to prevent warnings and maintain discoverability:
  ```powershell
  Get-ApprovedVerb  # list all approved verbs
  ```
- Common approved pairs: `Get-`/`Set-`, `New-`/`Remove-`, `Start-`/`Stop-`, `Import-`/`Export-`, `Invoke-`/`Test-`.

---

## Verification & Security Checklist

1. **No Hardcoded Secrets**: Confirm zero passwords, API keys, or connection strings appear in the script source.
2. **Parameter Validation**: Confirm all `[Parameter()]` inputs have a `[Validate*]` attribute.
3. **ShouldProcess on Destructive Ops**: Confirm any script with Delete/Format/Stop uses `[CmdletBinding(SupportsShouldProcess)]`.
4. **Pester Coverage**: Confirm at least one happy-path and one invalid-input test exist per function.
5. **StrictMode Enabled**: Confirm `Set-StrictMode -Version Latest` is at script top.
6. **Exit Codes**: Confirm script exits `0` on success and `1` on unhandled error.

---
*agy-skills — updated 2026-06-19*
