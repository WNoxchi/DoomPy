# 2017-Oct-18 17:19 - WNixalo
# Drawing and Writing on Image - OpenCV with Python for Image and Video Analysis 3
# https://www.youtube.com/watch?v=U6uIrq2eh_o&index=3&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import numpy as np
import cv2

from os import getcwd
img_path = getcwd() + '/../../Pictures/'
filename = 'Hiigaran_Hull_Paint.jpg'

img = cv2.imread(img_path + filename, cv2.IMREAD_COLOR)

# drawing a line (target, start, end, color_BGR [, linewidth])
cv2.line(img, (300,300), (1000,1000), (0, 0, 255), 5)

# draw rectange (target, topleft, botright, color_BGR, width)
cv2.rectangle(img, (300,150), (1500,1000), (0, 255, 0), 3)

# draw circle (target, center, radius, color, width) -- width=-1 fills circle
cv2.circle(img, (970,520), 50, (255, 0, 0), 2) # circle Ion Cannon
cv2.circle(img, (1120,425), 50, (255, 0, 0), 2) # circle Cmd Bridge

# draw polygon: list of points; optional: close after connecting
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2)) # OpenCV docs recmnd reshape to 1x2 array)
cv2.polylines(img, [pts], True, (0, 255, 255), 2) # (targ, [pts], connect, color, width)

# writing   puText(targ, text, startpos, font, size, color, thickness [, anti-aliasing])
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hiigaran Battlecruiser', (20, 100), font, 0.9, (200, 255, 255), 1, cv2.LINE_AA)

# display image
cv2.imshow('Battle Cruiser', img)
# wait for any key to be pressed
cv2.waitKey(0)
# close all windows
cv2.destroyAllWindows()
