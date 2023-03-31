# csv.py
"""
CSV stands for Comma-Separated Values and CSV files
are usually the way that data from spreadsheet
software (like Microsoft Excel or Google Sheets) is
exported into a portable format.
"""

with open('logger.csv') as log_csv_file:
  print(log_csv_file.read())
  