###########################################################
# Random Forest for Classification - Basic Template
###########################################################

# Import required Python packages

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Import sample data

my_df = pd.read_csv("data/sample_data_classification.csv")

# Split data into input and output obejcts

X = my_df.drop(["output"], axis = 1)
y = my_df["output"]

# Split data into training and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, stratify = y)

# Instantiate our model object

clf = RandomForestClassifier(random_state = 42)

# Train our model

clf.fit(X_train, y_train)

# Assess model accuracy

y_pred = clf.predict(X_test)
accuracy_score(y_test, y_pred)

# A Demonstration of Overfitting

y_pred_training = clf.predict(X_train)
accuracy_score(y_train, y_pred_training)

# # Plot our Decision Tree

# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree

# plt.figure(figsize=(25,15))
# tree = plot_tree(clf, 
#                  feature_names = X.columns, 
#                  filled = True, 
#                  rounded = True,
#                  fontsize = 24)


