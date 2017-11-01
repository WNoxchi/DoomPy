# Python Plays GTAV Tutorial:
# https://www.youtube.com/watch?v=tWqbl9IUdCg&index=3&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a
# https://github.com/Sentdex/pygta5
# ---------------------------------
# WNixalo - 2017-Oct-31 21:14
# 03: Direct Input
# NOTE: using EuroTruck Simulator 2 & DOOM 2016
################################################################################
# NOTE: this program presses W for 3 seconds, then D for 3 seconds.

import numpy as np
from PIL import ImageGrab
import cv2
import time

# this will not work: (DirectX games expect ScanCodes not VKs)
# import pyautogui
# for i in list(range(4))[::-1]:
#     print(i+1)
#     time.sleep(1)
# print('down')
# pyautogui.keyDown('w')
# time.sleep(3)
# print('up')
# pyautogui.keyUp('w')

# so we import (from local):
from directkeys import PressKey, ReleaseKey, W, A, S, D

# countdown for giving enough time to enter game after starting program
# makes a list of a generator, then flips it, and scans thru
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

# enter key presses to game
print('down')
PressKey(D)
time.sleep(3)
ReleaseKey(D)
print('up')
PressKey(W)
ReleaseKey(W)
