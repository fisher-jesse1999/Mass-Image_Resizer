@echo off
set /p width="Please enter the new width (in inches): "
set /p height="Please enter the new height (in inches): "
set startTime=%time%
forfiles /M *.png /C "cmd /c python resizer.py @FILE %width% %height%"
forfiles /M *.jpg /C "cmd /c python resizer.py @FILE %width% %height%"
echo Start: %startTime%
echo Finished: %time%