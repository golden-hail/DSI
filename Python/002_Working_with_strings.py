string1 = "data"
string2 = "science"
string3 = "infinity"

len(string1)

# index starts at 0!!!

# get index for letter d in data 
string1.index("d")

# grab first (0th) index
string3[0];

# slicing
string3[3:6]

#replace

string1.replace("a","o")
print(string1)

string1a = string1.replace("a","o")
print(string1a)

#concatenate

string4 = string1 + "-" + string2 + "-" + string3
print(string4)

#convert  / process text

string4.upper()
string4.lower()

string4.title()
string4.split("-")

# how many isntances of ()
string4.count("-")


# consider "" vs '': print('Don't know) = bad
print("Don't know")
print('He said "One Small Step for Man"')

# escape character can also remedy this
print('Don\'t know')
print("He said \"One Small Step for Man\"")

# type conversions
a = 123
type(a)
b = str(a)
type(b)

# string formatting (dynamically add info)

my_string = "RED ALERT - Meltdown in sector 7G. Please contact: Homer"

alert_level = "RED"
error_type = "Meltdown"
sector = "7G"
contact_name = "Homer"

my_string = f"{alert_level} ALERT - {error_type} in sector {sector}. Please contact: {contact_name}"
print(my_string)

alert_level = "AMBER"
error_type = "Overheating"
sector = "7H"
contact_name = "Lenny"

my_string = f"{alert_level} ALERT - {error_type} in sector {sector}. Please contact: {contact_name}"
print(my_string)

## python 2 (dot format approach)
my_string = "{} ALERT - {} in sector {}. Please contact: {}".format(alert_level,error_type,sector,contact_name)
print(my_string)

    # or
    
my_string = "%s ALERT - %s in sector %s. Please contact: %s" % (alert_level,error_type,sector,contact_name)
print(my_string)
