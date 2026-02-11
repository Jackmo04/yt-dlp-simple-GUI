$venvPath = Join-Path -Path $PSScriptRoot -ChildPath '.venv'

if (Test-Path -Path $venvPath -PathType Container) {
    Write-Host "[!] The environment is already set up."
    Write-Host "[*] You can start the application by running './Run.ps1'"
} else {
    Write-Host "[*] Setting up the environment..."
    python -m venv .venv
    Write-Host "[+] Virtual environment created at .venv"
    .\.venv\Scripts\Activate.ps1
    Write-Host "[*] Installing dependencies..."
    pip install -r "$PSScriptRoot\requirements.txt"
    Write-Host "[+] Dependencies installed"
    Deactivate
    Write-Host "[+] All done!"
}