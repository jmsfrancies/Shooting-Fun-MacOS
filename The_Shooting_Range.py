# You are welcome to write and include any other Python files you want or need
# however the game must be started by calling the main function in this file.
from graphics import *
import sys

def shooting(win,title,HowManyRounds):
    title.setText("Ready, Aim, Fire!")
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

def Ready(win, title, HowManyRounds):
    target_color = ["Blue", "Green", "Yellow", "Orange", "Red"]
    total = 0
#for loop that draws the target to shoot at!
    for i in reversed(range(35, 180, 35)):
        Target = Circle(Point(250, 250), i)
        Target.setFill("{0}".format(target_color[total]))
        Target.draw(win)
        total += 1
        
    title.setText("Cock your action! ")
    win.getMouse()
    

"""Function that starts the graphics window, demands the amount shooting that the user wants to perform,
and starts the ready function, and shooting function within the program."""

def main():
    win = GraphWin("The Shooting Range", 500, 500)
    win.setBackground("white")
    title = Text(Point(250, 25), """Welcome to The Shooting Range!
Where Precision and accuracy get further refined!""")
    title.setSize(14)
    title.setStyle("bold italic")
    title.draw(win)
    Text(Point(200,200), "How Many Rounds: ").draw(win)
    rounds = Entry(Point(300,200),5)
    rounds.setText("")
    rounds.draw(win)
    win.getMouse()
    HowManyRounds = int(rounds.getText())
    rounds.undraw()
    Ready(win, title, HowManyRounds)
    shooting(win,title,HowManyRounds)

main()
