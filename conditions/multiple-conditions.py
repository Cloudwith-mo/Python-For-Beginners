#!/usr/bin/env python3

# example of using multiple conditions (nested)

country = input('What country do you live in? ')

if country.lower() == 'canada':

    province = input('What province do you line in?')
    if province.lower() in('alberta', 'nunavut', 'yukon'):
        tax = 0.05
    elif province.lower() == 'ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0  

print('Your tax rate is: ' + str(tax) + '%')

