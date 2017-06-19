#Author: Cecelia Williams
#Last Revision: 02.05.2017
#Description: Ask the user for the time now (in hours),
#and ask for the number of hours to wait.
#Your program should output what the time will be on the clock
#when the alarm goes off.

currentTime = eval(input("What is the current time in military hours? "))
#1400                   #1300
hoursToWait = eval(input("How many hours should we wait before we go  ? "))
#22                     #12
hours = hoursToWait * 100                       #convert hours to military hours
timeToGo = ((hours % 2400) + currentTime)       #
if timeToGo > 2400:
    totalHours = hours + currentTime              #add converted hours to wait to the current time
    daysAway = totalHours // 2400                     #calculate number of days away if any
    alarmTime = timeToGo % 2400
    timeToGo = 0000
    timeToGo = alarmTime + timeToGo
else:
    timeToGo = hours + currentTime              #add converted hours to wait to the current time


print("We will be going home in ",daysAway ," days at ",timeToGo ," hours.")  #Print when we will be going home

#hoursToWait cannot be over 95 why????????
