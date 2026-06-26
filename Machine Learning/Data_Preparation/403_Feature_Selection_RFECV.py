# Recursive Feature Eliminstation with Cross Validation
    # iteratively removes input data with the weakest relationship with the output data, 
        # until the desired number of features is reached
# RECOMMENDED METHOD FOR FEATURE SELECTION
        
import pandas as pd
my_df = pd.read_csv("feature_selection_sample_data.csv")

from sklearn.feature_selection import RFECV
from sklearn.linear_model import LinearRegression
# regression: output is numeric 

X = my_df.drop(["output"], axis = 1)
y = my_df["output"]

regressor = LinearRegression()
feature_selector = RFECV(regressor) # CV = 5 as default

fit = feature_selector.fit(X, y)

# how many variables is optimal?
optimal_feature_count = feature_selector.n_features_
print(f"Optimal number of feature: {optimal_feature_count}") # 2

# what are the input variabels?

X_new = X.loc[:, feature_selector.get_support()]

import matplotlib.pyplot as plt

# go from 0 to 4 features
plt.plot(range(1, len(fit.cv_results_['mean_test_score']) + 1), fit.cv_results_['mean_test_score'], marker = "o")
plt.ylabel("Model Score")
plt.xlabel("Number of Features")
plt.title(f"Feature Selection using RFE \n Optimal number of features is {optimal_feature_count} (at score of {round(max(fit.cv_results_['mean_test_score']),4)})")
plt.tight_layout()
plt.show()

