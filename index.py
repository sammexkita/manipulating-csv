import csv

import os    
from chardet import detect

def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

# with open("SampleData.csv", mode="r",  encoding = get_encoding_type, errors='ignore') as csv_file:
#       csv_reader = csv.DictReader(csv_file)
#       line_count = 0
#       for row in csv_reader:
#             if line_count == 0:
#                 print("Column names are:".join(row))
#             print(row["Prospect ID"], f'line: {line_count}')
#             line_count += 1