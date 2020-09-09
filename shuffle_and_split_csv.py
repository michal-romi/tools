""" read a csv file without header and n files to split and then shuffle the file and split it into n smaller files
 Make sure to update the input_file, output_path and number of files you want
"""
import pandas as pd
import os
import sys


input_file = input("Enter file name to split: ")
num_of_files_to_split = input("Enter number of files to split to: ")
output_path = input("Enter output directory: ")

if os.path.exists(input_file):
    df = pd.read_csv(input_file,header=None)
else:
    print("Input file doesn't exist")
    sys.exit()

try:
    num_of_files_to_split = int(num_of_files_to_split)
except:
    print("Number of files to split into is not a number")
    sys.exit()

if os.path.exists(output_path):
    print("Start processing")
else:
    print("Output directory doesn't exist")
    sys.exit()

shuffled_df = df.sample(frac=1, random_state=1).reset_index(drop=True)
rows = shuffled_df.size
num_per_df = round(rows / num_of_files_to_split)

df_names = []
for i in range(num_of_files_to_split):
    df_names.append("df" + str(i))

start_index = 0
end_index = num_per_df

for i in range(num_of_files_to_split):
    if i != (num_of_files_to_split - 1):
        df_names[i] = shuffled_df[start_index:end_index]
        start_index = end_index
        end_index += num_per_df
    else:
        df_names[i] = shuffled_df[start_index:]

for i in range(num_of_files_to_split):
    file_name = output_path + '/' + str(i) + '.csv'
    df_names[i].to_csv(file_name)
