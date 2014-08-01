from Tkinter import *
import time
import LineObject
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


	line1 = LineObject.LineObject()
	line1.setDraw(w.create_line(line1.getX(), line1.getY(), line1.getX(), line1.getY() + 200, width=2))
	line1.setPos(10, 10)
	ObjectsList.append(line1)
	
	



	def drawObjects():
		#print 'drawing objects'
		
		for objectToDraw in ObjectsList: 
			objectToDraw.getDraw()


	def updateObjects():
		#print 'updating objects'
		for objectToUpdate in ObjectsList:
			objectToUpdate.update()

	def pressedUp(event):
		print 'pressed up'

	def pressedDown(event):
		print 'pressed Down'

	def releasedUp(event):
		print 'released up'

	def releasedDown(event):
		print 'released Down'


	
	master.bind('<Up>', pressedUp)
	master.bind('<Down>', pressedDown)
	master.bind('<KeyRelease-Up>', releasedUp)
	master.bind('<KeyRelease-Down>', releasedDown)

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



