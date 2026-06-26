##############################################
# Pandas - Exploring & Understanding our Data
##############################################

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = 'transactions')

transactions.shape # note: shape is an attribute, not a method, so no parens

# see top n data rows
transactions.head(20)

# see bottom n data rows
transactions.tail(10)

# get random sample from data 
transactions.sample()

# get n samples from data
transactions.sample(10)

# get samples of frac % of total rows 
sample = transactions.sample(frac = 0.1)

### Describe: This is important to run each time you import data 

transactions.describe()

# get the largest n row entries based on the sales_cost 
transactions.nlargest(25,"sales_cost")

# get the n smallest row entries based on sales_cost
transactions.nsmallest(25,"sales_cost")

# find the number of unique values for each column of data  
transactions.nunique()

#### Grab customer_details table for null values

customer_details = pd.read_excel("grocery_database.xlsx", sheet_name = 'customer_details')

# data table is too big to display it all
customer_details.isna()

# see how many missing data entries exist for a col of data
customer_details.isna().sum()