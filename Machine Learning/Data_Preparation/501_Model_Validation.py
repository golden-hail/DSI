# Models must be validated so that we can trust them


# Model Validation

import pandas as pd
my_df = pd.read_csv("feature_selection_sample_data.csv")

# Test/Train Split

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

X = my_df.drop(["output"], axis = 1)
y = my_df["output"]

## Regression Model
    # put 20% of data into the test set, 80% goes to training (regression model)
    # default shuffles data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# instatiate model
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
r2_score(y_test,y_pred)


## Classification Model
    # for classification , need one more parameter
    # stratification: ask both sets to attain the same proportion of the output class 
    # preserves percentage of for each class 

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, stratify = y)

# Cross Validation

from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold

cv_scores = cross_val_score(regressor, X, y, cv = 4, scoring = "r2") # default cv = 5

cv_scores.mean() # cross val score = 0.6379038172153191

# Regression 

cv = KFold(n_splits = 4, shuffle = True, random_state = 42)
cv_scores = cross_val_score(regressor, X, y, cv = cv, scoring = "r2")
cv_scores.mean() # cross val score = 0.7078051873514348 (better)

# Classification 

cv = KFold(n_splits = 4, shuffle = True, random_state = 42)
cv_scores = cross_val_score(clf, X, y, cv = cv, scoring = "accuracy")
cv_scores.mean() # cross val score = 0.7078051873514348 (better)