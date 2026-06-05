# DDOS INFINITY X - one-click publish to GitHub
# Run: powershell -ExecutionPolicy Bypass -File publish.ps1

$ErrorActionPreference = "Stop"
$env:Path = "C:\Program Files\Git\bin;C:\Program Files\GitHub CLI;" + $env:Path

$RepoName = "DDOS-INFINITY-X"
$Root = $PSScriptRoot
Set-Location $Root

Write-Host "`n=== DDOS INFINITY X - GitHub Publish ===`n" -ForegroundColor Magenta

# 1) GitHub login
$auth = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Login required. Browser will open..." -ForegroundColor Yellow
    gh auth login -h github.com -p https -w
}

$User = gh api user -q .login
Write-Host "Logged in as: $User" -ForegroundColor Green

# 2) Update repo URLs if username differs from adilf
if ($User -ne "adilf") {
    Write-Host "Updating links to github.com/$User/$RepoName ..." -ForegroundColor Cyan
    $files = @("README.md", "banner.py", "CREDITS.md", "PUBLISH_GITHUB.md", "Dockerfile", ".github\ISSUE_TEMPLATE\config.yml", ".github\ISSUE_TEMPLATE\feature_request.yml")
    foreach ($f in $files) {
        if (Test-Path $f) {
            (Get-Content $f -Raw) -replace "Infinity-X202/DDOS-INFINITY-X", "$User/$RepoName" -replace "github.com/Infinity-X202", "github.com/$User" | Set-Content $f -NoNewline
        }
    }
    git add -A
    git -c user.name="adil fayyaz" -c user.email="$User@users.noreply.github.com" commit -m "chore: set GitHub URLs to $User" 2>$null
}

# 3) Create repo (ignore if exists)
gh repo view "$User/$RepoName" 2>$null
if ($LASTEXITCODE -ne 0) {
    gh repo create $RepoName --public --description "DDOS INFINITY X - educational stress-testing framework by adil fayyaz" --source=. --remote=origin --push
} else {
    git remote remove origin 2>$null
    git remote add origin "https://github.com/$User/$RepoName.git"
    git push -u origin main
}

Write-Host "`nDone! https://github.com/$User/$RepoName`n" -ForegroundColor Green
