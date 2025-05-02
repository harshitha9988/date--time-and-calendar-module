import random
import time

def getRandomDate(startDate, endDate):
    print("printing a random date between", startDate, "and", endDate)

    x=random.random()
    y='%m/%d/%Y'

    startTime=time.mktime(time.strptime(startDate, y))
    endTime=time.mktime(time.strptime(endDate, y))

    randomTime=startTime+x*(endTime-startTime)
    randomDate=time.strftime(y,time.localtime(randomTime))
    return randomDate

print("Random Date = ", getRandomDate("1/1/2013", "12/12/2026"))
