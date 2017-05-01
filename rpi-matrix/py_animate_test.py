#!/usr/bin/python

# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

import Image
import ImageDraw
import ImageColor
import time
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)
matrix.SetWriteCycles(4)
# Bitmap example w/graphics prims
image = Image.new("RGB", (32, 32)) # Can be larger than matrix if wanted!!
draw = ImageDraw.Draw(image)
#color = PIL.ImageColor.rgb(0,0,255)
draw.rectangle((0,0,31,31),fill=(0,255,255),outline=1)
draw.line((0,0,31,31),fill=1)
matrix.SetImage(image.im.id,0,0)
time.sleep(2.0)
print "---------------"
matrix.Clear()
image = Image.open("circle_gif.gif")
image.load()
matrix.Fill((0,0,255))
image0 = Image.new("RGB", (32,32))
image1 = Image.new("RGB", (32,32))
image2 = Image.new("RGB", (32,32))

image0 = Image.open("Targeting1.png")
image0.load()
image1 = Image.open("Targeting2.png")
image1.load()
image2 = Image.open("Targeting3.png")
image2.load()


delay = 0.2
count = 0
while count < 10:
    matrix.SetImage(image0.im.id,0,0)
    time.sleep(delay)
    matrix.SetImage(image1.im.id,0,0)
    time.sleep(delay)
    matrix.SetImage(image2.im.id,0,0)
    time.sleep(delay)
    count += 1
count = 0
image0 = Image.open("circle_gif_0.jpg")
image0.load()
image1 = Image.open("circle_gif_1.jpg")
image1.load()
image2 = Image.open("circle_gif_2.jpg")
image2.load()
matrix.SetImage(image0.im.id,0,0)
time.sleep(delay)
matrix.SetImage(image1.im.id,0,0)
time.sleep(delay)
matrix.SetImage(image2.im.id,0,0)
time.sleep(delay)

while count < 25:
    matrix.SetImage(image0.im.id,0,0)
    time.sleep(delay)
    matrix.Clear()
    matrix.SetImage(image1.im.id,0,0)
    time.sleep(delay)
    matrix.Clear()
    matrix.SetImage(image2.im.id,0,0)
    time.sleep(delay)
    matrix.Clear()
    count += 1

#matrix.SetImage(image.im.id,0,0)

time.sleep(2.0)
matrix.Clear()
