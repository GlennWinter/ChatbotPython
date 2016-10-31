from graphics import *
import random
from time import sleep


#creates window 
windowSize = GraphWin("Grade Visualisation", 500, 500)
windowSize.setBackground(color_rgb(255,255,255))

red = ([255,0,0])
green = ([0,255,0])
blue = ([0,0,255])
#int = grades

blue = color_rgb(0,0,255)
red = color_rgb(255,0,0)
green = color_rgb(0,255,0)
purple = color_rgb(255,255,0)
yellow = color_rgb(0,255,255)
lightblue = color_rgb(255,0,255)
white = color_rgb(255,255,255)
black = color_rgb(0,0,0)

colour = [blue, red, green, purple, yellow, lightblue, white, black]

while True:
    with open('grades.txt','r+') as marks:
        for line in marks:
            for grades in line.split():
                print(grades)
                
                x = random.randrange(0,500)
                y = random.randrange(0,500)
                
                ball = Circle(Point(x,y), int(grades))
                ball.setFill(random.choice(colour))
                ball.draw(windowSize)
                
             #   poly = Polygon(Point(grades*2, grades),
                 #              Point(grades, grades),
                  #             Point(grades, grades))
                #              # Point(grades, grades),
                              # Point(grades, grades),
                              # Point(grades, grades))
               
                
              #  poly.setFill(color_rgb(255,0,0))
            #    poly.setWidth(100)
                #poly.setOutline(color_rgb(0,0,255))
                
              #  poly.draw(windowSize)
                
                
                
           #     square = Rectangle(Point(grades*2,grades*2), Point(grades, grades))
          #      square.setOutline(color_rgb(255,255,255))
            #    square.setFill(color_rgb(255,0,0))
             #   square.draw(windowSize)
                
                
                #square = Rectangle(Point(grades*2,grades*2),Point(grades, grades))
                #square.setOutline(color_rgb(0,0,0))
                #square.draw(windowSize)
               # text = Text(Point(200,200), grades)
                #setText
                #text.draw(windowSize)
                
        
                sleep(0.1)
   
