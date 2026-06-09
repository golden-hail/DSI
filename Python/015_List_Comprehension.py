# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:38:30 2026

@author: aiaqu
"""

# for loop

my_list = [1,2,3,4,5]
my_new_list = []

for i in my_list:
    my_new_list.append(i)
    
    
## list comprehension 
my_new_list = [i for i in my_list]


###############
# change the value of i in each loop

my_list = [1,2,3,4,5]
my_new_list = []

for i in my_list:
    my_new_list.append(i*i)
    
    # list comprehension
    
my_new_list = [i*i for i in my_list]

### Can also filter what you're appending 

my_list = [1,2,3,4,5]
my_new_list = []

for i in my_list:
    if i % 2 == 0:
        my_new_list.append(i)
        
            # list comprehension: add to new list only if divisible by 2
    
my_new_list = [i for i in my_list if i % 2 == 0]


## use created square_root function within a list comprehension to run each list element through the function 
def square_root(number):
    return number ** 0.5

my_list = [1,4,9,16,25]

my_new_list = [square_root(i) for i in my_list]

## listception  
my_list = [[1,8],[2,3],[3,17]]

## extract first element of each list 
my_new_list = [i[0] for i in my_list]

## extract first element from each list if the second element is the highest value
my_new_list = [i[0] for i in my_list if i[1] == max(i[1] for i in my_list)]