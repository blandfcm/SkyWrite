# INTIALIZATION

import pygame, math, sys
from pygame.locals import *
from x_wing import * 
from background import * 
from death_star import * 

#screen = pygame.display.set_mode((1024, 768))
screen = pygame.display.set_mode((540, 700))
#screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
clock = pygame.time.Clock();

# CREATE X_WING AND RUN
rect = screen.get_rect()
sky = SkySprite()
ship = ShipSprite()
x = XSprite()
y = YSprite()

death_star = DeathStarSprite(rect.center)

gameBackground = pygame.sprite.Group()
gameBackground.add(sky)

gameForeground = pygame.sprite.LayeredUpdates()
gameForeground.add(ship)
gameForeground.add(x)
gameForeground.add(y)

movingSprites = pygame.sprite.Group()
movingSprites.add(death_star)

while 1:
    # USER INPUT
    deltat = clock.tick(30)
    
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN
        
        if event.key == K_w:
            death_star.k_up = down * 4
            x.k_up = down * 4
        elif event.key == K_a:
            death_star.k_left = down * 4
            x.k_left = down * 4
        elif event.key == K_s:
            death_star.k_down = down * -4
            x.k_down = down * -4
        elif event.key == K_d:
            death_star.k_right = down * -4
            x.k_right = down * -4
        elif event.key == K_l:
            death_star.left_rotation = down * -1
        elif event.key == K_SEMICOLON:
            death_star.right_rotation = down * 1
        elif event.key == K_ESCAPE:
            gamexit=True
            pygame.quit()
            quit()

    # RENDERING
    screen.fill((0,0,0))

    gameForeground.update(deltat)
    movingSprites.update(deltat)

    gameBackground.draw(screen)
    movingSprites.draw(screen)
    gameForeground.draw(screen)

    pygame.display.flip();
