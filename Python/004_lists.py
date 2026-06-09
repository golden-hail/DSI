# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:12:17 2026

@author: aiaqu
"""
# create a list
list1 = []
type(list1)

    # method 2
list1 = [1, 2.5, "Three", 400000, True]
print(list1)

# length of list
len(list1)
    
################################
# Accessing Elements and Slicing    
################################

# Lists start at the 0th element
list1[0]
list1[3]

list1[5] # error, there is no 5th element because there are only 5 elements 
    # and we start at 0
    
# Access elements from the end of a list
list1[-1]

list2 = [0,1,2,34,5,6,7,8,9]
len(list2)

# "end" of the count (:) side is non-inclusive, to divide the list somewhere

    # list2[start:end]
list2[4:7] # = [4,5,6] # doesn't include the 4th element, 3, 
                        # but includes the 7th element, 6

    # list2[start:] # element after to end
list2[4:]

    # list2[:end]
list2[:4]

# 4th element from end to the 1st element from end
list2[-4,-1]

################################
# Adding Elements   
################################

planets = ["Mercury", "Venus", "Earth"]
print(planets)

planets.append("Jupiter")
print(planets)

planets.insert(3,"Mars")
print(planets)

outer_planets = ["Saturn", "Uranus", "Neptune", "Pluto"]

planets.extend(outer_planets)
print(planets)

# can also use plus signs to combine lists into one list
    # [1,2,3] +  [4,5,6]

################################
# Removing Elements    
################################

print(planets)

# .REMOVE elements(s) containing string value
planets.remove("Pluto")
print(planets)

# DEL value at index
del planets[2]
print(planets)

# POP pops out value, removes it from list and returns the value at the specified index
planets.pop(2)

################################
# Finding the Index of an Element 
################################

# index of mercury is 0
planets.index("Mercury")
planets.index("Earth")
planets.index("Tatooine") # error, not in list

# use the IN statement to check if the value exists in the list

"Earth" in planets #True
"Tatooine" in planets #False

################################
# Sorting Lists
################################

    # sorts by alphabetical order because they're strings
planets.sort()
print(planets)
    # sort by reverse order
planets.sort(reverse = True)
print(planets)

################################
# Copying Lists
################################

list1 = [1,2,3]
### This sets, essentailly, an alias for list1... copies the reference to the list (where it's located in memory)
# where list1 shares the 2 variable names but the value/variable is the same
list2 = list1

print(list1)
print(list2)

list2.append(4)

print(list1)
print(list2)

# to COPY a list, use copy
list1 = [1,2,3]
list2 = list1.copy()

list2.append(4)

print(list1)
print(list2)


