#!/usr/bin/python
from locationservices import *
from wordcontroller import *
from matrix_printer import *
from display_object import *
from scoreboard import *
from matrix_master import *
import string
import array
import numpy

word = "Scor:1"
print(set(string.ascii_lowercase).intersection(word))
print(set(string.ascii_uppercase).intersection(word))
print(set(string.digits).intersection(word))
print(set(string.punctuation).intersection(word))
#print(string.digits.index(word[0]))


typed_string_pix = numpy.zeros((32,32))
canvas_pix = display_object(0,0,32,32)
test_master = matrix_master(canvas_pix)

# display_object for user typed input (in typing game)
user_typed_obj = display_object(1,4,30,7)
test_master.display_object_list.append(user_typed_obj)

# display_object for the score
scoreboard_obj = scoreboard(1,16,4)
test_master.display_object_list.append(scoreboard_obj)

#print_to_matrix_default(displayAt(0,0,scoreboard_obj.getScoreboard_pix(0)))

user_input = raw_input("Press any key to start\t")
# take first char input --> initialize typed_string
#typed_string = array.array('c',[user_input])
typed_string = []
# add char input.pix --> user_typed_obj
#this_char = chartopix(user_input)
user_typed_idx = 0
score = 0
while(user_input != 'QUIT'):
    user_input = raw_input("Press any key\t")
    print(user_input)
    score += 1
    typed_string.append(user_input)
    #this_char = chartopix(user_input)
    #this_pix = displayAt(0, 0, this_char)
    #print_to_matrix_default(this_pix)
    #print("--------------------------------------------")
    for i in range(0,len(typed_string)):
        this_char = chartopix(typed_string[i])
        #print((i*5)+1)
        #user_typed_obj.grid_pix = overlayAt((i*5),0,this_char,user_typed_obj.grid_pix,0)
        test_master.display_object_list[1].pix = overlayAt((i * 5), 0, this_char, test_master.display_object_list[1].pix, 0)

    test_master.display_object_list[0].pix = displayAt(1,4, test_master.display_object_list[1].pix)
    test_master.display_object_list[0].pix = overlayAt(1,16,scoreboard_obj.getScoreboard_pix(score),test_master.display_object_list[0].pix,0)
    #print_to_matrix_default(user_typed_obj.pix)
    #print_to_matrix_default(test_master.display_object_list[1].pix)
    print_to_matrix_default(test_master.display_object_list[0].pix)
    print("--------------------------------------------")

