# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:15:12 2026

@author: aiaqu
"""

my_list = [1, 3.6, "Four"]

my_tuple = (1, 3.6, "Four")

# convert list type to Tuple
x = tuple(my_list)

# convert tuple to list
x = list(x)

# A Tuple is Immutable (it cannot be changed)
# list is mutable (can be mutated)

# we can create and delete tuple, but you cannot change the value OF a tuple

my_tuple.append(4) # ERROR - cannot append to tuples

my_tuple.sort() # ERROR - cannot sort tuples

# TUPLES are used for efficiency and speed of processing 
# - since it's immutable, it can be stored in a single block of memory 

## Similarities 
len(my_tuple)

    #can still index / extract elements 
my_tuple[0]
my_tuple[-1]
my_tuple[1:3]

my_tuple.index(3.6)

3.6 in my_tuple


