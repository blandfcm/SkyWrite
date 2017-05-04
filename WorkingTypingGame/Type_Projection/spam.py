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
    
        if event.type == KEYDOWN:
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
                l = KeyboardSprite('z', 3) ####Below are nonessential keys
            elif event.key == K_BACKQUOTE: 
                l = KeyboardSprite('`', 1)
            elif event.key == K_TAB: 
                l = KeyboardSprite('[TAB]', 0)
            elif event.key == K_CAPSLOCK: 
                l = KeyboardSprite('[CAPS]', 0)
            elif event.key == K_LSHIFT: 
                l = KeyboardSprite('[LSHIFT]', 0)
            elif event.key == K_LCTRL: 
                l = KeyboardSprite('[LCTRL]', 0)
            elif event.key == K_LSUPER: 
                l = KeyboardSprite('[LSUPER]', 1)
            elif event.key == K_LALT: 
                l = KeyboardSprite('[LALT]', 2)
            elif event.key == K_F1:
                l = KeyboardSprite('[F1]', 3)
            elif event.key == K_F2:
                l = KeyboardSprite('[F2]', 4)
            elif event.key == K_F3:
                l = KeyboardSprite('[F3]', 5)
            elif event.key == K_F4:
                l = KeyboardSprite('[F4]', 6)
            elif event.key == K_F5:
                l = KeyboardSprite('[F5]', 7)
            elif event.key == K_F6:
                l = KeyboardSprite('[F6]', 8)
            elif event.key == K_F7:
                l = KeyboardSprite('[F7]', 9)
            elif event.key == K_F8:
                l = KeyboardSprite('[F8]', 10)
            elif event.key == K_F9:
                l = KeyboardSprite('[F9]', 12)
            elif event.key == K_F10:
                l = KeyboardSprite('[F10]', 13)
            elif event.key == K_F11:
                l = KeyboardSprite('[F11]', 14)
            elif event.key == K_F12:
                l = KeyboardSprite('[F12]', 15)
            elif event.key == K_MINUS:
                l = KeyboardSprite('-', 12)
            elif event.key == K_EQUALS:
                l = KeyboardSprite('=', 13)
            elif event.key == K_BACKSPACE:
                l = KeyboardSprite('[BACK]', 14)
            elif event.key == K_LEFTBRACKET:
                l = KeyboardSprite('[', 12)
            elif event.key == K_RIGHTBRACKET:
                l = KeyboardSprite(']', 13)
            elif event.key == K_SEMICOLON:
                l = KeyboardSprite(';', 12)
            elif event.key == K_QUOTE:
                l = KeyboardSprite('\'', 13)
            elif event.key == K_BACKSLASH:
                l = KeyboardSprite('\\', 14)
            elif event.key == K_RETURN:
                l = KeyboardSprite('[RETURN]', 14)
            elif event.key == K_COMMA:
                l = KeyboardSprite(',', 10)
            elif event.key == K_PERIOD:
                l = KeyboardSprite('.', 11)
            elif event.key == K_SLASH:
                l = KeyboardSprite('/', 12)
            elif event.key == K_RSHIFT:
                l = KeyboardSprite('[RSHIFT]', 13)
            elif event.key == K_SPACE:
                l = KeyboardSprite('[SPACE]', 5)
            elif event.key == K_RALT:
                l = KeyboardSprite('[RALT]', 11)
            elif event.key == K_MENU:
                l = KeyboardSprite('[MENU]', 13)
            elif event.key == K_RCTRL:
                l = KeyboardSprite('[RCTRL]', 14)
            elif event.key == K_PRINT:
                l = KeyboardSprite('[PRINT]', 16)
            elif event.key == K_INSERT:
                l = KeyboardSprite('[INSERT]', 16)
            elif event.key == K_DELETE:
                l = KeyboardSprite('[DEL]', 16)
            elif event.key == K_LEFT:
                l = KeyboardSprite('<', 16)
            elif event.key == K_SCROLLOCK:
                l = KeyboardSprite('[SCRLK]', 17)
            elif event.key == K_HOME:
                l = KeyboardSprite('[HOME]', 17)
            elif event.key == K_END:
                l = KeyboardSprite('[END]', 17)
            elif event.key == K_UP:
                l = KeyboardSprite('/\\', 17)
            elif event.key == K_DOWN:
                l = KeyboardSprite('\\/', 17)
            elif event.key == K_BREAK:
                l = KeyboardSprite('[BREAK]', 18)
            elif event.key == K_PAGEUP:
                l = KeyboardSprite('[PgUP]', 18)
            elif event.key == K_PAGEDOWN:
                l = KeyboardSprite('[PgDOWN]', 18)
            elif event.key == K_RIGHT:
                l = KeyboardSprite('>', 18)
            elif event.key == K_NUMLOCK:
                l = KeyboardSprite('[NUMLK]', 19)
            elif event.key == K_KP7:
                l = KeyboardSprite('7', 19)
            elif event.key == K_KP4:
                l = KeyboardSprite('4', 19)
            elif event.key == K_KP1:
                l = KeyboardSprite('0', 19)
            elif event.key == K_KP0:
                l = KeyboardSprite('0', 19)
            elif event.key == K_KP_DIVIDE:
                l = KeyboardSprite('/', 20)
            elif event.key == K_KP8:
                l = KeyboardSprite('8', 20)
            elif event.key == K_KP5:
                l = KeyboardSprite('5', 20)
            elif event.key == K_KP2:
                l = KeyboardSprite('2', 20)
            elif event.key == K_KP_MULTIPLY:
                l = KeyboardSprite('*', 21)
            elif event.key == K_KP9:
                l = KeyboardSprite('9', 21)
            elif event.key == K_KP6:
                l = KeyboardSprite('6', 21)
            elif event.key == K_KP3:
                l = KeyboardSprite('3', 21)
            elif event.key == K_KP_PERIOD:
                l = KeyboardSprite('.', 21)
            elif event.key == K_KP_MINUS:
                l = KeyboardSprite('-', 22)
            elif event.key == K_KP_PLUS:
                l = KeyboardSprite('+', 22)
            elif event.key == K_KP_ENTER:
                l = KeyboardSprite('[ENTER]', 22)
            elif event.key == K_ESCAPE:
                gamexit=True
                pygame.quit()
                quit()
            letters.add(l)

    # RENDERING
    screen.fill((0,0,0)) #black background
    screen.blit(label,((screen.get_width()/2)-100,100)) #Prints "Start Typing" as defined above"
    
    letters.update(deltat)

    #prints number of sprites on the screen
    print len(letters)

    pygame.display.flip();

