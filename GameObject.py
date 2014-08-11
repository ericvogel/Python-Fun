import WorldData


def __init__():
	print'Loading GameObject class...Done'

class GameObject():
		
		
		def __init__(self):
			self.x = 0
			self.y = 0
			self.image = None

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
			#print self.image


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
			pass
		