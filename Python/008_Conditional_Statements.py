# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:18:45 2026

@author: aiaqu
"""

# Conditional statements, if elif 

""" 

What to do today?

If it is sunny...
     I'll go for a run

"""

weather = "Sunny"

if weather == "Sunny": # == is the statement True or False
    print("I'll go for a run")
        
##
    
weather = "Cloudy"

if weather == "Sunny": # == is the statement True or False
    print("I'll go for a run")
else:
    print("Let's just stay in bed")
    
##

weather = "Cloudy"

if weather == "Sunny": # == is the statement True or False
    print("I'll go for a run")
elif weather == "Cloudy":
    print("Let's hit the gym!")
else:
    print("Let's just stay in bed")
    
# Multiple Conditions
    
    # and
weather = "Sunny"
temp = 12

if weather == "Sunny" and temp > 15: 
    print("I'll go for a run")
else:
    print("Let's just stay in bed")

    # or
weather = "Sunny"
temp = 12

if weather == "Sunny" or temp > 15: 
    print("I'll go for a run")
else:
    print("Let's just stay in bed")
    
    # if variable is a boolean, don't need conditional ==
sunny = True

if sunny:
    print("I'll go for a run")
else:
    print("Let's just stay in bed")
    
# Example: check if number, i, is even or odd
i = 3

# take modules of 2 to see if an even number
if i % 2 == 0:
    print(f"{i} is an even number")
else:
    print(f"{i} is an odd number")
    