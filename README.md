# smartSpotlight: an automatic desktop wallpaper changer using windows spotlight wallpapers 
## 1. Automatically updates new background wallpapers from microsoft (takes from assets directory store locally) spotlight wallpapers
## 2. Automatically updates the wallpapers
# All using a a single click.

## Pre-requisites
A
1. Install anaconda latest version
https://www.anaconda.com/

2. Add anaconda scripts directory to your environment variable
Eg. Add the following path - **C:\Users\sidus\Anaconda3\Scripts\** to the path variable

## Configuration

### 1. Change paths in config.txt file

Specify the fromDirectory and the toDirectory variable in the config.txt file
a) fromDirectory - Should be the path to your assets directory in windows that stores the lock screen wallpapers
Alternatively for fromDirectory - You could also specify path to some other folder in your system from where only widescreen wallpapers suitable for desktop needs to be copied
b) toDirectory - The directory where the appropriate widescreen spotlight wallpapers will be stored (appended with .jpg ffor sptotlight wallpapers)

### 2. Change paths in bat files - smartSpotlight_v1.bat and randomBackground_v1.bat
In the first line of smartSpotlight_v1.bat replace the line with path of the directory where you have kept the smartSpotlight_v1.py file
In the first line of randomBackground_v1.bat replace the line with path of the directory where you have kept the randomBackground_v1.py file

### 3. (Optional) If you want amazing spotlight wallpaper archives
Download it from the below link and paste it in your toDirectory

## How to use

1. Just double click the smartSpotlight_v1.bat file to update all new wallpapers added by microsoft in the assets directory (if asset directory is specified as fromDirectory)
This would add all new wallpapers to your toDirectory (This bat file can be run once a week)

2. As and when you want to change the wallpaper double click the randomBackground_v1.bat


## Description of files code files used

### 1. smartSpotlight_v1.py
Updates all lockscreen wallpapers stored in the assets directory (or some other directory) to your directory (toDirectory) specified in the config file. Also renames the files to .jpg and checks if the image resolutions are wide enough to fit a desktop screen.

### 2. randomBackground_v1.py
Changes to a new wallpaper while randomly choosing a wallpaper from your specified folder(toDirectory) in the config file.

### 3. smartSpotlight_v1.bat and randomBackground_v1.bat
a) These are batch files that cd to your directory where the python codes files 1. and 2. are stored
b) Activates the Anaconda environment
c) Runs its respective python file
