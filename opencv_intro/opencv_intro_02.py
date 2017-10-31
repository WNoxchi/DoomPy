# Loading Video Source - OpenCV with Python for Image and Video Analysis 2
# https://www.youtube.com/watch?v=Jvf5y21ZqtQ&index=2&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

# Wayne Nixalo
# 2017-Oct-17 22:05

import cv2
import numpy as np

cap = cv2.VideoCapture(0) # uses 0th webcam
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # codec; XVID/avi doesnt work on MacOS
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1280,720)) # ensure same dimensions!

# displays color video
# while(True):
#     ret, frame = cap.read() # ret: True/False, frame: frame
#     cv2.imshow('frame', frame)
#
#     # break loop if press q
#     if cv2.waitKey(1) & 0xFF == ord('q'):    # has to be 1, idk why
#         break

# displays black-white video & color video
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)
    # NOTE: this doesnt work with out.wirte(gray) bc the grayscale conversion
    #       removes the alpha (?) channel. frame.shape = (720, 1280, 3)
    #       gray.shape = (720, 1280)

    cv2.imshow('frame', frame)
    cv2.imshow('noir', gray)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    if (cv2.waitKey(5) & 0xFF) == 27:
        break

# release camera in use from vid-capture
cap.release()
out.release()
cv2.destroyAllWindows()

# NOTE: cv2.waitKey() returns a 32bit int value. Key input is a 8 bit int
#       ASCII char. The '& 0xFF' gets you the tail 8 bits of waitKey()
#       0xFF = 11111111 --> all other bits = 0
