################################################
# Pandas - Adding & Dropping Columns
################################################

import pandas as pd

transactions = pd.read_excel('grocery_database.xlsx', sheet_name = "transactions")

# ADD a new column to a set of data

transactions["store_id"] = 1

# create a new column named "profit"
transactions["profit"] = transactions["sales_cost"]*0.2 # 0.2 = profit margin

import numpy as np

## ADDING COLUMNS

# create a new col called "sales_type" that determine if high or low cost
transactions["sales_type"] = np.where(transactions["sales_cost"] > 20, "Large", "Small")

# create new col based on multiple conditions
condition_rules = [transactions["sales_cost"] > 50, transactions["sales_cost"] > 20, transactions["sales_cost"] > 10]
outcomes = ["x-Large", "Large", "Medium"]

transactions["sales_type"] = np.select(condition_rules, outcomes, default = "Small")
    # default is small (aka less than 10$)
    
## DROPPING COLUMNS

new_df = transactions.drop(["sales_cost"], axis = 1) 
    #   axis = 1 means drop col
    # can use axis = 0- to drop rows
    

