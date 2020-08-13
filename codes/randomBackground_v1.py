# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:34:42 2020

@author: sidus
"""
import os
import ctypes
import numpy as np

configDict = {}
with open('../config.txt','r') as f:
    for line in f.readlines():
        if '\n' in line:
            line = line.replace('\n','')
        splitList = line.split('=')
        configDict[splitList[0]] = splitList[1]


toFiles = os.listdir(configDict['toDirectory'])
randomNum = np.random.randint(0,len(toFiles))
file = toFiles[randomNum]

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, configDict['toDirectory']+file , 1)
