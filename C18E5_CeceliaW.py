#Author: Cecelia Williams
#Last Revision: 04.30.2017
#Description: Chapter 18 Exercise 5

"""Write a function, recursive_min, that returns the
smallest value in a nested number list. Assume there are no
empty lists or sublists:"""
xs1 = ([2, 9, [1, 13], 8, 6])
xs2 = ([2, [[100, 1], 90], [10, 13], 8, 6])
xs3 = ([2, [[13, -7], 90], [1, 100], 8, 6])
xs4 = ([[13, 7], 90, -2, [1, 100], 8, 6])

def recursive_min(num_list):
    return low_num(num_list[1:], num_list[0]) if num_list else None

def low_num(num_list, min_num):
    """ Takes in a list of numbers, finds the minimum number """
    if not num_list:
        return min_num
    elif not isinstance(num_list, list):
        return min(num_list, min_num)
    else:
        return min(low_num(num_list[0],min_num),
                   low_num(num_list[1:],min_num))



print(xs1)
print("The minimum number was:")
print(recursive_min(xs1))
print(xs2)
print("The minimum number was:")
print(recursive_min(xs2))
print(xs3)
print("The minimum number was:")
print(recursive_min(xs3))
#print(xs4)
#print("The minimum number was:")
#print(recursive_min(xs4))


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
    test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    test(recursive_min(xs1) == 1)
    test(recursive_min([2, [[100, 1], 90],[10, 13], 8, 6]) == 1)
    test(recursive_min(xs2) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min(xs3) == -7)
    #test(recursive_min([[13, 7], 90, -2, [1, 100], 8, 6]) == -2)
    #test(recursive_min(xs4) == -2)

test_suite()
