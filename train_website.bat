@echo off
cd /d C:\sellbird
set /p target_url="Enter your website URL (e.g. https://yourbusiness.com): "
if "%target_url%"=="" (
    echo No URL entered. Exiting.
    pause
    exit /b
)
echo.
echo Training Sellbird on: %target_url% ...
echo This will analyze your site and create sellbird.local.yaml + skills automatically.
echo.
call .\venv\Scripts\sellbird.exe train %target_url%
echo.
echo ========================================================
echo Training finished!
echo ========================================================
pause
