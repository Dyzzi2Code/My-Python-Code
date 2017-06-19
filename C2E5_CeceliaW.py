#Author: Cecelia Williams
#Last Revision: 01.26.2017
#Description: Investment Calculator Chapter 2 Exercise 5

numberYears = eval(input("Please enter the number of years you would like to invest your money: "))
principalAmount = 10000.0
annualInterestRate = .08
interestCompoundPerYear = 12.0
earnedAmount = principalAmount * (1 + annualInterestRate / interestCompoundPerYear)**(interestCompoundPerYear * numberYears)
print("Your initial investment gave you a starting principal of $10,000.00 with an annual interest rate of 8% which is compounded every month.")
print(earnedAmount)
