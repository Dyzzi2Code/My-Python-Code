#Write a function is_factor(f, n) that passes these tests:

#test(is_factor(3, 12))
#test(not is_factor(5, 12))
#test(is_factor(7, 14))
#test(not is_factor(7, 15))
#test(is_factor(1, 15))
#test(is_factor(15, 15))
#test(not is_factor(25, 15))

#An important role of unit tests is that they can also act as
#unambiguous “specifications” of what is expected.
#These test cases answer the question Do we treat 1 and 15 as factors of 15?

from math import sqrt #call up math function and imports the square root function

def is_factor(f, n):
    print("Enter the first number in the pair to test for factor:")
    f = float(input("first number: "))
    print("Enter the second number in the pair to test for factor:")
    n = float(input("second number: "))
    if n % f == 0:
        print(f, " and ", n, " ARE factors of each other.")
    else:
        print(f, " and ", n, " ARE NOT factors of each other.")


#tests
(is_factor(3, 12))
(not is_factor(5, 12))
(is_factor(7, 14))
(not is_factor(7, 15))
(is_factor(1, 15))
(is_factor(15, 15))
(not is_factor(25, 15))
