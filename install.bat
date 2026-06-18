@echo off
:: SKILLS4VIBE Easy Install Script for Windows
:: ==========================================
::
:: This script simplifies installing SKILLS4VIBE skills for Mistral Vibe CLI.
::
:: Usage:
::   install.bat                    - Install or update skills
::   install.bat --uninstall        - Remove installed skills
::   install.bat --no-symlinks      - Copy files instead of symlinking
::
:: Requires: Python 3 and Git

python "%~dp0install.py" %*

echo.
echo If you see errors about symlinks on Windows, try running as Administrator
echo or use the --no-symlinks flag to copy files instead.
