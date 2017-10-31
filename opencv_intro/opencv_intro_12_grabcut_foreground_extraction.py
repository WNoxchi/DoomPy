# 2017-Oct-25 20:43
# https://www.youtube.com/watch?v=qxfP13BMhq0&index=12&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import cv2; import numpy as np; import matplotlib.pyplot as plt

path = 'images/'; fname = 'foreground-extract_00.jpg'
img = cv2.imread(path + fname)
mask = np.zeros(img.shape[:2], np.uint8)

# background & foreground models
bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

# the rectangle that encases this image's foreground (x1, y1, x2, y2)
rect = (500, 11, 640, 720)
# %10(x1y1) --> %90(x2y2) may work okay-ish

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img) # shows image
plt.colorbar()  # shows colorbar
plt.show()
