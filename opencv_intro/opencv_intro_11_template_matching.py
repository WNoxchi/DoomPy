# 2017-Oct-24 15:40
# https://www.youtube.com/watch?v=2CZltXv-Gpk&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=11

import cv2; import numpy as np

# finding a perfect or close (80%) match to a thing

fname = 'opencv-template-matching-python-tutorial.jpg'
tname = 'opencv-template-for-matching.jpg'
fpath = 'images/'

img_bgr = cv2.imread(fpath+fname)
img_gray= cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread(fpath+tname, 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.90
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

cv2.imshow('detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
