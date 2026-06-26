##########################################
# Pandas - PLotting Our Data Using Pandas
##########################################

import pandas as pd

transactions = pd.read_excel('grocery_database.xlsx', sheet_name = "transactions")
customer_details = pd.read_excel('grocery_database.xlsx', sheet_name = "customer_details")
product_areas = pd.read_excel('grocery_database.xlsx', sheet_name = "product_areas")

### PLOT (Lineplot default)

customer_details.plot() # plots everything with a lineplot 

daily_sales_summary = transactions.groupby("transaction_date")[["sales_cost","num_items"]].sum().reset_index()

# total sales by day (use new df)
daily_sales_summary["sales_cost"].plot()

# specify x axis
daily_sales_summary.plot(x = "transaction_date", y = "sales_cost")

# SCATTER Plot (parameter: kind)
daily_sales_summary.plot(x = "transaction_date", y = "sales_cost", kind = "line")

    # scatter 2 numerical values against each other to show a potential relationship
    # Ex: sales vs numer of items
    
daily_sales_summary.plot(x = "num_items", y = "sales_cost", kind = "scatter")

# BOX plot, one variable at a time to see how values of the plot 
    # are distributed from low values to high values

daily_sales_summary.plot(y = "sales_cost", kind = "box")
    # median equals 50 percentile...
    # !!I need to review these
    
# HISTOGRAM 
    # a plot made up of vertical bars that represent the frequency 
    # of data points in a given range
    
daily_sales_summary.plot(y = "sales_cost", kind = "hist")
        # x axis = daily sales cost
        # y axis = number of days
        # default # of groupings of x is 10
    
    # add more bins (groupings of x)
    
daily_sales_summary.plot(y = "sales_cost", kind = "hist", bins = 25)

# BAR Plot

product_areas.plot(y = "profit_margin", kind = "bar", x = "product_area_name")
