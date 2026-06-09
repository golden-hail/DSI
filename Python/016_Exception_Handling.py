# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:14:19 2026

@author: aiaqu
"""

age = int(input("Enter your age: "))

try:
    age = int(input("Enter your age: "))
    print(age)
except:
    print("Not a valid input, please try again")

'''
### Error examples
print(some_object)

my_list = [1,2]
my_list[4]

"a" + 5
int("Python")

3/0
'''

### GOOD FOR DEBUGGING

# print hand written error
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Not a valid input, please try again")

# more hints on error (actual mech error)
try:
    age = int(input("Enter your age: "))
    print(age)
except NameError:
    print("Not a valid input, please try again")
    
# output specific error type with message
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError as error_type:
    print(f"Not a valid input {error_type}, please try again")
    
# can point to an error log :O
