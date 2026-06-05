@echo off
title DDOS INFINITY X - Install
cd /d "%~dp0"

echo ==============================================
echo   DDOS INFINITY X - Install
echo   by adil fayyaz
echo ==============================================

where python >nul 2>&1
if errorlevel 1 (
    echo [!] Python not found. Install from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [*] Creating virtual environment...
python -m venv venv
if errorlevel 1 exit /b 1

echo [*] Installing dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 exit /b 1

if not exist "files\proxies" mkdir files\proxies
type nul > files\proxies\http.txt 2>nul

echo.
echo [+] Install complete!
echo.
echo   Start menu:  run.bat
echo   Or:        venv\Scripts\activate.bat
echo              python start.py
echo.
pause
