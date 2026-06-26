import pandas as pd
import numpy as np

my_df = pd.DataFrame({"A" : [1,2,4,np.nan,5,np.nan,7],
                      "B" : [4,np.nan,7,np.nan,1,np.nan,2]})

# Finding Missing Values with Pandas

my_df.isna()
my_df.isna().sum()

# Dropping Missing Values with Pandas

my_df.dropna() # drops any rows that have nan in them, no amtter the column
my_df.dropna(how = "any") # default
my_df.dropna(how = "all")
# drop any rows with a nan in the column subset 
my_df.dropna(how = "any", subset = ["A"])

my_df.dropna(how = "any", inplace = True)

# Filling Missing Values with Pandas
    # drop rows rather than fill them, in most cases, to keep data true

my_df = pd.DataFrame({"A" : [1,2,4,np.nan,5,np.nan,7],
                      "B" : [4,np.nan,7,np.nan,1,np.nan,2]})

my_df.fillna(value = 100)

# filling with mean or median may be a good practice, in some cases with little data 

mean_value = my_df["A"].mean()
my_df["A"].fillna(value = mean_value)

my_df.fillna(value = my_df.mean(), inplace = True)

# imputing replacement values for missing values

'''
'SimpleImputer' from scikit-learn enables the static imputation of missing values, 
    using either a constant value or a column mean, median, 
    or even the most common value 
'''

