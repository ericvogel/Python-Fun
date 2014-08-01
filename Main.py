from Tkinter import *
import time

def Run():
	frameRate = 30
	ObjectsList = []

	class LineObject():
		x = 0
		y = 0
		movingRight = True
		movingSpeed = 4

		def __init__(self):
			pass

		def setPos(self, newX, newY):
			self.x = newX
			self.y = newY
		def getX(self):
			return (self.x)
		
		def getY(self):
			return (self.y)
		def draw(self):
			w.create_line(line1.getX(), line1.getY(), line1.getX(), line1.getY()+100, width=2)

		def update(self):
			if ((self.getX() < 799) and (self.movingRight == True)):
				self.setPos(self.getX()+self.movingSpeed, self.getY())
			elif (self.getX() >= 799):
				self.setPos(self.getX()-self.movingSpeed, self.getY())
				self.movingRight = False
			elif ((self.getX() > 1) and (self.movingRight == False)):
				self.setPos(self.getX()-self.movingSpeed, self.getY())
			elif ((self.getX() <= 0)):
				self.setPos(self.getX()+self.movingSpeed, self.getY())
				self.movingRight = True
			else:
				print'Error wrong state reached for ' + str(self)
		


	def clearScreen():
		w.delete(ALL)


	line1 = LineObject()
	line1.setPos(10, 10)
	ObjectsList.append(line1)
	
	def drawObjects():
		#print 'drawing objects'
		
		for objectToDraw in ObjectsList: 
			objectToDraw.draw()


	def updateObjects():
		#print 'updating objects'
		for objectToUpdate in ObjectsList:
			objectToUpdate.update()

	def pressedUp(event):
		print 'pressed up'

	def pressedDown(event):
		print 'pressed Down'


	master = Tk()
	w = Canvas(master, width=800, height=600)
	w.pack()
	master.bind('<Up>', pressedUp)
	master.bind('<Down>', pressedDown)
	master.bind('<Up-KeyRelease>', releasedUp)
	master.bind('<Down-KeyRelease>', releasedDown)

	#timeOne = time.time()
	#print timeOne
	counter = 0
	while(True):
		clearScreen()
		timeOne = time.time()
		updateObjects()
		drawObjects()
		w.update()
		while timeOne+(1.0/frameRate)> time.time():
			time.sleep(.001)



Run()



