###########################################
# Matplotlib - Additional Plot Features
###########################################

import matplotlib.pyplot as plt

x_values = [0,1,2,3,4,5,6,7,8,9,10]
x_squared = [x ** 2 for x in x_values] 
x_cubed = [x ** 3 for x in x_values] 

# Basic Legend, with labels, and lim() (commented out) and override ticks
plt.plot(x_values, x_squared, label = "X Squared")
plt.plot(x_values, x_cubed, label = "X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The values of x")
# plt.xlim(2,8)
# plt.xticks(range(11)) # will do idx 0-10
# plt.xticks([]) # could leave numbers out
plt.ylabel("The values of y")
# plt.ylim(-100,600)
plt.grid(True)
plt.legend()
plt.show() 

# rotation = numbers of degrees
