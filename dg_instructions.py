# INTIALIZATION
import pygame, math, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock();

myfont = pygame.font.SysFont("None", 60)
title = myfont.render('Drawing Game Instructions', 0, (0,200,0))
t = myfont.render('Select Shape   Select Size    Edit Shape', 0, (0,0,200))
line1 = myfont.render('[0] - Dot             [S] - Small       [w] - Up', 0, (255,255,255))
line2 = myfont.render('[1] - Line           [M] - Medium   [a] - Left', 0, (255,255,255))
line3 = myfont.render('[2] - Square      [L] - Large       [s] - Down', 0, (255,255,255))
line4 = myfont.render('[9] - Clear                                   [d] - Right', 0, (255,255,255))
line5 = myfont.render('                                                     [r] - Rotate', 0, (255,255,255))
line6 = myfont.render('                                                     [p] - Place', 0, (255,255,255))
line7 = myfont.render('                                                     [o] - Delete', 0, (255,255,255))
line8 = myfont.render('* after Select Size hit [f] to fill a Square', 0, (255,255,255))
line9 = myfont.render('Type "QUIT" in either menu to end Program', 0, (200,0,0))

while 1:
    # RENDERING
    screen.fill((0,0,0)) #black background

    screen.blit(title,((screen.get_width()/2)-230,25))
    screen.blit(t,((screen.get_width()/2)-400,100))
    screen.blit(line1,((screen.get_width()/2)-400,150))
    screen.blit(line2,((screen.get_width()/2)-400,200))
    screen.blit(line3,((screen.get_width()/2)-400,250))
    screen.blit(line4,((screen.get_width()/2)-400,300))
    screen.blit(line5,((screen.get_width()/2)-400,350))
    screen.blit(line6,((screen.get_width()/2)-400,400))
    screen.blit(line7,((screen.get_width()/2)-400,450))
    screen.blit(line8,((screen.get_width()/2)-400,520))
    screen.blit(line9,((screen.get_width()/2)-400,575))
    
    pygame.display.flip();

