#Author: Cecelia Williams
#Last Revision: 04.30.2017
#Description: Chapter 18 Exercise 7


""" Write a function flatten that returns a simple list
    containing all the values in a nested list:"""
def flatten(my_list_of_lists):
    return sum(([x] if not isinstance(x, list)else flatten(x)
                for x in my_list_of_lists), [])

print(flatten([2,9,[2,1,13,2],8,[2,6]]))
print(flatten([[9,[7,1,13,2],8],[7,6]]))
print(flatten([[9,[7,1,13,2],8],[2,6]]))
print(flatten([[9,[7,1,13,2],8],[2,6]]))
print(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]))




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
    test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
    test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
    test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
    test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
                  ["this","a","thing","a","is","a","easy"])
    test(flatten([]) == [])

test_suite()
