# You are welcome to write and include any other Python files you want or need
# however your game must be started by calling the main function in this file.
from graphics import *
import sys
#from button import *


def Ready():
  win = GraphWin("Top Shot Shooting Range",500,500)
  win.setBackground("white")
  title = Text(Point(250,25),"Ready, Aim, Fire!")
  title.setSize(20)
  title.setStyle("bold italic")
  title.draw(win)
  Target_1 = Circle(Point(250,250),170)
  Target_2 = Circle(Point(250,250),135)
  Target_3 = Circle(Point(250,250),100)
  Target_4 = Circle(Point(250,250),65)
  Target_5 = Circle(Point(250,250),30)
  Target_1.setFill("blue")
  Target_2.setFill("Green")
  Target_3.setFill("grey")
  Target_4.setFill("yellow")
  Target_5.setFill("Red")
  Target_1.draw(win)
  Target_2.draw(win)
  Target_3.draw(win)
  Target_4.draw(win)
  Target_5.draw(win)
  win.getMouse()
  HowManyRounds = int(input("Enter the number of shots that you would like to take at the target: "))
  WhatCaliber = input("What Caliber Firearm would you like to use ( 9mm (1), .45 acp (2), 50 AE (3))?")
  total = 0
  if WhatCaliber != "1" and WhatCaliber != "2" and WhatCaliber != "3":
      print("Caliber is Not Available!")
      win.getMouse()
      win.close()
  if HowManyRounds >= 1:
    while total < HowManyRounds:
        if WhatCaliber == "1":    
            BulletHole = win.getMouse()
            x = BulletHole.getX()
            y = BulletHole.getY()
            BulletHole = Circle(Point(x,y),2.5)
            BulletHole.setFill("black")
            BulletHole.setOutline("white")
            BulletHole.draw(win)
            total = total + 1
        if WhatCaliber == "2":    
            BulletHole = win.getMouse()
            x = BulletHole.getX()
            y = BulletHole.getY()
            BulletHole = Circle(Point(x,y),4)
            BulletHole.setFill("black")
            BulletHole.setOutline("white")
            BulletHole.draw(win)
            total = total + 1
        if WhatCaliber == "3":    
            BulletHole = win.getMouse()
            x = BulletHole.getX()
            y = BulletHole.getY()
            BulletHole = Circle(Point(x,y),5.5)
            BulletHole.setFill("black")
            BulletHole.setOutline("white")
            BulletHole.draw(win)
            total = total + 1   
        else:
            title.setText("Great Shooting! Please Come Again!")
            win.getMouse()
            win.getMouse()
            win.close()


def main():
  print("""Welcome to The Top Shot Shooting Range!
Where Precision and accuracy get further refined!""")
  wannashoot = input("Would you Like to Shoot (y/n)? ")   
  if wannashoot == "y":
      Ready()
  else:
      print("Have a great day!")
 
main()