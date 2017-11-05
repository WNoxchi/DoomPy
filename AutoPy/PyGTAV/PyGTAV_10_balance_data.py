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

print(len(train_data))

df = pd.DataFrame(train_data)
print(df.head())
# apply string to column 1, apply counter to string -- visualize data
print(Counter(df[1].apply(str)))


# shuffling data to remove bias for specific actions
lefts = []
rights = []
forwards = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    # populate action arrays w/ appropriate data examples
    if choice == [1,0,0]:
        lefts.append([img, choice])
    elif choice == [0,1,0]:
        forwards.append([img, choice])
    elif choice == [0,0,1]:
        rights.append([img, choice])
    else:
        print("NO MATCH")

# ensure action arrays of same len
forwards = forwards[:len(lefts)][:len(rights)]  # will slice forwards up to len of shortest array
lefts    = lefts[:len(forwards)]#[:len(rights)]
rights   = rights[:len(forwards)]#[:len(lefts)]

final_data = forwards + lefts + rights

shuffle(final_data)
print(len(final_data))
np.save(data_dir+'training_data_v2.npy', final_data)




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

# After the data-array balancing operation:
# (DoomPy) C:\Users\Wayne\DoomPy\AutoPy\PyGTAV>python PyGTAV_10_balance_data.py
# 4500
#                                                    0          1
# 0  [[23, 24, 6, 6, 12, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# 1  [[23, 24, 6, 6, 13, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# 2  [[23, 24, 6, 6, 13, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# 3  [[23, 24, 6, 6, 13, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# 4  [[23, 24, 6, 6, 13, 15, 16, 14, 4, 6, 6, 7, 7,...  [0, 1, 0]
# Counter({'[0, 1, 0]': 3574, '[0, 0, 1]': 625, '[1, 0, 0]': 301})
# 912
#
# (DoomPy) C:\Users\Wayne\DoomPy\AutoPy\PyGTAV>
# 
# more or less evenly distributed .... I think..
