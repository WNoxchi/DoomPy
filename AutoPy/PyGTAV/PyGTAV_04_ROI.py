# Python Plays GTAV Tutorial:
# https://www.youtube.com/watch?v=h98js2usaVo&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a&index=4
# https://github.com/Sentdex/pygta5
# ---------------------------------
# WNixalo - 2017-Nov-01 00:04
# 04: Region of Interest
# NOTE: using EuroTruck Simulator 2 & DOOM 2016
################################################################################
# Specifies a Region of Interest for Lane-Line Detection
import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, W, A, S, D

# ETS2 gfx: 1280x768
res = [1280,768]    # game resolution
offst = [8,30]      # window border offsets x: 8, y: 30
# region of interest drawn over screenshot in paint
vertices = np.array([[0,767],[0,444],[319,326],[962,326],[1279,444],[1279,767]])
for i in range(len(vertices)):
    vertices[i][0] += offst[0]
    vertices[i][1] += offst[1]
bbox = (0+offst[0], 0+offst[1], res[0]+offst[0], res[1]+offst[1])
thresh = [140, 200]


def roi(img, vertices):
    mask = np.zeros_like(img) # Return an array of zeros with the same shape and type as a given array.
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(image):
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=thresh[0], threshold2=thresh[1])
    processed_img = roi(processed_img, [vertices])
    return processed_img

def main():
    last_time = time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox=bbox))
        new_screen = process_img(screen)
        print("Loop took {} seconds".format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('AUTOPY', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
