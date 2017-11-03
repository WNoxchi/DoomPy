# Python Plays GTAV Tutorial:
# https://www.youtube.com/watch?v=lhMXDqQHf9g&index=5&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a
# https://github.com/Sentdex/pygta5
# ---------------------------------
# WNixalo - 2017-Nov-01 15:45
# 05: Line Finding w/ Hough Lines
# NOTE: using EuroTruck Simulator 2 & DOOM 2016
################################################################################
# Specifies a Region of Interest for Lane-Line Detection
import numpy as np
from PIL import ImageGrab
import cv2
import time
# import pyautogui # <-- solves oversized window issues on some monitors ## didn't notice effect
from sys import platform

# Platform-specific window & roi:
if platform[:3] == 'win':   # could also wrap this in a try except AttributeError
    from directkeys import ReleaseKey, PressKey, W, A, S, D

if platform[:3] == 'win':
    # ETS2 Win gfx: 1280x768
    res = [1280,768]    # game resolution
    offst = [8,30]      # window border offsets x: 8, y: 30
    # region of interest drawn over screenshot in paint
    vertices = np.array([[0,767],[0,444],[319,326],[962,326],[1279,444],[1279,767]])
    for i in range(len(vertices)):
        vertices[i][0] += offst[0]
        vertices[i][1] += offst[1]
else:
    # YouTube box on Retina MacOS
    res = [1600,900]
    # proportions = [1600/1280,900/768]
    offst = [0, 280]
    # region of interest
    # vertices = np.array([[   0,  878],[   0,  508],[ 398,  373],[1202,  373],[1598,  508],[1598,  878]])
    # (debug) full window
    vertices = np.array([[0,res[1]],[0,0],[res[0],0],[res[0],res[1]]])

bbox = (0+offst[0], 0+offst[1], res[0]+offst[0], res[1]+offst[1])
# thresh = [110, 160] # orig: 140,200
thresh = [200,300]


def draw_lines(img, lines):
    '''lines are drawn on the original image. No return necessary'''
    try:
        for line in lines:
            coords = line[0] # format is [[[coords]]] --> line = [[coords]] --> line[0] = [coords]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]),
                                                            [255, 255, 0], 3) # (img, (x1,y1),(x2,y2),color,line_width
    except TypeError:
        pass

def roi(img, vertices):
    '''region of interest function'''
    mask = np.zeros_like(img) # Return an array of zeros with the same shape and type as a given array.
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(image):
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=thresh[0], threshold2=thresh[1])
    processed_img = roi(processed_img, [vertices])

    # adding a Gaussian blur to aid edge detection
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)

    # processed_img is the edges; (edges, rho, theta, threshold, minLineLen, maxLineGap)
    # returns: array of arrays that contain the lines
    # NOTE: 3rd from last arg `np.array([])` needed for the linelen & gaplen
    #       pars to be used
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 100, 5)
    draw_lines(processed_img, lines)
    return processed_img

def main():
    last_time = time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox=bbox))
        new_screen = process_img(screen)
        print("Loop took {} seconds. FPS: {}".format(time.time() - last_time, np.round(1./(time.time()-last_time), 3)))
        last_time = time.time()
        # for display on MacOS -- window is doubled, so halve size
        new_screen = cv2.resize(new_screen, None, fx=0.5, fy=0.5)
        cv2.imshow('AUTOPY', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
