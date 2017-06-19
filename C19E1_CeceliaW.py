#Author: Cecelia Williams
#Last Revision: 04.30.2017
#Description: Chapter 19 Exercise 1

"""
    Write a function named readposint that uses the input dialog to prompt the
    user for a positive integer and then checks the input to confirm that it
    meets the requirements. It should be able to handle inputs that cannot be
    converted to int, as well as negative ints, and edge cases (e.g. when the
    user closes the dialog, or does not enter anything at all.)"""

def readposint(user_input):
    if user_input < 0:
        print("This is a negative number!!!!")
        return False
    elif user_input > 0:
        print("Your POSITIVE!!!!")
        return True

    return

user_input = eval(input("Enter a positive number: "))

print(readposint(user_input))
print(readposint(-5))
print(readposint(50))
        















import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():  #have to add the def of "test_suite()"
    test(readposint(2) == True)
    test(readposint(-9) == False)
    test(readposint(54) == True)

test_suite()
