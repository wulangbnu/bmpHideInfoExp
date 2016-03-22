# -*- coding: utf-8 -*-

#import class Bmp
from bmpExp import Bmp

#bmg init with a BMP file Path
bmp = Bmp("test.bmp")

#get bmp file's Width and Height
width = bmp.getWidth()
height = bmp.getHeight()

for i in range(0,width*height*3,3):
	r = bmp.bitMapData[i]
	g = bmp.bitMapData[i+1]
	b = bmp.bitMapData[i+2]
	# do something here
	
# after change the 	bmp.bitMapData, you can save it to a new file with a new file path
bmp.saveToFile("test_new.bmp")