@echo off
setlocal EnableDelayedExpansion

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Downloading and installing Python...
    powershell -Command "Start-Process 'https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe' -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait"
    echo Python installed successfully.
)

:: Ensure pip is installed and up-to-date
python -m ensurepip --upgrade
python -m pip install --upgrade pip

:: Install customtkinter library
pip install customtkinter

echo CustomTkinter installation complete.

pause
