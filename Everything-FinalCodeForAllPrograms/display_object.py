#!/usr/bin/python
import numpy

class display_object:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pix = numpy.zeros((w,h))
        self.length = -1
        self.orientation = 0
        self.fill = -1
        # "Flat" color meaning either red [0]  green [1]  or blue [2]
        self.color_flat = 1
        # 32 x 32 x 3 color matrix
        self.color_rgb = numpy.zeros((32,32,3))
        self.id = -1

    def clear(self):
        self.pix[:][:] = 0

    def reset_info(self):
        self.length = -1
        self.orientation = 0
        self.fill = -1
        self.color = 0
        self.id = -1

    # id = [0] dot  [1] line    [2] square
    def setID(self, id):
        self.id = id

    def setLength(self, length):
        self.length = length

    def setOrientation(self, orientation):
        self.orientation = orientation

    # fill = 0 - not filled
    # fill = 1 - filled
    def setFill(self, fill):
        self.fill = fill

    # color = [0] red   [1] blue    [2] green
    def setColorFlat(self, color_flat):
        self.color_flat = color_flat

    # up    [0]
    # down  [1]
    # right [2]
    # left  [3]
    def move(self,dir):
        if dir == 0:
            self.y -= 1
        elif dir == 1:
            self.y += 1
        elif dir == 2:
            self.x += 1
        elif dir == 3:
            self.x -= 1
        else:
            print("Invalid direction")

#don't really need get methods
    def getCoordinates(self):
        return (self.x, self.y)

    def getDimensions(self):
        return (self.w, self.h)
