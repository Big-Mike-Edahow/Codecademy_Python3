# csv_files_explained.py
"""
We call all files with a list of different values a
CSV file and then use different delimiters (like a
comma or tab) to indicate where the different values
start and stop.

Notice the \n character, this is the escape sequence
for a new line. The possibility of a new line escaped
by a \n character in our data is why we pass the
newline='' keyword argument to the open() function.

Notice that when we call csv.DictReader we pass in the
delimiter parameter, which is the string that’s used
to delineate separate fields in the CSV.
"""

import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]
