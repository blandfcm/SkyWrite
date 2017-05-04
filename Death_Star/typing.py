# INTIALIZATION

import pygame, math, sys, time, os
from pygame.locals import *
from keyboard_typing import * 
from random import *

pygame.init()

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock();

myfont = pygame.font.SysFont("None", 60)

#Opens a text file for reading
#Words from text file are 6-letter words filtered from 
#https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-no-swears.txt
my_file = open('words.txt', "r")
words = my_file.read().splitlines() # fixes \n character for testing
my_file.close()
start_time = time.time()

score = 0
lives = 3
gameover = 0

size = len(words)
word_speed = 1*60 # everymultiple of 60 is second delay between words
count = word_speed
screen_words = pygame.sprite.LayeredUpdates()

user_input = ""
words_on_screen = []

def getWord():
    "generates new word to the screen"
    found = 1

    while found:
        selected_word = words[randint(0,size-1)]

        if len(words_on_screen) == 0:
            found = 0
        else:
            for i in range(0, len(words_on_screen)):
                if selected_word == words_on_screen[i]:
                    break 
                elif i == len(words_on_screen)-1:
                    found = 0
    
    words_on_screen.append(selected_word)    
    new_Word = Keyboard_TypingSprite(selected_word, randint(1,15))
    return new_Word

def addToWord(word, char):
    "adds a character to existing passed in string"
    
    typed_word = word 
    if char == "del" and len(typed_word) >= 0:
        typed_word = typed_word[0:-1]
    else:
        typed_word += char

    return typed_word 

def checkCorrect(attempt):
    for i in range (0,len(words_on_screen)):
        if attempt == words_on_screen[i]:
            updateScore(len(words_on_screen[i]))

            temp = screen_words.sprites()
            screen_words.remove(temp[i])
            del words_on_screen[i]

            return 1
    return 0

def updateScore(length):
    global score
    score = score + 10 * length
    #score = int(score + ((time.time() - start_time) * 0.25) + 10 * length)

def checkScore():
    global score
    global lives
    global gameover

    if lives <= 0:
        gameover = 1

    score_label1 = myfont.render('Score', 0, (255,0,0))
    score_label2 = myfont.render(str(score), 0, (255,255,255))

    lives_label1 = myfont.render('Lives', 0, (255,0,0))
    lives_label2 = myfont.render(str(lives), 0, (255,255,255))
    
    screen.blit(score_label1,((screen.get_width()/2 - 200,0)))
    screen.blit(score_label2,((screen.get_width()/2 - 190,60)))

    screen.blit(lives_label1,((screen.get_width()/2 + 200,0)))
    screen.blit(lives_label2,((screen.get_width()/2 + 240,60)))

def checkHeight():
    global lives
    temp = screen_words.sprites()

    for i in range(0, len(screen_words)):
        x,y = temp[i].position
        if(y > screen.get_height()):
            lives -= 1
            temp[i].position = (x, 100)

def drawScreen(deltat):
    screen.fill((0,0,0)) #black background
    screen_words.update(deltat)
    pygame.draw.rect(screen, (0,0,255), [0, 0, screen.get_width(), 100], 2)

while gameover == 0:
    # USER INPUT
    deltat = clock.tick(60)
     
    if count == word_speed:
        if len(screen_words) < len(words):
            screen_words.add(getWord())
            count = 0

    count += 1
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                user_input = addToWord(user_input, "del")
            elif event.key == K_SPACE:

                #two options here
                # 1. Always make user input return to nothing
                # 2. Incorrect answer keeps current input
                
                # 1.
                #if checkCorrect(user_input) == 1:
                    #user_input = ""
                # 2.
                checkCorrect(user_input)
                user_input = ""
            elif event.key == K_a:
                user_input = addToWord(user_input, "a")
            elif event.key == K_b:
                user_input = addToWord(user_input, "b")
            elif event.key == K_c:
                user_input = addToWord(user_input, "c")
            elif event.key == K_d:
                user_input = addToWord(user_input, "d")
            elif event.key == K_e:
                user_input = addToWord(user_input, "e")
            elif event.key == K_f:
                user_input = addToWord(user_input, "f")
            elif event.key == K_g:
                user_input = addToWord(user_input, "g")
            elif event.key == K_h:
                user_input = addToWord(user_input, "h")
            elif event.key == K_i:
                user_input = addToWord(user_input, "i")
            elif event.key == K_j:
                user_input = addToWord(user_input, "j")
            elif event.key == K_k:
                user_input = addToWord(user_input, "k")
            elif event.key == K_l:
                user_input = addToWord(user_input, "l")
            elif event.key == K_m:
                user_input = addToWord(user_input, "m")
            elif event.key == K_n:
                user_input = addToWord(user_input, "n")
            elif event.key == K_o:
                user_input = addToWord(user_input, "o")
            elif event.key == K_p:
                user_input = addToWord(user_input, "p")
            elif event.key == K_q:
                user_input = addToWord(user_input, "q")
            elif event.key == K_r:
                user_input = addToWord(user_input, "r")
            elif event.key == K_s:
                user_input = addToWord(user_input, "s")
            elif event.key == K_t:
                user_input = addToWord(user_input, "t")
            elif event.key == K_u:
                user_input = addToWord(user_input, "u")
            elif event.key == K_v:
                user_input = addToWord(user_input, "v")
            elif event.key == K_w:
                user_input = addToWord(user_input, "w")
            elif event.key == K_x:
                user_input = addToWord(user_input, "x")
            elif event.key == K_y:
                user_input = addToWord(user_input, "y")
            elif event.key == K_z:
                user_input = addToWord(user_input, "z")
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            print user_input
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

   
    drawScreen(deltat)
    checkHeight()
    checkScore()


    pygame.display.flip();


while gameover:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
