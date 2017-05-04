# INTIALIZATION

import pygame, math, sys
from pygame.locals import *
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock();

class SkySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(SkySprite, self).__init__()
        self.image = pygame.image.load("Sky/sky2.png")
        self.image = pygame.transform.scale(self.image, (1001, 1057))
        self.rect = self.image.get_rect()
        self.rect.center = (270, 200)
        #self.rect.x, self.rect.y = rect.center 
        #self.rect.y = 100
