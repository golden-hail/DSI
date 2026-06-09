# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:49:18 2026

@author: aiaqu
"""

# Extract a list of prime numbers under a specified value

''' 
## Version 1 (rerun from end at pop() command)
'''

n = 20
number_range = set(range(2, n+1))
primes_list = []

prime = number_range.pop() # pops out the first number, 2, because it is the first known prime number
primes_list.append(prime) # append to list "prime" since we are collection the prime numbers
    # find all multiples of 2, because they are not prime
    # range(start,stop,step) - increment our steps by our prime number
multiples = set(range(prime*2, n+1, prime))
    # update number_range array/set, only keep the values that are NOT multiples of 2 
    # (since they are divisible by 2, and therefor not prime)
number_range.difference_update(multiples)
    # ***made massive reduction to data that needs to be tested

'''
##  Version 2
'''

# upper bound
n = 1000

# range of number to be checked
number_range = set(range(2, n+1))

# empty list to append discovered primes to
primes_list = []

# while loop
while number_range: # while number_range has values in it
    prime = number_range.pop() 
    primes_list.append(prime) 
    multiples = set(range(prime*2, n+1, prime))
    number_range.difference_update(multiples)
    
# print our list of prime numbers 
print(primes_list)

# of primes that we found
prime_count = len(primes_list)

# Largest Prime
largest_prime = max(primes_list)
        
# Summary
print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")

'''
# Version 3 - in a function now
'''

# restart kernal so everything is fresh

def primes_finder(n):
    
    # range of number to be checked
    number_range = set(range(2, n+1))

    # empty list to append discovered primes to
    primes_list = []

    # while loop
    while number_range: # while number_range has values in it
        prime = number_range.pop() 
        primes_list.append(prime) 
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples)
        
    # print our list of prime numbers 
    # print(primes_list)

    # of primes that we found
    prime_count = len(primes_list)

    # Largest Prime
    largest_prime = max(primes_list)
            
    # Summary
    print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")
    
    return primes_list # THIS will pass us the value outside of the function and return it in the console


primes_list = primes_finder(100)    
print(primes_list)


primes_list = primes_finder(10000000)    








