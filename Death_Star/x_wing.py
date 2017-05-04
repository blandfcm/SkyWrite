# INTIALIZATION

import pygame, math, sys
from pygame.locals import *
#screen = pygame.display.set_mode((1024, 768))
#clock = pygame.time.Clock();

class ShipSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(ShipSprite, self).__init__()
        self.image = pygame.image.load("X_Wing/cockpit.png")
        self.rect = self.image.get_rect()
        self.rect.center = (270, 585)
    def update(self, deltat):
        print "-"

class XSprite(pygame.sprite.Sprite):
    width = 270 

    image1 = pygame.image.load("X/x1.png")
    image2 = pygame.image.load("X/x2.png")
    image3 = pygame.image.load("X/x3.png")
    image4 = pygame.image.load("X/x4.png")
    image5 = pygame.image.load("X/x5.png")
    image6 = pygame.image.load("X/x6.png")
    image7 = pygame.image.load("X/x7.png")
    image8 = pygame.image.load("X/x8.png")
    image9 = pygame.image.load("X/x9.png")
    image10 = pygame.image.load("X/x10.png")
    image11 = pygame.image.load("X/x11.png")

    def __init__(self):
        super(XSprite, self).__init__()
        self.image = self.image6
        self.rect = self.image.get_rect()
        self.rect.center = (307, 585)

        self.k_left = self.k_right = self.k_down = self.k_up = 0

    def update(self, deltat):
        self.width += self.k_left + self.k_right

        if self.width > 432 and self.width < 468:
            self.image = self.image1
        elif self.width > 396 and self.width < 432:
            self.image = self.image2
        elif self.width > 360 and self.width < 396:
            self.image = self.image3
        elif self.width > 324 and self.width < 360:
            self.image = self.image4
        elif self.width > 288 and self.width < 324:
            self.image = self.image5
        elif self.width > 252 and self.width < 288:
            self.image = self.image6
        elif self.width > 216 and self.width < 252:
            self.image = self.image7
        elif self.width > 180 and self.width < 216:
            self.image = self.image8
        elif self.width > 144 and self.width < 180:
            self.image = self.image9
        elif self.width > 108 and self.width < 144:
            self.image = self.image10
        elif self.width > 72 and self.width < 108:
            self.image = self.image11
        else:
            self.image = self.image
   
class YSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(YSprite, self).__init__()
        self.image = pygame.image.load("Y/y6.png")
        self.rect = self.image.get_rect()
        self.rect.center = (355, 586)

    def update(self, deltat):
        print "-"
