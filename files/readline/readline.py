# readline.py
"""
readline() returns one line from the file.

You can also specified how many bytes from
the line to return, by using the size parameter.
"""

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)
  