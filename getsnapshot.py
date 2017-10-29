# WNx - 2017-Oct-25 21:00
# Saves a screenshot from camera

import cv2; import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('press \'q\' to capture & exit', frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.imwrite('images/foreground-extract.jpg', frame)
        break
cv2.destroyAllWindows()
cap.release()
