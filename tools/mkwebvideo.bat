@echo off
SET FFMPEG="%PROGRAMFILES%\Natron\bin\ffmpeg.exe"

REM CONVERT TO WEB COMPATIBLE MP4
%FFMPEG% -an -i %1 -vcodec libx264 -pix_fmt yuv420p -profile:v baseline -level 3 %1-export.mp4
