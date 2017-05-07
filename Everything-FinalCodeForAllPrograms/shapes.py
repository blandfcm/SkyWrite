#!/usr/bin/python
import numpy
from locationservices import *

# works
def rect(w, h, fill):
    # fill: 0 empty, 1 filled
    rect_pix = numpy.zeros((w, h))
    if fill:
        rect_pix[:][:] = 1
    else:
        rect_pix[:][0] = 1
        rect_pix[:][w-1] = 1
        for i in range(0,w-1):
            rect_pix[i][h-1] = 1
            rect_pix[i][0] = 1
    return rect_pix

# works
def square(w, fill):
    # fill: 0 empty, 1 filled
    square_pix = numpy.zeros((w, w))
    if fill:
        square_pix[:][:] = 1
    else:
        square_pix[:][0] = 1
        square_pix[:][w - 1] = 1
        for i in range(0, w - 1):
            square_pix[i][w - 1] = 1
            square_pix[i][0] = 1
    return square_pix

# Works
# Diagonal square (diamond shape)
def square_d(w, fill):
    # fill: 0 empty, 1 filled
    pix_w = w+(w-1)
    square_d_pix = numpy.zeros((pix_w, pix_w))
    if fill:
        square_d_pix[0][(pix_w-1)/2] = 1
        square_d_pix[pix_w-1][(pix_w - 1) / 2] = 1
        for y in range(1,(pix_w+1)/2):
            square_d_pix[y][(pix_w-1)/2-y:(pix_w-1)/2+y + 1] = 1
            square_d_pix[pix_w-1-y][(pix_w - 1) / 2 - y:(pix_w - 1) / 2 + y + 1] = 1
        return square_d_pix
    else:
        mid = (pix_w-1)/2
        print mid
        print pix_w
        square_d_pix = overlayAt(0, 0, line_d(w,0), square_d_pix, 1)
        square_d_pix = overlayAt(0, (pix_w-1)/2, line_d(w, 1), square_d_pix, 1)
        square_d_pix = overlayAt((pix_w - 1) / 2, (pix_w - 1) / 2, line_d(w, 0), square_d_pix, 1)
        square_d_pix = overlayAt((pix_w - 1) / 2, 0, line_d(w, 1), square_d_pix, 1)
        return square_d_pix

# Works
# l - length of each arm of the cross
# T-shaped
def cross(l):
    pix_w = l*2
    print pix_w
    print (pix_w-1)/2
    cross_pix = numpy.zeros((pix_w-1,pix_w-1))
    cross_pix = overlayAt((pix_w-1)/2,0, line_v(pix_w-1), cross_pix, 1)
    cross_pix = overlayAt(0,(pix_w - 1) / 2, line_h(pix_w - 1), cross_pix, 1)
    return cross_pix


# Works
# l - length of each arm of the cross
# X-shaped
def cross_d(l):
    pix_w = l+(l-1)
    cross_pix = numpy.zeros((pix_w, pix_w))
    cross_pix = overlayAt(0, 0, line_d(l, 1), cross_pix, 1)
    cross_pix = overlayAt(0, (pix_w - 1) / 2, line_d(l, 0), cross_pix, 1)
    cross_pix = overlayAt((pix_w - 1) / 2, (pix_w - 1) / 2, line_d(l, 1), cross_pix, 1)
    cross_pix = overlayAt((pix_w - 1) / 2, 0, line_d(l, 0), cross_pix, 1)
    return cross_pix

# horizontal
def line_h(length):
    if length <= 0:
        print("length must be greater than 0")
        return -1
    line_h_pix = numpy.zeros((length,1))
    line_h_pix[:][:] = 1
    return line_h_pix

# vertical
def line_v(length):
    if length <= 0:
        print("length must be greater than 0")
        return -1
    line_v_pix = numpy.zeros((1,length))
    line_v_pix[:][:] = 1
    return line_v_pix

# diagonal      -- don't need, probs can delete
def line_d(x1, x2, y1, y2):
    # check to make sure params are true diagonal
    if abs(x2-x1) != abs(y2-y1):
        print("(x,y) params are not diagonal")
        return -1
    line_d_pix = numpy.zeros((abs(x2-x1)+1,abs(y2-y1)+1))
    # after check --> format x,y so x1 < x2 & y1 < y2
    if x2 < x1:
        x = list(reversed(numpy.arange(0, abs(x2-x1)+1, 1)))
    else:
        x = numpy.arange(0, abs(x2-x1)+1, 1)
    if y2 < y1:
        y = list(reversed(numpy.arange(0, abs(y2-y1)+1, 1)))
    else:
        y = numpy.arange(0, abs(y2-y1)+1, 1)

    # draw line
    #print(len(x))
    #print(x)
    #print(len(y))
    #print(y)
    #print(len(line_d_pix))
    for i in range(0,len(x)):
        line_d_pix[x[i]][y[i]] = 1
#    for r in range(x1,x2):
 #       for c in range(y1,y2):
    return line_d_pix

# diagonal alt
def line_d(length, slope):
    if length <= 0:
        print("length must be greater than 0")
        return 0
    # slope = 1 -> downward
    # slope = 0 -> upward
    line_d_pix = numpy.zeros((length,length))
    if slope:
        for i in range(0,length):
            line_d_pix[i][i] = 1
        return line_d_pix
    else:
        y = list(reversed(numpy.arange(0,length, 1)))
        for i in range(0,length):
            line_d_pix[i][y[i]] = 1
        return line_d_pix

