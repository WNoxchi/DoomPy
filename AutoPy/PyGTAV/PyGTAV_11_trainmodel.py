# PyGTAV: https://www.youtube.com/watch?v=wIxUp-37jVY&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a&index=10
# WNixalo - 2017-Nov-05 18:23
# 11: Training CNN for Self-Driving
################################################################################
# utility imports
import sys; import os
sys.path.insert(1, os.path.join(os.getcwd()+'/1-7_code/'))
sys.path.insert(1, os.path.join(os.getcwd()+'/8-13_code/'))

import numpy as np
from alexnet import alexnet

WIDTH = 102
HEIGHTS = 64
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'pygtav-car-{}-{}-{}-epochs.model'.format(LR, 'alexnet', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

train_data = np.load('training_data_v2.npy')

train = train_data[:-500]
test  = train_data[-500:]

# image data: i[0]: image; i[1]: action
train_features = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
train_labels   = [i[1] for i in train]

test_features = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
test_labels   = [i[1] for i in test]

model.fit({'input': train_features}, {'targets:' train_labels}, n_epochs=EPOCHS,
            validation_set=({'input': test_features}, {'targets:' test_labels}),
            snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

# tesnorboard --logdir=foo:C:\Users\Wayne\DoomPy\AutoPy\PyGTAV\log

model.save(MODEL_NAME)
