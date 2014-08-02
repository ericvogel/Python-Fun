from Tkinter import *
import WorldData


def __init__():
	print'Loading GameObject class...Done'

class GameObject():
		
		
		def __init__(self):
			self.x = 0
			self.y = 0
			self.image = None
			self.movingRight = True
			self.movingSpeed = 10
			self.counter = 0

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

		def bounce(self):
			if ((self.getX() < WorldData.getWorldWidth()-50) and (self.movingRight == True)):
				self.setPos(self.getX()+self.movingSpeed, self.getY())
			elif (self.getX() >= WorldData.getWorldWidth()-50):
				self.setPos(self.getX()-self.movingSpeed, self.getY())
				self.movingRight = False
			elif ((self.getX() > 50) and (self.movingRight == False)):
				self.setPos(self.getX()-self.movingSpeed, self.getY())
			elif ((self.getX() <= 50)):
				self.setPos(self.getX()+self.movingSpeed, self.getY())
				self.movingRight = True
			else:
				print'Error wrong state reached for ' + str(self)


		def move(self):
			if (WorldData.isDownPressed == True):
				self.setPos(self.getX(), self.getY()+self.movingSpeed)
			elif (WorldData.isUpPressed == True):
				self.setPos(self.getX(), self.getY()-self.movingSpeed)

			if (WorldData.isRightPressed == True):
				self.setPos(self.getX()+self.movingSpeed, self.getY())
			elif (WorldData.isLeftPressed == True):
				self.setPos(self.getX()-self.movingSpeed, self.getY())

		def update(self):
			#self.bounce()
			self.move()
			self.counter += 1
		