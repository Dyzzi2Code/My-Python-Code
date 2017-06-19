#Author: Cecelia Williams
#Last Revision: 04.01.2017
#Description:  Chapter 13 Exercise 3

#Write a program that reads a text file and produces an output file
#which is a copy of the file, except the first five columns of each
#line contain a four digit line number, followed by a space. Start
#numbering the first line in the output file at 1. Ensure that every
#line number is formatted to the same width in the output file. Use
#one of your Python programs as test data for this exercise: your
#output should be a printed and numbered listing of the Python program.

if __name__ == '__main__':
    pass

def add_line_number(originalfile, newfile):
    oldfilehandle = open(originalfile, "r")
    newfilehandle = open(newfile, "w")
    linecount = 1001
    while True:
        originalline = oldfilehandle.readline()
        if len(originalline) == 0:
            break
        newline = "{0:>4}".format(str(linecount)) + " " + originalline
        newfilehandle.write(newline)
        linecount += 1
    oldfilehandle.close()
    newfilehandle.close()
       
add_line_number("list.txt", "newList.txt")
