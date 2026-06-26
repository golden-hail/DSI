###################################################################
# Pandas - Dealing with Duplicate Data
###################################################################


import pandas as pd

my_df = pd.DataFrame({"customer_id" : [1,1,2,2,3],
                      "transaction_id" : [101,102,103,103,104]})

'''
# Rows 2 and 3 are duplicates
   customer_id  transaction_id
0            1             101
1            1             102
2            2             103
3            2             103
4            3             104
'''

# Use duplicated() method on DataFrame to get bool for each row - True = dupe
my_df.duplicated()

'''
0    False
1    False
2    False
3     True
4    False
dtype: bool
'''
my_df.duplicated().sum() # = 1 duplicate entry

# uuse dup[licated method on a column in a DataFrame]
my_df["customer_id"].duplicated()
'''
0    False
1     True
2    False
3     True
4    False
'''

# find index of the duplicate values of the DataFrame
my_df[my_df.duplicated()]

# method input, keep: default: keep the first entry in the DataFrame as the original
my_df.duplicated(keep = "first") # first instance

my_df.duplicated(keep = "last") # last instance is the one to keep

my_df.duplicated(keep = False) # True output - see below

'''
# keep = False True values are tagging rows that are not unique
0    False
1    False
2     True
3     True
4    False
dtype: bool
'''

#############
# drop_duplicates()
#############

my_df.drop_duplicates(inplace = True) 

