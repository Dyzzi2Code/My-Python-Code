#Author: Cecelia Williams
#Last Revision: 03.4.2017
#Description: Chapter 8 Exercise 10

#Write a function that recognizes palindromes.
#(Hint: use your reverse function to make this easy!):

#word = "banana"
word = "abba"
#word = "tenet"
#word = "straw warts"
#word = "a"

#string[start:stop:step]


def reverse(word):
    rev_string = word[::-1]
    return rev_string


print(reverse(word))

def is_palindrome(word):
    is_palindrome = True
    if word == reverse(word):
        is_palindrome = True
        print("string is a palindrome")
    else:
        is_palindrome = False
        print("String is not a palindrome")
    return is_palindrome
        



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
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    # test(is_palindrome(""))    # Is an empty string a palindrome?

test_suite()
