@echo off
echo ========================================
echo Task Automation Test Script for Windows
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://python.org
    pause
    exit /b 1
)

echo Python is installed. Checking dependencies...

REM Install dependencies if needed
echo Installing required packages...
pip install -r requirements-automation.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Dependencies installed successfully!
echo.
echo To test your automation setup:
echo 1. Get your GitHub token from GitHub Settings
echo 2. Run: python test_automation.py --token YOUR_TOKEN_HERE
echo.
echo Example:
echo python test_automation.py --token ghp_xxxxxxxxxxxxxxxxxxxx
echo.
pause 