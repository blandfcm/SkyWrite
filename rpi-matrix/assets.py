#!/usr/bin/python
import numpy

def loadLowerLetters(letters):
    lines = [line.rstrip('\n') for line in open('lowers_case.txt')]

    currentLine = 0
    for i in range(0, 26):
        for k in range(0, 7):
            for j in range(0, 5):
                letters[i + 65][k][j] = lines[currentLine][j]
            currentLine = currentLine + 1
    return letters

def loadUpperLetters(letters):
    lines = [line.rstrip('\n') for line in open('upper-letters.txt')]

    currentLine = 0
    for i in range(0, 26):
        for k in range(0, 7):
            for j in range(0, 5):
                letters[i + 65][k][j] = lines[currentLine][j]
            currentLine = currentLine + 1
    return letters

def loadLetters():
    letters = numpy.zeros((281, 7, 5))
    letters = loadUpperLetters(letters, 'upper-letters.txt', 26)
#    letters = loadCharacters(letters, 'lower_case.txt', 26)
    return letters
