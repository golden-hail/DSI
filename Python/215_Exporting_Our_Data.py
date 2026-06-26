######################################
# Pandas - Exporting Our Data
######################################

import pandas as pd
import numpy as np

my_df = pd.DataFrame({"A" : [1,2,3],
                      "B" : ["one", np.nan, "three"]})

my_df.to_csv('tester_export.csv')

# to export without index..
my_df.to_csv('tester_export.csv', index = False)
    # can change name of index column to "row ID"
    
# exporting specific columns only
my_df.to_csv('tester_export.csv', index = False, columns = ["B"])

# remove column names
my_df.to_csv('tester_export.csv', index = False, header = False)

# deal with NaN when exporting our data  na_rep()
my_df.to_csv('tester_export.csv', index = False, na_rep = 'MISSING')

# to .txt file
my_df.to_csv('tester_export.txt', index = False, na_rep = 'MISSING')

    # tab delimiter version
my_df.to_csv('tester_export.txt', index = False, sep = "\t")

# Export to xlsx
my_df.to_excel('tester_export.xlsx', sheet_name = "Sheet_12345")

# export to multiple .xlsx sheets 
my_other_df = my_df * 3

with pd.ExcelWriter('tester_export.xlsx') as excel_writer:
    my_df.to_excel(excel_writer, sheet_name = "Sheet_12345")
    my_other_df.to_excel(excel_writer, sheet_name = "Sheet_6789")

# GOTCHYA
# save to directory other than working directory (desktop)

# unicode escape error
# my_df.to_csv("C:\Users\aiaqu\OneDrive\Desktop\tester_export.csv", index = False)

# remedy 1
my_df.to_csv("C:\\Users\\aiaqu\\OneDrive\\Desktop\\tester_export.csv", index = False)

# remedy 2 RAW STRING
my_df.to_csv(r"C:\Users\aiaqu\OneDrive\Desktop\tester_export.csv", index = False)

