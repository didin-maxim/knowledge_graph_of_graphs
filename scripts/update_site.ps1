[CmdletBinding()]
param(
    [switch]$SkipChecks,
    [switch]$SkipIndex,
    [switch]$Commit,
    [switch]$Push,
    [switch]$IncludeAllChanges,
    [string]$Message = "Refresh site data",
    [string]$Remote = "origin",
    [string]$Branch = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $RepoRoot

function Invoke-Step {
    param(
        [string]$Name,
        [scriptblock]$Action
    )

    Write-Host ""
    Write-Host "==> $Name"
    & $Action
}

function Invoke-External {
    param(
        [string]$Program,
        [string[]]$Arguments
    )

    & $Program @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Program $($Arguments -join ' ') failed with exit code $LASTEXITCODE"
    }
}

if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot "tools\build_viewer.py"))) {
    throw "Run this script from inside the repository, or keep it in the repository scripts directory."
}

Invoke-Step "Repository" {
    Write-Host $RepoRoot
}

if (-not $SkipChecks) {
    Invoke-Step "Validate data" {
        Invoke-External "python" @("tools\validate.py")
    }

    Invoke-Step "Check links" {
        Invoke-External "python" @("tools\check_links.py")
    }
}

if (-not $SkipIndex) {
    Invoke-Step "Build search index" {
        Invoke-External "python" @("tools\build_index.py")
    }
}

Invoke-Step "Build viewer and GitHub Pages output" {
    Invoke-External "python" @("tools\build_viewer.py")
}

Invoke-Step "Current changes" {
    Invoke-External "git" @("status", "--short")
}

if ($Commit) {
    Invoke-Step "Stage changes" {
        if ($IncludeAllChanges) {
            Invoke-External "git" @("add", "-A")
        } else {
            Invoke-External "git" @(
                "add",
                "--",
                "data",
                "docs",
                "viewer",
                "scripts\update_site.ps1"
            )
        }
    }

    Invoke-Step "Commit changes" {
        & git diff --cached --quiet
        $diffExit = $LASTEXITCODE
        if ($diffExit -eq 0) {
            Write-Host "No staged changes to commit."
        } elseif ($diffExit -eq 1) {
            Invoke-External "git" @("commit", "-m", $Message)
        } else {
            throw "git diff --cached --quiet failed with exit code $diffExit"
        }
    }
}

if ($Push) {
    Invoke-Step "Push changes" {
        $targetBranch = $Branch
        if (-not $targetBranch) {
            $targetBranch = (& git rev-parse --abbrev-ref HEAD).Trim()
            if ($LASTEXITCODE -ne 0) {
                throw "Could not determine current git branch."
            }
        }
        if ($targetBranch -eq "HEAD") {
            throw "Cannot push from detached HEAD. Pass -Branch explicitly after checking out a branch."
        }
        Invoke-External "git" @("push", $Remote, $targetBranch)
    }
}

Write-Host ""
Write-Host "Done."
Write-Host "Local site file: $RepoRoot\docs\index.html"
if (-not $Commit -or -not $Push) {
    Write-Host "To publish, rerun with -Commit -Push after reviewing the status output."
}
