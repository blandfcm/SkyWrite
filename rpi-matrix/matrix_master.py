#!/usr/bin/python
from display_object import *

class matrix_master:

    display_object_list = []

#canvas is a display object for the entire LED matrix ("Canvas")
    def __init__(self, canvas):
        self.display_object_list.append(canvas)

