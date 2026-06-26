
# Feature Select using a simple Correlation Matrix

import pandas as pd
my_df = pd.read_csv("feature_selection_sample_data.csv")

# we don't want to use inputs that are in high correlation to each other 
# as inputs for linear regression (can violate multicoliniearity.. and can't trust output stats)

correlation_matrix = my_df.corr()

# input3 and input4 don't really correlate at all but input1 and 2 are really close... 
# could disclude some of this data... tbd