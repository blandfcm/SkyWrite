#!/usr/bin/python
from PIL import Image
import numpy, time
from rgbmatrix import Adafruit_RGBmatrix
from locationservices import displayAt

matrix = Adafruit_RGBmatrix(32,1)
#image = Image.open("Targeting1.png")
image = Image.open("circle_gif_1.jpg")
image.load()
im_pix = image.load()
pixr = numpy.zeros((32,32))
pixg = numpy.zeros((32,32))
pixb = numpy.zeros((32,32))
for x in range(0,32):
    for y in range(0,32):
        pix = im_pix[x,y]
        r = g = b = 0
#        if pix[0] > 128:
#            r = 255
#        if pix[1] > 128:
#            g = 255
#        if pix[2] > 128:
#            b = 255
        r = pix[0]
        g = pix[1]
        b = pix[2]
#        matrix.SetPixel(x,y,r/3,g,b)
        time.sleep(0.0025)
        pixr[x][y] = pix[0]
        pixg[x][y] = pix[1]
        pixb[x][y] = pix[2]
print int(pixr[31][31])
print int(pixg[31][31])
print int(pixb[31][31])
#for n in range(32, -image.size[0], -1):
#    matrix.SetImage(image.im.id,0,0)
#    time.sleep(0.025)
time.sleep(4.0)
matrix.Clear()
for x in range(0,32):
    for y in range(0,32):
        r = int(pixr[x][y]/3)
        g = int(pixg[x][y]/2)
        b = int(pixb[x][y]/2)
        if r > 0:
            temp = 1
        else:
            temp = 0
        matrix.SetPixel(x,y,r,g,b)
#        matrix.SetPixel(x,y,0,255,0)
#        matrix.SetPixel(x,y,0,0,255)       
#        matrix.SetPixel(x,y,int(pixr[x][y]/3+(temp*50)),int(pixg[x][y]),int(pixb[x][y]))
#        time.sleep(0.0025)
time.sleep(5.0)

'''
def img_to_pix(filename):
    matrix = Adafruit_RGBmatrix(32,1)
    im = Image.open("Targeting1.png")
    im_pix = im.load()
    pixr = numpy.zeros((32,32))
    pixg = numpy.zeros((32,32))
    pixb = numpy.zeros((32,32))
    for x in range(0,32):
        for y in range(0,32):
            pix = im_pix[x,y]
            pixr[x][y] = pix[0]
            pixg[x][y] = pix[1]
            pixb[x][y] = pix[2]
    print int(pixr[31][31])
    print int(pixg[31][31])
    print int(pixb[31][31])
#    for x in range(0,32):
#        for y in range(0,32):
#            matrix.SetPixel(x,y,int(pixr[x][y]),int(pixg[x][y]),int(pixb[x][y]))
#    time.sleep(5.0)
#    matrix.Clear()
    return (pixr,pixg,pixb)
'''
