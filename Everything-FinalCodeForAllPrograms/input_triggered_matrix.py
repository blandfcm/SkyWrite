#!/usr/bin/python
from locationservices0 import *
from wordcontroller import *
#from matrix_printer import *
import numpy
import sys, time
from rgbmatrix import Adafruit_RGBmatrix


# Max length of input = 6 char
class input_triggered_matrix:

    def __init__(self):
        # Initialize LED Matrix
        self.matrix = Adafruit_RGBmatrix(32, 1)

    def main(self, arg1, arg2):
        #   INPUT
        word = arg1
        score = arg2
        #   end INPUT
    
        # Initialize canvas
        canvas_pix = numpy.zeros((32, 32))
    
        # Word input -> canvas
        canvas_pix = overlayAt(1, 4, stringtopix(word), canvas_pix, 1)
    
        # Scoreboard -> canvas
        canvas_pix = overlayAt(1, 16, stringtopix("Score:"), canvas_pix, 1)
    
        # Score input -> canvas
        canvas_pix = overlayAt(1, 24, stringtopix(str(score)), canvas_pix, 1)
    
    #    print_to_matrix_default(canvas_pix)
        for x in range(0,32):
            for y in range(0,32):
                if canvas_pix[x][y] == 1:
                    self.matrix.SetPixel(x,y,255,0,0)
#        time.sleep(1.0)
#        matrix.Clear()

    def clear_matrix(self):
        self.matrix.Clear()
    
    def clear_word(self,score):
        # Initialize canvas
        canvas_pix = numpy.zeros((32, 32))
 
        # Word input -> canvas
        #canvas_pix = overlayAt(1, 4, stringtopix(word), canvas_pix, 1)

        # Scoreboard -> canvas
        canvas_pix = overlayAt(1, 16, stringtopix("Score:"), canvas_pix, 1)

        # Score input -> canvas
        canvas_pix = overlayAt(1, 24, stringtopix(str(score)), canvas_pix, 1)

    #    print_to_matrix_default(canvas_pix)
        for x in range(0,32):
            for y in range(0,32):
                if canvas_pix[x][y] == 1:
                    self.matrix.SetPixel(x,y,255,0,0)


    if __name__ == "__main__":
        main(sys.argv[1], sys.argv[2])
