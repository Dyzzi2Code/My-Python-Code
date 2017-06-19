#Author: Cecelia Williams
#Last Revision: 02.05.2017
#Description: On a roulette wheel the pockets are numbered  from 0 - 36.
#The colors of the pockets are as follows:

# Pocket 0 is green
# For pockets 1 through 10, the odd-numbered pockets are red
#    and the even-numbered pockets are black

# For pockets 11 through 18, the odd-numbered pockets are black
#    and the even-numbered pockets are red

# For pockets 19 through 28, the odd-numbered pockets are red
#    and the even-numbered pockets are black

# For pockets 29 through 36, the odd-numbered pockets are black
#    and the even-numbered pockets are red

#Write a program that asks the user to enter a pocket number and displays
#whether the pocket is green, red, or black. The program should display
#an error message if the user enters a number that is outside the range of 0 - 36.


pocket = eval(input("Please choose a pocket from 0 to 36, and I will tell you its color.  "))
 
if pocket > 36:
    print("That is an invalid choice!! Please choose a pocket from 0 to 36!! ")
if pocket == 0:
    print("The pocket you chose is green")
elif pocket <= 10:
    if pocket % 2 == 0:
        print("The pocket you chose is black")
    else:
        print("The pocket you chose is red")
elif pocket > 10 and pocket < 19:
    if pocket % 2 == 0:
        print("The pocket you chose is red")
    else:
        print("The pocket you chose is black")
elif pocket > 18 and pocket < 29:
    if pocket % 2 == 0:
        print("The pocket you chose is black")
    else:
        print("The pocket you chose is red")
elif pocket > 28 and pocket < 37:
    if pocket % 2 == 0:
        print("The pocket you chose is red")
    else:
        print("The pocket you chose is black")


