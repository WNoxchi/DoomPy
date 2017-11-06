# Python Plays GTAV Tutorial:
# https://www.youtube.com/watch?v=F4y4YOpUcTQ&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a&index=9
# Code adapted and coded-along with: https://github.com/Sentdex/pygta5/tree/master/Tutorial%20Codes
# ---------------------------------
# WNixalo - 2017-Nov-04 19:53
# 09: Neural Network Training Data for Self-Driving
# NOTE: using EuroTruck Simulator 2 & DOOM 2016
#       This code only compatible w/ MS Windows
# To get this to work I had to install pywin32 Build 221 from https://sourceforge.net/projects/pywin32/files/pywin32/
# and run the .exe as admin. pip installing the .whl file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32
# did not work. -- couldn't get the post-install script working. (Win8.1)
#
# Using pywin32 in grab_screen gives a huge speedup, although idk if pillow-simd
# would as well.
################################################################################

# Add paths to utility folders:
from sys import path as syspath
from os import path as ospath; from os import getcwd
syspath.insert(1, ospath.join(getcwd() + '/1-7_code/'))
syspath.insert(1, ospath.join(getcwd() + '/8-13_code/'))

import numpy as np
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from draw_lanes import draw_lanes
from grabscreen import grab_screen
from getkeys import key_check
import os

# convert pressed keys to one-hot array
def keys_to_output(keys):
    # [A,W,D]
    output = [0,0,0]
    # my model was defaulting to RIGHT bc no keys pressed results in RIGHT being
    # registered. So need to retrain.
    if 'A' in keys:
        output[0] = 1
    elif 'W' in keys:
        output[1] = 1
    elif: 'D' in keys:
        output[2] = 1
    return output

file_dir = 'train/'
file_name = 'training_data.npy'
if not os.path.exists(file_dir):
    os.mkdir(file_dir)

if os.path.isfile(file_dir+file_name):
    print("File exists. Loading data.")
    training_data = list(np.load(file_dir+file_name))    # this would be faster in pure NumPy
else:
    print("File does not exist. Starting new data set.")
    training_data = []


def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    last_time = time.time()
    while True:
        # region is bbox from PyGTAV_07_selfdrivingai.py
        screen = grab_screen(region=(8, 96, 1032, 734)) # (0,40,800,640)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (102, 64)) # roughly 0.1 scale
        keys = key_check()
        output = keys_to_output(keys)
        print(output)
        training_data.append([screen, output])
        # print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_dir+file_name, training_data)

if __name__ == "__main__":
    main()
