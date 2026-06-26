#################################################
# Pandas - Creating DataFrames
################################################# 

import pandas as pd

## The Date Frame (table of data with rows and columns)
my_df = pd.DataFrame()

    ## Method 1
    # for dictionaries, we use curly braces 
my_df = pd.DataFrame({"Name" : ["Tom", "Dick", "Harry"]})

    # columns need same number of rows to combine
my_df = pd.DataFrame({"Name" : ["Tom", "Dick", "Harry"],
                      "ID" : [101,102,103]})

    ## Method 2
my_list = [["Tom", 101], ["Dick", 102], ["Harry", 103]]

my_df = pd.DataFrame(my_list) # no column names..
my_df = pd.DataFrame(my_list, columns = ["Name", "ID"])

## IMPORTING

'''
.csv:
    Name,ID
    Tom,101
    Dick,102
    Happy,103
'''

###########################
# pandas read functionality
###########################
    # can specify column header names
my_data = pd.read_csv("tester_csv.csv")

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")

