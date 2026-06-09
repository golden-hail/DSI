# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:13:14 2026

@author: aiaqu
"""

import numpy as np

my_1d_array = np.array([1,2,3])
type(my_1d_array) # numpy.ndarray

# use shape to see dimentions of array (example: 1d array with 3 elements = (3,))
my_1d_array.shape # (3,).. array with only 1 dimension 

# like lists, we can access elements in arrays with square brackets

my_1d_array[0] # = 1

# with slicing, the first index is included but the last is excluded
my_1d_array[0:2] # array([1, 2])

my_1d_array[-1]

my_2d_array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(my_2d_array)

my_2d_array[0]
my_2d_array[1]

my_2d_array[0][1] # why is mine printing like (np.int64(2))
my_2d_array[0,1] 

my_2d_array[0:2,1:3] # = array([[2, 3],[7, 8]])

# populate 2d array with a single number
np.zeros(3)
np.zeros((3,3))
np.zeros((3,3,3))
np.ones((3,3,3))

np.full((3,3), 5)

# array with sequential numbers (start stop step logic)

np.arange(10) # define np as array 0-9 because end is noninclusive
np.arange(2,10)
np.arange(2,10,2)

# linear space start 1 to end 5, 20 spread out values
np.linspace(1,5,20)

# rounding functionality

float_array = np.linspace(1,5,20)
np.round(float_array,2)

# default = float value
np.random.rand(5)
np.random.rand(5,2)

# one list of 100 values between 20 and 80
np.random.randint(20,80,100)

# a 10x10 list of values between 20 and 80
np.random.randint(20,80,(10,10))

# # 1D array to 2D array
my_1d_array = np.random.randint(20,80,100)
my_2d_array = my_1d_array.reshape(10,10)
print(my_2d_array)
