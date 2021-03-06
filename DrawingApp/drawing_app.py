#!/usr/bin/python

import string, sys, shapes
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
shape_length_default = 5
shape_x_default = 15
shape_y_default = 15

# State machine hoo-ha
state = 0
running = 1     # keeps while loop going
shape_choosen = -1      #default- no shape
shape_orientation = 0   #default- horizontal
shape = display_object(15,15,shape_length,shape_length)

class Start(State):
    def run(self):
        print("Start")
    def next(self,input):
        return DrawingApp.select
class Select(State):
    def run(self):
        global canvas, layer, shape, shape_choosen, shape_length, shape_orientation
        print("Select")
        shape.clear()
        shape.reset_info()
        shape.x = 15
        shape.y = 15
        shape.length = 5
        #print_to_matrix_default(master.display_object_list[0].pix)
        print "select- canvas.pix"
        print_to_matrix_default(canvas.pix)
    def next(self,input):
        global canvas, layer, shape, shape_choosen, shape_length, shape_orientation
        user_input = raw_input("Select shape: dot [0] | line [1] | square [2] | Clear Canvas [9]")
        if user_input == 'QUIT':
            return DrawingApp.end_program
        elif int(user_input) == 0:
            print("You choose [dot]")
            shape_choosen = int(user_input)
            shape_orientation = 0
            shape.id = 0
            shape.orientation = 0
            shape.length = 1
            shape.pix[2][2] = 1
            return DrawingApp.create
        elif int(user_input) == 1:
            print("You choose [line]")
            shape_choosen = int(user_input)
            shape_orientation = 0
            shape.id = 1
            shape.orientation = 0
            shape.length = 5
            shape.pix = shapes.line_h(shape_length)
            return DrawingApp.create
        elif int(user_input) == 2:
            print("You choose [square]")
            shape_choosen = int(user_input)
            shape_orientation = 0
            shape.id = 2
            shape.orientation = 0
            shape.length = 5
            shape.fill = 0
            shape.pix = shapes.rect(shape_length, shape_length, 0)
            return DrawingApp.create
        elif int(user_input) == 9:
            print "Clearing Canvas..."
            return DrawingApp.clear_canvas
        else:
            print("Shape not found")
            return DrawingApp.select
class Create(State):
    def run(self):
        global canvas, layer, shape
        print("Create")
        # Start shape in the middle
        layer.pix = overlayAt(15, 15, shape.pix, canvas.pix, 1)
    def next(self,input):
        return DrawingApp.edit
class Edit(State):
    def run(self):
        global canvas, layer, shape
        print("Edit")
        layer.clear()
        layer.pix = overlayAt(shape.x, shape.y, shape.pix, canvas.pix, 1)
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
        elif user_input == 'm':
            return DrawingApp.expand
        elif user_input == 'n':
            return DrawingApp.reduce
        elif user_input == 'o':
            return DrawingApp.delete
        elif user_input == 'p':
            return DrawingApp.place
        else:
            print("command not found")
        return DrawingApp.edit
class Move_Up(State):
    def run(self):
        global canvas, layer, shape
        print("Move_Up")
        shape.y -= 1
        print shape.y
    def next(self,input):
        return DrawingApp.edit
class Move_Down(State):
    def run(self):
        global canvas, layer, shape
        print("Move_Down")
        shape.y += 1
        print shape.y
    def next(self,input):
        return DrawingApp.edit
class Move_Left(State):
    def run(self):
        global canvas, layer, shape
        print("Move_Left")
        shape.x -= 1
    def next(self,input):
        return DrawingApp.edit
class Move_Right(State):
    def run(self):
        global canvas, layer, shape
        print("Move_Right")
        shape.x += 1
    def next(self,input):
        return DrawingApp.edit
class Rotate(State):
    def run(self):
        global canvas, layer, shape, shape_choosen, shape_length, shape_orientation
        print("Rotate")
        print shape_choosen
        print shape_length
        print shape_orientation
        if shape.id == 0:
            # Rotating a dot does nothing
            pass
        elif shape.id == 1:
            # Line - default orientation = 0 (horizontal)
            # 0 _    1 /    2 |     3 \
            # rotation scheme:
            #   0 -> 1 -> 2 -> 3 -> 0 -> ...
            if shape.orientation == 0:
                shape.pix = shapes.line_d(shape_length, 1)
                shape_orientation = 1
                shape.orientation = 1
            elif shape.orientation == 1:
                shape.pix = shapes.line_v(shape_length)
                shape_orientation = 2
                shape.orientation = 2
            elif shape.orientation == 2:
                shape.pix = shapes.line_d(shape_length, 0)
                shape_orientation = 3
                shape.orientation = 3
            else:
                shape.pix = shapes.line_h(shape_length)
                shape_orientation = 0
                shape.orientation = 0
        elif shape.id == 2:
            # Square - default orientation = 0 (horizontal & vertical sides)
            # 0 |_|     1 v (diamond)
            if shape.orientation == 0:
                shape.pix = shapes.square_d(shape_length, 0)
                shape_orientation = 1
                shape.orientation = 1
            else:
                shape.pix = shapes.square(shape_length, 0)
                shape_orientation = 0
                shape.orientation = 0
        else:
            print "something went terribly wrong"
    def next(self,input):
        return DrawingApp.edit
class Expand(State):
    def run(self):
        global canvas, layer, shape
        print "Expand"
        if shape.length < 30:
            shape.length += 1
    def next(self,input):
        return DrawingApp.edit
class Reduce(State):
    def run(self):
        global canvas, layer, shape
        print "Reduce"
        if shape.length > 1:
            shape.length -= 1
    def next(self,input):
        return DrawingApp.edit
class Place(State):
    def run(self):
        global canvas, layer, shape
        print("Shape placed")
        canvas.pix = overlayAt(shape.x, shape.y, shape.pix, canvas.pix, 1)
        print_to_matrix_default(canvas.pix)
    def next(self,input):
        return DrawingApp.select
class Delete(State):
    def run(self):
        global canvas, layer, shape
        print("Delete")
    def next(self,input):
        return DrawingApp.select
class Clear_Canvas(State):
    def run(self):
        global canvas, layer, shape
        print("Clear_Canvas")
        canvas.clear()
    def next(self,input):
        return DrawingApp.select
class Save_Canvas(State):
    def run(self):
        global canvas, layer, shape
        print "Saving canvas..."
    def next(self, input):
        user_input = raw_input("[0] Continue with canvas    [1] Start with blank canvas     [2] Quit program")
        if user_input == 0:
            DrawingApp.select
        elif user_input == 1:
            DrawingApp.clear_canvas
        else:
            DrawingApp.end_program
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
DrawingApp.expand = Expand('state: expand')
DrawingApp.reduce = Reduce('state: reduce')
DrawingApp.place = Place('state: place')
DrawingApp.delete = Delete('state: delete')
DrawingApp.clear_canvas = Clear_Canvas('state: clear_canvas')
DrawingApp.end_program = End_Program('end_program')

user_input = raw_input("Press any key to start:")

DrawingApp().do()
