# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 09:23:12 2026

@author: aiaqu
"""

a = 10
b = 10.5

#int to float
c = float(a)
print(c)
print(type(c))

# float to int
d = int(b)
print(d)
print(type(d))

x = 10
y = 4

# operations
print(x + y)
print(x - y)
print(x / y)
print(x * y)

# floor division (end up with int as output)
print(x // y)

# one number to the power of another
print(x ** y)

# square root
print(81 ** 0.5)

# we got PEMDAS
print(x * y + y)
print(x * (y+y))

# modulus (remainder)

a = 10
b = 4

a % b

# in built numerical functions
a = -10
b = 10

print(max(a,b))
print(min(a,b))

abs(a)

    # rounding
a = 1234.5678

round(a,3)
round(a,0) # this value will still be a float (need to INT it)

round(a,-2) # rounds to the nearest 100 value (1200.0)
round(a,-3) # rounds to the nearest 1000 value (1000.0)

