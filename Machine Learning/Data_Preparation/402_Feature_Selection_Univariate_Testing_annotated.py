import pandas as pd
my_df = pd.read_csv("feature_selection_sample_data.csv")

'''
# Univaraiate testing uses statistical tests to show which input variables have the  
    strongest relationship with the output variables
    # with scikitLearn we use selectKBest which can be used in conjunction with many common tests 
        for relationship strength for both classification tasks and regression tasks
        
'''


#########################
# Regression Template
#########################

from sklearn.feature_selection import SelectKBest, f_regression

# store inputs and outputs as 2 separate objects (uppercase X and lowercase y)

X = my_df.drop(["output"], axis = 1) 
y = my_df["output"]

# instantiate SelectKBest, 
    # f_regression assess the relationship between each input variable and output variable,
        # then gives an f score and p value for the data set telling us how confident 
        # we can be that these is a true and robust relationship between the input and output
    # k is the number of variables that we would like to select (default 10)
    
feature_selector = SelectKBest(f_regression, k = "all")

fit = feature_selector.fit(X,y)
fit.pvalues_ # lower here is better (more confident), relationship = more robust

fit.scores_ # f scores.. higher value = stronger relationship

#create dataframe with info from each

p_values = pd.DataFrame(fit.pvalues_)
scores = pd.DataFrame(fit.scores_)

# dataframe with input variable names
input_variable_names = pd.DataFrame(X.columns)
summary_stats = pd.concat([input_variable_names,p_values,scores], axis = 1)

summary_stats.columns = ["input_var", "p_value", "f_score"]

# sorting is good
summary_stats.sort_values(by = "p_value", inplace = True)

# create threshold for values to isolate inputs with a robust relation to outputs
p_value_thresh = 0.05
score_thresh = 5

selected_variables = summary_stats.loc[(summary_stats["f_score"] >= score_thresh) & (summary_stats["p_value"] <= p_value_thresh)]

select_variables = selected_variables["input_var"].tolist()

# update our object X to only include the variables within the prescribed threshold 
X_new = X[select_variables]

## Ready to build model, on on variables we believe to be most important 

# changing k (not as good as above, because we rarely know how many input variables matter)

feature_selector = SelectKBest(f_regression, k = 2)
fit = feature_selector.fit(X,y)
X_new1 = feature_selector.transform(X) # just transfo from here comes out as array, no col names
feature_selector.get_support()
X_new1 = X.loc[:,feature_selector.get_support()]

#########################
# Classification Template
#########################

from sklearn.feature_selection import SelectKBest, chi2

X = my_df.drop(["output"], axis = 1) 
y = my_df["output"]

feature_selector = SelectKBest(chi2, k = "all")

fit = feature_selector.fit(X,y)

p_values = pd.DataFrame(fit.pvalues_)
scores = pd.DataFrame(fit.scores_)

# dataframe with input variable names
input_variable_names = pd.DataFrame(X.columns)
summary_stats = pd.concat([input_variable_names,p_values,scores], axis = 1)

summary_stats.columns = ["input_var", "p_value", "chi2_score"]

summary_stats.sort_values(by = "p_value", inplace = True)

# create threshold for values to isolate inputs with a robust relation to outputs
p_value_thresh = 0.05
score_thresh = 5

selected_variables = summary_stats.loc[(summary_stats["chi2_score"] >= score_thresh) & (summary_stats["p_value"] <= p_value_thresh)]

select_variables = selected_variables["input_var"].tolist()

# update our object X to only include the variables within the prescribed threshold 
X_new = X[select_variables]

## Ready to build model, on on variables we believe to be most important 






