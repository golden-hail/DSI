##########################################
# Pandas - Sorting and Ranking
##########################################

import pandas as pd

customer_details = pd.read_excel("grocery_database.xlsx", sheet_name = "customer_details")


# SORTING
    # always sorts smallest to largest values
customer_details.sort_values(by = "distance_from_store", inplace = True)
    
    # what is was wanted largest to smallest value?
customer_details.sort_values(by = "distance_from_store", inplace = True, ascending = False)

    # sort by [dist], then credit_score where where are ties in dist
customer_details.sort_values(by = ["distance_from_store","credit_score"], inplace = True)

    # sort by but with nan values as the top of the sort_val
customer_details.sort_values(by = "distance_from_store", inplace = True, na_position = "first")

# RANKING

import numpy as np

x = pd.DataFrame({"column1" : [1,1,1,2,3,4,5,np.nan,6,8]})

    ### NOTE: ctrl i whle having a method selected 
        # will give you more information about it ###

x["column1"].rank()
x["column1_rank"] = x["column1"].rank()


'''
        RANK Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns'}, default 0
            Index to direct ranking.
            For `Series` this parameter is unused and defaults to 0.
        method : {'average', 'min', 'max', 'first', 'dense'}, default 'average'
            How to rank the group of records that have the same value (i.e. ties):

            * average: average rank of the group
            * min: lowest rank in the group
            * max: highest rank in the group
            * first: ranks assigned in order they appear in the array
            * dense: like 'min', but rank always increases by 1 between groups
'''

x["column1_rank"] = x["column1"].rank()

x['average_rank'] = x["column1"].rank(method = "average")
x['min_rank'] = x["column1"].rank(method = "min")
x['max_rank'] = x["column1"].rank(method = "max")
x['first_rank'] = x["column1"].rank(method = "first")
x['dense_rank'] = x["column1"].rank(method = "dense")

    # na_option allows for nan values to be put on the top or bottom 
x['dense_rank_na_top'] = x["column1"].rank(method = "dense", na_option = "top")
x['dense_rank_na_bottom'] = x["column1"].rank(method = "dense", na_option = "bottom")