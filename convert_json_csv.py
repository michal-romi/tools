import json
from cherrypicker import CherryPicker
import pandas as pd
import os


input_file = input ("Enter a json file: ")
output_file = input ("Enter the output file name: ")

if os.path.exists(input_file):
    with open(input_file, encoding='utf-8') as f:
        content = json.load(f)
        print("json file contains {} rows".format(len(content)))

    picker = CherryPicker(content)
    flat = picker.flatten().get()
    df = pd.DataFrame(flat)
    df.to_csv(output_file)
else:
    print("File doesn't exist")