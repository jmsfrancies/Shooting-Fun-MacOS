# You are welcome to write and include any other Python files you want or need
# however the game must be started by calling the main function in this file.
from graphics import *
import sys


def Ready(win, title, HowManyRounds):
    target_color = ["Blue", "Green", "Yellow", "Orange", "Red"]
    total = 0
#for loop that draws the target to shoot at!
    for i in reversed(range(35, 180, 35)):
        Target = Circle(Point(250, 250), i)
        Target.setFill("{0}".format(target_color[total]))
        Target.draw(win)
        total += 1

#for loop that draws each shot per mouse click
    for i in range(HowManyRounds):
        BulletHole = win.getMouse()
        x = BulletHole.getX()
        y = BulletHole.getY()
        BulletHole = Circle(Point(x, y), 4.5)
        BulletHole.setFill("black")
        BulletHole.setOutline("white")
        BulletHole.draw(win)


    title.setText("Great Shooting! Please Come Again!")
    win.getMouse()
    win.getMouse()
    win.close()


def main():
    win = GraphWin("The Shooting Range", 500, 500)
    win.setBackground("white")
    title = Text(Point(250, 25), """Welcome to The Shooting Range!
Where Precision and accuracy get further refined!""")
    title.setSize(14)
    title.setStyle("bold italic")
    title.draw(win)
    HowManyRounds = 15
    win.getMouse()
    Ready(win, title, HowManyRounds)


main()
