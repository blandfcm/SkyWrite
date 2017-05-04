#!/usr/bin/python

# Simple RGBMatrix example, using only Clear(), Fill() and SetPixel().
# These functions have an immediate effect on the display; no special
# refresh operation needed.
# Requires rgbmatrix.so present in the same directory.

import numpy, pprint, sys, Queue
from assets import loadLetters
from charFlipper import flip
from wordcontroller import chartopix
from locationservices import displayAt
import string
import time
from rgbmatrix import Adafruit_RGBmatrix
from shapes import *

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)
time.sleep(2.0)
matrix.Clear()
#shapes- rect test	
square_fill = rect(5,7,0)
square_empt = rect(5,7,1)
#for row in square_empt:
#    for val in row:
#        print '{:4}'.format(val)
#    print
test_screen0 = displayAt(0,0,square_fill)
test_screen1 = displayAt(0,7,square_empt)

for i in range(0, 32):
    for j in range(0, 32):
        if test_screen0[i][j] == 1:
            matrix.SetPixel(i,j,255,0,0)
        elif test_screen1[i][j] == 1:
            matrix.SetPixel(i,j,0,0,255)
        else:
            matrix.SetPixel(i,j,0,0,0)

time.sleep(5.0)
matrix.Clear()

