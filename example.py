# -*- coding: utf-8 -*-

import sys
#import class Bmp
from bmpExp import Bmp

def hideInfo(imgPath, hideInfo,newImgSavePath):
	bmp = Bmp(imgPath)
	width = bmp.getWidth()
	height = bmp.getHeight()
	length = len(hideInfo)

	for i in range(length):
		hide = ord(hideInfo[i])
		base = 7*i;
		if base+7 > width*height*3:
			print "Error, the hideInfo is too long!"
			break
		for j in range(7):
			bmp.bitMapData[j+base] = (bmp.bitMapData[j+base]&(0xfe))|((hide>>j)&1)
	
	# use 0 to present the end 
	base = 7*length
	if base+7 <= width*height*3:
		for j in range(7):
			bmp.bitMapData[j+base] = (bmp.bitMapData[j+base]&(0xfe))

	bmp.saveToFile(newImgSavePath)

def showInfo(imgPath):
	bmp = Bmp(imgPath)
	width = bmp.getWidth()
	height = bmp.getHeight()
	length = width*height*3

	hideInfo = ''
	for i in range(length):
		base = 7*i
		hidechar = 0
		for j in range(7):
			hidechar |= ((bmp.bitMapData[j+base]&1)<<j)
		if hidechar == 0:
			break
		hideInfo += chr(hidechar)

	print hideInfo

if __name__ == '__main__':
	if len(sys.argv) != 5 and len(sys.argv) != 3:
		print "usage: python example.py bmpImgPath hide hideInfo(hideFile hideFilePath) newBmpImgSavePath or python example.py bmpImgPath show"
	
	elif len(sys.argv) == 5:
		if sys.argv[2] != 'hide' and sys.argv[2] != 'hideFile':
			print "usage: python example.py bmpImgPath hide hideInfo(hideFile hideFilePath) newBmpImgSavePath"
		elif sys.argv[2] == 'hide':
			hideInfo(sys.argv[1],sys.argv[3],sys.argv[4])
		else:
			try:
				hideFile = open(sys.argv[3],'r')
				hideInfo(sys.argv[1],hideFile.read(),sys.argv[4])
			except Exception, e:
				print e
			finally:
				hideFile.close()

	elif len(sys.argv) == 3:
		if sys.argv[2] != 'show':
			print "usage: python example.py bmpImgPath show"
		else:
			showInfo(sys.argv[1])
