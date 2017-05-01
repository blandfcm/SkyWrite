#!/usr/bin/python

import string, sys, shapes
#import display_object
from display_object import *
from matrix_master import *
from locationservices import *
from matrix_printer import *
from State import State
from StateMachine import StateMachine

# Base canvas object, all drawing will be done on this
canvas = display_object(0,0,32,32)
master = matrix_master(canvas)
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
shape = display_object(15,15,shape_length,shape_length)

class Start(State):
    def run(self):
        print("Start")
    def next(self,input):
        return DrawingApp.select
class Select(State):
    def run(self):
        print("Select")
        shape.clear()
        shape.x = 15
        shape.y = 15
        print_to_matrix_default(master.display_object_list[0].pix)
    def next(self,input):
        user_input = raw_input("Select shape: dot [0] | line [1] | square [2] ")
        if user_input == 'QUIT':
            return DrawingApp.end_program
        elif int(user_input) == 0:
            print("You choose [dot]")
            shape_choosen = int(user_input)
            # shape.pix = 1
            shape.pix[2][2] = 1
            return DrawingApp.create
        elif int(user_input) == 1:
            print("You choose [line]")
            shape_choosen = int(user_input)
            shape.pix = shapes.line_h(shape_length)
            return DrawingApp.create
        elif int(user_input) == 2:
            print("You choose [square]")
            shape_choosen = int(user_input)
            shape.pix = shapes.rect(shape_length, shape_length, 0)
            return DrawingApp.create
        else:
            print("Shape not found")
            return DrawingApp.select
class Create(State):
    def run(self):
        print("Create")
        # start shape in the middle
        temp = canvas.pix
        #layer.pix = overlayAt(15,15,shape.pix,canvas.pix,1)
        layer.pix = overlayAt(15, 15, shape.pix, master.display_object_list[0].pix, 1)
        print_to_matrix_default(layer.pix)
    def next(self,input):
        return DrawingApp.edit
class Edit(State):
    def run(self):
        print("Edit")
        layer.clear()
        layer.pix = overlayAt(shape.x,shape.y,shape.pix,master.display_object_list[0].pix,1)
        print_to_matrix_default(layer.pix)
    def next(self,input):
        print("Edit shape options:")
        print("Move shape: up [w] | down [s] | left [a] | right [d]")
        print("Rotate shape: [r]")
        print("Delete shape: [o]")
        user_input = raw_input("Place shape: [p]")
        if user_input == 'QUIT':
            return DrawingApp.end_program
        elif user_input == 'w':
            return DrawingApp.move_up
        elif user_input == 's':
            return DrawingApp.move_down
        elif user_input == 'a':
            return DrawingApp.move_left
        elif user_input == 'd':
            return DrawingApp.move_right
        elif user_input == 'r':
            return DrawingApp.rotate
        elif user_input == 'o':
            return DrawingApp.delete
        elif user_input == 'p':
            return DrawingApp.place
        else:
            print("command not found")
        return DrawingApp.edit
class Move_Up(State):
    def run(self):
        print("Move_Up")
        shape.y -= 1
    def next(self,input):
        return DrawingApp.edit
class Move_Down(State):
    def run(self):
        print("Move_Down")
        shape.y += 1
    def next(self,input):
        return DrawingApp.edit
class Move_Left(State):
    def run(self):
        print("Move_Left")
        shape.x -= 1
    def next(self,input):
        return DrawingApp.edit
class Move_Right(State):
    def run(self):
        print("Move_Right")
        shape.x += 1
    def next(self,input):
        return DrawingApp.edit
class Rotate(State):
    def run(self):
        print("Rotate")
    def next(self,input):
        return DrawingApp.edit
class Place(State):
    def run(self):
        print("Shape placed")
        canvas.pix = overlayAt(shape.x,shape.y,shape.pix,master.display_object_list[0].pix,1)
        #canvas.pix = layer.pix
        print_to_matrix_default(master.display_object_list[0].pix)
    def next(self,input):
        return DrawingApp.select
class Delete(State):
    def run(self):
        print("Delete")
    def next(self,input):
        return DrawingApp.select
class Clear_Canvas(State):
    def run(self):
        print("Clear_Canvas")
    def next(self,input):
        return DrawingApp.select
class End_Program(State):
    def run(self):
        print("Ending Program... Goodbye")
    def next(self,input):
        program_running = 0

class DrawingApp(StateMachine):
    def __init__(self):
        # Initial State
        StateMachine.__init__(self, DrawingApp.start)



# Static variable initialization
DrawingApp.start = Start('state: start')
DrawingApp.select = Select('state: select')
DrawingApp.create = Create('state: create')
DrawingApp.edit = Edit('state: edit')
DrawingApp.move_up = Move_Up('state: move_up')
DrawingApp.move_down = Move_Down('state: move_down')
DrawingApp.move_left = Move_Left('state: move_left')
DrawingApp.move_right = Move_Right('state: move_right')
DrawingApp.rotate = Rotate('state: rotate')
DrawingApp.place = Place('state: place')
DrawingApp.delete = Delete('state: delete')
DrawingApp.clear_canvas = Clear_Canvas('state: clear_canvas')
DrawingApp.end_program = End_Program('end_program')

user_input = raw_input("Press any key to start:")

program_running = 1
while(program_running):
    print("While loop")
    user_input = raw_input()
    print(DrawingApp().currentState.__str__())
    DrawingApp().do()
    #DrawingApp().runAll(user_input)