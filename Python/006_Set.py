# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:24:26 2026

@author: aiaqu
"""

my_set = {1,2,3}

# convert sets to lists/ tuples

my_set([1,2,3])
##########################
# no duplicates are allowed to exist within a set (each value is unique)
##########################
my_set = {1,1,2,3} # outputs {1,2,3}, duplicates are removed 
print(my_set)

# cannot index
my_set[0] # Error 'set' object is not subscriptable

my_list = [1,2,1,2,1,4,5,6,1]
unique_values = set(my_list)
print(unique_values)

## CAN use len function
len(my_set) # 3 elements

##########################
## CAN add values to the list (ADD and UPDATE)
##########################

my_set.add(4)
print(my_set)

my_set.update({5,6,7})
print(my_set)

##########################
## CAN remove values to the list (DISCARD and REMOVE)
##########################

my_set.discard(7)
print(my_set)

    # this works fine even though it doesn't exist, no error
my_set.discard(9)
print(my_set)

my_set.remove(9) # if value does not exist, throw error
print(my_set)

##########################
## Differences Between Sets
##########################

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

# Find values that do not exist in set 2 from set 1
set1.difference(set2) # {1,2}

# find values that do not exist in set 1 from set 2
set2.difference(set1) # {6,7}

# assign set1 to only the values not contained within set2
set1.difference_update(set2)
print(set1)

##########################
## Shared Values Between Sets
##########################

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

set1.intersection(set2)

# update set to common set elements/values
set1.intersection_update(set2)