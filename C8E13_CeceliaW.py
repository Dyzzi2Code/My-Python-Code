#Author: Cecelia Williams
#Last Revision: 03.04.2017
#Description: Chapter 8 Exercise 13
#Write a function that removes all occurrences of a string from another string

def remove(sub_string,orig_string):
    #   Return the lowest index in the string where substring sub is found
    location = orig_string.find(sub_string)
    if location < 0:
        return orig_string
    #   Remove sub_string first instance and concatinate the remainder of string 
    new_string = orig_string[:location] + orig_string[location+len(sub_string):]
    return new_string


print(remove('an', 'banana'))
print(remove('cyc', 'bicycle'))
print(remove('iss', 'Mississippi'))
print(remove('egg', 'bicycle'))


def remove_all(sub_string,orig_string):
    parent_string = orig_string
    while parent_string:
        #   Call remove() to remove all instances of sub_string
        if remove(sub_string,parent_string) == parent_string:
            return remove(sub_string,parent_string)
        else:
            parent_string = remove(sub_string,parent_string)

print(remove_all('an', 'banana'))
print(remove_all('cyc', 'bicycle'))
print(remove_all('iss', 'Mississippi'))
print(remove_all('egg', 'bicycle'))







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
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")

test_suite()




