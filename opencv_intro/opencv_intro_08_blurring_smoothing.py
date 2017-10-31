# 2017-Oct-24 13:28
# https://www.youtube.com/watch?v=sARklx6sgDk&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=8

import cv2; import numpy as np; import os

# camera shape = (720, 1280, 3)
new_resolution = (360, 640)
new_resolution = new_resolution[::-1]

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # heu saturation and value

    # hsv hue sat value
    lower_red = np.array([0, 200, 80])
    upper_red = np.array([50, 255, 255])
                                        # Blue: 100:220;120:255;0:255

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # blurring by averaging pixels
    kernel = np.ones((15, 15), np.float32) / 225 # 15*15=225

    # resizing output
    frame_resized = cv2.resize(frame, new_resolution)
    mask_resized  = cv2.resize(mask, new_resolution)
    res_resized   = cv2.resize(res, new_resolution)

    # applying (averaging) smoothing kernel
    smoothed = cv2.filter2D(res_resized, -1, kernel)

    # smoothing via gaussian blur
    gsblur = cv2.GaussianBlur(res_resized, (15, 15), 0)
    # smoothing via median blur
    median = cv2.medianBlur(res_resized, 15)
    # smoothing via bilateral blur
    bilateral = cv2.bilateralFilter(res_resized, 15, 75, 75)

    # display image
    cv2.imshow('frame', frame_resized)
    # cv2.imshow('mask', mask_resized)
    # cv2.imshow('result', res_resized)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('gsblur', gsblur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(1) & 0xFF # waitKey(5)?
    if (k == 27) or (k == 13):
        break
    # if cv2.waitKey(5) & 0xFF == 27: # 'esc':27; 'return':13
    #     break

cv2.destroyAllWindows()
cap.release()
