# Looks at other available numerical data and makes the assumption 
# that other similar looking data points will give a better estimation 
# as what the missing value is likely to be

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

my_df = pd.DataFrame({"A" : [1,2,3,4,5],
                      "B" : [1,1,3,3,4],
                      "C" : [1,2,9,np.nan,20]})

# Let's ask the KNNImputer to estimate a value for the nan in Col "C"

## SimpleImputer would only look at column "C" to determine the missing value
imputer = SimpleImputer()
imputer.fit_transform(my_df) # Fills in C with 8

'''
Definition : KNNImputer(*, missing_values=np.nan, n_neighbors=5, 
                            weights="uniform", metric="nan_euclidean",
                            copy=True, add_indicator=False, 
                            keep_empty_features=False)
'''

## KNN takes columns A and B into account, as well as C
knn_imputer = KNNImputer()
knn_imputer.fit_transform(my_df) # fills in C with 8 (default, 5 nearest neighbors)

knn_imputer = KNNImputer(n_neighbors = 1)
knn_imputer.fit_transform(my_df) # 9

knn_imputer = KNNImputer(n_neighbors = 2)
knn_imputer.fit_transform(my_df) # 14.5

# WEIGHTS (uniform is default)
knn_imputer = KNNImputer(n_neighbors = 2, weights = "distance")
knn_imputer.fit_transform(my_df) # 13.55634919

'''
array([[ 1.        ,  1.        ,  1.        ],
       [ 2.        ,  1.        ,  2.        ],
       [ 3.        ,  3.        ,  9.        ],
       [ 4.        ,  3.        , 13.55634919],
       [ 5.        ,  4.        , 20.        ]])

Values of 3 and 3 (row 3) are closer than values of 5 and 4 (row 5), 
so 9 gets a higher weighting than 20 since the value is closer
'''

# convert returned array back into a DataFrame
my_df1 = pd.DataFrame(knn_imputer.fit_transform(my_df), columns = my_df.columns)


## SCIKIT is recommended for imputing vs Pandas (since they don't fit and tranform)
# which help ensure we are applying the same imputation logic that is applied 
# to test data as training data
