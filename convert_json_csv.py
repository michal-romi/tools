import json
from cherrypicker import CherryPicker
import pandas as pd


input_file = 'c:\Temp\json_test.json'
output_file = 'c:\Temp\converted_file.csv'

with open(input_file, encoding='utf-8') as f:
    content = json.load(f)
    print("json file contains {} rows".format(len(content)))

picker = CherryPicker(content)
flat = picker.flatten().get()
df = pd.DataFrame(flat)
df.to_csv(output_file)

