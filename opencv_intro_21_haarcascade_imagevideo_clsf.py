# 2017-Oct-28 02:37
# pt21 (trained cascade):
# https://www.youtube.com/watch?v=-Mhy-5YNcG4&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=21

import cv2; import numpy as np;

# Same code as opencv_intro_16...py but added new trained cascade

# https://github.com/itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
# https://github.com/itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

haar_eye = 'haarcascade_eye.xml'
haar_frontface = 'haarcascade_frontalface_default.xml'
haar_fighterjet = 'su30sm_cascade.xml'
path = 'images/'

eye_cascade  = cv2.CascadeClassifier(path+haar_eye)
face_cascade = cv2.CascadeClassifier(path+haar_frontface)
fjet_cascade = cv2.CascadeClassifier(path+haar_fighterjet)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (640,360))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    fjets = fjet_cascade.detectMultiScale(gray, 2.4, 3)

    for (x,y,w,h) in fjets:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'TARGET LOCK', (x-w, y-h), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

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
