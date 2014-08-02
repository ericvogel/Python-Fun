from Tkinter import *
import time
import GameObject
import WorldData



master = Tk()
master.title( WorldData.gameName + " - Powered by the BlackHawk Engine")
w = Canvas(master, width = WorldData.getWorldWidth(), height = WorldData.getWorldHeight())
w.pack()

if(WorldData.debugging):
	debugWindow = Tk()
	debugWindow.title(WorldData.gameName + " - Debug Window")
	t1 = Text(debugWindow)
	t1.insert(INSERT, "Up Arrow Pressed\nDown Arrow Pressed\nLeft Arrow Pressed\nRight Arrow Pressed")
	t1.pack()
	t1.tag_add("up", 1.0, 1.16)
	t1.tag_add("down", 2.0, 2.18)
	t1.tag_add("left", 3.0, 3.18)
	t1.tag_add("right", 4.0, 4.19)



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
		if (WorldData.debugging):
			t1.tag_config("up", background= "green")
		#print 'pressed up'

	def pressedDown(event):
		WorldData.isDownPressed = True
		if (WorldData.debugging):
			t1.tag_config("down", background= "green")
		#print 'pressed Down'

	def releasedUp(event):
		WorldData.isUpPressed = False
		if (WorldData.debugging):
			t1.tag_config("up", background= "red")
		#print 'released up'

	def releasedDown(event):
		WorldData.isDownPressed = False
		if (WorldData.debugging):
			t1.tag_config("down", background= "red")
		#print 'released Down'

	def pressedRight(event):
		WorldData.isRightPressed = True
		if (WorldData.debugging):
			t1.tag_config("right", background= "green")
		#print 'pressed Right'

	def pressedLeft(event):
		WorldData.isLeftPressed = True
		if (WorldData.debugging):
			t1.tag_config("left", background= "green")
		#print 'pressed Left'

	def releasedRight(event):
		WorldData.isRightPressed = False
		if (WorldData.debugging):
			t1.tag_config("right", background= "red")
		#print 'released Right'

	def releasedLeft(event):
		WorldData.isLeftPressed = False
		if (WorldData.debugging):
			t1.tag_config("left", background= "red")
		#print 'released Left'


	
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



