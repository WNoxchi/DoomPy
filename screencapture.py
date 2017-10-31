# Saves screen caps for [time] seconds.
# For demonic-data collection in DoomPy Demonic Detector.
# 2017-Oct-31 01:58-03:10-04:59 Wayne Nixalo

from time import time, sleep
from sys import exit, stdout
from os import getcwd; from os.path import expanduser
from os import mkdir; from os.path import exists
from PIL.ImageGrab import grab # NOTE: only Win & OSX at this time
from glob import glob

dpath = 'demdata/'
TIME = None
INTERVAL = 0.5  # seems my code cant save faster than every 3.3 seconds yet..
# FORMAT = 'png' # unsure .png or .jpg yet
FORMAT = 'jpg'
if not exists(dpath): mkdir(dpath)

# get time to record from user
while type(TIME) != type(int()):
    try:
        TIME = int(input('Enter time (seconds) to screen capture: '))
    except ValueError:
        continue
    # if enter a big time, check if sure
    if type(TIME) == type(int()) and TIME > 60:
        check = '0'
        while check != 'y' or check != 'n':
            check = input('Time greater than one minute. Are you sure? [y/n]: ').lower()[0]
            if check == 'n':
                TIME = None
                break
            else:
                break
    # if time == zero or null, quit
    if TIME == None: exit('No time entered: Quitting')
    if TIME <= 0: exit('Time ≤ Zero. Quitting')

# begin capturing screen
print("Beginning Screen Capture\n{:<15}{}\n{:<15}{:<5}seconds\n{:<15}{:<5}seconds".format(
        'DIRECTORY:', dpath, 'INTERVAL:', INTERVAL, 'TIME:', TIME))

# another way to do the screen cap loop:
t_start = time()
t_stop = t_start
# start index at last numbered image in data folder
n_img = int(max(glob(dpath+'*')[:-8:-4])[-8:-4]) if glob(dpath+'*') else 0
n_init = n_img
# while t_stop - t_start < TIME:
#     # update progress message
#     n_img += 1
#     stdout.write("\r")
#     stdout.write("Capturing Image: {:<5}".format(n_img)); stdout.flush()
#     # capture screenshot
#     if FORMAT == 'jpg':
#         grab().convert("RGB").save(dpath+'img_{:0=4d}.jpg'.format(n_img))
#     else:
#         grab().save(dpath+'img_{:0=4d}.png'.format(n_img))
#     # enforce a maximum save rate
#     if time() - t_stop < INTERVAL: sleep(INTERVAL)
#     t_stop = time()

print("Screen Capture Complete. {} files saved to: {}".format(n_img-n_init,
        expanduser(getcwd())+'/'+dpath))

# ORIGINAL SAVE LOOP ###########################################################
# # loop {time/interval} time steps
# trange = int(TIME / INTERVAL)
# for tstep in range(trange):
#     # update progress message                                                   # "\r" returns cursur to beginning of line.
#     stdout.write("\r")                                                          # output isn't written until newline "\n"
#     stdout.write("Capturing Image: {} / {:<5}".format(tstep+1, trange))         # so need manually .flush() output stream
#     stdout.flush()                                                              # {:>5} right-padding to ensure overwrite line
#     # capture screenshot
#     if FORMAT == 'jpg':
#         grab().convert("RGB").save(dpath+'img_{:0=4d}.jpg'.format(tstep))
#     else:
#         grab().save(dpath+'img_{:04d}.png'.format(tstep))
#     # pause for {INTERVAL} seconds
#     sleep(INTERVAL)
#
######## DEV NOTES #############################################################
# The if/else image save section takes about 3 seconds. Testing saving in
# isolation, saving a .png file takes longer than converting (removing the
# alpha channel for RGBA->RGB) to .jpg and saving, by what feels like a second.
#
# The save loop w/o the actual saving takes about 50-100μs. I'll need to find
# a faster way to save screens. I want to use Python-MSS, but I'm not able to
# save screens without it doubling the image dimensions with black padding on
# every call after first at this time. I don't know if that's a bug or me not
# knowing how to use it - though the documentation isn't very illuminating.
#
# relevent test output:
# 1509439816.129442
# Capturing Image: 1    5.412101745605469e-05
# img: 1
# 1509439817.134116
# Capturing Image: 2    0.00014901161193847656
# img: 2
# 1509439818.139162
# Capturing Image: 3    0.00011801719665527344
#
# Earlier output:
# Capturing Image: 1 / 4    3.4304521083831787
# Capturing Image: 2 / 4    3.323068141937256
# Capturing Image: 3 / 4    3.364055871963501
# Capturing Image: 4 / 4    3.3840599060058594
#
# ^ This increases with {INTERVAL}, hence the change to a conditional max rate.
