# Python Plays GTAV Tutorial:
# https://www.youtube.com/watch?v=ks4MPfMq8aQ&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a
# https://github.com/Sentdex/pygta5
# ---------------------------------
# WNixalo - 2017-Oct-31 15:23
# 01: Intro & Screen Reading
# NOTE: using EuroTruck Simulator 2 for this
################################################################################

# doing a screen grab
import numpy as np; import cv2
from PIL import ImageGrab
import time

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,280,800, 880))) # x1,y1, x2,y2     # <- still works w/o np.array() but
    # screen = ImageGrab.grab(bbox=(5, 20, 1085, 740))                          # further operations (gray, edges) need
    # printscreen_numpy = np.array(screen.getdata(), dtype='uint8')\
    #             .reshape((screen.size[1], screen.size[0], 4)) # last arg is shape: need 4 for png (RGBA)
    print('Loop toop {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    # cv2.imshow('window', printscreen_numpy)                                     # 3 for jpg (RGB)
    cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# testing time:
# Loop toop 0.880932092666626 seconds
# Loop toop 0.8467299938201904 seconds
# Loop toop 0.8412389755249023 seconds
# Loop toop 0.8724269866943359 seconds
