#########################################
# Pandas - LOC and ILOC
#########################################

'''
In Python's pandas library, df.loc[] is a label-based indexing property
 used to select, filter, and modify specific rows and columns in a DataFrame. 
 It relies on explicit row index labels and column names 
 rather than integer position
'''
import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")

# often only want to consider certain rows or columns in our data frames

#transactions.loc[row_labels, column_label]
#transactions.iloc[row_indexes, column_indexes]

# ILOC - specificy conditions on rows and columns but primarily using indices/idx pos
    # I-LOC (I for index)
    # slice and dice data frames!

transactions.iloc[0]
transactions.iloc[0:4]
transactions.iloc[[0,30,51]]

    # can also select rows
    
transactions.iloc[0:4,[0,3,-1]] # [rows 0-3,[ycols, ycols]]

# all rows but only columns that we ask for
transactions.iloc[:,[0,3,-1]]

# LOC - specificy conditions on rows and columns primarily using labels or names
    # use column NAMES

transactions.loc[0]
# using a value as an index
transactions.set_index("customer_id", inplace = True)
transactions.loc[642]

transactions.reset_index(inplace = True)

    # list of transaction names
list(transactions)

transactions.loc[0:10,"customer_id"]

 # can change order of columns because the index is the same
transactions.loc[0:10,["customer_id", "product_area_id", "sales_cost"]]

# CONDITIONAL LOGIC

transactions["customer_id"] == 642

# only return the rows where this condition is true
transactions.loc[transactions["customer_id"] == 642]

# then only select columns of interest
transactions.loc[transactions["customer_id"] == 642, ["customer_id", "sales_cost"]]

# find where customer id is 642 and num_items > 5
    # both conditions must be in their own ()s
transactions.loc[(transactions["customer_id"] == 642) & (transactions["num_items"] > 5)]

# if one of the conditions is true
transactions.loc[(transactions["customer_id"] == 642) | (transactions["num_items"] > 5)]

# ISIN()
transactions.loc[transactions["customer_id"].isin([642,700])]

## What if condition was not true (what if we wanted all other customers other than?)
transactions.loc[~transactions["customer_id"].isin([642,700])]





