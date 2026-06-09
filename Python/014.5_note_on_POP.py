# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:32:24 2026

@author: aiaqu
"""

'''
pop() method usually extracts the LOWEST element of a set. Sets though, by definition are unordered.


### The pop() method will usually extract the lowest element of a set. 
    Sets however are, by definition, unordered. The items are stored internally with some order, 
    but this internal order is determined by the hash code of the key 
    (which is what allows retrieval to be so fast). 

### This hashing method means that we can't 100% rely on it successfully getting the lowest value. 
    In very rare cases, the hash provides a value that is not the lowest.
    
    
### The simplest solution to force the minimum value to be used is to replace the line...

prime = number_range.pop()

...with the lines...

prime = min(sorted(number_range))

number_range.remove(prime)


Where we firstly force the identification of the lowest number in the number_range into our prime variable, 
    and following that we remove it.

However, because we have to sort the list for each iteration of the loop in order to get the minimum value, 
    it's slightly slower than what we saw with pop()!
'''