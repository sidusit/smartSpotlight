# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:08:51 2020

@author: sidus
"""


import os
from PIL import Image
import shutil

def checkResolution(fromDirectory,wallpaperFilename):
    img = Image.open(fromDirectory+wallpaperFilename)
    if img.width>1900:
        return True
    else:
        return False

# Code to update the wallpapers from the spotlight directory
def updateSpotlightWallpapers(fromDirectory, toDirectory):
    fromFiles = os.listdir(fromDirectory)
    toFiles = os.listdir(toDirectory)
    for f in fromFiles:
        if checkResolution(fromDirectory, f):
            if f.lower().endswith(('jpg','jpeg','png','bmp','tiff')):
                if f not in toFiles:
                    shutil.copy(fromDirectory+f, toDirectory)
            else:
                if f+'.jpg' not in toFiles:
                    shutil.copy(fromDirectory+f, toDirectory)
                    os.replace(toDirectory+f,toDirectory+f+'.jpg')

configDict = {}
with open('../config.txt','r') as f:
    for line in f.readlines():
        if '\n' in line:
            line = line.replace('\n','')
        splitList = line.split('=')
        configDict[splitList[0]] = splitList[1]

try:
    updateSpotlightWallpapers(configDict['fromDirectory'], configDict['toDirectory'])
    print('Successfull')
except:
    print('Unsuccessful..!')
    
