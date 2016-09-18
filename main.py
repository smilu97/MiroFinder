from PIL import Image
import numpy as np

def imageLoad(filepath) :
	im = Image.open(filepath)
	return im.load(), im.size # RGBA, Access : pix[x,y]

class MazeFinder :
	image = -1
	imagePath = -1
	imagePixel = -1
	allowColors = -1
	startPoint = -1
	endPoint = -1
	colorAllowOffset = 20
	def __init__(self) :
		pass

	def checkColor(color) :
		for i in range(len(allowColors)) :
			if (allowColors[i][0] < color[0] < allowColors[i][2]) and (allowColors[i][3] < color[1] < color[5]) and (allowColors[i][6] < color[2] < allowColors[i][8]) :
				return True
		return False

	def getInputs(self) :
		self.imagePath = raw_input("Image path : ")
		self.image = Image.open(self.imagePath)
		self.imagePixel = self.image.load()
		self.allowColors = []
		allowColor_num = int(raw_input("Allow color num :"))
		for colorIdx in range(allowColor_num) :
			R_val = int(raw_input("%d color R : " % (colorIdx+1)))
			G_val = int(raw_input("%d color G : " % (colorIdx+1)))
			B_val = int(raw_input("%d color B : " % (colorIdx+1)))
			self.allowColors.append((R_val - self.colorAllowOffset, R_val, R_val + self.colorAllowOffset,
								G_val - self.colorAllowOffset, G_val, G_val + self.colorAllowOffset,
								B_val - self.colorAllowOffset, B_val, B_val + self.colorAllowOffset))
		self.startPoint = (int(raw_input("Start Point X : ")), int(raw_input("Start Point Y : ")))
		self.endPoint = (int(raw_input("End Point X : ")), int(raw_input("End Point Y : ")))


if __name__ == '__main__':
	mazeFinder = MazeFinder()
	mazeFinder.getInputs()
	
