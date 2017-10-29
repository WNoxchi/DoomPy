# 2017-Oct-25 21:28
# https://www.youtube.com/watch?v=UquTAf_9dVA&index=14&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

# feature matching is a lot more flexible than template matching
# this is a bruteforce matching algorithm

import cv2; import numpy as np; import matplotlib.pyplot as plt

path = 'images/'; ftarg = 'feature-match-target.jpg'
ftest = 'feature-match-test.jpg'

img_targ = cv2.imread(path+ftarg, 0)
img_test = cv2.imread(path+ftest, 0)

# similarity detector
orb = cv2.ORB_create()

# define keypoints & their descriptors
kp1, des1 = orb.detectAndCompute(img_targ, None)
kp2, des2 = orb.detectAndCompute(img_test, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# find & sort matches based on confidence\distance
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img_out = cv2.drawMatches(img_targ, kp1, img_test, kp2, matches[:10], None, flags=2)

plt.imshow(img_out)
plt.show()
