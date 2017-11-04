# Python Plays GTAV Tutorial:
# https://www.youtube.com/watch?v=CAr7UupSUh0&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a&index=6
# https://github.com/Sentdex/pygta5
# ---------------------------------
# WNixalo - 2017-Nov-03 15:05
# 06: Lane Finding
# NOTE: using EuroTruck Simulator 2 & DOOM 2016
################################################################################
import numpy as np
from PIL import ImageGrab
import cv2
import time
# import pyautogui
from numpy import ones, vstack
from numpy.linalg import lstsq
from statistics import mean


# Platform-specific window & roi:
from sys import platform
if platform[:3] == 'win':   # could also wrap this in a try except AttributeError
    from directkeys import ReleaseKey, PressKey, W, A, S, D

if platform[:3] == 'win':
    # ETS2 Win gfx: 1280x768
    res = [1280,768]    # game resolution
    offst = [8,30]      # window border offsets x: 8, y: 30
    # region of interest drawn over screenshot in paint
    vertices = np.array([[0,767],[0,444],[319,326],[962,326],[1279,444],[1279,767]])
    for i in range(len(vertices)):
        vertices[i][0] += offst[0]
        vertices[i][1] += offst[1]
else:
    # YouTube box on Retina MacOS
    res = [1600,900]
    # proportions = [1600/1280,900/768]
    offst = [0, 280]
    # region of interest
    # vertices = np.array([[   0,  878],[   0,  508],[ 398,  373],[1202,  373],[1598,  508],[1598,  878]])
    # (debug) full window
    vertices = np.array([[0,res[1]],[0,0],[res[0],0],[res[0],res[1]]])

bbox = (0+offst[0], 0+offst[1], res[0]+offst[0], res[1]+offst[1])


def roi(img, vertices):
    # blank mask
    mask = np.zeros_like(img)

    # filling pixls inside polygon defd by 'vertices' w/ the fill color
    cv2.fillPoly(mask, vertices, 255)

    # returning the image only where mask pixls are nonzero
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lanes(img, lines, color=[0, 255, 255], thickness=3):
    # if this failes, go w/ some default line
    try:
        # finds maximum y value for a lane marker
        # (since we cant assume the horizon wiill always be at the same pt)
        ys = []
        for i in lines:
            for ii in i:
                ys += [ii[1],ii[3]]
        min_y = min(ys) # highest point
        max_y = max(ys) # lowest point
        # new_lines = []
        line_dict = {}

        for idx, i in enumerate(lines):
            # print('for idx, i in enumerate(lines): .. ', idx, i)
            for xyxy in i:
                # These 4 lines:
                # modified from http://stackoverflow.com/questions/21565994/method-to-return-the-equation-of-a-straight-line-given-two-points
                # Used to calculate the defn of a line, given 2 sets of coords.
                x_coords = (xyxy[0], xyxy[2])
                y_coords = (xyxy[1], xyxy[3])
                A = vstack([x_coords, ones(len(x_coords))]).T
                m, b = lstsq(A, y_coords)[0]

                # m = 0.1 if m == 0 else m

                # Calculating our new and improved xs
                # NOTE: getting div zero errors; little patch:
                # m = 0.01 if m == 0 else m
                x1 = (min_y-b)/m
                x2 = (max_y-b)/m

                line_dict[idx] = [m,b,[int(x1),min_y, int(x2),max_y]]
                # new_lines.append([int(x1), min_y, int(x2), max_y])
                # print('line_dict: ', line_dict)

        final_lanes = {}

        for idx in line_dict:
            # print('line_dict index: ', idx)
            final_lanes_copy = final_lanes.copy()
            m = line_dict[idx][0]
            b = line_dict[idx][1]
            line = line_dict[idx][2]

            if len(final_lanes) == 0:
                final_lanes[m] = [ [m,b,line] ]

            else:
                found_copy = False

                for other_ms in final_lanes_copy:

                    if not found_copy:
                        if abs(other_ms*1.1) > abs(m) > abs(other_ms*0.9):
                            if abs(final_lanes_copy[other_ms][0][1]*1.1) > abs(b) > abs(final_lanes_copy[other_ms][0][1]*0.9):
                                final_lanes[other_ms].append([m,b,line])
                                found_copy = True
                                break
                        else:
                            final_lanes[m] = [ [m,b,line] ]

        line_counter = {}

        # print('final_lanes:', final_lanes)

        for lanes in final_lanes:
            line_counter[lanes] = len(final_lanes[lanes])

        # print('line_counter: ', line_counter)

        top_lanes = sorted(line_counter.items(), key=lambda item: item[1])[::-1][:2]

        # print('top_lanes: ', top_lanes)

        lane1_id = top_lanes[0][0]
        lane2_id = top_lanes[1][0]
        # print('lane1_id: ', lane1_id)
        # print('lane2_id: ', lane2_id)


        def average_lane(lane_data):
            # print('lane_data:', lane_data)
            x1s = []
            y1s = []
            x2s = []
            y2s = []
            for data in lane_data:
                # print('data:', data)
                x1s.append(data[2][0])
                y1s.append(data[2][1])
                x2s.append(data[2][2])
                y2s.append(data[2][3])
            # print(x1s, x2s, y1s, y2s)
            # print('SUCCESS')
            return int(mean(x1s)), int(mean(y1s)), int(mean(x2s)), int(mean(y2s))

        # print('lane1_id', lane1_id)
        # print('lane2_id', lane2_id)

        # print('final_lanes: ', final_lanes)

        # print('final_lanes[lane1_id]: ', final_lanes[lane1_id])
        # print('final_lanes[lane2_id]: ', final_lanes[lane2_id])

        # print('average_lane(final_lanes[lane1_id]): ', average_lane(final_lanes[lane1_id]))
        # print('average_lane(final_lanes[lane2_id]): ', average_lane(final_lanes[lane2_id]))

        l1_x1, l1_y1, l1_x2, l1_y2 = average_lane(final_lanes[lane1_id])
        l2_x1, l2_y1, l2_x2, l2_y2 = average_lane(final_lanes[lane2_id])

        # print('1, 2:', [l1_x1, l1_y1, l1_x2, l1_y2], [l2_x1, l2_y1, l2_x2, l2_y2])

        return [l1_x1, l1_y1, l1_x2, l1_y2], [l2_x1, l2_y1, l2_x2, l2_y2]
    except Exception as e:
        print(str(e), 'in draw_lines: Line 59-168')

def process_img(image, vertices=vertices):
    original_image = image
    # convert to gray
    # processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## No Need to cvt to Gray: Canny convrts
    # edge detection
    processed_img = cv2.Canny(image, threshold1=200, threshold2=300)

    processed_img = cv2.GaussianBlur(processed_img,(5,5),0)

    vertices = vertices

    processed_img = roi(processed_img, [vertices])

    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                                     rho   theta   thresh  min length, max gap:
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 20, 15)
    # print('lines = cv2.HoughLinesP(..) = ', lines)
    # print('num lines (HoughLP): ', len(lines))
    try:
        l1, l2 = draw_lanes(original_image, lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0,255,0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 30)
    except Exception as e:
        print(str(e), 'in process_img: Line 186-191')
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255,0,0], 3)

            except Exception as e:
                print(str(e), 'in process_img: Line 196-200')
    except Exception as e:
        print(str(e), 'in process_img: Line 186-202')
        pass

    return processed_img, original_image

last_time = time.time()
while True:
# for i in range(3):
    screen = np.array(ImageGrab.grab(bbox=bbox))
    ttime = time.time() - last_time
    print("Frame took {} seconds. FPS: {}".format(ttime, 1./ttime))
    last_time = time.time()
    new_screen, original_image = process_img(screen)

    if platform[:3] == 'dar':
        original_image = cv2.resize(screen, None, fx=0.3, fy=0.3)
        new_screen = cv2.resize(new_screen, None, fx=0.3, fy=0.3)

    cv2.imshow('window', new_screen)
    # cv2.imshow('window2', original_image)
    cv2.imshow('window2', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    # cv2.imshow('window2', cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
# cv2.destroyAllWindows()
