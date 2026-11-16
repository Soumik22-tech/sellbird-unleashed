@echo off
cd /d C:\sellbird
call .\venv\Scripts\activate.bat
echo Starting Sellbird Worker Loop...
sellbird run
pause
