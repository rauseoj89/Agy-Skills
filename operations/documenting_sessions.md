---
name: "Documenting Sessions"
description: "Automatically tracks developer and agent session logs inside a hidden, git-ignored directory (CHG-Review) after Git pushes."
category: "generic/operations"
tools_required: ["git-mcp", "terminal-mcp"]
last_updated: 2026-05-24
---

# 🧠 Skill: Documenting Sessions (docum-md)

## 🎯 Goal
Automate tracking, capturing, and daily markdown logging of work sessions inside a private, hidden `CHG-Review` directory, ensuring `.gitignore` enforcements are strictly maintained to protect internal logs from being exposed to remote public repositories.

## 📊 Inputs Required
- Target project/repository path.
- Summary of changes, commands executed, decisions made, and achievements during the session.

---

## 🛠️ Step-by-Step Instructions

1. **Initialize private review area**:
   - Check if a directory named `CHG-Review` exists at the root of the active project. If not, create it.
   - On Windows, mark the directory with the **Hidden** OS attribute so it is not visible by default in standard file explorers.
   - Check if `.gitignore` exists at the project root. If not, create it.
   - Verify that `CHG-Review/` is registered in `.gitignore`. If not, append it with a `# Private change review directory` comment header.

2. **Session captures (Daily Review)**:
   - Identify when a work session concludes or immediately after running a `git push` command.
   - Format a structured session log using the markdown template.
   - Save or append the session log to `CHG-Review/YYYY-MM-DD.md` (using current local date).
   - If a log file already exists for that date, cleanly append the new entry below a fresh session timestamp separator rather than overwriting.

---

## 🛡️ Verification & Security Checklist

1. **Zero Git Exposure**: Run `git status` or `git status --ignored` to verify that `CHG-Review/` is fully ignored and never staged for commit.
2. **Windows Folder Attribute**: Confirm the directory has the `Hidden` attribute set.
3. **Format Integrity**: Verify the session review outputs have clean line breaks and compile properly formatted headers.

---

## ⚙️ Automated Integration Script (PowerShell)
You can automate this skill using this robust PowerShell utility. Save this script as `docum-helper.ps1` inside your local tools directory:

```powershell
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("Initialize", "LogSession")]
    [string]$Action,

    [Parameter(Mandatory=$false)]
    [string]$Summary,

    [Parameter(Mandatory=$false)]
    [string]$ProjectPath = (Get-Location).Path
)

# Helper function to find Git repository root
function Get-GitRoot ($path) {
    $current = Get-Item -Path $path
    while ($current -ne $null) {
        if (Test-Path (Join-Path $current.FullName ".git")) {
            return $current.FullName
        }
        $current = $current.Parent
    }
    return $path
}

$rootPath = Get-GitRoot $ProjectPath
$chgReviewPath = Join-Path $rootPath "CHG-Review"
$gitIgnorePath = Join-Path $rootPath ".gitignore"

switch ($Action) {
    "Initialize" {
        Write-Host "Initializing CHG-Review folder at: $chgReviewPath"
        
        # 1. Create folder if not exists
        if (-not (Test-Path -Path $chgReviewPath)) {
            New-Item -ItemType Directory -Path $chgReviewPath | Out-Null
            Write-Host "Created CHG-Review directory."
        }
        
        # 2. Make it hidden (Windows specific)
        try {
            $folder = Get-Item -Path $chgReviewPath -Force
            if (-not ($folder.Attributes -match "Hidden")) {
                $folder.Attributes = $folder.Attributes -bor [System.IO.FileAttributes]::Hidden
                Write-Host "Set hidden attribute on CHG-Review."
            }
        } catch {
            Write-Warning "Failed to set Hidden attribute: $_"
        }

        # 3. Handle .gitignore
        if (-not (Test-Path -Path $gitIgnorePath)) {
            New-Item -ItemType File -Path $gitIgnorePath | Out-Null
            Write-Host "Created new .gitignore file."
        }

        # Check if CHG-Review is already ignored
        $ignored = $false
        $lines = Get-Content -Path $gitIgnorePath -ErrorAction SilentlyContinue
        if ($lines -ne $null) {
            foreach ($line in $lines) {
                if ($line.Trim() -eq "CHG-Review" -or $line.Trim() -eq "CHG-Review/") {
                    $ignored = $true
                    break
                }
            }
        }

        if (-not $ignored) {
            # Add entry to gitignore
            Add-Content -Path $gitIgnorePath -Value "`r`n# Private change review directory`r`nCHG-Review/"
            Write-Host "Added CHG-Review/ to .gitignore."
        } else {
            Write-Host "CHG-Review/ is already in .gitignore."
        }
        
        Write-Host "Initialization complete successfully!"
    }
    
    "LogSession" {
        if ([string]::IsNullOrWhiteSpace($Summary)) {
            Write-Error "Summary is required for LogSession action."
            exit 1
        }
        
        # Ensure initialization runs first to make sure paths are correct
        if (-not (Test-Path -Path $chgReviewPath)) {
            New-Item -ItemType Directory -Path $chgReviewPath | Out-Null
        }
        try {
            $folder = Get-Item -Path $chgReviewPath -Force
            if (-not ($folder.Attributes -match "Hidden")) {
                $folder.Attributes = $folder.Attributes -bor [System.IO.FileAttributes]::Hidden
            }
        } catch {}
        
        # Determine the log file name: YYYY-MM-DD.md
        $dateStr = Get-Date -Format "yyyy-MM-dd"
        $logFilePath = Join-Path $chgReviewPath "$dateStr.md"
        $timeStr = Get-Date -Format "HH:mm:ss"
        
        $newLogFile = -not (Test-Path -Path $logFilePath)
        
        $content = [System.Text.StringBuilder]::new()
        
        if ($newLogFile) {
            $content.AppendLine("# Session Review - $dateStr")
            $content.AppendLine()
            $content.AppendLine("Private developer/agent session logs for $dateStr. Not tracked by git.")
            $content.AppendLine()
        }
        
        $content.AppendLine("## Session Log: $timeStr")
        $content.AppendLine()
        $cleanedSummary = $Summary.Trim() -replace '\\n', "`r`n" -replace '\\r', ""
        $content.AppendLine($cleanedSummary)
        $content.AppendLine()
        $content.AppendLine("---")
        $content.AppendLine()
        
        # Append content using UTF-8 encoding
        [System.IO.File]::AppendAllText($logFilePath, $content.ToString(), [System.Text.Encoding]::UTF8)
        
        Write-Host "Successfully logged session to: $logFilePath"
    }
}
```

---
*Created by Efficiency Core*
