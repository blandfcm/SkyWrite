import numpy
import time
from random import randint
from rgbmatrix import Adafruit_RGBmatrix
#from random import randint

matrix = Adafruit_RGBmatrix(32,1)

x = numpy.zeros((50))
y = numpy.zeros((50))
r = numpy.zeros((50))
g = numpy.zeros((50))
b = numpy.zeros((50))
for s in range(0,100): 
    for i in range(0,50):
        x[i] = randint(0,31)
        y[i] = randint(0,31)
        r[i] = randint(1,255)
        g[i] = randint(1,255)
        b[i] = randint(1,255)
        matrix.SetPixel(int(x[i]),int(y[i]),int(r[i]),int(g[i]),int(b[i]))
        time.sleep(0.0025)
    matrix.Clear()
    #time.sleep(1)
    
#for j in range(0,50):
#    matrix.SetPixel(x[j],y[j],r[j],g[j],b[j])
#    time.sleep(1)
