#####################################################
# Pands - Joining and Merging Dataframes
#####################################################

import pandas as pd

# JOINING

df_a = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6]})
df_b = pd.DataFrame({"C" : [1,2,3], "D" : [4,5,6]})

# put data frame side by side
df_c = pd.concat([df_a, df_b], axis = 1)

# put data frame on top of one another
df_c = pd.concat([df_a, df_b], axis = 0) # see below

'''
Since data frames have different column headers...
     A    B    C    D
0  1.0  4.0  NaN  NaN
1  2.0  5.0  NaN  NaN
2  3.0  6.0  NaN  NaN
0  NaN  NaN  1.0  4.0
1  NaN  NaN  2.0  5.0
2  NaN  NaN  3.0  6.0
'''

df_a = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6]})
df_b = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6]})
df_c = pd.concat([df_a, df_b], axis = 0)

    # can also use append
df_a.append(df_a) # concat is better thoS

## MERGING ##

df_a = pd.DataFrame({"user_id" : [1,2,3,5,7], "age" : [41,15,60,18,29]})
df_b = pd.DataFrame({"user_id" : [1,2,3,4,5], "gender" : ["m","f","f","f","m"]})

## INNER JOIN

pd.merge(df_a,df_b, how = "inner", on = "user_id")
'''
# only returned rows where the joining column finds data present in both dataframes

   user_id  age gender
0        1   41      m
1        2   15      f
2        3   60      f
3        5   18      m
'''

## LEFT JOIN

pd.merge(df_a,df_b, how = "left", on = "user_id")

'''
    # all rows from the first (left) DataFrame and append values from a second DataFrame
    # where the merging column finds matches in both tables 
    
    user_id  age gender
 0        1   41      m
 1        2   15      f
 2        3   60      f
 3        5   18      m
 4        7   29    NaN
'''

# OUTER JOIN

pd.merge(df_a,df_b, how = "outer", on = "user_id")

'''
# All rows included in the output and any values that can be appended through
    # a match in the join column will be present otherwise it'lll be left as nan/null'
    user_id   age gender
 0        1  41.0      m
 1        2  15.0      f
 2        3  60.0      f
 3        4   NaN      f
 4        5  18.0      m
 5        7  29.0    NaN
'''

# JOIN ON MULTIPLE COLUMNS

pd.merge(df_a,df_b, how = "outer", on = ["user_id","column2"])

df_b.rename(columns = {"user_id" : "customer_id"}, inplace = True)
    # can't JOIN on user_id because the names are different between df_a and df_b
pd.merge(df_a,df_b, how = "inner", left_on = ["user_id"], right_on = "customer_id")

# default is inner join


