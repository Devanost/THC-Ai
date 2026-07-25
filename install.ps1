# THC Ai - One-liner Installer for Windows
$ErrorActionPreference = "Stop"

Write-Host "🚀 Installing THC Ai..." -ForegroundColor Cyan

# Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed. Please install it from python.org" -ForegroundColor Red
    exit 1
}

# Create a temporary directory
$tempDir = [System.IO.Path]::GetTempFileName()
Remove-Item $tempDir
New-Item -ItemType Directory -Path $tempDir | Out-Null
Set-Location $tempDir

# Clone the repository
Write-Host "📦 Fetching latest version from GitHub..." -ForegroundColor Cyan
git clone --quiet https://github.com/Devanost/THC-Ai.git .

# Install the package
Write-Host "⚙️ Installing dependencies and setting up 'thc-ai' command..." -ForegroundColor Cyan
python -m pip install . --quiet

# Clean up
Set-Location $HOME
Remove-Item -Recurse -Force $tempDir

Write-Host "✅ THC Ai installed successfully!" -ForegroundColor Green
Write-Host "👉 Type 'thc-ai' to start talking." -ForegroundColor Green
