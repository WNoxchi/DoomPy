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

df = pd.DataFrame(train_data)
print(df.head())
# apply string to column 1, apply counter to string -- visualize data
print(Counter(df[1].apply(str)))

# for data in train_data:
#     img = data[0]
#     choice = data[1]
#     cv2.imshow('test', img)
#     print(choice)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break



# first visualization of data. Roughly 70% is Forward, 20% Right, 10% Left.
# 0  [[23, 24, 6, 6, 12, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# 1  [[23, 24, 6, 6, 13, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# 2  [[23, 24, 6, 6, 13, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# 3  [[23, 24, 6, 6, 13, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# 4  [[23, 24, 6, 6, 13, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# Counter({'[0, 1, 0]': 3574, '[0, 0, 1]': 625, '[1, 0, 0]': 301})
