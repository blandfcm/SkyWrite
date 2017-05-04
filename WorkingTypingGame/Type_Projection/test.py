# INTIALIZATION

import pygame, math, sys
from pygame.locals import *
from keyboard import * 

pygame.init()

screen = pygame.display.set_mode((1024, 768))
#screen = pygame.display.set_mode((540, 700))
#screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
clock = pygame.time.Clock();

myfont = pygame.font.SysFont("None", 60)
label = myfont.render('Start Typing', 0, (255,255,255))
# CREATE X_WING AND RUN
rect = screen.get_rect()

letter = KeyboardSprite('z', 1)

letters = pygame.sprite.Group()
letters.add(letter)

tick_ignore = 0

def shoot1(letter):
    label = myfont.render('z', 0, (255, 255, 255))
    return label

while 1:
    # USER INPUT
    deltat = clock.tick(60)
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if tick_ignore == 0:
            if not hasattr(event, 'key'): continue
            down = event.type == KEYDOWN
            
            if   event.key == K_0:
                l = KeyboardSprite('0', 11)
            elif event.key == K_1:
                l = KeyboardSprite('1', 2)
            elif event.key == K_2:
                l = KeyboardSprite('2', 3)
            elif event.key == K_3:
                l = KeyboardSprite('3', 4)
            elif event.key == K_4:
                l = KeyboardSprite('4', 5)
            elif event.key == K_5:
                l = KeyboardSprite('5', 6)
            elif event.key == K_6:
                l = KeyboardSprite('6', 7)
            elif event.key == K_7:
                l = KeyboardSprite('7', 8)
            elif event.key == K_8:
                l = KeyboardSprite('8', 9)
            elif event.key == K_9:
                l = KeyboardSprite('9', 10)
            elif event.key == K_a:
                l = KeyboardSprite('a', 2)
            elif event.key == K_b:
                l = KeyboardSprite('b', 7)
            elif event.key == K_c:
                l = KeyboardSprite('c', 5)
            elif event.key == K_d:
                l = KeyboardSprite('d', 5)
            elif event.key == K_e:
                l = KeyboardSprite('e', 4)
            elif event.key == K_f:
                l = KeyboardSprite('f', 6)
            elif event.key == K_g:
                l = KeyboardSprite('g', 7)
            elif event.key == K_h:
                l = KeyboardSprite('h', 8)
            elif event.key == K_i:
                l = KeyboardSprite('i', 9)
            elif event.key == K_j:
                l = KeyboardSprite('j', 9)
            elif event.key == K_k:
                l = KeyboardSprite('k', 10)
            elif event.key == K_l:
                l = KeyboardSprite('l', 11)
            elif event.key == K_m:
                l = KeyboardSprite('m', 9)
            elif event.key == K_n:
                l = KeyboardSprite('n', 8)
            elif event.key == K_o:
                l = KeyboardSprite('o', 10)
            elif event.key == K_p:
                l = KeyboardSprite('p', 11)
            elif event.key == K_q:
                l = KeyboardSprite('q', 2)
            elif event.key == K_r:
                l = KeyboardSprite('r', 5)
            elif event.key == K_s:
                l = KeyboardSprite('s', 4)
            elif event.key == K_t:
                l = KeyboardSprite('t', 6)
            elif event.key == K_u:
                l = KeyboardSprite('u', 8)
            elif event.key == K_v:
                l = KeyboardSprite('v', 6)
            elif event.key == K_w:
                l = KeyboardSprite('w', 3)
            elif event.key == K_x:
                l = KeyboardSprite('x', 4)
            elif event.key == K_y:
                l = KeyboardSprite('y', 7)
            elif event.key == K_z: 
                l = KeyboardSprite('z', 3)
            elif event.key == K_ESCAPE:
                gamexit=True
                pygame.quit()
                quit()

            letters.add(l)

            tick_ignore = 1
        else:
            tick_ignore = 0


    # RENDERING
    screen.fill((0,0,0))
    screen.blit(label,(100,100))
    
    letters.update(deltat)

    print len(letters)

    
    #gameBackground.draw(screen)

    pygame.display.flip();

