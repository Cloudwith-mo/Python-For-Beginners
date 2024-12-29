#!/usr/bin/env python3

# datetime library, to get date
from datetime import datetime, timedelta

# today's' date
today = datetime.now()

# the now function returns a datetime object
print('Today is: ' + str(today))

# time delta is used to define a period (yesterday)
print()
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# last week
print()
one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))

# day, month, year
print()
print('Days: ' + str(today.day))
print('Month: ' + str(today.month))
print('Yearys: ' + str(today.year))
# hour, min, sec
print('Hours: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('second: ' + str(today.second))

# birthday
print()
bday = input('When is your birthday (dd/mm/yyyy)?')
bday = datetime.strptime(bday, '%d/%m/%Y')
print('Birthday: ' + str(bday))

# birthday eve
print()
one_day = timedelta(days=1)
bday_eve = bday - one_day
print('Day before birthday: ' + str(bday_eve))

# age in years
print()
print('You are ' + str(today.year - bday.year) + ' years old!')