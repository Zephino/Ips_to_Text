@echo off
setlocal
REM Converts every .ips file in this folder to a .txt file in this folder.
REM Keep this .bat, ips_to_text.py, and your .ips files together.

cd /d "%~dp0"

REM Find Python (tries "python" first, then "py")
set "PY="
where python >nul 2>nul && set "PY=python"
if not defined PY where py >nul 2>nul && set "PY=py"
if not defined PY (
    echo Python was not found. Install it from https://www.python.org/downloads/
    echo and tick "Add Python to PATH" during install.
    pause
    exit /b 1
)

if not exist "ips_to_text.py" (
    echo ips_to_text.py is not in this folder: %~dp0
    pause
    exit /b 1
)

set "FOUND=0"
for %%F in (*.ips) do (
    set "FOUND=1"
    echo Converting %%F ...
    %PY% "ips_to_text.py" "%%~fF"
)

if "%FOUND%"=="0" echo No .ips files found in %~dp0

echo.
echo Done. Text files are in: %~dp0
pause
