#!/usr/bin/env python3
from datetime import datetime

# function to print the current time & task assigned
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'
print_time('first name assigned')

for x in range(0,10):
    print(x)
print_time('loop completed')

# function to get user initials
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')

last_name = input('Enter your last name: ')

print('your initials are: ' + get_initial(first_name) + get_initial(last_name))

# Function to get the area code of your number
def get_area_code(number):
    area_code = number[0:3]
    return area_code

phone_number = input('What is your phone number: ')

print('Your are code is: ' + get_area_code(phone_number))
