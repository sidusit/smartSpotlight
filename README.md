# smartSpotlight
An automatic desktop wallpaper changer using windows spotlight wallpapers 
1. Automatically updates new background wallpapers from microsoft spotlight wallpapers
2. Automatically updates the wallpapers

**All using a a single click. !!**

## Pre-requisites
1. Download and Install anaconda latest version
  -  https://www.anaconda.com/

2. Add anaconda scripts directory path to your *path* environment variable
  - Eg. Find your Anaconda installed directory path and Add the following path, Example the following path *C:\Users\sidus\Anaconda3\Scripts\* to your environment *path* variable

## Configuration

### A. Change paths in configuration file

Specify the fromDirectory and the toDirectory variable in the config.txt file
1. *fromDirectory* - Should be the path to your assets directory in windows that stores the lock screen wallpapers.
    - You could also specify path to some other folder in your system from where only widescreen wallpapers suitable for desktop needs to be copied
2. *toDirectory* - The directory where the appropriate widescreen spotlight wallpapers will be stored (appended with .jpg for spotlight wallpapers)

### B. Change paths in bat files
  - For *smartSpotlight_v1.bat* replace the first line with path of the directory where you have kept the *smartSpotlight_v1.py* file.
  - For  *Background_v1.bat* replace the first line with path of the directory where you have kept the *randomBackground_v1.py* file


### C. (Optional) If you want amazing spotlight wallpaper archives
Download and Extract from below link and cut-paste the wallpers to you *toDirectory*
https://www.dropbox.com/sh/a3hymsi4i5rf8kw/AABbieyT6sbr3aoSw3j3U9Ila?dl=0

## How to use

1. Just double click the *smartSpotlight_v1.bat* file to update all new wallpapers added by microsoft in the assets directory
 (if asset directory is specified as fromDirectory)
  - **Recommendation** - This bat file can be run once a week (Or schedule it using windows task scheduler - https://www.youtube.com/watch?v=n2Cr_YRQk7o)

2. When you want to change the wallpaper double click the randomBackground_v1.bat (This can also be scheduled like above)

## Description of files code files used

### 1. smartSpotlight_v1.py
  - Updates all lockscreen wallpapers stored in the assets directory (or some other directory) to your directory (toDirectory) specified in the config file. 
  - Also renames the files to .jpg and checks if the image resolutions are wide enough to fit a desktop screen.

### 2. randomBackground_v1.py
Changes to a new wallpaper while randomly choosing a wallpaper from your specified folder(toDirectory) in the config file.

### 3. smartSpotlight_v1.bat and randomBackground_v1.bat
  - These are batch files that cd to your directory where the python codes files 1. and 2. are stored
  - Activates the Anaconda environment  
  - Runs its respective python file
