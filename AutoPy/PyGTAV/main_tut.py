# Python Plays GTAV Tutorial:
# https://www.youtube.com/watch?v=F4y4YOpUcTQ&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a&index=9
# Code adapted and coded-along with: https://github.com/Sentdex/pygta5/tree/master/Tutorial%20Codes
# ---------------------------------
# WNixalo - 2017-Nov-04 19:53
# 09: Neural Network Training Data for Self-Driving
# NOTE: using EuroTruck Simulator 2 & DOOM 2016
#       This code only compatible w/ MS Windows
################################################################################

# Add paths to utility folders:
from sys import path as syspath
from os import path as ospath; from os import getcwd
syspath.insert(1, ospath.join(getcwd() + '1-7_code/')
syspath.insert(1, ospath.join(getcwd() + '8-13_code/')

import numpy as np
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from draw_lanes import draw_lanes
from grabscreen import grab_screen
from getkeys import key_press
import os

# convert pressed keys to one-hot array
def keys_to_output(keys):
    # [A,W,D]
    output = [0,0,0]

    if 'A' in keys:
        output[0] = 1
    elif 'W' in keys:
        output[1] = 1
    else:   # 'D'
        output[2] = 1
    return output

file_name = 'training_data_

last_time = time.time()
while True:
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    screen = grab_screen(region=(0,40,800,640))
    print('Frame took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    new_screen,original_image, m1, m2 = process_img(screen)
    #cv2.imshow('window', new_screen)
    cv2.imshow('window2',cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

    if m1 < 0 and m2 < 0:
        right()
    elif m1 > 0  and m2 > 0:
        left()
    else:
        straight()

    #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
