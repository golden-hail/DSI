'''
removal of outliers should have CAREFUL consideration
    # should only really do it when...
    # we think there is going to be a detrimental effect on the modeling process 
    # due to certain datapoints skewing things so much that the model can no longer 
    generalize rules for the dataset
'''

import pandas as pd

my_df = pd.DataFrame({"input1" : [15,41,44,47,50,53,56,59,99],
                      "input2" : [29,41,44,47,50,53,56,59,66]})

my_df.plot(kind = "box", vert = False)

outlier_columns = ["input1", "input2"]

## Boxplot approach

for column in outlier_columns:
    lower_quartile = my_df[column].quantile(0.25)
    upper_quartile = my_df[column].quantile(0.75)
    iqr = upper_quartile - lower_quartile # inter quartile range
    # extend quartile range by a factor (common is 1.5)
    iqr_extended = iqr * 1.5
    min_border = lower_quartile - iqr_extended
    max_border = upper_quartile + iqr_extended
    
    outliers = my_df[(my_df[column] < min_border) | (my_df[column] > max_border)].index
    print(f"{len(outliers)} outliers detected in column {column}")
    
    # remove outliers from the DataFrame
    
    my_df.drop(outliers, inplace = True) # 2 outliers
    
## Standard Deviation Approach

my_df = pd.DataFrame({"input1" : [15,41,44,47,50,53,56,59,99],
                      "input2" : [29,41,44,47,50,53,56,59,66]})

outlier_columns = ["input1", "input2"]

for column in outlier_columns:
    
    mean = my_df[column].mean()
    std_dev = my_df[column].std()
    
    min_border = mean - std_dev * 3
    max_border = mean + std_dev * 3
    
    outliers = my_df[(my_df[column] < min_border) | (my_df[column] > max_border)].index
    print(f"{len(outliers)} outliers detected in column {column}")
    
    # remove outliers from the DataFrame
    
    my_df.drop(outliers, inplace = True) # 0 outliers dropped
