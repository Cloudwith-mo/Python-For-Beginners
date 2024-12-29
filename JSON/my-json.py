#!/usr/bin/env python3
import json

# creat dict
person_dict = {'first':'Muhammad', 'middle':'Kolawole'}
# Add additional key pais to dictionary as needed
person_dict['last'] = ['Adeyemi']

# create json with nested dict 
staff_dict = {}
staff_dict['Program Manager'] = person_dict 

# create list object and add it to the dictionary
language_list = ['JS', 'Pyhton', 'HTML', 'CSS']
person_dict['languages'] = language_list


# Convert dictionary to json
person_json = json.dumps(person_dict)
peopkle_json = json.dumps(staff_dict)

# Print json object 
print(person_json)
print(staff_dict)
