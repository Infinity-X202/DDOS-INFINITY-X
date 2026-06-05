@echo off
title DDOS INFINITY X - Pubblica su GitHub
color 0D
set "PATH=C:\Program Files\Git\bin;C:\Program Files\GitHub CLI;%PATH%"
cd /d "%~dp0"

echo.
echo  ============================================
echo   DDOS INFINITY X - Pubblicazione GitHub
echo   by adil fayyaz
echo  ============================================
echo.

gh auth status >nul 2>&1
if errorlevel 1 (
    echo  [1/2] Apri il browser e autorizza GitHub...
    echo        Codice e link appariranno tra pochi secondi.
    echo.
    start https://github.com/login/device
    gh auth login -h github.com -p https -w
    if errorlevel 1 (
        echo.
        echo  ERRORE: login non completato. Riprova.
        pause
        exit /b 1
    )
)

echo.
echo  [2/2] Creo il repository e carico i file...
echo.
powershell -ExecutionPolicy Bypass -File "%~dp0publish.ps1"
echo.
pause
