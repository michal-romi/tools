# This program reads from a csv file to a dataframe and then takes an n number of randomly chosen rows and outputs to a file
# The Main purpose of this program is to help with QA tasks
import pandas as pd

# input parameters to update by the user
input_file = 'c:/Temp/US_new_leafs.csv'
output_file = 'c:/Temp/sample.csv'
pct_to_sample = 0.1

df = pd.read_csv(input_file, encoding='latin-1')

tot_rows = df.shape[0]
num_to_sample = round(tot_rows*pct_to_sample)
sample = df.sample(num_to_sample)

sample.to_csv(output_file)