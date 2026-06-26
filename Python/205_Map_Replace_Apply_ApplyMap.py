#######################################################
# Pandas - Adding & Dropping Columns (LOL nemeric)
#######################################################

import pandas as pd
customer_details = pd.read_excel("grocery_database.xlsx", sheet_name = "customer_details")
product_areas = pd.read_excel("grocery_database.xlsx", sheet_name = "product_areas")

'''
# MAP - transform values in a column to another value, applies to series datas
    # It's an attribute of the series data type, can't be used on a dataframe
    # Enter MAP are a library 
    
'''
#### Column is created through mapping
customer_details["gender_nemeric"] = customer_details["gender"].map({"M" : 0,
                                                                     "F" : 1})

customer_details["gender_nemeric"] = customer_details["gender"].map({"F" : 1})

#### REPLACE

customer_details["gender_nemeric"] = customer_details["gender"].replace({"M" : 0,
                                                                     "F" : 1})
    # gender_numeric column is regenerated everytime it is run, 
        # here we are only replacing "f"s with 1s in the gender_number colum

customer_details["gender_nemeric"] = customer_details["gender"].replace({"F" : 1})

#### APPLY
    # A function to apply to a series of data (in the example's case, a column of data)
    
product_areas["product_area_name"].apply(len)

# Function that updates profit margin figures based on our pricing strategy
# if higher than 0.2 (20%) it needs to increase by some small amount, if not it needs to decrease?

def update_profit_margin(profit_margin):
    if profit_margin > 0.2:
        return profit_margin * 1.2
    else:
        return profit_margin * 0.8
    
    # creating a new column based on the output of our function 
    
product_areas["profit_margin_updated"] = product_areas["profit_margin"]. apply(update_profit_margin)

x = pd.DataFrame({"A" : [1,2], "B" : [3,4], "C" : [5,6]})

    # APPLY works on axis = 0
x.apply(max)
x.apply(max, axis = 1)

# APPLYMAP

def square(n): # these functions work on a per datatype basis
    return n ** 2

x.applymap(square)