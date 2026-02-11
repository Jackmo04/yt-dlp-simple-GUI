# yt-dlp simple GUI

Simple Python program implementing a GUI for downloading Youtube Audio/Video using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

**Disclaimer:** This was intended to be a project for personal use and as such not a lot of attention was put into making it accessible to everyone.

## Installation
- It is reccomended for now that you **don't** use the compiled version, as it doesn't yet support update checking. If you still want to use it, you can find the latest release [here](https://github.com/Jackmo04/yt-dlp-simple-GUI/releases/latest).

## Usage
### Prerequisites
- Python 3.10 or higher

### Quick start
- Clone this repo to a local directory
- If you're on Windows, simply run `.\Run.ps1` in Powershell [[1]](#note1)
- If you're on Linux, simply run `./run.sh` in the terminal [[2]](#note2)

## Manual compilation
### Prerequisites
- Python 3.10 or higher

### Compiling
- Clone this repo to a local directory
- On Windows run `.\Install.ps1` [[1]](#note1)
- On Linux run `./install.sh` [[2]](#note2)
- If succesfull, you'll find the executable in the newly created `bin/` directory

## Notes

<a id='note1'>[1]</a> - Windows Powershell scripts might not work because they aren't signed. In this case you'll have to instead run:
```powershell
powershell.exe -ExecutionPolicy Bypass -File .\Run.ps1
```
If you just want to be able to run the script without bypassing the execution policy every time, you can change the execution policy for the current user (**MIGHT HAVE SECURITY IMPLICATIONS**) by running:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
in Powershell as an administrator.
For more information, see [this](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy) Microsoft documentation.

<a id='note2'>[2]</a> - On Linux, you might need to make the script executable by running:
```bash
chmod +x ./run.sh
``` 
before executing it.
