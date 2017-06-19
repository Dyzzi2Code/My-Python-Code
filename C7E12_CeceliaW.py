#Author: Cecelia Williams
#Last Revision: 02.18.2017
#Description: Chapter 7 Exercise 12
               
import turtle

wn = turtle.Screen()            #Sets up the window with its attributes
wn.bgcolor("lightpink")
cece = turtle.Turtle()

draw = [(50, 90), (50, 90), (50, 90), (50, 135), (72, 90), (35, 90), (35, 90), (72,0)]

def drawHouse():

    for x, y in draw:
        cece.pensize(3)
        cece.color("black")
        cece.forward(x)
        cece.left(y)

drawHouse() 
wn.mainloop()

