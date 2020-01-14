#assignment_7
#Author: Marlon Do Couto
#Program to create smileys using functions

from graphics import *

#defining the window function with window=graphwin
    
def window():
    window =GraphWin("face")
    window.setBackground("grey")
    window.setCoords(0.0,0.0,50,50)
    return window

#defining the drawing of the circle at the window function:

def drawcircle(window,x,y,radius):
    shape=Circle(Point(x,y),radius)
    shape.setFill('yellow')
    shape.setOutline('yellow')
    shape.draw(window)

#defining the main function to connect the two functions:

def main():
    win=window()
    drawcircle(win,5,5,5)
    drawcircle(win,25,25,10)
    drawcircle(win,40,40,5)

main()
    
    
