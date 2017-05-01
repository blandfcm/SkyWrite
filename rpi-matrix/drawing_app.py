#!/usr/bin/python
import numpy
from display_object import *
#import display_object
import shapes
from locationservices import *
from matrix_printer import *

# Base canvas object, all drawing will be done on this
canvas = display_object(0,0,32,32)

# Temp canvas layer while shape is being edited
layer = display_object(0,0,32,32)

# Select Shape char
#   dot     [0]
#   line    [1]
#   square  [2]
shape_options = ""
shape_length = 5

# State machine hoo-ha
state = 0
running = 1     # keeps while loop going
shape_choosen = -1      #default- no shape
shape = display_object(0,0,shape_length,shape_length)

def start():
    #print "Program start...\n"
#       STATE NOT CHANGED IN DEF METHODS
    state = 1

def select_shape():
    #    shape_choosen = -1
    user_input = raw_input("Select shape: dot [d] | line [l] | square [s] ")
    if user_input == 'QUIT':
        state = 9
    elif int(user_input) == 0:
        print("You choose [dot]")
        shape_choosen = int(user_input)
        shape.pix = 1
        state = 3
    elif int(user_input) == 1:
        print("You choose [line]")
        shape_choosen = int(user_input)
        shape.pix = shapes.line_h(shape_length)
        state = 3
    elif int(user_input) == 2:
        print("You choose [square]")
        shape_choosen = int(user_input)
        shape.pix = shapes.rect(shape_length,shape_length,0)
        state = 3
    else:
        print("Shape not found")

def create_shape():
    print "State 2\n"
    # can optimize by moving to select_shape() if/elif
def edit_shape():
    print "State 3\n"
    # Update current edit layer to include newly selected shape
    layer.pix = overlayAt(0,0,shape.pix,canvas.pix,1)
    user_input = raw_input()
    if user_input == 'QUIT':
        state = 9
    elif user_input.lower() == 'w':
        state = 4
    elif user_input.lower() == 's':
        state = 5
    elif user_input.lower() == 'a':
        state = 6
    elif user_input.lower() == 'd':
        state = 7
    elif user_input.lower() == 'r':
        state = 8
    else:
        print("command not found")

def move_up():
    print "State 4\n"
def move_down():
    print "State 5\n"
def move_left():
    print "State 6\n"
def move_right():
    print "State 7\n"
def rotate_shape():
    print "State 8\n"
def place_shape():
    print "State 9\n"
    shape_choosen = -1      # reset back to default
def delete_shape():
    print "State 10\n"
    shape_choosen = -1      # reset back to default
def clear_canvas():
    print "State 11\n"
def end_program():
    print "Program quitting... Goodbye\n"
    running = 0

states = {
    0 : start,
    1 : select_shape,
    2 : create_shape,
    3 : edit_shape,
    4 : move_up,
    5 : move_down,
    6 : move_left,
    7 : move_right,
    8 : rotate_shape,
    9 : place_shape,
    10 : delete_shape,
    11 : clear_canvas,
    12 : end_program,
}

user_input = raw_input("Press any key to start ")
while(running):
    print(state)
    states[state]()

while(user_input != 'QUIT'):
    user_input = raw_input("Select shape: dot [d] | line [l] | square [s] ")
    print("Shape choosen")
    state = int(user_input)
    states[state]()
#    if shape_options.index(user_input) > -1:

#    else:
#        print("No such shape, try again")