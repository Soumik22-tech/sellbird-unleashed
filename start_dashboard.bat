@echo off
cd /d C:\sellbird
call .\venv\Scripts\activate.bat
echo Starting Sellbird Dashboard on http://127.0.0.1:5555 ...
sellbird dashboard
pause
