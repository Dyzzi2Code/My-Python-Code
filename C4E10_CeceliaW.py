#Author: Cecelia Williams
#Last Revision: 02.04.2017
#Description:Write a void function to draw a star, where the length of each side is 100 units.
#(Hint: You should turn the turtle by 144 degrees at each point.)
#Extend your program above. Draw five stars, but between each,
#pick up the pen, move forward by 350 units, turn right by 144,
#put the pen down, and draw the next star. You’ll get something like this:
#Chapter 4 Exercise 10

import turtle

def drawFivePointStar(c):           #define the function with only 1 parameter
    for i in range(5):              #for loop to make the pen turn its angels to make the star
        c.pensize(3)                #Pen line size
        c.color("magenta")          #Color of pen ink
        c.forward(100)              #print line while moving forward 100 pixels
        c.left(144)                 #turn the pen 144 degrees 

wn = turtle.Screen()                #creates a window with turtle attributes
wn.bgcolor("purple")                #gives the windows background the color teal


cece = turtle.Turtle()              #Creates my instance of the turtle who completes this task
for i in range(5):                  #For loop to make the the circle of 5 stars
    drawFivePointStar(cece)         #Calls the function to write the stars
    cece.penup()                    #picks up the pen to stop writing
    cece.forward(350)               #moves forward 350 pixels
    cece.right(144)                 #turn right 144 degrees
    cece.pendown()                  #put the pen down

wn.mainloop()
    
