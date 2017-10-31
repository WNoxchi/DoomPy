# 2017-Oct-17 21:10
# Wayne Nixalo
#
# Intro and loading Images - OpenCV with Python for Image and Video Analysis 1
# https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import cv2
import numpy as np
import matplotlib.pyplot as plt

from os import getcwd
img_path = getcwd() + '/../../Pictures/'

# imgfile and filter to apply (BGR in cv2)
# reads in as color img, removes alpha channel (deg of opaqueness)
#   NOTE: other options:
#           IMREAD_COLOR
#           IMREAD_UNCHANGED
#         Can also specfy by num: 0:grayscl, 1:color, -1:unchgd
img = cv2.imread(img_path+'Hiigaran_Hull_Paint.jpg', cv2.IMREAD_GRAYSCALE)

# display image
cv2.imshow('image', img)
# wait for a key to be pressed
cv2.waitKey(0)
# close all windows
cv2.destroyAllWindows()


# # OpenCV:BGR, MatplotLib:RGB
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([300,1000],[300,1000], 'c', linewidth=1)
# plt.show()

# saving loaded image to current directory
cv2.imwrite('gray_hbc2.jpg', img)



# NOTE: also works: (2017-Oct-19 17:09)
# img_name = 'Hiigaran_Hull_Paint.jpg'
# img_path = os.path.expanduser('~/Pictures/')
