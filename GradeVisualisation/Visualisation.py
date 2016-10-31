from graphics import *
import random
from time import sleep

#creates window 
windowSize = GraphWin("Grade Visualisation", 500, 500)
windowSize.setBackground(color_rgb(255,255,255))

#makes a red circle
def red():
  circle = Circle(Point(x,y), int(grades))
  circle.setFill(color_rgb(255,0,0))
  circle.draw(windowSize)
                    
  gradeText = Text(Point(x,y), grades)
  gradeText.draw(windowSize)

#makes a green circle  
def green():
  circle = Circle(Point(x,y), int(grades))
  circle.setFill(color_rgb(0,255,0))
  circle.draw(windowSize)
                    
  gradeText = Text(Point(x,y), grades)
  gradeText.draw(windowSize)

#makes an orange circle
def orange():
  circle = Circle(Point(x,y), int(grades))
  circle.setFill(color_rgb(255,165,0))
  circle.draw(windowSize)
                    
  gradeText = Text(Point(x,y), grades)
  gradeText.draw(windowSize)

#Opens text file and reads grades in
while True:
    with open('grades.txt','r+') as marks:
        for line in marks:
            for grades in line.split():
                print(grades)

                #Places circle randomly in the window
                x = random.randrange(0,500)
                y = random.randrange(0,500)

                #Depending on grade, different colour circles representing good or bad grades
                if int(grades) >= int(60):
                    green()

                elif int(grades) >= int(50):
                    orange()
                
                elif int(grades) <= int(49):
                    red()    
                
                sleep(0.1)
   
