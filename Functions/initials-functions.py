#!/usr/bin/env python3


# function to get user initials
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')

last_name = input('Enter your last name: ')

print('your initials are: ' + get_initial(name = first_name, force_uppercase = True) + get_initial(last_name, True)) 