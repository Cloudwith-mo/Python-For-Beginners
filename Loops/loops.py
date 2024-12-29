#!/usr/bin/env python3

# Loop through a collection
people = ['Muhammad', 'Ibrahim']

for name in people:
    print(name)

print()

# Looping a number of times
for index in range(0,2):
    print(index)

print()

# Looping with a condition
names = ['Muhammad', 'Kolawole', 'Adeyemi']
index = 0
while index<len(names):
    print(names[index])
    # Change the condition
    index = index + 1

print()