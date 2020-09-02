# The purpose of this program is to load 2 csv files and lookup values from a column in the first file on the second file.
# this should perform the same way the vlookup option does in excel but return all the corresponding columns from the second file
# in the end you will get a combined file with df1 and the relevant columns from df2 and in addition to exract files:
# both - containing all the rows that are joined between the 2 file and diff which are all the rows that don't appear in the other file


import pandas as pd

# input parameters to update by the user
input_file1 = 'c:/Temp/US_new_leafs.csv'
input_file2 = 'c:/Temp/UK_new_leafs.csv'
output_path = 'c:/Temp/'

col_to_search_df1 = 'Cat ID'
col_to_search_df2 = 'Cat ID'

df1 = pd.read_csv(input_file1, encoding='latin-1')
df2 = pd.read_csv(input_file2, encoding='latin-1')

#values_list = df2[col_to_search_df2].tolist()

# def is_in_column(data, values):
#     if data in values:
#         return True
#     else:
#         return False


#df1['exist_in_df2'] = df1[col_to_search_df1].apply(is_in_column, values=values_list)

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

diff = output_path + 'diff.csv'
both = output_path + 'both.csv'
combined = output_path + 'combined.csv'
dataframe_difference(df1, df2,file=diff)
dataframe_difference(df1, df2,which='both',file=both)

combined_file = df1.merge(df2,how='left',left_on=col_to_search_df1,right_on=col_to_search_df2,copy=False,indicator=True)
combined_file.to_csv(combined)



