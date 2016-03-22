# -*- coding: utf-8 -*-

import struct

class Bmp:
	bitMapData = ''

	__biWidth = 0
	__biHeight = 0
	__bitMapFileHeader = ''
	__bitMapInfoHeader = ''

	def __init__(self,imgpath):
		try:
			img = open(imgpath,"rb")
		except Exception,e:
			print e
		else:
			bftype = img.read(2)
			if(bftype!="BM"):
				print "Error, not a valid BMP img file!"
				return
			
			#BITMAPFILEHEADER 14byte
			img.seek(0)
			self.__bitMapFileHeader = img.read(14)
			biSize = struct.unpack("I",img.read(4))[0]
			self.__biWidth = struct.unpack("I",img.read(4))[0]
			self.__biHeight = struct.unpack("I",img.read(4))[0]
			biPlanes = struct.unpack("H",img.read(2))[0]
			#BMP图像的色深, 这里只处理24位真彩色BMP
			biBitCount = struct.unpack("H",img.read(2))[0]
			if biBitCount != 24:
				print "Error, not a valid BMP img file!"
				return

			img.seek(14)
			self.__bitMapInfoHeader = img.read(biSize)
			self.bitMapData = list(img.read(self.__biWidth*self.__biHeight*3))
			for i in range(0,self.__biWidth*self.__biHeight*3,3):
				b = ord(self.bitMapData[i])
				g = ord(self.bitMapData[i+1])
				r = ord(self.bitMapData[i+2])
				self.bitMapData[i] = r
				self.bitMapData[i+1] = g
				self.bitMapData[i+2] = b
		finally:
			img.close()

	def getWidth(self):
		return self.__biWidth

	def getHeight(self):
		return self.__biHeight

	def saveToFile(self, newImgPath):
		if len(self.bitMapData) != self.__biWidth*self.__biHeight*3:
			print "Error, the length of bitMapData is not valid!"
			return
		try:
			newImg =  open(newImgPath,'wb')
		except Exception,e:
			print e
		else:
			newImg.write(self.__bitMapFileHeader)
			newImg.write(self.__bitMapInfoHeader)
			for i in range(0,self.__biWidth*self.__biHeight*3,3):
				r = self.bitMapData[i]
				g = self.bitMapData[i+1]
				b = self.bitMapData[i+2]
				newImg.write(struct.pack("BBB",b,g,r))
		finally:
			newImg.close()
