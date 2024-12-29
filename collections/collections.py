#!/usr/bin/env python3

muhammad = {}
muhammad['first'] = 'Muhammad'
muhammad['last'] = 'Adeyemi'

ibrahim = {}
ibrahim['first'] = 'Ibrahim'
ibrahim['last'] = 'Abiodun'

people = []
people.append(muhammad)
people.append(ibrahim)
people.append({
    'first':'Warren', 'last':'Buffet'
})

print(people)