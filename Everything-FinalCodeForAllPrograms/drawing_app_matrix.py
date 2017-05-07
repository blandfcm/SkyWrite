#!/usr/bin/python

from locationservices import *
#from matrix_printer import *
import numpy
import sys, time
from rgbmatrix import Adafruit_RGBmatrix
from random import randint

# Max length of input = 6 char
class drawing_app_matrix:

    def __init__(self):
        # Initialize LED Matrix
        self.matrix = Adafruit_RGBmatrix(32, 1)

    def main(self, arg1, arg2):
        self.matrix.Clear()

        #   INPUT
        pix = arg1
        rainbow = arg2
        #   end INPUT
        
        #print_to_matrix_default(canvas_pix)
        if rainbow:
            for x in range(0,32):
               for y in range(0,32):
                    if pix[x][y] == 1:
                     self.matrix.SetPixel(x,y,randint(0,255), randint(0,255), randint(0,255))
        else:
            for x in range(0,32):
                for y in range(0,32):
                    if pix[x][y] == 1:
                        self.matrix.SetPixel(x,y,255,0,0)


    def clear_matrix(self):
        self.matrix.Clear()

    if __name__ == "__main__":
        main(sys.argv[1], sys.argv[2])
