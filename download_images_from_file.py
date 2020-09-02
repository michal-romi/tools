import urllib.request
from pathlib import Path

lines = []
# Make sure to change the path to the file you want to read from
with open("C:\\Temp\\other\\other.csv") as file:
    for line in file:
        line = line.strip()  # remove spaces / special characters
        lines.append(line)  # for storing in memory which can help with larger files
        # make sure to updatethe location to which the images will be saved
        # takes the last part of the url as the new file name
        filename = Path("C:\\Temp\\other\\" + line.split('/')[-1])
        urllib.request.urlretrieve(line, filename)

