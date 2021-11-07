@echo off
reg delete "HKCU\SOFTWARE\INRIA\Natron" /f
rmdir /S /Q %LOCALAPPDATA%\INRIA\Natron
