# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:38:55 2026

@author: aiaqu
"""

'''
For each element in a collection: 
    do STUFF
'''

my_string = "Cup of Coffee"

for i in my_string:
    print(i.upper())
    
    
# For loop through list

my_list = ["Cup", "of", "Coffee"]

for i in my_list:
    print(i)
  
    # Ex 2 with ints
my_list = [1,2,3,4,5,6,7,8,9]

for i in my_list:
    i_squared = i ** 2
    print(i,i_squared)
    
    # OR
    
for i in my_list:
    print(i,i ** 2)
    
for i in my_list:
    print(i,"Loop Finished", type(i))
    
## !!can find enumerate to find indices

my_list = ["a","b","c"]

for idx, i in enumerate(my_list):
    print(idx,i)

for i in my_list:
    for j in my_list:
        print(i,j)
'''        
## RANGE

range(start, stop, step)
'''

for i in range(10,100,5):
    print(i)
    
'''
    Example from 008_Conditional_Statements
    
'''

# Example: check if number, i, is even or odd
i = 3

# take modules of 2 to see if an even number
if i % 2 == 0:
    print(f"{i} is an even number")
else:
    print(f"{i} is an odd number")
    
# for Loops this time 
my_nums = list(range(0,20))
print(my_nums)

for i in my_nums:
    
    if i % 2 == 0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")

################
# skip an element/ break a loop
################
'''
# When a loop sees CONTINUE.. 
loop goes back to the top starting with
the next element 

Example: say we want to skip numbers 
divisible by 3
'''
     
for i in range(0,21):
    if i % 3 == 0:
        continue
    print(i)
    
'''
PASS for placeholder code that does nothing??
'''

'''
 BREAK breaks the loop and stops it completely
''' 

for i in range(0,21):
    if i > 10:
        break
    print(i)
    
    
