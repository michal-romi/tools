import pandas as pd
import os
import sys
from os import listdir
from os.path import isfile, join
onlyfiles = []

# input parameters to update by the user
input_dir = input ("Enter the directory path where all the files to be merged: ")
input_dataset_name = input("Enter dataset_name: ")
output_path = input ("Enter output directory: ")

headers = ["corpus_name", "sentence_number", "source_sentence", "metadata"]

if os.path.exists(input_dir):
    # create a list with all the relevant file names in the directory
    onlyfiles = [f for f in listdir(input_dir) if isfile(join(input_dir, f))]
else:
    print("Directory doesn't exist")
    sys.exit()


if os.path.exists(output_path):
    print ("Starting reading files process")
    num_of_files = len(onlyfiles)
    print("There are ", num_of_files, " files in the directory")

    # based on the number of files - create a list of equal number of dataframes to which the files will be loaded
    i =1
    list_of_df_names = []
    while i <= num_of_files:
        df_name = "df" + str(i)
        list_of_df_names.append(df_name)
        i+=1

    # read each file to its correspondent dataframe from the list_of_df_names by a loop over the 2 lists (file names and df names)
    numerator = 0
    while numerator < num_of_files:
        full_file_name = os.path.join(input_dir,onlyfiles[numerator])
        print ("Working on file ", full_file_name)
        list_of_df_names[numerator] = pd.read_csv(full_file_name, encoding='Latin1', sep='\\t',engine='python')
        # assign the same headers to each df so the concatenation will be smooth
        list_of_df_names[numerator].columns = [headers]
        print("number of columns in df",numerator, " is " ,len(list_of_df_names[numerator].columns))
        numerator+=1

else:
    print("Output path doesn't exist")
    sys.exit()

# merge all the relevant dfs into a single one

merged_df = pd.concat(list_of_df_names,axis=0,ignore_index=True)
print("number of columns in merged df ", len(merged_df.columns))
merged_df['dataset_name'] = input_dataset_name
merged_df['seq_id'] = merged_df.index
merged_df['target_sentence'] = ""

merged_df = merged_df[["dataset_name", "seq_id", "corpus_name", "sentence_number", "source_sentence", "target_sentence", "metadata"]]

merged_df_file = os.path.join(output_path,"merged.csv") #output_path + '/merged.csv'
merged_df.to_csv(merged_df_file, index=False,sep='\t')
print("Output file is in ", merged_df_file)