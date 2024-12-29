#!/usr/bin/env python3

# calculate tax price
price = input('What is your totale price? ')
price =float(price)

if price >= 1.00:
    tax = 0.0825
else:
    tax = 0

price = price + (price * tax)
print('Your total price is: ' + str(price))


# country
print()
country = input('What is your home country? ')

if country.lower() == 'usa':
    print('You\'re American, you must love Amaerican basketball & football.')
else:
    print('You\'re a foreigner, you must be familiar with traditional football.')