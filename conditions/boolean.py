#!/usr/bin/env python3

# Asking user for gpa & lowest grade to see if they made honour roll
gpa = float(input('What is your GPA? '))
lowest_grade = float(input('What is your lowest grade? '))

if gpa >=.85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False


if honour_roll:
    print('Congrats, you\'ve made the hounot roll!')
else:
    print('You didn\'t quite make the honour roll, keep trying,& keep up the great work!')