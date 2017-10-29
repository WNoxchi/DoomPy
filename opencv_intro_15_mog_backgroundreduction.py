# 2017-Oct-25 21:51
# https://www.youtube.com/watch?v=8-3vl71TjDs&index=15&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import cv2; import numpy as np

# building on foreground extraction using MOG background reduction algorithm
# finds changes from prev frame, note as foreground, note non-changes as
# background and remove

# good for surveilance camera footage scanning

path = 'images/'
fname = 'nukevid.mp4'

# can also just use webcame for this
# cap = cv2.VideoCapture(path+fname); camera=False
cap = cv2.VideoCapture(0); camera=True

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    _, frame = cap.read()
    # print(frame.shape)

    if camera: frame=cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))

    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg mask', fgmask)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
