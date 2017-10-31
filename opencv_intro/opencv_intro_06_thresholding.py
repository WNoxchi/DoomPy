# 2017-Oct-19 18:23
# https://www.youtube.com/watch?v=jXzkxsT9gxM&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=6

import cv2; import numpy as np

img_dir = 'images/'

img = cv2.imread(img_dir + 'bookpage.jpg')

# apply threshold to low light image
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

# grascale image
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# apply threshold to grayscaled image
retval, threshold_gray = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

# gaussian adaptive threshold -- adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# otsu threshold
# retval2, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('orig', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold_gray', threshold_gray)
cv2.imshow('gauss', gauss)
# cv2.imshow('otsu', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
