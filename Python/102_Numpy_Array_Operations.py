# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:13:14 2026

@author: aiaqu
"""

import numpy as np

my_1d_array = np.random.randint(2,8,16)

# array operations
np.max(my_1d_array)
    # or
my_1d_array.max()

# other ops
my_1d_array.min()
my_1d_array.mean()
my_1d_array.sum()
my_1d_array.std()

my_2d_array = my_1d_array.reshape(4,4)
print(my_1d_array)
print(my_2d_array)

my_2d_array.max()

# maximum value from each column 
my_2d_array.max(axis = 0)

# maximum value from each row 
my_2d_array.max(axis = 1)

# find the index of the element taht has the min or max value (ARGMAX AND ARGMIN)
my_2d_array.argmax(axis = 0)

    # row now ya'll
    
my_2d_array.argmax(axis = 0)

# can sort numpy array 

np.sort(my_1d_array)

# add subtract multiply and divide by array values 

a = np.array([1,2,3,4,5])

a + 10
a - 10
a * 10
a / 10

b = np.array([3,7,1,2,6])

# add arrays element by element - 
    # we would get an error is the shape (ie size) of the arrays are not the same
a + b

a = np.array([-2,-1,0,1,2])

np.square(a)

np.sqrt(a) # square root of negative is NaN

np.sign(a) # check positive or naegative (or 0)

np.sin(a)
np.cos(a)
np.tan(a)

# dot- product
a = np.array([1,2,3])
b = np.array([4,5,6])

np.dot(a,b)
