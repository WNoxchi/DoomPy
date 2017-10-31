# 2017-Oct-19 17:26
# https://www.youtube.com/watch?v=_gfNpJmWIug&index=5&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import cv2; import numpy as np
img_dir = 'images/'

# these two images same size
img1 = cv2.imread(img_dir + '3D-Matplotlib.png')
img2 = cv2.imread(img_dir + 'mainsvmimage.png')

# this image smaller
img3 = cv2.imread(img_dir + 'hiigaran_seal.jpg')

# add = img1 + img2

# built-in cv2 add operation
# add = cv2.add(img1, img2) # adds all pixel values together

# weighted add -- (img1, w1, img2, w2, gamma); w1 + w2 = 1
# add = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
#
# cv2.imshow('add', add)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Imposing img3 atop img1 and remove the white from img3

# start by thresholding img3:
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols] # region of img1 to cover w/ img3

# create mask of img3 & convert
img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY) # grayscale vsn of img3
# apply threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
    # NOTE: mask will be the threshold.
    #       ( target_img, threshold value, max value, threshold type)
    #       inv binary threshold is 0/1: if above 220: -> 0, if below: --> 255

# cv2.imshow('', mask)

# invisible part
mask_inv = cv2.bitwise_not(mask) # parts where no mask (black areas)
img1_bg  = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg  = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img3_fg', img3_fg)
cv2.imshow('dst', dst)

# NOTE: xxx_bitwise -- similar to python bitwise logical operations


cv2.waitKey(0)
cv2.destroyAllWindows()







#
