#Author: Cecelia Williams
#Last Revision: 04.26.2017
#Chapter 2 - 6 Vanity Plates
#Description -  This program will accept a plate request from the user
#and tell the user if the plate does or does not violate the rules below,
#and which rule (just the first one if more than one) the request violates.
#All characters must be letters or numbers (eg no spaces or punctuation marks)
#Minimum of 2 characters.
#Maximum of 6 characters.
#Must begin with two letters. 
#Cannot have letters and numbers intermixed (eg “MG53TD")
#Numbers must come at the end.
#First number cannot be 0 (zero).

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
punctuation = " ,./<>?':;[]\{}|-=_+)(*&^%$#@!`~"
vanity_plate = input("Enter your valid Vanity Plate: \n")

def make_vanity_plate(list1,list2,vanity_plate):
    if(len(vanity_plate) > 7 or len(vanity_plate) < 2):
        print("Too short to be valid")
        return 1
        print("Length of the plate has failed")
    if (vanity_plate[0] not in list1 or vanity_plate[1] not in list1):
        print("First 2 characters must be letters")
        return 1
        print("Beginning characters of the plate have failed")
    for i in range(2, len(vanity_plate)- 1):
        if(vanity_plate[i] in list2 and vanity_plate[i+1] in list1):
            print("You cannot mix the letters and numbers. Numbers must come at the end")
            return 1
           
                
    print("Thank you for using Mass Vanity License Plate")
    print("Your new vanity plate will arrive in 7 - 14 business days")
    return 0


result = make_vanity_plate(letters, numbers, vanity_plate)
if result == 0:
    print("Valid")
else:
    print("Invalid")
    




