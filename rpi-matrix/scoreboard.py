#!/usr/bin/python
import numpy
from locationservices import *
from display_object import *
from wordcontroller import *

class scoreboard:

    #num_ints is the max # of integer places the score will keep track of
    def __init__(self, x, y, num_ints):
        # pretty sure x,y aren't needed
        self.x = x
        self.y = y
        self.w = 30
        self.h = 15
        self.num_ints = num_ints
        self.base_obj = display_object(x,y,30,15)
        self.score_string_obj = display_object(x,y,30,7)
        self.score_string_obj.pix = stringtopix("Score:")
        self.score_int_obj = display_object(x,y+8,30,7)

    def getScoreboard_obj(self, score):
        score_int_pix = stringtopix(str(score))
        self.base_obj.pix = overlayAt(0, 8, score_int_pix, self.base_obj.pix, 1)
#        self.score_int_obj.pix = overlayAt(self.score_int_obj.x,self.score_int_obj.y,score_int_pix,numpy.zeros((self.score_int_obj.w,self.score_int_obj.h)),1)
        self.base_obj.pix = overlayAt(0, 0, self.score_string_obj.pix, self.base_obj.pix, 1)
        return self.base_obj

    def getScoreboard_pix(self,score):
        score_int_pix = stringtopix(str(score))
        self.base_obj.pix = overlayAt(0, 8, score_int_pix, self.base_obj.pix, 1)
#        self.score_int_obj.pix = overlayAt(self.score_int_obj.x,self.score_int_obj.y,score_int_pix,numpy.zeros((self.score_int_obj.w,self.score_int_obj.h)),1)
        self.base_obj.pix = overlayAt(0, 0, self.score_string_obj.pix, self.base_obj.pix, 1)
        return self.base_obj.pix