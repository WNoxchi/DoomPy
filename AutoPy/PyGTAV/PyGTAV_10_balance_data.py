# PyGTAV: https://www.youtube.com/watch?v=wIxUp-37jVY&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a&index=10
# WNixalo - 2017-Nov-04 22:00
# 10: Balancing self-driving training data
################################################################################
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

data_dir   = 'train/'
train_data = np.load(data_dir+'training_data.npy')

for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test', img)
    print(choice)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
