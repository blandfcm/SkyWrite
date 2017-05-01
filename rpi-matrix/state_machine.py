#!/usr/bin/python

class state_machine:

    def __init__(self):
        self.state = 0

    # state = 0
    # do nothing
    def start(self):
        print("State: Start")

    def move_shape(self,key):
        if key == 'w':
            if shape.y > 0:
                shape.y -= 1
        elif key == 's':
            if shape.y < 31:
                shape.y += 1
        elif key == 'd':
            if shape.x < 31:
                shape.x += 1
        elif key == 'a':
            if shape.x > 0:
                shape.x -= 1