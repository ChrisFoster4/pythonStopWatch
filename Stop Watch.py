import time
from graphics import *
##Initialising Variables
def drawIntialScreen(graphicsWindow):
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
    #close
    close = Rectangle(Point(,),Point(,))
    close.setFill
    #close box line 1

    #close box line 2

def waitForStartClick(graphicsWindow):
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
             initialText.undraw()
             mainLoop(graphicsWindow)
             print("break on line 41 called")
             break 

def mainLoop(graphicsWindow):
    print("mainLoop called")
    box = ""
    timeToDisplay = Text(Point(50,25),"")
    timeToDisplay.setSize(36)
    timeToDisplay.draw(graphicsWindow)
    secondsSinceStart = 0 
    minutes = 0
    hours = 0
    timer = True
    ##Drawing static text
    secondsText = Text(Point(160,12),"Seconds")
    minutesText = Text(Point(100,12),"Minutes")
    hoursText = Text(Point(40,12),"Hours")
    secondsText.draw(graphicsWindow)
    minutesText.draw(graphicsWindow)
    hoursText.draw(graphicsWindow)
    x = True
    paused = False
    while timer== True:
        if paused == False:
            secondsSinceStart = secondsSinceStart + 1
            print(paused)
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
            box = checkBoxClicked(graphicsWindow,mouseClick,timeToDisplay)
            print("box86 ",box)
        if box == "reset":
            print("reset box pressed")
            resetMessage = Text(Point(100,100),"Time set to zero")
            resetMessage.draw(graphicsWindow)

            time.sleep(1) 
            resetMessage.undraw()
            secondsSinceStart = 0
        elif box == "pause":
            if paused == True:
                paused = False
            else:
                paused = True
            print("paused = ",paused)
              #  print("line 100",paused)
              #  box = ""
             ##   return(box)
              #  print("pause pressed")
              #  print("pause detected line 104")
              #  while paused == True:
              #      print("in pause loop")
              #      box = checkBoxClicked(graphicsWindow,mouseClick,timeToDisplay)
              #      print("In pause loop. box = ",box)
              #      if box == "pause":
              #          paused = False
              #          break #if pause is pressed again stop being paused
              #      else:
              #           print("Paused waiting for pause")
              #           print("asdisad box",box)
              #           time.sleep(1)
        elif box == "stop":
            print("Stop button Pressed")
            timer = False
            timeToDisplay.undraw()
            waitForStartClick(graphicsWindow)
        #if box == start ignore
        #return(box)

def checkBoxClicked(graphicsWindow,mouseClick,timeToDisplay):
    print("checkBoxClicked called")
    print("most recent mouse click:",mouseClick.getX(),mouseClick.getY())
    if mouseClick.getX()>10 and mouseClick.getX()<50 and mouseClick.getY()>150 and mouseClick.getY()<190:
        box = "start"
    elif mouseClick.getX()>60 and mouseClick.getX()<100 and mouseClick.getY()>150 and mouseClick.getY()<190:
        box = "pause"
    elif mouseClick.getX()>110 and mouseClick.getX()<150 and mouseClick.getY()>150 and mouseClick.getY()<190:
        box = "stop"
    elif mouseClick.getX()>160 and mouseClick.getX()<200 and mouseClick.getY()>150 and mouseClick.getY()<190:
        box = "reset"
    else:
        box = ""
        print("No box clicked")
    print("box line 129",box) 
    return(box)    #add a close box
    
def main():
    graphicsWindow = GraphWin("Stop Watch",200,200)
    drawIntialScreen(graphicsWindow)
    waitForStartClick(graphicsWindow) #should call main loop

#Calling main
main()
