# Python Plays GTAV Tutorial:
# https://www.youtube.com/watch?v=v07t_GEIQzI&index=2&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a
# https://github.com/Sentdex/pygta5
# ---------------------------------
# WNixalo - 2017-Oct-31 19:59
# 02: OpenCV Basics
# NOTE: using EuroTruck Simulator 2 for this
################################################################################

# doing a screen grab
import numpy as np
from PIL import ImageGrab
import cv2
import time
from sys import platform # checking OS for resolution

# OS check for propper resolution
if platform[:3] == 'win':
    bbox = (5, 20, 1085, 740)
    thresh1=100
    thresh2=300

else:
    bbox = (0,280,800, 880)
    thresh1=200
    thresh2=300

def process_img(original_image):
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=thresh1, threshold2=thresh2)
    return processed_img

last_time = time.time()
while(True):
    last_time = time.time()
    screen = np.array(ImageGrab.grab(bbox=bbox)) # x1,y1, x2,y2; WNXG750:bbox=(5, 20, 1085, 740)

    new_screen = process_img(screen)
    print('Loop took {} seconds'.format(time.time()-last_time))
    cv2.imshow('window', new_screen)

    # cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break




# import numpy as np
# from PIL import ImageGrab
# import cv2
# import time
#
#
# def process_img(image):
#     original_image = image
#     # convert to gray
#     processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # edge detection
#     processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
#     return processed_img
#
# def main():
#     last_time = time.time()
#     while True:
#         screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
#         #print('Frame took {} seconds'.format(time.time()-last_time))
#         last_time = time.time()
#         new_screen = process_img(screen)
#         cv2.imshow('window', new_screen)
#         #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             break
#
# main()
