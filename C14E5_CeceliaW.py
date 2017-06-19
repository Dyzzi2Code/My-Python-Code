#Author: Cecelia Williams
#Last Revision: 04.14.2017
#Description: Chapter 14 Exercise 5

import random
import math
##########################   TICKET LISTS   ##########################
your_ticket = [12, 25, 16, 22, 38, 42]

my_tickets = [ [ 7, 17, 37, 19, 23, 43],      
               [ 7,  2, 13, 41, 31, 43],      
               [ 2,  5,  7, 11, 13, 17],      
               [13, 17, 37, 19, 23, 43] ]     

tonights_lotto = []

prime_nums = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

#######################################################################

#   a- Each lotto draw takes six random balls, numbered from 1 to 49.
#   Write a function to return a lotto draw.
def make_random_ints_no_dups(num, lower_bound, upper_bound):
   """
     Generate a list containing num random ints between
     lower_bound and upper_bound. upper_bound is an open bound.
     The result list cannot contain duplicates.
   """
   result = []
   rng = random.Random()
   for i in range(num):
        while True:
            ball = rng.randrange(lower_bound, upper_bound)
            if ball not in result:
                break
        result.append(ball)
   return result

#######################################################################

#   b- Write a function that compares a single ticket and a draw,
#   and returns the number of correct picks on that ticket:
def lotto_match(tonights_lotto, your_ticket):
    matched = 0
    for i in your_ticket:
        for j in tonights_lotto:
            if i == j:
               matched += 1
               print(("Matched Number(s): "),(j))
               print("Total number of matches on your_ticket: ")
    return(matched)
    
#######################################################################

#   c- Write a function that takes a list of tickets and a draw,
#   and returns a list telling how many picks were correct on each ticket:
def lotto_matches(my_tickets, tonights_lotto):
    matches = 0
    matched = []
    ticket = 0
    for element in my_tickets:
        ticket += 1
        print(("Ticket number "),(ticket),(": "),(element))
        for i in element:
            for j in tonights_lotto:
                matched = 0
                if i == j:
                    matches += 1
                    matched += 1
                    print(("Matched Number(s): "),(j))
                    print(("Number of Matches: "),(matched))      
    print("Total number of matches through all of my_tickets: ")
    return(matches)

#######################################################################

#   d- Write a function that takes a list of integers,
#   and returns the number of primes in the list:
def primes_in(first_list,second_list):
   count = 0
   for i in first_list:
      if i in second_list:
         count += 1
         
   return(count)

#######################################################################
   
#  e- Write a function to discover whether the computer scientist
#  has missed any prime numbers in her selection of the four tickets.
#  Return a list of all primes that she has missed:
def prime_misses(first_list,second_list):
   ticket_picks = []
   picks_fixed = []
   primes_not_used = []
   ticket_picks = [item for sublist in second_list for item in sublist]
   list.sort(ticket_picks)
   for i in ticket_picks:
      if i not in picks_fixed:
         picks_fixed.append(i)
   for i in prime_nums:
      if i not in picks_fixed:
         primes_not_used.append(i)
   return primes_not_used




##########################   MAIN  FUNCTION   ##########################
def main():
   print("Exercise 5.A")
   tonights_lotto = make_random_ints_no_dups(6, 1, 49)
   print("This is tonights lotto draw: ")
   print(tonights_lotto)
   print()
   print("Exercise 5.B")
   print("Comparing your ticket to tonights draw,")
   print(("Your ticket had the following numbers: "),(your_ticket))
   print(lotto_match(tonights_lotto, your_ticket))
   print()
   print("Exercise 5.C")
   print("Comparing my tickets to tonights draw,")    
   print(lotto_matches(my_tickets,tonights_lotto))
   print()
   print("Exercise 5.D")
   print("Prime numbers 1 - 49 are as follows: ")
   print(prime_nums)
   print()
   print("Quantity of prime numbers in tonights lotto draw are: ")
   print(primes_in(tonights_lotto, prime_nums))
   print()
   print("Quantity of prime numbers in your ticket are: ")
   print(primes_in(your_ticket, prime_nums))
   print()
   print("Exercise 5.E")
   print("Prime numbers missed on all of my tickets are: ")
   print(prime_misses(prime_nums,my_tickets))
   


main()







            
