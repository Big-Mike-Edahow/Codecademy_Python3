# open.py
"""
The open() function opens a file, and returns it as a file object.

Write to an Existing File
To write to an existing file, you must add a parameter
to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

with open('bad_bands.txt', 'w') as bad_bands_doc:

  bad_bands_doc.write('Garbage')
  