# 2017-Oct-24 14:31

import cv2; import numpy as np

cap = cv2.VideoCapture(0)
resolution = (720//2,1280//2)
resolution = resolution[::-1]

# print(resolution)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, resolution)

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)

    edges = cv2.Canny(frame, 100, 200)

    cv2.imshow('original', frame)
    # cv2.imshow('laplacian', laplacian)

    # cv2.imshow('sobelx', sobelx)
    # cv2.imshow('sobely', sobely)

    cv2.imshow('canny-edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: break

cv2.destroyAllWindows()
cap.release()
