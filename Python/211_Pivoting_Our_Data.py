###########################################
# Pandas - Pivoting our Data
###########################################

# pivot table 
# 2 col against each other one on y on on x axis, sum values of a third col using some agg

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")
product_areas = pd.read_excel("grocery_database.xlsx", sheet_name = "product_areas")
transactions = pd.merge(transactions, product_areas, how = "inner", on = "product_area_id")

transactions.head()

sales_summary = transactions.groupby(["transaction_date", "product_area_name"])["sales_cost"].sum().reset_index()

# Can also do this by pivot table
    # index as y axis
    # by default, will give the mean of each value?
sales_summary_pivot = transactions.pivot_table(index = "transaction_date",
                                               columns = "product_area_name",
                                               values = "sales_cost",
                                               aggfunc = "sum")

'''
product_area_name    Dairy    Fruit     Meat  Non-Food  Vegetables
transaction_date                                                  
2020-04-01         1043.14  1137.81  1448.21   4667.76     1306.45
2020-04-02         1204.71  1722.27  1684.33   3834.35      758.39
2020-04-03         1122.61  1508.80  1221.80   3861.28      887.49
2020-04-04         1232.02  1946.22  1506.92   5172.59      678.26
2020-04-05          995.28  1367.22  1337.26   4621.97      967.90
'''

sales_summary_pivot.plot()

# with multiple indices and with fill_value (What to replace nan/null with)
sales_summary_pivot = transactions.pivot_table(index = ["transaction_date", "profit_margin"],
                                               columns = "product_area_name",
                                               values = "sales_cost",
                                               aggfunc = "sum",
                                               fill_value = 0,
                                               margins = True,
                                               margins_name = "Total")

# Use Margins to get totals for the highest value of rows




