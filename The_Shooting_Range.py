# You are welcome to write and include any other Python files you want or need
# however your game must be started by calling the main function in this file.
from graphics import *
import sys

def Ready(win,title,HowManyRounds,WhatCaliber):
  total = 0
  target_color = ["Blue","Green","Yellow","Orange","Red"]
  for i in reversed(range(30,171,35)):
        Target = Circle(Point(250,250),i)
        Target.setFill("{0}".format(target_color[total]))
        Target.draw(win)
        total = total + 1
        
  

  if int(HowManyRounds) >= 1:
    for i in range(HowManyRounds):
        if WhatCaliber == 1:    
            BulletHole = win.getMouse()
            x = BulletHole.getX()
            y = BulletHole.getY()
            BulletHole = Circle(Point(x,y),2.5)
            BulletHole.setFill("black")
            BulletHole.setOutline("white")
            BulletHole.draw(win)



      
    title.setText("Great Shooting! Please Come Again!")
    win.getMouse()
    win.getMouse()
    win.close()


def main():
    win = GraphWin("The Shooting Range",500,500)
    win.setBackground("white")
    title = Text(Point(250,25),"""Welcome to The Machine Gun Shooting Range!
Where Precision and accuracy get further refined!""")
    title.setSize(20)
    title.setStyle("bold italic")
    title.draw(win)
    HowManyRounds = 30
    WhatCaliber = 1
    win.getMouse()
    Ready(win,title,HowManyRounds,WhatCaliber)
 
main()