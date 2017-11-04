# Python Plays GTAV Tutorial:
# https://www.youtube.com/watch?v=CLFp9D9-0Eo&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a&index=7
# https://github.com/Sentdex/pygta5
# ---------------------------------
# WNixalo - 2017-Nov-04 12:33
# 07: Self Driving Car
# NOTE: using EuroTruck Simulator 2 & DOOM 2016
################################################################################
import numpy as np
from PIL import ImageGrab
import cv2
import time
from numpy import ones, vstack
from numpy.linalg import lstsq
from statistics import mean
from sys import platform
# import pyautogui

# OS check:
if platform[:3] == 'win':
    from directkeys import ReleaseKey, PressKey, W, A, S, D
    res = [1024,638]
    offst = [8,96]
    vertices = np.array([[0,637],[0,369],[255,271],[770,271],[1023,369],[1023,637]])
    # vertices = np.array([[0,res[1]],[0,0],[res[0],0],[res[0],res[1]]])
    for i in range(len(vertices)):
        vertices[i][0] += offst[0]
        vertices[i][1] += offst[1]
else:
    res = [1600,900]
    offst = [0, 280]
    # vertices = np.array([[   0,  878],[   0,  508],[ 398,  373],[1202,  373],[1598,  508],[1598,  878]])
    vertices = np.array([[0,res[1]],[0,0],[res[0],0],[res[0],res[1]]])

bbox = (0+offst[0], 0+offst[1], res[0]+offst[0], res[1]+offst[1])
thresh = [200,300,180] # threshold: [Canny1, Canny2, Hough]

def roi(img, vertices):
    # blank mask
    mask = np.zeros_like(img)
    # filling pixls inside polgon defd by 'vertices' w/ fill color
    cv2.fillPoly(mask, vertices, 255)
    # returning image only where mask pixls are nonzero
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lanes(img, lines, color=[0,255,255], thickness=3):
    # tolerance for grouping lines
    TOL = 0.4
    # if this fails go w/ some default line
    try:
        # finds max y val for lane marker (cant assume horzn always at same pt)
        ys = []
        for i in lines:
            for ii in i:
                ys += [ii[1], ii[3]]
        min_y = min(ys)
        max_y = res[1] + offst[1]
        line_dict = {}

        for idx, i in enumerate(lines):
            for xyxy in i:
                # Thse 4 lines used to calc defn of line, given 2 sets of coords
                # modified frm: http://stackoverflow.com/questions/21565994/method-to-return-the-equation-of-a-straight-line-given-two-points
                x_coords = (xyxy[0], xyxy[2])
                y_coords = (xyxy[1], xyxy[3])
                A = vstack([x_coords, ones(len(x_coords))]).T
                m, b = lstsq(A, y_coords)[0]

                m = 0.001 if m == 0 else m  # dealing w/ zero-slope errors

                # Calculating new xs
                x1 = (min_y - b) / m
                x2 = (max_y - b) / m

                # store slope, bias, x & y foreaach line to dict
                line_dict[idx] = [m, b, [int(x1), min_y, int(x2), max_y]]

        final_lanes = {}

        # group lines w/ similar slope together. 2 most common slopes are lanes
        for idx in line_dict:
            final_lanes_copy = final_lanes.copy()
            m = line_dict[idx][0]
            b = line_dict[idx][1]
            line = line_dict[idx][2]

            if len(final_lanes) == 0:
                final_lanes[m] = [ [m, b, line] ]

            else:
                found_copy = False

                for other_ms in final_lanes_copy:
                    if not found_copy:
                        if abs(other_ms * (1+TOL)) > abs(m) > abs(other_ms * (1-TOL)):
                            if abs(final_lanes_copy[other_ms][0][1]*(1+TOL)) > abs(b) > abs(final_lanes_copy[other_ms][0][1]*(1-TOL)):
                                final_lanes[other_ms].append([m, b, line])
                                found_copy = True
                                break
                        else:
                            final_lanes[m] = [ [m, b, line] ]
        line_counter = {}

        for lanes in final_lanes:
            line_counter[lanes] = len(final_lanes[lanes])

        top_lanes = sorted(line_counter.items(), key=lambda item: item[1])[::-1][:2]

        lane1_id = top_lanes[0][0]
        lane2_id = top_lanes[1][0]

        # aggregate lines into lane 1 and 2
        def average_lane(lane_data):
            x1s = []
            x2s = []
            y1s = []
            y2s = []
            for data in lane_data:
                x1s.append(data[2][0])
                y1s.append(data[2][1])
                x2s.append(data[2][2])
                y2s.append(data[2][3])
            return int(mean(x1s)), int(mean(y1s)), int(mean(x2s)), int(mean(y2s))

        l1_x1, l1_y1, l1_x2, l1_y2 = average_lane(final_lanes[lane1_id])
        l2_x1, l2_y1, l2_x2, l2_y2 = average_lane(final_lanes[lane2_id])
        # return lanes and slopes
        return [l1_x1, l1_y1, l1_x2, l1_y2], [l2_x1, l2_y1, l2_x2, l2_y2], lane1_id, lane2_id

    except Exception as e:
        print(str(e), "in draw_lines: block 51-130")

def process_img(image, vertices=vertices, thresh=thresh):
    original_image = image

    processed_img = cv2.Canny(image, threshold1=thresh[0], threshold2=thresh[1])
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
    # vertices=vertices
    processed_img = roi(processed_img, [vertices])

    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    # (image, rho, theta, thresh, minlen, maxgap)
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, thresh[2], 20, 15)
    m1, m2 = 0, 0   # defaults
    try:
        l1, l2, m1, m2 = draw_lanes(original_image, lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0,255,0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 30)
    except Exception as e:
        # print(str(e), "in process_img: block 143-148")
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255,0,0], 3)
            except Exception as e:
                print(str(e), "in process_img: block 152-155")
    except Exception as e:
        print(str(e), "in process_img: block 149-159")
        pass

    return processed_img, original_image, m1, m2

# preliminary commands
def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    # ReleaseKey(W)
def left():
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)
    # ReleaseKey(A)
def right():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(W)
    # ReleaseKey(D)
def brake():
    PressKey(S)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(W)

# simple countdown
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=bbox))
    λtime = time.time() - last_time
    print("Frame: {} seconds. FPS: {}".format(λtime, 1./λtime))
    last_time = time.time()

    new_screen, original_image, m1, m2 = process_img(screen, vertices, thresh)
    # new_screen, original_image = process_img(screen)

    if platform[:3] == 'dar':
        original_image = cv2.resize(screen, None, fx=0.3, fy=0.3)
        new_screen = cv2.resize(new_screen, None, fx=0.3, fy=0.3)
    else:
        original_image = cv2.resize(screen, None, fx=0.6, fy=0.6)
        new_screen = cv2.resize(new_screen, None, fx=0.6, fy=0.6)

    cv2.imshow('Edges (\'q\' to quit)', new_screen)
    cv2.imshow('Lane Lines (\'q\' to quit)', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

    # super-basic prelim AI
    if platform[:3] == 'win':
        # if both lines on a side (same slope) turn
        if m1 < 0 and m2 < 0:
            print("TURN RIGHT")
            right()
        elif m1 > 0 and m2 > 0:
            print("TURN LEFT")
            left()
        # if slope steep enough, accel; otws brake
        elif abs(m1) > 0.01 and abs(m2) > 0.01:
            print("PRESS GAS")
            straight()
        else:
            # print("PRESS BRAKE")
            # brake()

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
