# INTIALIZATION

import pygame, math, sys
from pygame.locals import *
screen = pygame.display.set_mode((1024, 768))

image1 = pygame.image.load("Death_Star/deathstar1.png")
image2 = pygame.image.load("Death_Star/deathstar2.png")

class DeathStarSprite(pygame.sprite.Sprite):
    count = 0
    speedMultiplier = 1.00

    left_rotation = 0
    right_rotation = 0
    rotate = 0

    first_image = image1
    second_image = image2
    def __init__(self, position):
        super(DeathStarSprite, self).__init__()

        #self.image = pygame.image.load("Death_Star/deathstar1.png")
        self.image = self.first_image
        self.rect = self.image.get_rect()
        
        self.position = position

        self.speed = 50
        self.k_left = self.k_right = self.k_down = self.k_up = 0

    def update(self, deltat):
        width = self.k_left + self.k_right
        height = self.k_up + self.k_down 
        self.rotate += self.left_rotation + self.right_rotation

        if self.speedMultiplier < 1.75:
            self.speedMultiplier += 0.0002
        if self.speed > 0:
            self.speed -= 0.01 * self.speedMultiplier
        

        if self.image == self.first_image:
            self.second_image = pygame.transform.rotate(image2, self.rotate)
        else:
            self.first_image = pygame.transform.rotate(image1, self.rotate)

        x, y = self.position
          
        x += width * self.speedMultiplier
        y += height * self.speedMultiplier
       
        self.position = (x,y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
    
        if self.count >= self.speed:
            if self.image == self.first_image:
                self.image = self.second_image
                self.count = 0
            else:
                self.image = self.first_image 
                self.count = 0
        print "-------"
        print x
        print y
        #print self.speedMultiplier
        #print self.speed
        self.count += 5


