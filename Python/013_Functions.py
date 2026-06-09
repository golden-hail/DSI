# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:41:16 2026

@author: aiaqu
"""

'''
# built in function (SUM, MAX, PRINT)
# a function is a wrapper for a process we can call upon 
# DEF - a function is being defined

# using PASS is good for troubleshooting - 
    piping in code before writing it,
    though actually nothing would happen as a result 
'''

def happy_birthday():
    pass

# call the function - run the code within the function
happy_birthday()

def happy_birthday():
    print("Happy Birthday!")
    
happy_birthday() # calling functions like this surpress console 
    # output from within the called function
    
# this function takes in a name and adds it to our brithday message
    
def happy_birthday(name):
    print(f"Happy Birthday {name}!")
    
happy_birthday("Sue")
happy_birthday("Sachin") 

happy_birthday() # <- ERROR: missing inputs defined in the function

#### With a default value now

def happy_birthday(name = "Human"):
    print(f"Happy Birthday {name}!")
    
happy_birthday("Sue")
happy_birthday("Sachin") 

happy_birthday()  