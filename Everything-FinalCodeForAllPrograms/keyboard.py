# INTIALIZATION

import pygame, math, sys
from pygame.locals import *
screen = pygame.display.set_mode((1024, 768))

pygame.init()

font_size = 60
myFont = pygame.font.SysFont("None", font_size)

class KeyboardSprite(pygame.sprite.Sprite):
    label = myFont.render('a', 0, (255, 255, 255))
    def __init__(self, letter, column):
        super(KeyboardSprite, self).__init__()
        
        self.label = myFont.render(letter, 0, (255, 255, 255))

        if(column < 12):
            startX = ((screen.get_width()/2) - ((11 - column)*font_size/2))
            print startX
        else:
            startX = ((screen.get_width()/2) + ((column-11)*font_size/2))
            print startX

        self.position = (startX, screen.get_height());

        self.speed = 1

    def update(self, deltat):
        x, y = self.position
          
        y -= 6
       
        self.position = (x,y)
        screen.blit(self.label, (x,y))

        #deletes the sprite if it is offscreen to be efficient
        if y < 0:
            self.kill()
