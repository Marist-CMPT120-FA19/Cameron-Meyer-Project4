from graphics import *
def main():
	win= GraphWin()
	b=Rectangle(Point(50,20),Point(150,175))
	b.setFill("black")
	b.draw(win)
	r= Circle(Point(100,50),20)
	r.setFill("red")
	r.draw(win)
	y= Circle(Point(100,100),20)
	y.setFill("yellow")
	y.draw(win)
	g= Circle(Point(100,150),20)
	g.setFill("green")
	g.draw(win)


main()


