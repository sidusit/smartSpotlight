# smartSpotlight: an Automatic Desktop Wallpaper changer for Windows
Automatic update of background wallpapers using windows lock screen (spotlight) and wallpaper change, All using a a single click.

## Pre-requisites
A
1. Install anaconda latest version
https://www.anaconda.com/

2. Add anaconda scripts directory to your environment variable
Eg. Add the following path - **C:\Users\sidus\Anaconda3\Scripts\** to the path variable

1. Install python 
https://www.python.org/downloads/
check if you have the following libraries
os 
PIL
shutil
ctypes
numpy

## Configuration

### 1. Change paths in config.txt file

Specify the fromDirectory and the toDirectory variable in the config.txt file.
fromDirectory - Should be the path to your assets directory in windows that stores the lock screen wallpapers
toDirectory - 

## How to use



## Files used

### 1. smartSpotlight_v1.py and smartSpotlight_v1.bat
Updates all lockscreen wallpapers stored in the Assets directory(or some other directory) to your directory specified in the config file. Also renames the files to .jpg and check if the image resolutions are wide enough to fit a desktop screen.


### 2. randomBackground_v1.py and randomBackground_v1.bat
Changes to a new wallpaper while randomly choosing a wallpaper from your specified folder in the config directory.
