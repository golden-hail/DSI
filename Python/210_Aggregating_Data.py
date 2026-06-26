##############################################
# Pandas - Aggregating data using GROUPBY
##############################################

import pandas as pd

'''
# SQL equivalent of what we are trying to achieve
select
    product_area_id,
    count(*) as row_count,
    sum(sales) as total_sales
    
from
    transactions
    
group by
    product_area_id
'''

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")
product_areas = pd.read_excel("grocery_database.xlsx", sheet_name = "product_areas")

# business insight - where the sales could be driven from, product area wise? 
transactions["sales_cost"].sum()

transactions = pd.merge(transactions, product_areas, how = "inner", on = "product_area_id")

transactions["product_area_name"].value_counts()

###########
## GROUPBY
###########

'''
# help us understand the proportions of how many product area name hits
product_area_name
Fruit         8699
Vegetables    8473
Non-Food      7784
Dairy         7360
Meat          6190
Name: count, dtype: int64
'''
# groupby product_area_name then find sum of the sales cost
transactions.groupby("product_area_name")["sales_cost"].sum()
'''
product_area_name
Dairy         175792.77
Fruit         252033.53
Meat          240892.82
Non-Food      747129.45
Vegetables    133879.25

'''

transactions.groupby("product_area_name")["sales_cost"].quantile([0.25,0.5,0.75])

### GROUPBY returns a series ###
sales_summary = transactions.groupby("product_area_name")["sales_cost"].sum()

# To make the series a DataFrame
sales_summary = transactions.groupby("product_area_name")["sales_cost"].sum().reset_index()

###########
## GROUPBY multiple columns
###########

sales_summary = transactions.groupby(["product_area_name", "transaction_date"])["sales_cost"].sum().reset_index()

# to also sum the num_items
sales_summary = transactions.groupby(["product_area_name", "transaction_date"])[["sales_cost","num_items"]].sum().reset_index()

# sum and mean of columns (starting back with one column)

# sum
sales_summary = transactions.groupby("product_area_name")["sales_cost"].agg("sum").reset_index()

# sum and mean
sales_summary = transactions.groupby("product_area_name")["sales_cost"].agg("sum", "mean").reset_index()

sales_summary = transactions.groupby(["product_area_name", "transaction_date"])[["sales_cost","num_items"]].agg("sum", "mean").reset_index()

# different aggs on different columns (instead of passing in list, we pass in dict)

sales_summary = transactions.groupby("product_area_name").agg({"sales_cost" : "sum", "num_items" : ""}).reset_index()



