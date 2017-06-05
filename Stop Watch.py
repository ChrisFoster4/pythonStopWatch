import time
from graphics import *
##Initialising Variables
secondsSinceStart = 0 
minutes = 0
hours = 0
graphicsWindow = GraphWin("Stop Watch",200,200)
timer = True
box = ""
timeToDisplay = Text(Point(50,25),"")
timeToDisplay.setSize(36)
timeToDisplay.draw(graphicsWindow)
##Drawing static text
secondsText = Text(Point(160,12),"Seconds")
minutesText = Text(Point(100,12),"Minutes")
hoursText = Text(Point(40,12),"Hours")
##Drawing controls
#start/unpause(resume)
start = Rectangle(Point(10,150),Point(50,190))
start.setFill("light green")
start.draw(graphicsWindow)
#pause
pause = Rectangle(Point(60,150),Point(100,190))
pause.setFill("blue")
pause.draw(graphicsWindow)
#stop
stop = Rectangle(Point(110,150),Point(150,190))
stop.setFill("red")
stop.draw(graphicsWindow)
#reset
reset = Rectangle(Point(160,150),Point(199,190))
reset.setFill("orange")
reset.draw(graphicsWindow)



minutesText = Text(Point(100,12),"Minutes")
##Main Loop
print("Press start to begin")
#Waiting for the mouse to be within the start box
startClicked=False
mouseClick = Point(0,0)
initialText = Text(Point(100,100),"Press the green box to start")
initialText.draw(graphicsWindow)
while startClicked == False:
    mouseClick = graphicsWindow.getMouse()
    print(mouseClick.getX())
    print(mouseClick.getY())
    if mouseClick.getX()>10 and mouseClick.getX()<50 and mouseClick.getY()>150 and mouseClick.getY()<190:
         startClicked == True
         break 
initialText.undraw()
secondsText.draw(graphicsWindow)
minutesText.draw(graphicsWindow)
hoursText.draw(graphicsWindow)
while timer == True:
    secondsSinceStart = secondsSinceStart + 1
    minutes = (secondsSinceStart //60 -(hours*60))
    hours = (secondsSinceStart//3600)
    secondsToPrint = (secondsSinceStart-((minutes*60)+(hours*3600)))
    
    
    
    #Stops seconds being -3600 when hours and minutes are 0.
    if secondsToPrint <1:
        secondsToPrint = 0
    space = " "
    timeToBePrinted = (hours,minutes,secondsToPrint)
    timeToDisplay.undraw()
    timeToDisplay = Text(Point(100,50),timeToBePrinted)
    
    timeToDisplay.draw(graphicsWindow)
    time.sleep(1)
    
    #Where use clicked
    mouseClick = graphicsWindow.checkMouse()
    if mouseClick == None:
        box = ""
    else:
        if mouseClick.getX()>10 and mouseClick.getX()<50 and mouseClick.getY()>150 and mouseClick.getY()<190:
            box = "start"
        elif mouseClick.getX()>60 and mouseClick.getX()<100 and mouseClick.getY()>150 and mouseClick.getY()<190:
            box = "pause"
            
        
        elif mouseClick.getX()>110 and mouseClick.getX()<150 and mouseClick.getY()>150 and mouseClick.getY()<190:
            box = "stop"
            timer = False
        elif mouseClick.getX()>160 and mouseClick.getX()<200 and mouseClick.getY()>150 and mouseClick.getY()<190:
            box = "reset"
            secondsSinceStart = 0
            
    print("box",box)
    
