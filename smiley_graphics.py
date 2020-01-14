#smiley_graphic.py
#example of clone from page 95
from graphics import *

leftEye = Circle(Point(100,50),5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
win=GraphWin()
leftEye.draw(win)

#cloning leftEye into a rightEye:

rightEye=leftEye.clone()
rightEye.move(20,0)
rightEye.draw(win)
