######################################
# Pandas - Accessing Columns
######################################

import pandas as pd

transactions = pd.read_excel('grocery_database.xlsx', sheet_name = 'transactions')

'''
# in SQL
select
    customer_id,
    sales_cost
    
from
    transactions
'''

# selecting a column
new_df = transactions.customer_id

my_var = 'customer_id'
transactions.my_var # fails

# This method is better.. data that exists in the column
new_df = transactions["customer_id"] # converts col vals into a series?? 0.o
transactions[my_var] 

# data frames are 2d, series are 1d, so need double brackets to convert
new_df = transactions[["customer_id"]]

new_df = transactions[["customer_id", "sales_cost"]]