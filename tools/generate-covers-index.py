import os
import re
import sys
import json

print("Generate Json [v0.0.1]\n\n")


# Location of covers/
coversDir = "../covers/"

# Check if directory exists
if not os.path.exists(coversDir):
	# Ask user location of covers directory
	coversDir = str(input("Path to covers/ directory: "))


# Save release data in array
data = []

for path, dirs, files in os.walk(coversDir):
    # Remove path to covers directory in output
    name = "".join(path.rsplit(coversDir))

    # Only sort releases
    if ("[" in name) and ("]" in name):

        item = {
            "artist": "",
            "release_name": "",
            "year": ""
        }

        # Split name via path "/"
        if os.name == 'nt':
            nameSplit = name.split("\\")
        else:
            nameSplit = name.split("/")

        # Get artist as first directory
        item["artist"] = nameSplit[0]

        # Extract year from "[]"
        item["year"] = re.search('(?<=\[).+?(?=\])', nameSplit[1]).group(0)

        # Extract Title - everything after "]"
        item["release_name"] = re.search('(?<=\] ).*', nameSplit[1]).group(0)

        # Add item to data array
        data.append(item)


# Create data/ directory
if not os.path.exists('data/'):
    os.makedirs('data')
    
# Save data to json file
with open('data/album-covers-data.json', 'w') as file:
    json.dump(data, file, indent=4) #ensure_ascii=False
