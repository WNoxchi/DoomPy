# https://www.youtube.com/watch?v=sARklx6sgDk&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=9

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

    # resizing output
    frame_resized = cv2.resize(frame, new_resolution)
    mask_resized  = cv2.resize(mask, new_resolution)
    res_resized   = cv2.resize(res, new_resolution)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask_resized, kernel, iterations=1)
    dilation = cv2.dilate(mask_resized, kernel, iterations=1)

    # opening tries to remove false positives (white pxls in background)
    opening = cv2.morphologyEx(mask_resized, cv2.MORPH_OPEN, kernel)
    # closing tries to remove false negatives (black pxls in watned field)
    closing = cv2.morphologyEx(mask_resized, cv2.MORPH_CLOSE, kernel)

    # difference btwn input image and opening of image
    # ....
    # difference btwn closing of input image and image
    # ....

    # display image
    cv2.imshow('frame', frame_resized)
    cv2.imshow('result', res_resized)
    # cv2.imshow('erosion', erosion)
    # cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(1) & 0xFF # waitKey(5)?
    if (k == 27) or (k == 13):
        break
    # if cv2.waitKey(5) & 0xFF == 27: # 'esc':27; 'return':13
    #     break

cv2.destroyAllWindows()
cap.release()
