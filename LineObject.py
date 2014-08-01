from Tkinter import *
import WorldData


def __init__():
	print'Loading LineObject class...Done'

class LineObject():
		
		
		def __init__(self):
			self.x = 0
			self.y = 0
			self.image = None
			self.movingRight = True
			self.movingSpeed = 4

		def setPos(self, newX, newY):
			self.x = newX
			self.y = newY
		def getX(self):
			return (self.x)
		
		def getY(self):
			return (self.y)
		
		def getDraw(self):
			return self.image
		
		def setDraw(self, newImage):
			self.image = newImage
			print self.image

		def update(self):
			if ((self.getX() < WorldData.getWorldWidth()-1) and (self.movingRight == True)):
				self.setPos(self.getX()+self.movingSpeed, self.getY())
			elif (self.getX() >= WorldData.getWorldWidth()-1):
				self.setPos(self.getX()-self.movingSpeed, self.getY())
				self.movingRight = False
			elif ((self.getX() > 1) and (self.movingRight == False)):
				self.setPos(self.getX()-self.movingSpeed, self.getY())
			elif ((self.getX() <= 0)):
				self.setPos(self.getX()+self.movingSpeed, self.getY())
				self.movingRight = True
			else:
				print'Error wrong state reached for ' + str(self)
		