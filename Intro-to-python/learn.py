#!/usr/bin/env python3

# print('Hellor world')

# name=input('Please enter your name: ')
# print('\nYour name is: '+name)

first_name = input('What is you first name?: ')
last_name = input('What is your last name?: ')
fav_book = input('What is your favorite book?: ')

#print('Hello, ' + first_name.capitalize() + ' ' + last_name.capitalize() + '. ' \
 #     + fav_book.capitalize() + ' is an awesome book!')

output = f'Hello, {first_name} {last_name}. {fav_book} is an awesome book!'
print(output)