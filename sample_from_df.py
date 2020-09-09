"""This program reads from a csv file to a dataframe and then takes an n number of randomly chosen rows and outputs to a file
   The Main purpose of this program is to help with QA tasks
"""
import pandas as pd
import os
import sys

# input parameters to update by the user
input_file = input("Enter file name: ")
output_file = input("Enter output file name: ")
pct_to_sample = input ("Enter % of rows to sample between 0 to 1: ")

if os.path.exists(input_file):
    df = pd.read_csv(input_file, encoding='latin-1')
else:
    print("Input file doesn't exist ")
    sys.exit()

try:
    pct = float(pct_to_sample)
except:
    print("% entered is not a number")
    sys.exit()
if pct >=0 and pct<=1:
    pct_to_sample = pct
else:
    print("% to sample is not between o and 1")
    sys.exit()

tot_rows = df.shape[0]
num_to_sample = round(tot_rows*pct_to_sample)
sample = df.sample(num_to_sample)

sample.to_csv(output_file)
