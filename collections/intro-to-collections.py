#!/usr/bin/env python3
 
# List are collections of items
names = ['Muhammad', 'Kolawole']
scores = []
scores.append(98) #add item to the end
scores.append(99)

print(names)
print(scores)
print(scores[1])

# Arrays are also a collection items
from array import array
scores = array('d')
print()
print(scores)

scores.append(97)
scores.append(96)

print()
print(scores)
print(scores[1])

# Common operations
print()
brands = ['Nike', 'Jordan']
print(len(brands)) # number of items

brands.insert(0, 'Adidas') #insert before index
brands.insert(1, 'Reebok')
print(brands)

brands.sort() #sort in alphabetical order or least to greatest.
print(brands)

top_brands = brands[1:3] #Retrieving ranges
print(top_brands)

# Dictionaries
person = {'first': 'Mo'}
person['middle'] = 'Kolawole'
print()
print(person)
print(person['first'])