# https://www.youtube.com/watch?v=88HdqNDQsEk&index=16&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq
# 2017-Oct-27 19:11

import cv2; import numpy as np;

# Haar Cascades are large xml files w/ many featuresets each corresponding to
# specific objects
# ffs just use a CNN...

# https://github.com/itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
# https://github.com/itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

haar_eye = 'haarcascade_eye.xml'
haar_frontface = 'haarcascade_frontalface_default.xml'
path = 'images/'

eye_cascade  = cv2.CascadeClassifier(path+haar_eye)
face_cascade = cv2.CascadeClassifier(path+haar_frontface)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (640,360))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) # rectangle: start pt, end pt
        roi_gray = gray[y:y+h, x:x+w] # region of image is row,col
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
