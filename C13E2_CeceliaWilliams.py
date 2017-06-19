#Author: Cecelia Williams
#Last Revision: 04.01.2017
#Description:  Chapter 13 Exercise 2

#Write a program that reads a file and prints only those lines
#that contain the substring snake.

with open("Snakes.txt") as file:
    for line in file:
        if "snakes" in line:
            print(line.split())
