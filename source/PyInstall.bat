@echo off
set b=%cd%
pyinstaller -F -i "%b%\Automate Statistics.ico" "%b%\Automate Statistics.py"
pause