# 2017-Oct-28 01:23
# https://www.youtube.com/watch?v=eay7CgPlCyo&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=20
# https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

# first make dirs to hold data & info:
# $ mkdir data info

# then run command:
# $ opencv_createsamples -img SU30SM_half.jpeg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 800

# finally this command:
# $ opencv_createsamples -info info/info.lst -num 800 -w 20 -h 20 -vec positives.vec

# ... we want to place the output somewhere, so let's create a new data directory:
#
# mkdir data and your workspace should look like:
#
# opencv_workspace
# --neg
# ----negimages.jpg
# --opencv
# --info
# --data
# --positives.vec --bg.txt
# --watch5050.jpg

# actual training (this will take time)
# $ opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 700 -numNeg 350 -numStages 10 -w 20 -h 20

# this verison of training can be halted & outputs to a file
# $ nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 700 -numNeg 350 -numStages 10 -w 20 -h 20 &

# in UNIX (POSIX?) bash: "nohub program &" runs 'program' and will not interrupt
# it if a logout signal is given. That signal will be sent to file: nohup.out.



# OUTPUT:
# PARAMETERS:
# cascadeDirName: data
# vecFileName: positives.vec
# bgFileName: bg.txt
# numPos: 700
# numNeg: 350
# numStages: 10
# precalcValBufSize[Mb] : 1024
# precalcIdxBufSize[Mb] : 1024
# acceptanceRatioBreakValue : -1
# stageType: BOOST
# featureType: HAAR
# sampleWidth: 20
# sampleHeight: 20
# boostType: GAB
# minHitRate: 0.995
# maxFalseAlarmRate: 0.5
# weightTrimRate: 0.95
# maxDepth: 1
# maxWeakCount: 100
# mode: BASIC
#
# ===== TRAINING 0-stage =====
# <BEGIN
# POS count : consumed   700 : 700
# NEG count : acceptanceRatio    350 : 1
# Precalculation time: 1
# +----+---------+---------+
# |  N |    HR   |    FA   |
# +----+---------+---------+
# |   1|        1|        1|
# +----+---------+---------+
# |   2|        1|        1|
# +----+---------+---------+
# |   3|        1| 0.648571|
# +----+---------+---------+
# |   4|        1| 0.234286|
# +----+---------+---------+
# END>
# Training until now has taken 0 days 0 hours 0 minutes 11 seconds.
#
# ===== TRAINING 1-stage =====
# <BEGIN
# POS count : consumed   700 : 700
# NEG count : acceptanceRatio    350 : 0.247175
# Precalculation time: 1
# +----+---------+---------+
# |  N |    HR   |    FA   |
# +----+---------+---------+
# |   1|        1|        1|
# +----+---------+---------+
# |   2|        1| 0.608571|
# +----+---------+---------+
# |   3|        1| 0.608571|
# +----+---------+---------+
# |   4| 0.998571| 0.328571|
# +----+---------+---------+
# END>
# Training until now has taken 0 days 0 hours 0 minutes 22 seconds.
#
# ===== TRAINING 2-stage =====
# <BEGIN
# POS count : consumed   700 : 701
# NEG count : acceptanceRatio    350 : 0.0915751
# Precalculation time: 1
# +----+---------+---------+
# |  N |    HR   |    FA   |
# +----+---------+---------+
# |   1|        1|        1|
# +----+---------+---------+
# |   2|        1|        1|
# +----+---------+---------+
# |   3| 0.997143| 0.822857|
# +----+---------+---------+
# |   4| 0.997143| 0.548571|
# +----+---------+---------+
# |   5| 0.995714| 0.411429|
# +----+---------+---------+
# END>
# Training until now has taken 0 days 0 hours 0 minutes 34 seconds.
#
# ===== TRAINING 3-stage =====
# <BEGIN
# POS count : consumed   700 : 704
# NEG count : acceptanceRatio    350 : 0.048537
# Precalculation time: 1
# +----+---------+---------+
# |  N |    HR   |    FA   |
# +----+---------+---------+
# |   1|        1|        1|
# +----+---------+---------+
# |   2|        1|        1|
# +----+---------+---------+
# |   3| 0.995714| 0.682857|
# +----+---------+---------+
# |   4| 0.995714| 0.468571|
# +----+---------+---------+
# END>
# Training until now has taken 0 days 0 hours 0 minutes 45 seconds.
#
# ===== TRAINING 4-stage =====
# <BEGIN
# POS count : consumed   700 : 707
# NEG count : acceptanceRatio    350 : 0.0255773
# Precalculation time: 1
# +----+---------+---------+
# |  N |    HR   |    FA   |
# +----+---------+---------+
# |   1|        1|        1|
# +----+---------+---------+
# |   2| 0.998571| 0.691429|
# +----+---------+---------+
# |   3| 0.998571| 0.691429|
# +----+---------+---------+
# |   4| 0.995714| 0.554286|
# +----+---------+---------+
# |   5| 0.995714| 0.554286|
# +----+---------+---------+
# |   6| 0.997143| 0.488571|
# +----+---------+---------+
# END>
# Training until now has taken 0 days 0 hours 0 minutes 59 seconds.
#
# ===== TRAINING 5-stage =====
# <BEGIN
# POS count : consumed   700 : 709
# NEG count : acceptanceRatio    350 : 0.0153725
# Precalculation time: 1
# +----+---------+---------+
# |  N |    HR   |    FA   |
# +----+---------+---------+
# |   1|        1|        1|
# +----+---------+---------+
# |   2|        1|        1|
# +----+---------+---------+
# |   3|        1| 0.911429|
# +----+---------+---------+
# |   4|        1| 0.785714|
# +----+---------+---------+
# |   5| 0.995714| 0.577143|
# +----+---------+---------+
# |   6| 0.997143| 0.457143|
# +----+---------+---------+
# END>
# Training until now has taken 0 days 0 hours 1 minutes 12 seconds.
#
# ===== TRAINING 6-stage =====
# <BEGIN
# POS count : consumed   700 : 711
# NEG count : acceptanceRatio    350 : 0.00732647
# Precalculation time: 1
# +----+---------+---------+
# |  N |    HR   |    FA   |
# +----+---------+---------+
# |   1|        1|        1|
# +----+---------+---------+
# |   2| 0.997143| 0.662857|
# +----+---------+---------+
# |   3| 0.997143| 0.662857|
# +----+---------+---------+
# |   4| 0.995714| 0.471429|
# +----+---------+---------+
# END>
# Training until now has taken 0 days 0 hours 1 minutes 23 seconds.
#
# ===== TRAINING 7-stage =====
# <BEGIN
# POS count : consumed   700 : 715
# NEG count : acceptanceRatio    350 : 0.00431667
# Precalculation time: 1
# +----+---------+---------+
# |  N |    HR   |    FA   |
# +----+---------+---------+
# |   1|        1|        1|
# +----+---------+---------+
# |   2|        1|        1|
# +----+---------+---------+
# |   3| 0.998571| 0.817143|
# +----+---------+---------+
# |   4| 0.998571| 0.725714|
# +----+---------+---------+
# |   5| 0.997143|     0.62|
# +----+---------+---------+
# |   6| 0.995714| 0.645714|
# +----+---------+---------+
# |   7|        1| 0.688571|
# +----+---------+---------+
# |   8| 0.995714| 0.574286|
# +----+---------+---------+
# |   9| 0.995714| 0.411429|
# +----+---------+---------+
# END>
# Training until now has taken 0 days 0 hours 1 minutes 41 seconds.
#
# ===== TRAINING 8-stage =====
# <BEGIN
# POS count : consumed   700 : 718
# NEG count : acceptanceRatio    350 : 0.00207858
# Precalculation time: 1
# +----+---------+---------+
# |  N |    HR   |    FA   |
# +----+---------+---------+
# |   1|        1|        1|
# +----+---------+---------+
# |   2| 0.998571| 0.897143|
# +----+---------+---------+
# |   3| 0.998571| 0.897143|
# +----+---------+---------+
# |   4| 0.995714| 0.777143|
# +----+---------+---------+
# |   5| 0.995714| 0.802857|
# +----+---------+---------+
# |   6| 0.995714| 0.654286|
# +----+---------+---------+
# |   7| 0.995714| 0.571429|
# +----+---------+---------+
# |   8| 0.995714| 0.457143|
# +----+---------+---------+
# END>
# Training until now has taken 0 days 0 hours 1 minutes 57 seconds.
#
# ===== TRAINING 9-stage =====
# <BEGIN
# POS count : consumed   700 : 721
# NEG count : acceptanceRatio    2 : 0.000651042
# Required leaf false alarm rate achieved. Branch training terminated.
