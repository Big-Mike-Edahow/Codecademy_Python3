# dictreader.py
"""
In Python we can convert data from a csv file into a
dictionary using the csv library’s DictReader object.
"""

import csv

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])
