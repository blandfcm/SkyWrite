#!/usr/bin/python
import numpy

def print_to_matrix_default(thing):
    dRow = len(thing)
    dCol = len(thing[0])
    for y in range(0, dCol):
        for x in range(0, dRow):
            print(int(thing[x][y])),
        print('\n')

# display_thing is a display_object
def print_to_matrix_color(display_thing):
    for y in range(len(display_thing.pix)):
        for x in range(len(display_thing.pix[0])):
            print(int(display_thing.color_flat*display_thing.pix[x][y]))
        print('\n')
