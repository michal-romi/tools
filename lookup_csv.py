"""The purpose of this program is to load 2 csv files and lookup values from a column in the first file on the second file.
this should perform the same way the vlookup option does in excel but return all the corresponding columns from the second file
in the end you will get a combined file with df1 and the relevant columns from df2 and in addition to exract files:
both - containing all the rows that are joined between the 2 file and diff which are all the rows that don't appear in the other file
"""

import pandas as pd
import os
import sys

# input parameters to update by the user
input_file1 = input ("Enter first file to compare: ")
input_file2 = input ("Enter second file to compare: ")
output_path = input ("Enter output directory: ")

col_to_search_df1 = input("Enter column name you want to search from the first file: ")
col_to_search_df2 = input("Enter the column name from the second file to search in: ")

if os.path.exists(input_file1):
    df1 = pd.read_csv(input_file1, encoding='latin-1')
else:
    print("First file doesn't exist")
    sys.exit()

if os.path.exists(input_file2):
    df2 = pd.read_csv(input_file2, encoding='latin-1')
else:
    print("Second file doesn't exist")
    sys.exit()

if os.path.exists(output_path):
    print ("Starting vlookup")
else:
    print("Output path doesn't exist")
    sys.exit()

def dataframe_difference(df1, df2,file,which=None):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(df2,
                              indicator=True,
                              how='outer')
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    diff_df.to_csv(file)
    return diff_df

diff = output_path + '/diff.csv'
both = output_path + '/both.csv'
combined = output_path + '/combined.csv'
dataframe_difference(df1, df2,file=diff)
dataframe_difference(df1, df2,which='both',file=both)

combined_file = df1.merge(df2,how='left',left_on=col_to_search_df1,right_on=col_to_search_df2,copy=False,indicator=True)
combined_file.to_csv(combined)



