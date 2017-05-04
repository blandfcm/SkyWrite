#!/usr/bin/python
import numpy

def rect(w, h, fill):
    #fill: 0 empty, 1 filled
    square_pix = numpy.zeros((w, h))
    if fill:
        square_pix[:][:] = 1
    else:
        square_pix[:][0] = 1
        square_pix[:][w-1] = 1
        for i in range(0,w-1):
            square_pix[i][h-1] = 1
            square_pix[i][0] = 1
    return square_pix

