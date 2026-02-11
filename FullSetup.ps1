$venvPath = Join-Path -Path $PSScriptRoot -ChildPath '.venv'

if (Test-Path -Path $venvPath -PathType Container) {
    Write-Host "[!] The environment is already set up."
} else {
    Write-Host "[*] Setting up the environment..."
    python -m venv .venv
    Write-Host "[+] Virtual environment created at .venv"
    .\.venv\Scripts\Activate.ps1
    Write-Host "[*] Installing dependencies..."
    pip install -r "$PSScriptRoot\requirements.txt"
    Write-Host "[+] Dependencies installed"
    Write-Host "[*] Installing PyInstaller..."
    pip install pyinstaller
    Write-Host "[+] PyInstaller installed"
    Write-Host "[*] Compiling the application..."
    python "$PSScriptRoot\build.py"
    Deactivate
    Write-Host "[*] Removing build artifacts..."
    New-Item -Type Directory -Name 'bin\'
    Move-Item -Path "$PSScriptRoot\dist\*" -Destination "$PSScriptRoot\bin\" -Force
    Remove-Item -Path "$PSScriptRoot\dist" -Force
    Remove-Item -Path "$PSScriptRoot\build" -Recurse -Force
    Remove-Item -Path "$PSScriptRoot\*.spec" -Force
    Remove-Item -Path "$PSScriptRoot\.venv" -Recurse -Force
    Write-Host "[+] Build complete and environment cleaned up"
    write-host "[*] You can find the compiled application in the 'bin' directory."
}