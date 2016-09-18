from PIL import Image
import numpy as np

INFINITE = 2147483647

def imageLoad(filepath) :
	im = Image.open(filepath)
	return im.load(), im.size # RGBA, Access : pix[x,y]

class MazeFinder :
	image = -1
	imagePath = -1
	imagePixel = -1
	allowColors = -1
	resultColor = -1
	startPoint = -1
	endPoint = -1
	colorAllowOffset = 20
	minDist = -1
	tracker = -1
	nextOffsets = ((1,0),(-1,0),(0,1),(0,-1))
	resultColorAlpha = 255
	resultThickness = 5
	def __init__(self) :
		pass

	def checkPosition(self,pos) :
		if (0 <= pos[0] < self.image.size[0]) and (0 <= pos[1] < self.image.size[1]) :
			return True
		return False

	def checkColor(self, color) :
		for allowColor in self.allowColors :
			if (allowColor[0] < color[0] < allowColor[2]) and (allowColor[3] < color[1] < allowColor[5]) and (allowColor[6] < color[2] < allowColor[8]) :
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
		self.resultColor = (int(raw_input("Result Color R : ")), int(raw_input("Result Color G : ")), int(raw_input("Result Color B : ")), self.resultColorAlpha)
		self.startPoint = (int(raw_input("Start Point X : ")), int(raw_input("Start Point Y : ")))
		self.endPoint = (int(raw_input("End Point X : ")), int(raw_input("End Point Y : ")))

	def getInputs_test(self) :
		self.imagePath = 'miro1.png'
		self.image = Image.open(self.imagePath)
		self.imagePixel = self.image.load()
		self.allowColors = [(82, 92, 102, 19, 29, 39, 7, 17, 27)]
		self.resultColor = (0, 0, 255)
		self.startPoint = (23, 748)
		self.endPoint = (1348, 25)

	def dijkstra(self) :
		before = np.ones(self.image.size, 'int32')
		todo = []
		minDist = np.zeros(self.image.size, 'int32')
		minDist.fill(INFINITE)
		todid = np.zeros(self.image.size, 'int32')
		tracker = np.zeros(self.image.size, 'int32')
		minDist[self.startPoint] = 0
		todo.append(self.startPoint)
		todid[self.startPoint] = 1
		do_perc = self.image.size[0] * self.image.size[1] / 100
		do_cnt = do_perc
		do_p = 0
		while len(todo) != 0 :
			minval = INFINITE
			minidx = -1
			for idx, point in enumerate(todo) :
				newval = minDist[point]
				if newval < minval :
					minval = newval
					minidx = idx
			minpoint = todo[minidx]
			del todo[minidx]
			# Find Minimum Mindist in Todo
			nowPosition = minpoint
			for nextOffset in self.nextOffsets : # see next positions
				nextPosition = (nowPosition[0] + nextOffset[0], nowPosition[1] + nextOffset[1])
				if (self.checkPosition(nextPosition) == False) or (before[nextPosition] == 0) : # check if already seen and check range
					continue
				newval = minDist[nowPosition] + 1
				if newval < minDist[nextPosition] : # update minimum distance
					minDist[nextPosition] = newval
					tracker[nextPosition] = nowPosition[0] * self.image.size[0] + nowPosition[1]
				if todid[nextPosition] == 0 and self.checkColor(self.imagePixel[nextPosition]) : # check if already have been pushed to todo and check color
					todo.append(nextPosition)
					todid[nextPosition] = 1
			before[nowPosition] = 0
			do_cnt -= 1
			if do_cnt == 0 :
				do_cnt = do_perc
				do_p += 1
				print 'dijkstra : %d%%' % do_p

		self.minDist = minDist
		self.tracker = tracker
	def printRoute(self) :
		if self.minDist[self.endPoint] == INFINITE :
			pass
		else :
			cur = self.endPoint
			while cur != self.startPoint :
				p1 = self.resultThickness / 2
				for i in range(self.resultThickness) :
					for j in range(self.resultThickness) :
						self.imagePixel[cur[0] - p1 + i, cur[1] - p1 + j] = self.resultColor
				tmp = self.tracker[cur]
				x = tmp / self.image.size[0]
				y = tmp - x * self.image.size[0]
				cur = (x,y)
	def run(self) :
		self.getInputs()
		print 'got input, do dijkstra...'
		self.dijkstra()
		print 'dijkstra complete, print route...'
		self.printRoute()
		print 'printed route'
		self.image.show()
	def testrun(self) :
		self.getInputs_test()
		print 'got input, do dijkstra...'
		self.dijkstra()
		print 'dijkstra complete, print route...'
		self.printRoute()
		print 'printed route'
		self.image.show()



if __name__ == '__main__':
	mazeFinder = MazeFinder()
	mazeFinder.run()