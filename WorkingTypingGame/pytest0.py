#!/usr/bin/python

# Simple RGBMatrix example, using only Clear(), Fill() and SetPixel().
# These functions have an immediate effect on the display; no special
# refresh operation needed.
# Requires rgbmatrix.so present in the same directory.

import numpy, pprint, sys, Queue
#from assets import loadLetters
#from charFlipper import flip
from wordcontroller import chartopix
from locationservices import displayAt
#import string
import time
from rgbmatrix import Adafruit_RGBmatrix
from shapes import rect
#from read_img import img_to_pix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)

#Fill screen red (packed color value)
#matrix.Fill(0xFF0000)
#pause (1 sec - i think)
time.sleep(1.0)

#clear matrix
matrix.Clear()

#SetPixel(x,y,r,g,b)
#matrix.SetPixel(4,4,255,0,0)
#matrix.SetPixel(5,4,0,255,0)
#matrix.SetPixel(6,4,0,255,255)
#time.sleep(1.0)
matrix.Fill(0xFFFFFF)
time.sleep(2)
#matrix.Clear()
matrix.SetPixel(0,0,255,0,0)
matrix.SetPixel(0,10,0,0,0)
matrix.Clear()
time.sleep(0.025)
matrix.SetPixel(0,10,0,255,0)
matrix.SetPixel(10,0,0,0,255)
matrix.SetPixel(20,20,255,255,255)
time.sleep(4)
matrix.Clear()
pixr = numpy.zeros((32,32))
pixr[:][:] = 0
pixg = numpy.zeros((32,32))
pixg[:][:] = 255
pixb = numpy.zeros((32,32))
pixb[:][:] = 255
for x in range(0,32):
    for y in range(0,32):
        matrix.SetPixel(x,y,int(pixr[x][y]/2),int(pixg[x][y]/2),int(pixb[x][y]/2))
time.sleep(3.0)
matrix.Clear()

charW = 5
charH = 7
#zero = [[0 for x in range(charW) for y in range(charH)]
letters = numpy.zeros((26, 5, 7))
#letters_t = numpy.zeros((26, 7, 5))
lines = [line.rstrip('\n') for line in open('upper-letters.txt')]
lcount = 0
for i in range(0, 26):
    for k in range(0, 7):
        for j in range(0, 5):
            #letters_t[i][k][j] = lines[lcount][j]
            letters[i][j][k] = lines[lcount][j]
        lcount = lcount + 1
#line 0 (x:0->6, y:0->31)
#display0 = numpy.zeros((30, 
pix = numpy.zeros((32, 32, 3))
pix_letter = chartopix("B")
time.sleep(2.0)
matrix.Clear()

#locationservices- displayAt test
test_screen = displayAt(10, 10, pix_letter)

for i in range(0, 32):
    for j in range(0, 32):
        if test_screen[i][j] == 1:
            matrix.SetPixel(i,j,255,0,0)
        else:
            matrix.SetPixel(i,j,0,0,0)
	
time.sleep(4.0)
pix_letter = chartopix("")
for j in range(0, 7):
    for i in range(0, 5):
        if pix_letter[i][j] == 1:
            matrix.SetPixel(i,j,255,0,0)

time.sleep(2.0)
matrix.Clear()
