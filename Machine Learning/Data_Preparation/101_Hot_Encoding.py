import pandas as pd
from sklearn.preprocessing import OneHotEncoder

X = pd.DataFrame({"input1" : [1,2,3,4,5],
                  "input2" : ["A", "A", "B", "B", "C"],
                  "input3" : ["X", "X", "X", "Y", "Y"]})

categorical_vars = ["input2", "input3"]

one_hot_encoder = OneHotEncoder(sparse_output = False, drop = "first") 
    # sparse = false to get array

encoder_vars_array = one_hot_encoder.fit_transform(X[categorical_vars])

encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

encoder_vars_df = pd.DataFrame(encoder_vars_array, columns = encoder_feature_names)

# concatinate this new dataframe back onto our original input variable df
# to ensure we have everything together in one place for modeling

X_new = pd.concat([X.reset_index(drop=True), encoder_vars_df.reset_index(drop = True)], axis = 1)
    # axis 1 = cols, not rows

# drop them again
X_new.drop(categorical_vars, axis = 1, inplace = True)

# Don't fall into Dummy Variable Trap!
# do not violate multicolinearity 



