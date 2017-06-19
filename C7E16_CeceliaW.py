#Author: Cecelia Williams
#Last Revision: 02.19.2017
#Description: Chapter 7 Exercise 16

#Write a function sum_of_squares(xs) that computes the sum
#of the squares of the numbers in the list xs.
#For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
#test(sum_of_squares([2, 3, 4]) == 29)
#test(sum_of_squares([ ]) == 0)
#test(sum_of_squares([2, -3, 4]) == 29)

import sys
import random
#xs = ([2,-3,4])#brackets on inside of parenthesis
#xs = []
#xs = ([2,3,4])
#xs = []

#give 3 numbers randomly to compute square sums
#for i in range(3):
#    xs.append(random.randint(0,10))
    
    
def sum_of_squares(xs):
    sum_of_squares = 0 #initialize to 0 to make sure memory slot it empty
    print(xs)
    for i in (xs):
        number_sqrd = i * i
        sum_of_squares += number_sqrd
    return sum_of_squares

#print (sum_of_squares(xs))



def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():  #have to add the def of "test_suite()"
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)

test_suite()

