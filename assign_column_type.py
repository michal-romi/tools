import pandas as pd
import os


input_file = input ("Enter a csv file: ")

column_types = []
if os.path.exists(input_file):
    # read file to a dataframe
    df = pd.read_csv(input_file, encoding='utf-8')

    # add the column type in the title of each column
    column_names = list(df.columns)
    for col in column_names:
        col_type = ""
        if "str" in str(type(df[col][0])):
            col_type = col + " " + "string"
        elif "int" in str(type(df[col][0])):
            col_type = col + " " + "int"
        elif "float" in str(type(df[col][0])):
            col_type = col + " " + "decimal"
        elif "date" in str(type(df[col][0])):
            col_type = col + " " + "date"

        column_types.append(col_type)

    print (column_types)
else:
    print("File doesn't exist")