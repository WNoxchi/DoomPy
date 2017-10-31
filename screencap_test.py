# screen capture test for DoomPy    -   2017-Oct-31 01:44
# WNixalo

import numpy as np; import cv2;

# General;
# from mss import mss
# Windows:
# from mss.windows import MSS as mss
# Linux
# from mss.linux import MSS as mss
# MacOS X
from mss.darwin import MSS as mss

# Module Instance:
sct = mss()

# screenshot of monitor 0:
i = '02'
filen = sct.shot(output='images/screenshot{}.png'.format(i))
print(filen)
