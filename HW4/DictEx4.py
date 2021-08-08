#Exercise 4: Initialize dictionary with default values
#Given:
from pprint import pprint
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

dict1 = dict.fromkeys(employees, defaults)
pprint(dict1)

