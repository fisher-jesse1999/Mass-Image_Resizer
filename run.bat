@echo off
echo ===== Jesse's Image Resizer =====
echo Warning: resizing the same image multiple times can degrade the quality of the photo.
echo Consider having the program not overwrite your existing images if you are unsure of the size you want.

set /p width="Please enter the new width (in inches): "
set /p height="Please enter the new height (in inches): "
set /p overwrite="Would you like your current images overwritten? (yes/no): "

set startTime=%time%

@REM process any png files in the current directory
if exist *.png (
    forfiles /M *.png /C "cmd /c python resizer.py @FILE %width% %height% %overwrite%"
) else (
    echo No .png files were found, moving on.
)

@REM process any jpg files in the current directory
if exist *.jpg (
    forfiles /M *.jpg /C "cmd /c python resizer.py @FILE %width% %height% %overwrite%"
) else (
    echo No .jpg files were found, moving on.
)

@REM check for resized files, and create a new directory for them if needed
if exist resized-* (
    if not exist resizedPhotos mkdir resizedPhotos
    move resized-* resizedPhotos
    echo Your resized files have been stored in the resizedPhotos folder.
)

echo Start: %startTime%
echo Finished: %time%