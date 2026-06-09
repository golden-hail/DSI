# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:43:51 2026

@author: aiaqu
"""
## Instead of containing elements as values, 
    # it holds elements in pairs, 
    # namely unique keys and their associated values (key value pairs)

# most common use is as a look up table

# example: Contact book - people have a phone number assigned to them, uniquely
    # request a friend from the phone book as a key, 
    # then we would be provided with the phone number, which is the value
    
my_dict = {}

# set
a = {1,2,3}

# In this example, strings are keys and ints are values 
planet_dict = {
    "Mercury" : 8,
    "Venus" : 6,
    "Earth" : 5,
    "Mars" : 7,
    "Jupiter" : 1,
    "Saturn" : 2,
    "Uranus" : 3,
    "Neptune" : 4
    }

# values can be lists, tuples, or sets, even dictionaries
 #can use length
 
len(planet_dict)

# how do we access a value?

# Method 1

planet_dict["Mars"] # return 7
planet_dict["Jupiter"] # return 1

# Method 2 GET
 # it allows us to enter a default value to be returned if we search for a value and don't get a return
 
planet_dict.get("Mars")
 # can return a default value in instances when key is not present

planet_dict.get("Pluto", 0) # returns 0 because Pluto is not in planet_dict

planet_dict["Pluto"] # key error

"Saturn" in planet_dict
"Pluto" in planet_dict

planet_dict.keys()
planet_dict.values()

# add new key value pair
planet_dict["Pluto"] = 9
print(planet_dict)

# edit values in a key-value pair
planet_dict["Uranus"] = 4
planet_dict["Neptune"] = 3
print(planet_dict)

# can remove values with POP
planet_dict.pop("Earth")
print(planet_dict)
