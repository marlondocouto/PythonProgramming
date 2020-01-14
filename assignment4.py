#wintery.py
#program displays a winter scene with a Xmas tree and a snowman

from graphics import *

def xmas():
    #setting up the GraphWin and the background:
    win=GraphWin("Winter Scene!",300,300)
    win.setBackground('cyan')
    win.setCoords(0.0,0.0,30.0,30.0)
    displaytext=Text(Point(15,1),"Winter Scene! - Marlon Do Couto")
    displaytext.setStyle('bold')
    displaytext.draw(win)
    
    """1 - Setting up the snowman with 3 larger circles"""
    
    #setting up first circle as the base of the snowman:
    p1=Point(9,10)
    circ=Circle(p1,7)
    circ.setFill('white')
    circ.setOutline('white')
    circ.draw(win)
    #setting up the second snowball:
    p2=p1.clone()
    p2.move(0,8)
    circ2=Circle(p2,4.5)
    circ2.setFill('white')
    circ2.setOutline('white')
    circ2.draw(win)
    #setting up last circle as the head of the snowman:
    p3=p2.clone()
    p3.move(0,6)
    circ3=Circle(p3,3)
    circ3.setFill('white')
    circ3.setOutline('white')
    circ3.draw(win)
    #setting up the eyes
    """p3 is set at coords(9,24) putting y-coords for circ3 at (9,27) through(9,21)
    eyes should be y~24"""
    p4=Point(8,25)
    Eye1=Circle(p4,0.5)
    Eye1.setFill('black')
    Eye1.draw(win)
    p5=p4.clone()
    p5.move(2,0)
    Eye2=Circle(p5,0.5)
    Eye2.setFill('black')
    Eye2.draw(win)
    #setting up the nose:
    nose1=Point(9,23.5)
    nose2=Point(9.25,24)
    nose3=Point(8.75,24)
    fullnose=Polygon(nose1,nose2,nose3)
    fullnose.setFill('orange')
    fullnose.setOutline('orange')
    fullnose.draw(win)
    #setting up black buttons on second snowball:
    button1=Circle(p2,0.5)
    button1.setFill('brown')
    button1.setOutline('brown')
    button1.draw(win)
    button2=button1.clone()
    button2.move(0,-2)
    button2.draw(win)
    button3=button1.clone()
    button3.move(0,2)
    button3.draw(win)

    """2 - setting up the Xmas tree with a rectangular base and 4 triangles"""
    
    #setting up the base of the tree:
    base=Rectangle(Point(22,2),Point(24,7))
    base.setFill('brown')
    base.setOutline('brown')
    base.draw(win)
    #setting up the tree body:
    triangle1=Polygon(Point(29,7),Point(17,7),Point(23,17))
    triangle1.setFill('green')
    triangle1.setOutline('green')
    triangle1.draw(win)

    triangle2=Polygon(Point(27.5,12),Point(18.5,12),Point(23,21))
    triangle2.setFill('green')
    triangle2.setOutline('green')
    triangle2.draw(win)

    triangle3=Polygon(Point(26.5,16),Point(19.5,16),Point(23,22))
    triangle3.setFill('green')
    triangle3.setOutline('green')
    triangle3.draw(win)

    triangle4=Polygon(Point(25.5,20),Point(20.5,20),Point(23,24))
    triangle4.setFill('green')
    triangle4.setOutline('green')
    triangle4.draw(win)

    """3 - Setting up the decorations on the tree"""

    #setting up the star at the top with four triangles:
    
    star1=Polygon(Point(24,24.5),Point(23,24.75),Point(23,24.25))
    star1.setFill('yellow')
    star1.setOutline('yellow')
    star1.draw(win)

    star2=Polygon(Point(22,24.5),Point(23,24.75),Point(23,24.25))
    star2.setFill('yellow')
    star2.setOutline('yellow')
    star2.draw(win)

    star3=Polygon(Point(23,23.5),Point(22.75,24.5),Point(23.25,24.5))
    star3.setFill('yellow')
    star3.setOutline('yellow')
    star3.draw(win)

    star4=Polygon(Point(23,25.5),Point(22.75,24.5),Point(23.25,24.5))
    star4.setFill('yellow')
    star4.setOutline('yellow')
    star4.draw(win)

    #setting up remaining decor:
    #lower row:
    p6=Point(23,7)
    ball=Circle(p6,.5)
    ball.setFill('yellow')
    ball.setOutline('yellow')
    ball.draw(win)

    ball2=ball.clone()
    ball2.move(5,0)
    ball2.draw(win)

    ball3=ball.clone()
    ball3.move(-5,0)
    ball3.draw(win)

    #2nd lower row:
    ball4=ball.clone()
    ball4.move(0,5)
    ball4.setFill('red')
    ball4.setOutline('red')
    ball4.draw(win)

    ball5=ball4.clone()
    ball5.move(-4,0)
    ball5.draw(win)
    ball6=ball4.clone()
    ball6.move(4,0)
    ball6.draw(win)

    #3rd lower row:
    ball7=ball4.clone()
    ball7.move(0,4)
    ball7.setFill('blue')
    ball7.setOutline('blue')
    ball7.draw(win)

    ball8=ball7.clone()
    ball8.move(3,0)
    ball8.draw(win)
    ball9=ball7.clone()
    ball9.move(-3,0)
    ball9.draw(win)

    #upper row:
    ball10=ball7.clone()
    ball10.move(0,4)
    ball10.setFill('orange')
    ball10.setOutline('orange')
    ball10.draw(win)

    ball11=ball10.clone()
    ball11.move(-2,0)
    ball11.draw(win)
    ball12=ball10.clone()
    ball12.move(2,0)
    ball12.draw(win)
    

xmas()
