# readlines.py
"""
.readlines() returns a list containing each line in
the file as a list item.

Use the hint parameter to limit the number of lines
returned. If the total number of bytes returned
exceeds the specified number, no more lines are
returned.
"""

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)
