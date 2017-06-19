#Write a function called hypotenuse that returns the length of the hypotenuse
#of a right triangle given the lengths of the two legs as parameters:
#test(hypotenuse(3, 4) == 5.0)
#test(hypotenuse(12, 5) == 13.0)
#test(hypotenuse(24, 7) == 25.0)
#test(hypotenuse(9, 12) == 15.0)

from math import sqrt #call up math function and imports the square root function

def hypotenuse(shortest, nextShortest):
    print("Enter the length of the shortest side of the triangle:")
    shortest = float(input("shortest length: "))
    print("Enter the length of the next shortest side of the triangle:")
    nextShortest = float(input("next shortest length: "))

    hypotenuse = sqrt(shortest**2 + nextShortest**2)
    print("The length of the hypotenuse is", hypotenuse )
    return 0.0


(hypotenuse(3, 4) == 5.0)
(hypotenuse(12, 5) == 13.0)
(hypotenuse(24, 7) == 25.0)
(hypotenuse(9, 12) == 15.0)
