# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:46:51 2026

@author: aiaqu
"""

import numpy as np

my_1d_array = np.zeros(10)
print(my_1d_array)

# index into array to change the value of an element
my_1d_array[0] = 50
print(my_1d_array)

# can also do this with slicing 
my_1d_array[3:6] = 50
print(my_1d_array)

# can search through elements in array and see WHERE a condition is true/ a value exists

np.where(my_1d_array == 50) #output = (array([0, 3, 4, 5]),) <- nothing after comma since no column

my_2d_array = np.array([[1,5,9],[8,5,5]])
print(my_2d_array)

np.where(my_2d_array == 5) # row 0, column 1 is the first instance of 5

np.where(my_2d_array < 5)
np.where(my_2d_array >= 5)
np.where(my_2d_array != 5)

# WHERE will work with empty parens but will just return the indices of non-0 values

# for multi-dimensional arrays, argwhere can provide index of values in a new array
np.argwhere(my_2d_array == 5)

# can use to subset
    # find index of elements where the element is > 5

index = np.where(my_2d_array > 5)
print(index)

    # use the index to find out what those values are (that are greater than 5) 
    # since we have the index

my_2d_array[index]

    # change values > 5 to 100 by using the > 5 indices
my_2d_array[index] = 100
print(my_2d_array)

# WHERE cleverly isolates elements based on defined conditions 
    #  no matter where they are we can manipulate them!

# asking if all values in my_1d_array are non-0 
np.all(my_1d_array) # False, there are 0s

np.all(my_1d_array >= 0)
np.all(my_1d_array > 5)

## are any elements in array non 0
np.any(my_1d_array) # at least one data point is non-0

## Vertical and Horozontal Stack
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a)
print(b)

# VSTACK: dimensions must work for stacking on top of each other
# number of columns in 2 arrays must be equal

v = np.vstack((a,b))
print(v)

    #stack more!
v = np.vstack((a,b,a,b))
print(v)

# HSTACK: dimensions must work for stacking on top of each other
# number of rows in 2 arrays must be equal
    
h = np.hstack((a,b))
print(h)

    #stack more wiiiide
h = np.hstack((a,b,a,b))
print(h)

# can flatten data into 1 array
print(my_2d_array)

my_2d_array.flatten()


