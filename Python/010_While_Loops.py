# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:09:37 2026

@author: aiaqu
"""

'''
WHILE some condition is true:
    do something
    test if condition is still true
    
    # determines if loop should reiterate again 
        # or if it should stop
'''

i = 1

while i <= 5:
    print(i)
    i += 1
    
# can still use CONTINUE and BREAK
## BREAK overrides while condition in WHILE loops

i = 1

while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
    
