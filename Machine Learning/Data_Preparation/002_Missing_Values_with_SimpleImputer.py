# IMPUTE: Import/impute missing values in data

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

my_df = pd.DataFrame({"A" : [1,4,7,10,13],
                     "B" : [3,6,9,np.nan,15],
                     "C" : [2,5,np.nan,11,np.nan]})

# 1) Instantiate our inputer object using the SimpleImputer class we imported above
imputer = SimpleImputer()

# ctrl i
'''
missing_valuesint, float, str, np.nan, None or pandas.NA, default=np.nan
The placeholder for the missing values. All occurrences of missing_values will be imputed. 
For pandas' dataframes with nullable integer dtypes with missing values, 
missing_values can be set to either np.nan or pd.NA.

strategystr or Callable, default='mean'
The imputation strategy.

If "mean", then replace missing values using the mean along each column. 
    Can only be used with numeric data.

If "median", then replace missing values using the median along each column. 
    Can only be used with numeric data.

If "most_frequent", then replace missing using the most frequent value along each column.  
    Can be used with strings or numeric data. If there is more than one such value, only the smallest is returned.

If "constant", then replace missing values with fill_value. 
    Can be used with strings or numeric data.

If an instance of Callable, then replace missing values using the scalar statistic returned by running 
the callable over a dense 1d array containing non-missing values of each column.
'''

## 2 steps for test data applications
# calculate the values it needs to impute (fit), 
imputer.fit(my_df)

# then apply the logic onto our data
imputer.transform(my_df)

my_df1 = imputer.transform(my_df)

## run both at once! ## ON TRAINING DATA ONLY -
imputer.fit_transform(my_df) ## ON TRAINING DATA ONLY - 
    # imputation rules must be based on our trained data
    
my_df2 = pd.DataFrame(imputer.fit_transform(my_df), columns = my_df.columns)

# we can specify aspecific lists of columns to impute

imputer.fit_transform(my_df[["B"]])
my_df["B"] = imputer.fit_transform(my_df[["B"]])

