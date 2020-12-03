import hashlib
import pandas as pd
import os
from PIL import Image
import requests
import urllib.request

def compute_md5(image_path):
    try:
        filename = "c:/Temp/temp_image.JPG"
        urllib.request.urlretrieve(image_path, filename)
        im = Image.open(filename).tobytes()
        m2 = hashlib.md5()
        m2.update(im)
        md5_out = m2.hexdigest()
        return str(md5_out)
    except:
        return str('NA')

input_file = input ("Enter a csv file: ")
input_column = input("Enter the column name with the url: ")

if os.path.exists(input_file):
    # read file to a dataframe
    df = pd.read_csv(input_file, encoding='utf-8')
    output_file = input_file.split(".")[0] + "_output.csv"

    # create a new column with the MD5 hash for each url
    if input_column in df.columns:
        df['MD5'] = df[input_column].apply(compute_md5)
    else:
        print("Column name doesn't exist")
    df.drop_duplicates(subset=['MD5'])
    df.to_csv(output_file,index=False)
else:
    print("File doesn't exist")