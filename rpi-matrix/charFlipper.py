#!/usr/bin/python
import numpy

def flip(letter):
	lret = numpy.zeros((5,7))
	for i in range(0, 5):
		for j in range(0, 7):
			lret[i][j] = letter[j][i]
	return lret

