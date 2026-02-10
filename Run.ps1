$venvPath = Join-Path -Path $PSScriptRoot -ChildPath '.venv'

if (-not (Test-Path -Path $venvPath -PathType Container)) {
    .\Setup.ps1
}

.\.venv\Scripts\Activate.ps1
python "$PSScriptRoot\main.py"
Deactivate
