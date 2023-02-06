import numpy as np
import cv2 as cv
import math, random

from matplotlib import pyplot as plt

def dft(x):

    ans = {}
    real_ans = []
    img_ans = []
    phase = []
    freq = []
    radius = []
    N = len(x)

    for k in range(N):
        a = 0
        b = 0
        for n in range(N):
            a += x[n]*math.cos(2*math.pi*k*n/N)
            b -= x[n]*math.sin(2*math.pi*k*n/N)

        real_ans.append(a)
        img_ans.append(b)
        radius.append(math.sqrt((a/N)**2 + (b/N)**2))
        phase.append(math.atan2(b, a))
        freq.append(k)

    ans = {"real" : real_ans, "img": img_ans, "radius": radius, "phase": phase, "freq": freq}

    return ans


def randomPoints(x, y):

    return [dft(x), dft(y)]

def extractor(filename='makima.jfif', step=1):
    im = cv.imread(filename)
    imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow("thresholded image", thresh)

    #contour_img = cv.drawContours(im, contours, 0, (0, 255, 0), 3)

    # print(contours[0])

    cxs = []
    cys = []
    vals = []

    for ind in range(0,len(contours[0]),step):
        cxs.append(contours[0][ind][0][0])
        cys.append(-contours[0][ind][0][1])
        vals.append(cxs[-1] + 1j * cys[-1])

    return randomPoints(cxs, cys)
#
# extractor()