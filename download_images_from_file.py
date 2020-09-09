import urllib.request
from pathlib import Path
import os
import re

input_file = input("Enter input file name with no header: ")
temp = re.split(r'(\\|\/)',input_file)[:-1]
path = ""
for i in temp:
    path = path+i


lines = []
# Make sure to change the path to the file you want to read from
if os.path.exists(input_file):
    with open(input_file) as file:
        for line in file:
            line = line.strip()  # remove spaces / special characters
            lines.append(line)  # for storing in memory which can help with larger files
            # make sure to updatethe location to which the images will be saved
            # takes the last part of the url as the new file name
            filename = Path(path + line.split('/')[-1])
            try:
                urllib.request.urlretrieve(line, filename)
            except:
                print("couldn't open file {}".format(filename) )

else:
    print("File doesn't exist")