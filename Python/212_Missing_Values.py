#######################################################
# Pandas - Pivoting our Data
#######################################################

# clean data, deal with missing values
    # leave them missing?
    # remove rows?
    # where we fill values with a value of our choice
    
import pandas as pd
customer_details = pd.read_excel("grocery_database.xlsx", sheet_name = "customer_details")

# how many values in each of our columns are missing?
customer_details.isna().sum()

# see how many values in each column are not nan/null
customer_details.notna().sum()

# to do on a specific column instead of whole dataframe
customer_details["distance_from_store"].isna().sum()

# use True return from .isna() method run on the DataFrames column (which is a series) 
    # to index into the whole table are return all rows where the distance_from_store is NaN
customer_details[customer_details["distance_from_store"].isna()]

# now for not NaN values
customer_details[customer_details["distance_from_store"].notna()]

# Lets dropNa to drop the NaN values
    ### HOW determines whether we drop rows or columns
        # Default = ANY - if ANY value in a row is missing, the whole row gets chopped 
            # ALL - drop where every value in that row is missing
    ### SUBSET for if we want to have certain columns checked for missing values
    ### inplace if we want to commit to dropping it on a DataFrame overwrite

customer_details.dropna(how = 'any') # [857 rows x 4 columns]

customer_details.dropna(how = 'all') # [870 rows x 4 columns] <- no rows are dropped

customer_details.dropna(how = 'any', subset = ["distance_from_store"])

customer_details.dropna(how = 'any', subset = ["distance_from_store", "gender"])

####################
# Insert or Impute placeholder value for nans
####################

###########
## fillna()
###########

import numpy as np

my_df = pd.DataFrame({"A" : [1,2,4,np.nan,5,np.nan,7],
                     "B" : [4,np.nan,7,np.nan,1,np.nan,2]})

# fill nan in DataFrame with "0" instead
my_df["A"].fillna(value=0)

############
### impute()
############

# create a variable that holds the mean of all values in series "A", 
    # then use that value in place of the NaNs

impute_value = my_df["A"].mean()
my_df["A"].fillna(value=impute_value)

## EXAMPLES with removing NaN values from customer_details columns, intelligently
customer_details.isna().sum()

# Assign nan gender entries to "U" (for unknown)... (good for ML practice)
customer_details["gender"].fillna(value="U", inplace = True)

    # check the missing values to ensure our change took place 
customer_details.isna().sum()

    # USE DESCRIBE() to get a summary of data in the column of choice
customer_details["distance_from_store"].describe()

# Assign median() value to NaNs  for distance_from_store
    ### MEDIAN IS ALWAYS RELIABLE for imputed data, mean may not be due to outliers
customer_details["distance_from_store"].fillna(value = customer_details["distance_from_store"].median(), inplace = True)
 


