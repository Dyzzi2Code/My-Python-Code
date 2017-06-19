import turtle
wn = turtle.Screen()            #Sets up the window with its attributes
wn.bgcolor("lightpink")         #Sets the window's background color

cece = turtle.Turtle()          #Creates my turtle
cece.shape("turtle")            #Gives my turtle its shape
cece.color("black")             #The starting turtle color is black
cece.stamp()                    #Prints the black turtle

move = 30                       #Sets the first move to be 30 degrees 
for i in range(12):             #For loop to iterate through the twelve hours of the clock
    cece.penup()                #Lift the pen to stop writing
    cece.forward(60)            #Move forward 60 pixels
    cece.pendown()              #Put the pen down to write
    cece.color("purple")        #Sets all of the lines to be purple in color
    cece.forward(30)            #Move forward writing the line which is 30 pixels long
    cece.penup()                #Lift the pen to stop writing
    cece.forward(15)            #Move forward 15 pixels
    cece.color("hotpink")       #Sets all of the Turtles to be hot pink in color
    cece.stamp()                #Prints the hot pink turtle
    cece.color("red")           #Sets the controlling turtle to red 
    cece.home()                 #Returns the controlling turtle to the begining position in the center with current degree status
    cece.right(move)            #Rotates the controlling turtle to the right 
    move = move + 30            #Sets each additional turtle to be 30 degrees apart from the last

wn.mainloop()                   #End the program
    

