from graphics import *
import random
from time import sleep


#creates window 
windowSize = GraphWin("Grade Visualisation", 500, 500)
windowSize.setBackground(color_rgb(255,255,255))
while True:
    with open('grades.txt','r+') as marks:
        for line in marks:
            for grades in line.split():
                print(grades)
                
                square = Rectangle(Point(0, 0), Point(500,500))
                square.setOutline(color_rgb(255,255,255))
                square.setFill(color_rgb(255,255,255))
                square.draw(windowSize)
                square = Rectangle(Point(grades*2,grades*2),Point(grades, grades))
                square.setOutline(color_rgb(0,0,0))
                square.draw(windowSize)
                text = Text(Point(200,200), grades)
                text.draw(windowSize)
        
                sleep(0.2)
   