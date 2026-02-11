$FirstRun = $false

if (-not (Test-Path -Path ".venv")) {
    $FirstRun = $true
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv .venv
}

.\.venv\Scripts\Activate.ps1

if ($FirstRun) {
    Write-Host "Installing dependencies..." -ForegroundColor Cyan
    pip install -r requirements.txt
}

python src/main.py

deactivate