# PyGTAV: https://www.youtube.com/watch?v=H5D-6IsFn40&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a&index=12
# WNixalo - 2017-Nov-05 20:05
# 12: Testing AlexNet Self-Driving Var NN Model
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
from alexnet import alexnet
import os

WIDTH = 102
HEIGHT = 64
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'pygtav-car-{}-{}-{}-epochs.model'.format(LR, 'alexnet', EPOCHS)
DIR = 'train/'

turn_thresh = 0.65
fwd_thresh  = 0.6
t_time = 0.09

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
def left():
    PressKey(A)
    PressKey(W)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)
def right():
    PressKey(D)
    PressKey(W)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)
def letgo():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    ReleaseKey(D)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(DIR+MODEL_NAME)

def main():
    print('Loading Driver Bot. Press \'Z\' to pause 10 seconds, Ctrl-C: Quit')
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    while True:
        if not paused:
            # region is bbox from PyGTAV_07_selfdrivingai.py
            screen = grab_screen(region=(8, 96, 1032, 734)) # (0,40,800,640)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (102, 64)) # roughly 0.1 scale
            # λtime = time.time()-last_time
            # print('Frame: {} seconds. FPS: {}'.format(λtime, 1/λtime))
            # last_time = time.time()

            # returns list of predicted one-hot moves. last arg 1 for Grayscale;
            # 3 if RGB model. We're passing a single feature at a time, and we
            # want to get a single action at a time, so specify 1st idx.
            prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]
            # moves = list(np.around(prediction))
            # print(moves, prediction)

            if prediction[1] > fwd_thresh:
                straight()
                print(prediction, ' FORWARD')
            elif prediction[0] > turn_thresh:
                left()
                print(prediction, ' LEFT')
            elif prediction[2] > turn_thresh:
                right()
                print(prediction, ' RIGHT')
            else:
                letgo()
                print(prediction, ' LETGO')

            # if moves == [1,0,0]:
            #     left()
            # elif moves == [0,1,0]:
            #     straight()
            # elif moves == [0,0,1]:
            #     right()
            # elif moves == [0,0,0]:
            #     letgo()

        # for stopping program
        keys = key_check()
        if 'Z' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(10)

if __name__ == "__main__":
    main()
