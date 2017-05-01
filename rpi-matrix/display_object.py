#!/usr/bin/python
import numpy

class display_object:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pix = numpy.zeros((w,h))

    def clear(self):
        self.pix[:][:] = 0

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