from Tkinter import *
import time
import GameObject
import WorldData



master = Tk()
w = Canvas(master, width = WorldData.getWorldWidth(), height = WorldData.getWorldHeight())
w.pack()


def getW():
	return w

def Run():
	frameRate = 30
	ObjectsList = []
	global w
	global master

	def clearScreen():
		w.delete(ALL)


	line1 = GameObject.GameObject()
	line1.setDraw(PhotoImage(file = 'Bin/Images/img.gif'))
	line1.setPos(10, 100)
	ObjectsList.append(line1)
	
	



	def drawObjects():
		#print 'drawing objects'
		
		for objectToDraw in ObjectsList: 
			w.create_image(objectToDraw.getX(), objectToDraw.getY(), image = objectToDraw.getDraw())
			w.create_line(objectToDraw.getX(), objectToDraw.getY(), 400, 300)
			#print objectToDraw.getDraw()


	def updateObjects():
		#print 'updating objects'
		for objectToUpdate in ObjectsList:
			objectToUpdate.update()

	def pressedUp(event):
		WorldData.isUpPressed = True
		print 'pressed up'

	def pressedDown(event):
		WorldData.isDownPressed = True
		print 'pressed Down'

	def releasedUp(event):
		WorldData.isUpPressed = False
		print 'released up'

	def releasedDown(event):
		WorldData.isDownPressed = False
		print 'released Down'

	def pressedRight(event):
		WorldData.isRightPressed = True
		print 'pressed Right'

	def pressedLeft(event):
		WorldData.isLeftPressed = True
		print 'pressed Left'

	def releasedRight(event):
		WorldData.isRightPressed = False
		print 'released Right'

	def releasedLeft(event):
		WorldData.isLeftPressed = False
		print 'released Left'


	
	master.bind('<Up>', pressedUp)
	master.bind('<Down>', pressedDown)
	master.bind('<KeyRelease-Up>', releasedUp)
	master.bind('<KeyRelease-Down>', releasedDown)
	master.bind('<Right>', pressedRight)
	master.bind('<Left>', pressedLeft)
	master.bind('<KeyRelease-Right>', releasedRight)
	master.bind('<KeyRelease-Left>', releasedLeft)

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



