
import pandas as pd 

my_df = pd.DataFrame({"Height" : [1.98,1.77,1.76,1.80,1.64],
                      "Weight" : [99, 81,70,86,82]})

## STANDARD SCALER
from sklearn.preprocessing import StandardScaler

# instantiate StandardScaler class
scale_standard = StandardScaler()

# apply the fit method to apply the rules of scaling 
# and then transform method to apply the scaling method to our data

    # for one column
scale_standard.fit_transform(my_df[["Height"]])

my_df_standardised = pd.DataFrame(scale_standard.fit_transform(my_df), columns = my_df.columns)


## NORMALIZATION
from sklearn.preprocessing import MinMaxScaler

scale_norm = MinMaxScaler()
scale_norm.fit_transform(my_df)
scale_norm_normal = pd.DataFrame(scale_norm.fit_transform(my_df), columns = my_df.columns)
