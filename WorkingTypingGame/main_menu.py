# INTIALIZATION

import pygame, math, sys, time, os
from pygame.locals import *
import subprocess
import input_triggered_matrix

pygame.init()

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock();

myfont = pygame.font.SysFont("None", 60)

selection = 0
arrowHeight = screen.get_height()/2 - 120

games = ['Typing Game', 'Typing Spam', 'Death Star']

def drawScreen(deltat):
    screen.fill((0,0,0)) #black background
    pygame.draw.rect(screen, (0,0,255), [screen.get_width()/2 - 200, screen.get_height()/2 - 200, screen.get_width()/2 - 50, screen.get_height()/2-50], 2)
    
    title = myfont.render('Main Menu', 0, (255, 255, 255))
    screen.blit(title,((screen.get_width()/2 - 150, screen.get_height()/2 - 180)))

    arrow_label = myfont.render('>', 0, (255,255,255))
    screen.blit(arrow_label,((screen.get_width()/2 - 150, arrowHeight)))

    for i in range(0, len(games)):
        label = myfont.render(games[i], 0, (255,255,255))
        screen.blit(label,((screen.get_width()/2 - 100, screen.get_height()/2 - 120 + i*60)))

def drawArrow(movement):
    global arrowHeight

    if movement == 1:
        if arrowHeight > screen.get_height()/2 - 120:
            arrowHeight -= 60
    else:
        if arrowHeight < screen.get_height()/2:
            arrowHeight += 60
    
def selectGame():
    global arrowHeight
    global selection
    
    if arrowHeight == screen.get_height()/2 - 120:
        #sys.path.insert(0, 'Type_Projection/')
        import typing.py
    elif arrowHeight == screen.get_height()/2 - 60:
        import spam.py 
    elif arrowHeight == screen.get_height()/2:
        process = subprocess.Popen("ls")

    selection = 1

while selection == 0:
    # USER INPUT
    deltat = clock.tick(60)
     
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                drawArrow(1) 
            elif event.key == K_DOWN:
                drawArrow(0)
            elif event.key == K_RETURN:
                selectGame()
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    drawScreen(deltat)
    pygame.display.flip();
