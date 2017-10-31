# 2017-Oct-19 16:46
# Image Operations - OpenCV with Python for Image and Video Analysis 4

import numpy as np
import cv2
import os

img_dir = os.path.expanduser('~/Pictures/')
img_name = 'Hiigaran_Hull_Paint.jpg'

# source image
img = cv2.imread(img_dir+img_name, cv2.IMREAD_COLOR)

# reference specfc pixel
# px = img[55,55] # returns color value
# print(px)

# modifying pixel
# img[55,55] = [255,255,255]
# px  = img[55,55]
# print(px)

# ROI - region of image
# roi = img[100:150, 100:150]
# print(roi)

# img[100:150, 100:150] = [255,255,255] # turn region into white square

# copy and paste region of image
img_piece = img[200:300, 200:300]
img[0:100, 0:100] = img_piece # must be same size

cv2.imshow('bc', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
