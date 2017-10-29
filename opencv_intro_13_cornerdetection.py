# 2017-Oct-25 21:17
# https://www.youtube.com/watch?v=6e6NbNegChU&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=13

import cv2; import numpy as np

path = 'images/'; fname = 'opencv-corner-detection-sample.jpg'

img = cv2.imread(path+fname)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray) # cvt to float32 to satisfy algo

# (targetimage, howmany, imagequality, mindistancebtwnfeatures)
corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10)
corners = np.int0(corners)

count = 0
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)
    count += 1

print(count)

cv2.imshow('Corners', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
