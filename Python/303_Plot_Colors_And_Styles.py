###########################################
# Matplotlib - Plot Colors and Styles
###########################################

import matplotlib.pyplot as plt

x_values = [0,1,2,3,4,5,6,7,8,9,10]
x_squared = [x ** 2 for x in x_values] 
x_cubed = [x ** 3 for x in x_values] 

plt.plot(x_values, x_squared, label = "X Squared", color = "deeppink", linewidth = 2, linestyle = "--")

## with RGB 
# plt.plot(x_values, x_cubed, label = "X Cubed", color = [1.0,0.5,0.25])

## with hex
plt.plot(x_values, x_cubed, label = "X Cubed", color = "#0000FF", linewidth = 2, linestyle = ":")

plt.title("Exponential Growth")
plt.xlabel("The values of x")
plt.ylabel("The values of y")
plt.legend()
plt.show() 

# different line types (linestyle): 
        # dotted lines are good for overall average vs series
        # predition into the future, or an overall average 

#############################

# Markers: 
    
x_values = [0,1,2,3,4,5,6,7,8,9,10]
x_squared = [x ** 2 for x in x_values] 
x_cubed = [x ** 3 for x in x_values] 

plt.style.available

plt.plot(x_values, x_squared, label = "X Squared", color = "deeppink", linewidth = 2, marker = ".")

## with RGB 
# plt.plot(x_values, x_cubed, label = "X Cubed", color = [1.0,0.5,0.25])

## with hex
plt.plot(x_values, x_cubed, label = "X Cubed", color = "#0000FF", linewidth = 2, marker = "o", markersize = 10, markerfacecolor = "red", markeredgecolor = "green")

plt.title("Exponential Growth")
plt.xlabel("The values of x")
plt.ylabel("The values of y")
plt.legend()
plt.show() 

# other styles

plt.style.available
plt.style.use('seaborn-poster')

plt.plot(x_values, x_squared, label = "X Squared")
plt.plot(x_values, x_cubed, label = "X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The values of x")
plt.ylabel("The values of y")
plt.legend()
plt.show() 

