# Moule for handling CSV files
import csv

"""
Structure of a CSV file:
The first row is the column headers, hence make sure to 
include them separately before writing and extract them 
separately or skip over them if not needed while reading data.
"""


# Writing to a CSV file
"""
Writing will overwrite existing stuff. 
We can write lists as well as dictionaries into a CSV file.
"""

###

# Writing lists into a CSV file

# Field names to write
fields = ["SI No", "Name", "Age"]
# List data to write
listdata = [
    ["1", "Darshan", "18"],
    ["2", "Ajay", "18"],
    ["3", "Kishan", "17"],
]

# Opening csv file in write mode and creating a file object
with open("../test.csv", "w", newline='') as csvfile:
    # Creating a writer object
    filewriter = csv.writer(csvfile)
    # Putting the headings
    filewriter.writerow(fields)

    # Writing the data
    # Takes care of linebreaks and everything
    filewriter.writerows(listdata)

###

# Writing dictionaries in to CSV file

# Field names to write
fields = ["SI No", "Name", "Age"]
# Data to write
dictdata = [
    {"SI No": "1", "Name": "Darshan", "Age": "18"},
    {"SI No": "2", "Name": "Ajay", "Age": "18"},
    {"SI No": "3", "Age": "17", "Name": "Kishan", },
]

# Opening csv file in write mode and creating a file object
with open("../test.csv", "w", newline='') as csvfile:
    # Creating a dictionary writer object
    filewriter = csv.DictWriter(csvfile, fieldnames=fields)
    # Putting in the headings
    filewriter.writeheader()

    # Writing dictionary data
    filewriter.writerows(dictdata)
    # The DictWriter will match the dictionary keys to the
    # headers and automatically do the job

###
###
###

# Reading from a CSV file
# Opening a csv file in read mode and making a file object
with open('../test.csv', 'r', newline='') as csvfile:
    # Creating a reader object
    filereader = csv.reader(csvfile)
    # Extracting only the headings
    fields = next(filereader)

    # List to store extracted data
    rows = []

    # Extracting data, row by row
    for row in filereader:
        # Each line in the CSV file will be returned as a list
        rows.append(row)

    print(rows)
"""
Sample output:
[['1', ' Darshan', ' 18'], ['2', ' Ajay', ' 18'], ['3', ' Kishan', ' 17']]  
"""
